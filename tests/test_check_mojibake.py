from scripts import check_mojibake


def test_find_mojibake_scans_all_raw_modules_and_output(tmp_path):
    raw_file = tmp_path / "source" / "raw" / "11-replicator-core" / "page.md"
    output_file = tmp_path / "output" / "11_Replicator_Core.md"
    raw_file.parent.mkdir(parents=True)
    output_file.parent.mkdir(parents=True)

    raw_file.write_text("NVIDIA Omniverseâ¢ page", encoding="utf-8")
    output_file.write_text("Rotate 90Âº around X", encoding="utf-8")

    findings = check_mojibake.find_mojibake(tmp_path)

    finding_paths = {finding.path.relative_to(tmp_path).as_posix() for finding in findings}
    assert "source/raw/11-replicator-core/page.md" in finding_paths
    assert "output/11_Replicator_Core.md" in finding_paths


def test_find_mojibake_detects_observed_missed_sequences(tmp_path):
    output_file = tmp_path / "output" / "missed.md"
    output_file.parent.mkdir(parents=True)
    output_file.write_text(
        "handâ\x80\x91write left â\x86\x90 right â\x96º down â\x96¼ minus â\x88\x92",
        encoding="utf-8",
    )

    findings = check_mojibake.find_mojibake(tmp_path)

    assert len(findings) == 1
    assert findings[0].count == 5
