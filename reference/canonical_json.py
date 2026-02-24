import json
from typing import Any

def canonicalize(obj: Any) -> str:
    """
    Deterministic JSON serialization:
    - keys sorted
    - no extra whitespace
    - UTF-8
    """
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def canonical_bytes(obj: Any) -> bytes:
    return canonicalize(obj).encode("utf-8")
