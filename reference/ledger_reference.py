import hashlib
from dataclasses import dataclass
from typing import Any, Dict, Optional

from .canonical_json import canonical_bytes

GENESIS_HASH = "GENESIS"

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def compute_event_hash(event: Dict[str, Any]) -> str:
    """
    Hash the canonical JSON bytes of the event record.
    The record includes prev_hash so this forms a hash chain.
    """
    return sha256_hex(canonical_bytes(event))

@dataclass
class LedgerEvent:
    org_id: str
    event_id: str
    prev_hash: str
    payload: Dict[str, Any]
    current_hash: str

class InMemoryLedger:
    """
    MVP ledger implementation (in-memory).
    Replace with Postgres later without changing the API surface.
    """
    def __init__(self) -> None:
        self._by_org: Dict[str, list[LedgerEvent]] = {}

    def last_hash(self, org_id: str) -> str:
        events = self._by_org.get(org_id, [])
        return events[-1].current_hash if events else GENESIS_HASH

    def append(self, org_id: str, event_id: str, payload: Dict[str, Any]) -> LedgerEvent:
        prev = self.last_hash(org_id)
        record = {
            "org_id": org_id,
            "event_id": event_id,
            "prev_hash": prev,
            "payload": payload,
        }
        cur = compute_event_hash(record)
        ev = LedgerEvent(org_id=org_id, event_id=event_id, prev_hash=prev, payload=payload, current_hash=cur)
        self._by_org.setdefault(org_id, []).append(ev)
        return ev

    def get_event(self, org_id: str, event_id: str) -> Optional[LedgerEvent]:
        for ev in self._by_org.get(org_id, []):
            if ev.event_id == event_id:
                return ev
        return None

    def tamper_payload(self, org_id: str, event_id: str, new_payload: Dict[str, Any]) -> bool:
        """
        For experiments: mutate stored payload to simulate tampering.
        (Does NOT recompute hash, so verify should fail.)
        """
        ev = self.get_event(org_id, event_id)
        if not ev:
            return False
        ev.payload = new_payload
        return True

    def verify(self, org_id: str) -> Dict[str, Any]:
        events = self._by_org.get(org_id, [])
        if not events:
            return {"org_id": org_id, "ok": True, "count": 0, "message": "no events"}

        prev = GENESIS_HASH
        for idx, ev in enumerate(events):
            if ev.prev_hash != prev:
                return {"org_id": org_id, "ok": False, "count": len(events), "bad_index": idx, "reason": "prev_hash_mismatch"}

            record = {
                "org_id": ev.org_id,
                "event_id": ev.event_id,
                "prev_hash": ev.prev_hash,
                "payload": ev.payload,
            }
            expected = compute_event_hash(record)
            if ev.current_hash != expected:
                return {"org_id": org_id, "ok": False, "count": len(events), "bad_index": idx, "reason": "hash_mismatch"}

            prev = ev.current_hash

        return {"org_id": org_id, "ok": True, "count": len(events)}
