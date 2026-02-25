\# Cryptographic Proof Summary



LICITRA implements an append-only hash chain:



current\_hash = SHA256(prev\_hash || canonical\_json(payload))



Each organization maintains an independent chain.



Verification recomputes the full chain from GENESIS.



Tampering scenarios detected:



\- payload mutation

\- prev\_hash overwrite

\- deletion / reordering

\- replay (duplicate event\_id)



Evidence bundles include:



\- verify report

\- full event chain

\- rollback decision

\- timestamp

\- SHA256 checksum



PDF exports include:



\- event count

\- first/last hashes

\- tail chain link proof

\- bundle checksum



All experiments are reproducible via scripts in this repository.

