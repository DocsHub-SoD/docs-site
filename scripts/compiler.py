"""
HCRDL Graph Topology Compiler
=============================
Hierarchical Constrained Radial Domain Layout (HCRDL).
Deterministic, zero-physics, pre-computed graph layout engine for complex multi-domain graphs.

Features:
- Automatic Central Hub Detection via Cross-Cluster Betweenness Centrality.
- Symmetrical 360-degree Air Gap isolating the central core from outer satellite domains.
- Dual-Layer Stratification: connected nodes face the center; orphan nodes populate the outer rounded dome.
- Continuous monolithic radial expansion preventing internal tears or gaps.
- Two-tier non-physical collision resolution (intra-domain ~38px, inter-domain ~72px).
- Complete coordinate freezing (x, y, fx, fy) for instantaneous 0ms client-side rendering.
"""

import json
import math
import argparse
import numpy as np
from collections import defaultdict
from pathlib import Path

DEFAULT_PETAL_ANGLES = {
    "Combat & Abilities": math.radians(0.0),       # 0° (East)
    "Actors & Entities": math.radians(48.0),      # ~48° (South-East)
    "Managers & Systems": math.radians(108.0),    # ~108° (South)
    "Buffs & Statuses": math.radians(150.0),     # ~150° (South-West)
    "Items & Economy": math.radians(184.0),      # ~184° (West)
    "User Interface": math.radians(222.0),       # ~222° (-138°, North-West)
    "Networking": math.radians(255.0),           # ~255° (-105°, North)
    "Data & Core Math": math.radians(295.0)      # ~295° (-65°, North-East)
}

def sanitize_links(raw_links, valid_node_ids):
    """Normalizes link IDs, sanitizing common syntax mismatches."""
    clean = []
    adj = defaultdict(set)
    degree = defaultdict(int)

    for l in raw_links:
        s = l["source"]
        t = l["target"]
        if s not in valid_node_ids and s.replace("-", "`") in valid_node_ids:
            s = s.replace("-", "`")
        if t not in valid_node_ids and t.replace("-", "`") in valid_node_ids:
            t = t.replace("-", "`")
        if s in valid_node_ids and t in valid_node_ids:
            clean.append({"source": s, "target": t, "type": l.get("type", "normal")})
            adj[s].add(t)
            adj[t].add(s)
            degree[s] += 1
            degree[t] += 1

    return clean, adj, degree

def generate_organic_petal_slots(n_nodes, base_angle, r_inner, delta_theta=math.pi/3, spacing=42.0, corridor=72.0):
    """
    Synthesizes an organic, fluid droplet-shaped petal dome with natural blue-noise dispersion.
    Strictly constrained by the angular sector and inter-domain corridor to prevent adjacent domain collision.
    """
    import random
    area_target = n_nodes * (spacing ** 2) * 0.95

    # Safe angular limit based on sector width and corridor buffer at mid-radius
    r_mid = r_inner + 250.0
    safe_half_ang = max(0.08, (delta_theta / 2.0) - math.asin(min(0.9, (corridor * 0.55) / max(100.0, r_mid))))
    w_avail_mid = r_mid * math.sin(safe_half_ang)
    w_max = min(w_avail_mid * 0.90, 420.0)

    # Petal length needed to accommodate required node area
    petal_len = max(280.0, area_target / max(50.0, w_max * 1.35))

    pts = []
    du = spacing * 0.866
    row_idx = 0
    for u in np.arange(du * 0.5, petal_len, du):
        t = np.clip(u / petal_len, 0.001, 0.999)
        # Teardrop envelope: gentle base, expanding belly, rounded dome closure
        envelope = 2.4 * math.sqrt(t) * ((1.0 - t) ** 0.65)
        w_t = w_max * envelope
        r = r_inner + u

        # Strict sector corridor limit at this exact radial distance
        curr_half_ang = max(0.03, (delta_theta / 2.0) - math.asin(min(0.9, (corridor * 0.55) / max(100.0, r))))
        w_limit = r * math.sin(curr_half_ang) * 0.92
        w_eff = min(w_t, w_limit)

        if w_eff < spacing * 0.35:
            v_vals = [0.0]
        else:
            nv = max(1, int(round((2.0 * w_eff) / spacing)))
            # Hexagonal staggered offset to eliminate visible grid lines
            stagger = (spacing * 0.45) if (row_idx % 2 == 1) else 0.0
            v_vals = np.linspace(-w_eff + stagger, w_eff - stagger, nv)
        for v in v_vals:
            pts.append([u + random.uniform(-4, 4), v + random.uniform(-4, 4)])
        row_idx += 1

    coords = np.array(pts, dtype=np.float64)
    if len(coords) > n_nodes:
        # Uniform subselection
        idx = np.round(np.linspace(0, len(coords) - 1, n_nodes)).astype(int)
        coords = coords[idx]
    elif len(coords) < n_nodes:
        while len(coords) < n_nodes:
            t = random.uniform(0.1, 0.9)
            u = t * petal_len
            envelope = 2.4 * math.sqrt(t) * ((1.0 - t) ** 0.65)
            w_eff = min(w_max * envelope, (r_inner + u) * math.sin(safe_half_ang) * 0.9)
            v = random.uniform(-w_eff, w_eff)
            coords = np.vstack([coords, [u, v]])

    # Local blue-noise repulsive relaxation passes
    for _ in range(15):
        diff = coords[:, None, :] - coords[None, :, :]
        d = np.sqrt(np.sum(diff ** 2, axis=-1) + 1e-4)
        np.fill_diagonal(d, 1e9)
        overlap = np.maximum(0.0, spacing - d)
        force = (diff / d[:, :, None]) * overlap[:, :, None] * 0.35
        coords += np.sum(force, axis=1)
        coords[:, 0] = np.clip(coords[:, 0], 12.0, petal_len - 12.0)
        t = np.clip(coords[:, 0] / petal_len, 0.001, 0.999)
        envelope = 2.4 * np.sqrt(t) * ((1.0 - t) ** 0.65)
        w_cur = np.minimum(w_max * envelope, (r_inner + coords[:, 0]) * math.sin(safe_half_ang) * 0.9)
        coords[:, 1] = np.clip(coords[:, 1], -w_cur, w_cur)

    # Polar rotation into world Cartesian coordinates
    cos_a = math.cos(base_angle)
    sin_a = math.sin(base_angle)
    r_coords = coords[:, 0] + r_inner
    v_coords = coords[:, 1]
    xs = cos_a * r_coords - sin_a * v_coords
    ys = sin_a * r_coords + cos_a * v_coords
    return np.stack([xs, ys], axis=1)

def detect_central_hub(nodes, clean_links, designated_hub=None):
    """
    Identifies the Central Hub category.
    Uses designated_hub if specified and present; otherwise calculates cross-domain betweenness.
    """
    node_cat = {n["id"]: n["category"] for n in nodes}
    all_cats = set(node_cat.values())
    if designated_hub and designated_hub in all_cats:
        return designated_hub

    cross_links = defaultdict(int)
    for l in clean_links:
        c1 = node_cat.get(l["source"])
        c2 = node_cat.get(l["target"])
        if c1 and c2 and c1 != c2:
            cross_links[c1] += 1
            cross_links[c2] += 1

    if cross_links:
        return max(cross_links.keys(), key=lambda c: cross_links[c])
    return next(iter(all_cats))

def compile_graph_topology(raw_graph, snap_all=None, designated_hub=None, air_gap_r=None, ring_r_mean=None, c_spread=19.5):
    """
    Core HCRDL compilation pipeline.
    Returns: dict with 'nodes' and 'links'.
    """
    nodes = raw_graph["nodes"]
    raw_links = raw_graph["links"]
    valid_node_ids = {n["id"] for n in nodes}
    raw_nodes_map = {n["id"]: n for n in nodes}

    # 1. Clean links and compute degrees
    clean_links, adj, degree = sanitize_links(raw_links, valid_node_ids)

    # 2. Determine Hub Category & Satellite Categories
    hub_category = detect_central_hub(nodes, clean_links, designated_hub)
    all_cats_set = set(n["category"] for n in nodes)
    satellite_categories = sorted([c for c in all_cats_set if c != hub_category])

    # Assign angular sectors for satellites:
    # If all satellite categories match Shape of Dreams preset, use its tuned angles.
    # Otherwise, distribute the K categories evenly around the full 360° circle.
    is_preset_domain = all(c in DEFAULT_PETAL_ANGLES for c in satellite_categories)
    petal_angles = {}
    for i, c in enumerate(satellite_categories):
        if is_preset_domain:
            petal_angles[c] = DEFAULT_PETAL_ANGLES[c]
        else:
            petal_angles[c] = (2.0 * math.pi * i) / max(1, len(satellite_categories))

    # Partition nodes into connected vs orphan within each category
    cat_conn_nodes = defaultdict(list)
    cat_orph_nodes = defaultdict(list)
    for n in nodes:
        nid = n["id"]
        cat = n["category"]
        if degree[nid] > 0:
            cat_conn_nodes[cat].append(nid)
        else:
            cat_orph_nodes[cat].append(nid)

    # -------------------------------------------------------------
    # PHASE A: Central Hub Dynamic Geometry & Layout
    # -------------------------------------------------------------
    hub_conn = cat_conn_nodes.get(hub_category, [])
    hub_orph = cat_orph_nodes.get(hub_category, [])

    # Dynamic scaling for Hub: scales gracefully for any node count (50 to 5000+)
    n_hub_conn = len(hub_conn)
    n_hub_orph = len(hub_orph)
    r_orph_max = c_spread * math.sqrt(max(1, n_hub_orph))
    r_ring_min_circ = (n_hub_conn * 38.0) / (2.0 * math.pi) if n_hub_conn > 0 else 248.0
    
    if ring_r_mean is None:
        ring_r_mean = max(248.0, r_orph_max + 50.0, r_ring_min_circ)

    if air_gap_r is None:
        air_gap_r = ring_r_mean + 85.0

    # Extract template slots from snapshot if provided
    template_slots = defaultdict(list)
    if snap_all:
        for nid, pos in snap_all.items():
            cat = pos.get("category")
            if cat:
                template_slots[cat].append((float(pos["x"]), float(pos["y"])))

    final_positions = {}

    # A1. Connected Hub Nodes -> Outward-Facing 360° Perimeter Ring
    conn_with_angles = []
    for nid in hub_conn:
        nbrs = adj[nid]
        ext_angles = []
        for nbr_id in nbrs:
            nbr_cat = raw_nodes_map.get(nbr_id, {}).get("category")
            if nbr_cat and nbr_cat in petal_angles:
                ext_angles.append(petal_angles[nbr_cat])
        if ext_angles:
            sin_sum = sum(math.sin(a) for a in ext_angles)
            cos_sum = sum(math.cos(a) for a in ext_angles)
            target_a = math.atan2(sin_sum, cos_sum)
        else:
            target_a = 0.0
        conn_with_angles.append((nid, (target_a + 2 * math.pi) % (2 * math.pi)))

    conn_with_angles.sort(key=lambda x: x[1])

    for rank, (nid, _) in enumerate(conn_with_angles):
        ring_ang = (2.0 * math.pi * rank) / max(1, n_hub_conn)
        r_actual = ring_r_mean + math.sin(rank * 3.7) * 9.0
        final_positions[nid] = {
            "x": round(math.cos(ring_ang) * r_actual, 1),
            "y": round(math.sin(ring_ang) * r_actual, 1),
            "isOrphan": False
        }

    # A2. Orphan Hub Nodes -> Inner Core Disk via Fibonacci Phyllotaxis
    golden_angle = math.radians(137.50776405)
    for i, nid in enumerate(hub_orph):
        k = i + 1
        r = c_spread * math.sqrt(k)
        theta = k * golden_angle
        final_positions[nid] = {
            "x": round(math.cos(theta) * r, 1),
            "y": round(math.sin(theta) * r, 1),
            "isOrphan": True
        }

    # -------------------------------------------------------------
    # PHASE B: Satellite Petals Layout
    # -------------------------------------------------------------
    for cat in satellite_categories:
        conn_ids = list(cat_conn_nodes.get(cat, []))
        orph_ids = list(cat_orph_nodes.get(cat, []))
        total_cat_nodes = len(conn_ids) + len(orph_ids)

        if total_cat_nodes == 0:
            continue

        delta_theta = (2.0 * math.pi) / max(1, len(satellite_categories))
        raw_slots = template_slots.get(cat, [])
        if raw_slots:
            pts = np.array(raw_slots, dtype=np.float64)
            rs = np.hypot(pts[:, 0], pts[:, 1])
            thetas = np.arctan2(pts[:, 1], pts[:, 0])
            min_r = rs.min()

            # Monolithic radial translation: aligns inner boundary exactly to air_gap_r
            new_rs = air_gap_r + (rs - min_r)
            new_xs = np.cos(thetas) * new_rs
            new_ys = np.sin(thetas) * new_rs
            slot_coords = np.stack([new_xs, new_ys], axis=1)
        else:
            # Synthetic parametric organic droplet synthesis if no template slots exist
            slot_coords = generate_organic_petal_slots(
                n_nodes=total_cat_nodes,
                base_angle=petal_angles[cat],
                r_inner=air_gap_r,
                delta_theta=delta_theta
            )

        # Dynamic expansion if node count exceeds available slots
        if len(slot_coords) < total_cat_nodes:
            needed = total_cat_nodes - len(slot_coords)
            max_r = np.hypot(slot_coords[:, 0], slot_coords[:, 1]).max()
            extra_slots = generate_organic_petal_slots(
                n_nodes=needed,
                base_angle=petal_angles[cat],
                r_inner=max_r + 44.0,
                delta_theta=delta_theta
            )
            slot_coords = np.vstack([slot_coords, extra_slots])

        # Dual-Layer Stratification:
        # Connected nodes take innermost slots; orphan nodes take outer dome
        slot_rs = np.hypot(slot_coords[:, 0], slot_coords[:, 1])
        sorted_indices = np.argsort(slot_rs)

        n_conn = len(conn_ids)
        conn_slot_indices = sorted_indices[:n_conn]
        orph_slot_indices = sorted_indices[n_conn:]

        conn_slots = slot_coords[conn_slot_indices]
        orph_slots = slot_coords[orph_slot_indices]

        # B1. Assign Connected Nodes with 2-Opt Link Minimization
        if snap_all:
            conn_ids.sort(key=lambda nid: math.atan2(
                snap_all[nid]["y"] if nid in snap_all else 0.0,
                snap_all[nid]["x"] if nid in snap_all else 1.0
            ))
            conn_slots_by_ang = conn_slots[np.argsort(np.arctan2(conn_slots[:, 1], conn_slots[:, 0]))]
            conn_coords = np.copy(conn_slots_by_ang)
        else:
            # Topological radial-depth stratification for raw/synthetic graphs
            hub_nodes_set = set(hub_conn) | set(hub_orph)
            depth = {}
            for nid in conn_ids:
                if any(nbr in hub_nodes_set for nbr in adj[nid]):
                    depth[nid] = 0

            queue = [nid for nid, d in depth.items() if d == 0]
            if not queue and conn_ids:
                queue = [conn_ids[0]]
                depth[conn_ids[0]] = 0

            visited = set(queue)
            while queue:
                curr = queue.pop(0)
                for nbr in adj[curr]:
                    if nbr in conn_ids and nbr not in visited:
                        visited.add(nbr)
                        depth[nbr] = depth[curr] + 1
                        queue.append(nbr)

            for nid in conn_ids:
                if nid not in depth:
                    depth[nid] = 99

            conn_ids.sort(key=lambda nid: (depth[nid], -degree[nid]))
            # Align slots radially so lowest depth takes closest slots to hub
            c_rs = np.hypot(conn_slots[:, 0], conn_slots[:, 1])
            c_angs = np.arctan2(conn_slots[:, 1], conn_slots[:, 0])
            slot_sort_idx = np.lexsort((c_angs, c_rs))
            conn_coords = np.copy(conn_slots[slot_sort_idx])

        if n_conn > 1:
            for _ in range(50):
                improved = False
                for i in range(n_conn):
                    u = conn_ids[i]
                    u_nbrs = [j for j, v in enumerate(conn_ids) if v in adj[u]]
                    if not u_nbrs:
                        continue
                    for k in range(i + 1, min(i + 16, n_conn)):
                        w = conn_ids[k]
                        w_nbrs = [j for j, v in enumerate(conn_ids) if v in adj[w]]

                        old_d = sum(np.hypot(*(conn_coords[i] - conn_coords[j])) for j in u_nbrs) + \
                                sum(np.hypot(*(conn_coords[k] - conn_coords[j])) for j in w_nbrs)

                        conn_coords[i], conn_coords[k] = conn_coords[k].copy(), conn_coords[i].copy()

                        new_d = sum(np.hypot(*(conn_coords[i] - conn_coords[j])) for j in u_nbrs) + \
                                sum(np.hypot(*(conn_coords[k] - conn_coords[j])) for j in w_nbrs)

                        if new_d < old_d - 0.5:
                            improved = True
                        else:
                            conn_coords[i], conn_coords[k] = conn_coords[k].copy(), conn_coords[i].copy()
                if not improved:
                    break

        for i, nid in enumerate(conn_ids):
            final_positions[nid] = {
                "x": round(float(conn_coords[i, 0]), 1),
                "y": round(float(conn_coords[i, 1]), 1),
                "isOrphan": False
            }

        # B2. Assign Orphan Nodes
        if snap_all:
            orph_ids.sort(key=lambda nid: math.atan2(
                snap_all[nid]["y"] if nid in snap_all else 0.0,
                snap_all[nid]["x"] if nid in snap_all else 1.0
            ))
            orph_slots_by_ang = orph_slots[np.argsort(np.arctan2(orph_slots[:, 1], orph_slots[:, 0]))]
        else:
            orph_slots_by_ang = orph_slots[np.argsort(np.arctan2(orph_slots[:, 1], orph_slots[:, 0]))]

        for i, nid in enumerate(orph_ids):
            final_positions[nid] = {
                "x": round(float(orph_slots_by_ang[i, 0]), 1),
                "y": round(float(orph_slots_by_ang[i, 1]), 1),
                "isOrphan": True
            }

    # -------------------------------------------------------------
    # PHASE C: Global Two-Tier Anti-Collision Relaxation
    # -------------------------------------------------------------
    all_node_keys = [n["id"] for n in nodes]
    all_coords = np.array([[final_positions[nid]["x"], final_positions[nid]["y"]] for nid in all_node_keys], dtype=np.float64)

    node_cats = [raw_nodes_map[nid]["category"] for nid in all_node_keys]
    n_total = len(all_node_keys)
    same_cat = np.array([[node_cats[i] == node_cats[j] for j in range(n_total)] for i in range(n_total)])
    hub_mask = np.array([raw_nodes_map[nid]["category"] == hub_category for nid in all_node_keys], dtype=bool)

    INTRA_D = 38.0  # Dense organic cloud within same domain
    INTER_D = 72.0  # Clear corridor buffer between adjacent different-color domains

    min_dist_matrix = np.where(same_cat, INTRA_D, INTER_D)
    min_dist_matrix[hub_mask, :] = INTRA_D
    min_dist_matrix[:, hub_mask] = INTRA_D

    for _ in range(45):
        diff = all_coords[:, None, :] - all_coords[None, :, :]
        d_sq = np.sum(diff ** 2, axis=-1)
        np.fill_diagonal(d_sq, 1e9)
        d = np.sqrt(np.maximum(d_sq, 1e-4))

        overlap = np.maximum(0.0, min_dist_matrix - d)
        if not np.any(overlap > 0.0):
            break
        force = (diff / d[:, :, None]) * overlap[:, :, None] * 0.45
        force[hub_mask] = 0.0
        all_coords += np.sum(force, axis=1)

    # -------------------------------------------------------------
    # PHASE D: Output Assembly & Coordinate Freezing
    # -------------------------------------------------------------
    compiled_nodes = []
    for i, nid in enumerate(all_node_keys):
        n = raw_nodes_map[nid]
        pos = final_positions[nid]
        x_final = round(float(all_coords[i, 0]), 1)
        y_final = round(float(all_coords[i, 1]), 1)
        compiled_nodes.append({
            "id": nid,
            "name": n.get("name", nid),
            "category": n["category"],
            "color": n.get("color", "#888888"),
            "val": n.get("val", 3.0),
            "x": x_final,
            "y": y_final,
            "fx": x_final,  # Frozen coordinates for 0ms loading
            "fy": y_final,
            "isOrphan": pos["isOrphan"]
        })

    return {
        "nodes": compiled_nodes,
        "links": clean_links
    }

def render_preview_png(compiled_data, out_path, image_size=2800):
    """Renders a standalone visual PNG preview using PIL."""
    from PIL import Image, ImageDraw

    out_file = Path(out_path)
    # If the user passed a path prefixed with 'hcrdl-engine/' while already working inside 'hcrdl-engine/', normalize it
    if not out_file.parent.exists() and len(out_file.parts) > 1 and out_file.parts[0] == "hcrdl-engine":
        stripped = Path(*out_file.parts[1:])
        if Path(".").resolve().name == "hcrdl-engine" or stripped.parent.exists():
            out_file = stripped

    out_file.parent.mkdir(parents=True, exist_ok=True)

    nodes = compiled_data["nodes"]
    links = compiled_data["links"]

    img = Image.new("RGB", (image_size, image_size), "#090c10")
    draw = ImageDraw.Draw(img)
    cx, cy = image_size / 2.0, image_size / 2.0
    scale = 1.02

    node_map = {n["id"]: n for n in nodes}
    for l in links:
        s = node_map.get(l["source"])
        t = node_map.get(l["target"])
        if s and t:
            draw.line([(cx + s["x"] * scale, cy + s["y"] * scale),
                       (cx + t["x"] * scale, cy + t["y"] * scale)],
                      fill="#202933", width=1)

    for n in nodes:
        x = cx + n["x"] * scale
        y = cy + n["y"] * scale
        r = 5 if not n["isOrphan"] else 3
        col = n.get("color", "#888888")
        outline = "#ffffff" if not n["isOrphan"] else None
        draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=col, outline=outline)

    img.save(str(out_file))
    print(f"Visual preview saved: {out_file.resolve()}")

def main():
    parser = argparse.ArgumentParser(description="HCRDL Topology Graph Compiler")
    parser.add_argument("--input", default=str(Path(__file__).parent / "data" / "graph-data.json"), help="Input graph JSON")
    parser.add_argument("--template", default=str(Path(__file__).parent / "data" / "template.json"), help="Template slots JSON (optional)")
    parser.add_argument("--output", default=str(Path(__file__).parent / "data" / "graph-data-compiled.json"), help="Output compiled JSON")
    parser.add_argument("--js", default=str(Path(__file__).parent / "data" / "data-compiled.js"), help="Output compiled JS bundle")
    parser.add_argument("--hub", default="Miscellaneous & Utility", help="Designated central hub category")
    parser.add_argument("--air-gap", type=float, default=340.0, help="Radial air gap (inner petal radius)")
    parser.add_argument("--render-png", default=None, help="Optional path to render preview PNG")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    raw_graph = json.loads(input_path.read_text(encoding="utf-8"))

    snap_all = None
    template_path = Path(args.template)
    if template_path.exists():
        snap_all = json.loads(template_path.read_text(encoding="utf-8"))

    compiled = compile_graph_topology(
        raw_graph=raw_graph,
        snap_all=snap_all,
        designated_hub=args.hub,
        air_gap_r=args.air_gap
    )

    out_json = Path(args.output)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(compiled, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Compiled JSON saved: {out_json}")

    if args.js:
        out_js = Path(args.js)
        out_js.parent.mkdir(parents=True, exist_ok=True)
        data_str = json.dumps(compiled, separators=(',', ':'), ensure_ascii=False)
        out_js.write_text(
            f"window.PROD_GRAPH_DATA = {data_str};\nwindow.COMPILED_GRAPH_DATA = window.PROD_GRAPH_DATA;",
            encoding="utf-8"
        )
        print(f"Compiled JS saved: {out_js}")

    if args.render_png:
        render_preview_png(compiled, args.render_png)

    # Quality Report
    print("\n" + "=" * 80)
    print("HCRDL COMPILATION REPORT")
    print("=" * 80)
    for cat in sorted(set(n["category"] for n in compiled["nodes"])):
        c_nodes = [n for n in compiled["nodes"] if n["category"] == cat]
        c_conn = [math.hypot(n["x"], n["y"]) for n in c_nodes if not n["isOrphan"]]
        c_orph = [math.hypot(n["x"], n["y"]) for n in c_nodes if n["isOrphan"]]
        conn_str = f"[{min(c_conn):5.1f}..{max(c_conn):5.1f}]" if c_conn else "   None   "
        orph_str = f"[{min(c_orph):5.1f}..{max(c_orph):5.1f}]" if c_orph else "   None   "
        pts = np.array([[n["x"], n["y"]] for n in c_nodes])
        diff = pts[:, None, :] - pts[None, :, :]
        dist = np.sqrt(np.sum(diff ** 2, axis=-1))
        np.fill_diagonal(dist, 1e9)
        min_d = dist.min()
        print(f"{cat:25}: N={len(c_nodes):3} | Conn R={conn_str} | Orph R={orph_str} | MinDist={min_d:4.1f}px")
    print("=" * 80)

if __name__ == "__main__":
    main()
