\# Threat Model



\## Covered Attacks



\- Payload modification

\- Event replay

\- Event deletion

\- Chain reordering

\- Cross-org contamination



Detected via:



\- hash mismatch

\- prev\_hash mismatch

\- unique(org\_id,event\_id)



\## Not Covered



\- Root DB compromise

\- Kernel-level tampering

\- Memory attacks

\- Side-channel leakage



Assumption:



Database is writable but not silently forgeable without detection.



LICITRA detects integrity violations after-the-fact.

It does not prevent privileged attackers.

