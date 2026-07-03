#!/usr/bin/env python3
"""logtool CLI — archive a named log file.

Usage: python cli.py archive <logname>
"""
import argparse
from logtool.archive import archive


def main() -> int:
    p = argparse.ArgumentParser(prog="logtool")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("archive", help="archive logs/<name> into backups/")
    a.add_argument("name", help="log file name (without path)")
    args = p.parse_args()
    if args.cmd == "archive":
        return archive(args.name)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
