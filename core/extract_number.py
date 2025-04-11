import re
from pathlib import Path


def extract_number(p: Path) -> int:
    match = re.search(r'\d+', p.stem)
    return int(match.group()) if match else 0