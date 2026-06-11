"""
Master execution script for Bluestock Mutual Fund Analytics Capstone.
Runs the main project pipeline steps.
"""

import subprocess
import sys


def run_script(script_path):
    """Run a Python script and show its status."""
    print(f"\nRunning {script_path}...")
    result = subprocess.run([sys.executable, script_path])

    if result.returncode == 0:
        print(f"Completed: {script_path}")
    else:
        print(f"Failed: {script_path}")


def main():
    """Execute project scripts in order."""
    scripts = [
        "scripts/data_ingestion.py",
        "scripts/data_cleaning.py",
        "scripts/load_sqlite.py",
        "scripts/recommender.py",
    ]

    for script in scripts:
        run_script(script)

    print("\nPipeline execution finished.")


if __name__ == "__main__":
    main()