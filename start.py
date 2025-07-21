#!/usr/bin/env python
"""
Simple check for whether gunicorn is available.
"""
import subprocess
import sys

try:
    import gunicorn
    print("Gunicorn is available")
except ImportError:
    print("Gunicorn is not available")
    sys.exit(1)

# Start the Flask app with gunicorn
if __name__ == "__main__":
    subprocess.run([
        "gunicorn", 
        "--bind", "0.0.0.0:$PORT",
        "app:app"
    ])
