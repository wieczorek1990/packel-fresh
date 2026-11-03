from typing import List


def read_hosts(file_path: str) -> List[str]:
    """Read a file and return a list of non-empty, stripped lines."""
    with open(file_path) as file:
        return [line.strip() for line in file if line.strip()]


def read_single_host(file_path: str) -> str:
    """Read a file and return the first non-empty, stripped line."""
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                return line
    return ""
