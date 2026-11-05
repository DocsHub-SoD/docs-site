"""
Orchestrates graph data compilation for docs-site.
Checks SHA256 of taxonomy & API data; only runs compiler.py if structure changed.
"""

import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PUBLIC_DIR = REPO_ROOT / "docs" / "public"
GRAPH_DATA_PATH = PUBLIC_DIR / "graph-data.json"
CACHE_HASH_PATH = REPO_ROOT / "scripts" / ".graph_hash"
DATA_REPO_DIR = REPO_ROOT.parent / "docs-data"

TAXONOMY_PATH = DATA_REPO_DIR / "api-taxonomy.json"
GRAPH_INPUT_PATH = DATA_REPO_DIR / "api-graph.json"


def compute_inputs_hash():
    hasher = hashlib.sha256()
    for p in [TAXONOMY_PATH, GRAPH_INPUT_PATH]:
        if p.exists():
            hasher.update(p.read_bytes())
    return hasher.hexdigest()


def run():
    current_hash = compute_inputs_hash()
    
    # Check if rebuild is necessary
    if CACHE_HASH_PATH.exists() and GRAPH_DATA_PATH.exists():
        cached_hash = CACHE_HASH_PATH.read_text(encoding="utf-8").strip()
        if cached_hash == current_hash and "--force" not in sys.argv:
            print("[build-graph] Graph taxonomy & dependencies unchanged. Using cached graph-data.json.")
            return

    print("[build-graph] Changes detected or first run. Compiling HCRDL topology...")
    
    # Import compiler module
    sys.path.append(str(Path(__file__).resolve().parent))
    import compiler

    # Ensure source data is fresh
    if not GRAPH_DATA_PATH.exists():
        print(f"[build-graph] Error: Source {GRAPH_DATA_PATH} not found.")
        return

    raw_graph = json.loads(GRAPH_DATA_PATH.read_text(encoding="utf-8"))
    compiled = compiler.compile_graph_topology(raw_graph, designated_hub="Miscellaneous & Utility")
    
    # Add legend back
    compiled["legend"] = raw_graph.get("legend", {})

    GRAPH_DATA_PATH.write_text(json.dumps(compiled, separators=(',', ':'), ensure_ascii=False), encoding="utf-8")
    CACHE_HASH_PATH.write_text(current_hash, encoding="utf-8")
    print(f"[build-graph] Successfully compiled and frozen {len(compiled['nodes'])} node positions into {GRAPH_DATA_PATH}")


if __name__ == "__main__":
    run()
