#!/usr/bin/env python3
"""Backward-compatible wrapper for check_mojibake.py."""
from check_mojibake import main


if __name__ == "__main__":
    raise SystemExit(main())
