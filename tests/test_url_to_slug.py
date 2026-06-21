"""Regression tests for url_to_slug uniqueness."""
from collect import url_to_slug


def test_slug_uses_last_3_path_segments_to_avoid_collision():
    # Two Python API pages whose URLs only differ in a parent segment
    # used to collide because only the last segment was taken.
    url_a = "https://docs.isaacsim.omniverse.nvidia.com/latest/isaacsim.core.experimental.prims/config/python_api.html"
    url_b = "https://docs.isaacsim.omniverse.nvidia.com/latest/isaacsim.core.experimental.objects/config/python_api.html"
    assert url_to_slug(url_a) != url_to_slug(url_b)


def test_slug_drops_latest_version_prefix():
    url = "https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/index.html"
    assert url_to_slug(url) == "replicator_tutorials__index"
    assert "latest" not in url_to_slug(url)


def test_slug_strips_html_suffix():
    url = "https://docs.isaacsim.omniverse.nvidia.com/latest/replicator_tutorials/tutorial_replicator_overview.html"
    slug = url_to_slug(url)
    assert not slug.endswith(".html")
    assert slug == "replicator_tutorials__tutorial_replicator_overview"


def test_slug_short_url_falls_back_to_fewer_segments():
    # Root-ish URL with only one or two segments shouldn't crash.
    assert url_to_slug("https://docs.isaacsim.omniverse.nvidia.com/latest/index.html") == "index"
    assert url_to_slug("https://docs.isaacsim.omniverse.nvidia.com/latest/introduction.html") == "introduction"


def test_slug_uniqueness_across_all_manifests(tmp_path):
    """Ensure every page in every existing manifest maps to a unique slug."""
    import json
    from collections import Counter
    from pathlib import Path

    manifests_dir = Path(__file__).resolve().parents[1] / "manifests"
    for f in manifests_dir.glob("*.json"):
        m = json.loads(f.read_text())
        mod = m["module"]
        base = m.get("base_url", "https://docs.isaacsim.omniverse.nvidia.com/latest")
        slugs = []
        for pg in m["pages"]:
            url = pg["url"]
            if url.startswith("/"):
                url = base.rstrip("/") + url
            slugs.append(url_to_slug(url))

        dupes = {s: c for s, c in Counter(slugs).items() if c > 1}
        assert not dupes, f"Module {mod} has slug collisions: {dupes}"
