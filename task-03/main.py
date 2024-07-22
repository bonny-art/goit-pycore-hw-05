"""
Log file processing script.

Reads a log file, counts log levels, and optionally filters logs by a specified log level.
"""

import sys
from typing import List, Dict, Optional
from pathlib import Path

from load_logs import load_logs
from count_logs_by_level import count_logs_by_level
from display_log_counts import display_log_counts
from print_logs_by_level import print_logs_by_level

def main() -> None:
    """
    Main function for log file processing. Reads a log file, counts
    log levels, and optionally filters by a specified log level.

    Usage:
        python main.py <logfile_path> [log_level]

    Args:
        None. Command line arguments are used:
            logfile_path (str): Path to the log file.
            log_level (Optional[str]): Optional log level to filter logs (e.g., INFO, ERROR).

    Raises:
        SystemExit: If the log file path is not provided or the file is not found.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <logfile_path> [log_level]")
        sys.exit(1)

    logfile_path: str = sys.argv[1]
    log_level: Optional[str] = sys.argv[2].upper() if len(sys.argv) > 2 else None

    if not Path(logfile_path).is_file():
        print(f"File not found: {logfile_path}")
        sys.exit(1)

    logs: List[Dict[str, str]] = load_logs(logfile_path)

    log_counts: Dict[str, int] = count_logs_by_level(logs)

    display_log_counts(log_counts, log_level)

    if log_level:
        print_logs_by_level(logs, log_level)

if __name__ == "__main__":
    main()
