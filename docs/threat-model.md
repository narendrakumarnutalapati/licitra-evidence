# Threat Model

This document outlines the integrity threats LICITRA is designed to detect, and the assumptions under which it operates.

---

## Covered Attacks

LICITRA detects the following runtime integrity violations:

- Payload modification  
- Event replay (duplicate event_id)  
- Event deletion  
- Chain reordering  
- Cross-organization contamination  

Detection mechanisms:

- SHA-256 hash mismatch  
- Previous-hash mismatch  
- Database uniqueness constraint on (org_id, event_id)  

Any modification to historical records breaks the chain and is surfaced during verification.

---

## Not Covered

LICITRA does NOT attempt to defend against:

- Root database compromise  
- Kernel-level tampering  
- In-memory attacks  
- Side-channel leakage  

These are outside the scope of an application-layer integrity primitive.

---

## Assumptions

- Database storage may be writable by attackers  
- Attackers cannot silently forge a full hash chain without detection  

---

## Security Model

LICITRA provides *after-the-fact* integrity verification.

It detects historical manipulation deterministically.

It does not attempt to prevent privileged attackers.

---

LICITRA is designed as a cryptographic runtime evidence layer — not a complete security system.
