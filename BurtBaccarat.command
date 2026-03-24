#!/usr/bin/env python3

from pathlib import Path
import sys


projectRoot = Path(__file__).resolve().parent
if str(projectRoot) not in sys.path:
	sys.path.insert(0, str(projectRoot))

from burtBaccarat import runCli


if __name__ == "__main__":
	runCli()
