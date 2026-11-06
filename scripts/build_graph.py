"""
Orchestrates graph data compilation for docs-site.
In CI/Cloudflare environments, graph-data.json is already compiled and tracked in git.
Compiler is only run locally if explicit or if numpy is installed.
"""

import hashlib
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PUBLIC_DIR = REPO_ROOT / "docs" / "public"
GRAPH_DATA_PATH = PUBLIC_DIR / "graph-data.json"
CACHE_HASH_PATH = REPO_ROOT / "scripts" / ".graph_hash"
DATA_REPO_DIR = REPO_ROOT.parent / "docs-data"

TAXONOMY_PATH = DATA_REPO_DIR / "api-taxonomy.json"
GRAPH_INPUT_PATH = DATA_REPO_DIR / "api-graph.json"
TEMPLATE_PATH = REPO_ROOT / "scripts" / "template.json"


def compute_inputs_hash():
    hasher = hashlib.sha256()
    for p in [TAXONOMY_PATH, GRAPH_INPUT_PATH]:
        if p.exists():
            hasher.update(p.read_bytes())
    return hasher.hexdigest()


def run():
    # If graph-data.json exists (already compiled and tracked in git):
    if GRAPH_DATA_PATH.exists() and GRAPH_DATA_PATH.stat().st_size > 1000:
        # Check if we are in CI / Cloudflare Pages or if numpy is missing
        is_ci = os.environ.get("CF_PAGES") == "1" or os.environ.get("CI") == "true"
        try:
            import numpy
            has_numpy = True
        except ImportError:
            has_numpy = False

        if is_ci or not has_numpy:
            print("[build-graph] CI environment or standalone runtime detected. Using precomputed graph-data.json.")
            return

        current_hash = compute_inputs_hash()
        if CACHE_HASH_PATH.exists():
            cached_hash = CACHE_HASH_PATH.read_text(encoding="utf-8").strip()
            if cached_hash == current_hash and "--force" not in sys.argv:
                print("[build-graph] Graph taxonomy & dependencies unchanged. Using cached graph-data.json.")
                return

    print("[build-graph] Compiling HCRDL topology...")
    sys.path.append(str(Path(__file__).resolve().parent))
    try:
        import compiler
        snap_all = None
        if TEMPLATE_PATH.exists():
            snap_all = json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))

        raw_graph = json.loads(GRAPH_DATA_PATH.read_text(encoding="utf-8"))
        compiled = compiler.compile_graph_topology(
            raw_graph,
            snap_all=snap_all,
            designated_hub="Miscellaneous & Utility",
            air_gap_r=340.0
        )
        compiled["legend"] = raw_graph.get("legend", {})

        # Merge call graph & type usage dependencies
        deps_path = DATA_REPO_DIR / "dependencies.json"
        if deps_path.exists():
            deps = json.loads(deps_path.read_text(encoding="utf-8"))
            node_ids = {n["id"] for n in compiled["nodes"]}
            existing_links = {(l["source"], l["target"]) for l in compiled["links"]}

            for s, d in deps.items():
                if s not in node_ids:
                    continue
                for t in d.get("uses", []):
                    if t in node_ids and s != t and (s, t) not in existing_links:
                        existing_links.add((s, t))
                        compiled["links"].append({"source": s, "target": t, "type": "uses"})

            for uid in node_ids:
                parts = uid.split(".")
                if len(parts) > 2:
                    parent_id = ".".join(parts[:-1])
                    if parent_id in node_ids:
                        if (parent_id, uid) not in existing_links and (uid, parent_id) not in existing_links:
                            existing_links.add((parent_id, uid))
                            compiled["links"].append({"source": parent_id, "target": uid, "type": "declares"})

            connected_ids = set()
            for l in compiled["links"]:
                connected_ids.add(l["source"])
                connected_ids.add(l["target"])

            for n in compiled["nodes"]:
                n["isOrphan"] = n["id"] not in connected_ids

        GRAPH_DATA_PATH.write_text(json.dumps(compiled, indent=2, ensure_ascii=False), encoding="utf-8")
        current_hash = compute_inputs_hash()
        CACHE_HASH_PATH.write_text(current_hash, encoding="utf-8")
        print(f"[build-graph] Compiled and frozen {len(compiled['nodes'])} nodes into {GRAPH_DATA_PATH}")
    except Exception as e:
        print(f"[build-graph] Warning: Could not run compiler ({e}). Falling back to existing graph-data.json.")


if __name__ == "__main__":
    run()
