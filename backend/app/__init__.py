"""Backend package initialization."""

from pathlib import Path
import sys

# Ensure the project root is on the Python path so that the ``shared`` package
# can be imported when running the app with ``--app-dir backend``.
ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))