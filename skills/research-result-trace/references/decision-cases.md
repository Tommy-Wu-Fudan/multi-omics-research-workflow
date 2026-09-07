# Comparisons requiring semantic checks

Read only the case relevant to the supplied claim.

| Case | Required distinction |
|---|---|
| Logistic versus Cox | Binary outcome with a continuous feature predictor yields an OR per feature unit; time-to-event models may yield HR. Equal numbers do not make the labels interchangeable. |
| Model variants | Full adjustment, component-excluded sensitivity, sex-specific or alternative covariate models have different identities. Do not transfer a result across them. |
| Multiple testing | A nominal P cannot support an FDR-significance claim. Record the source family and adjusted value; values below 0.05 in a different family are not substitutes. |
| Not estimable | Distinguish no eligible instruments, zero events, failed fit, not run, not applicable and missing source. None is a null effect estimate. |
| MR scale | A binary trait may have raw linear-model beta rather than log odds. Require source-scale metadata before supporting a per-doubling odds statement. |
| Set counts | Compare inclusive/exclusive intersections, all-significant versus direction-concordant sets, and selected display versus full set. Count directions and members using the stated rule. |
| Execution claims | A proposed plan, successful document generator or passing text check does not prove statistical rerunning. A later audit can retract an earlier accusation; inspect actual code lineage. |
| Scientific language | Association does not establish causality, independent replication, mediation or tissue origin. A functional network or shared locus alone cannot support those stronger claims. |
| Figure numbering | Stable artifact identity and current display number differ. Use the user's selected delivery package and its mapping. |
| Formula or preprocessing claims | Trace actual fields, units, column membership and sequence. Fixed column positions alone do not establish biological feature identity; a code comment can be stale. |

Uncertainty in one clause does not invalidate a separately checkable number. Split compound claims when their dispositions differ. If sources conflict, describe the disagreement and the evidence needed to choose; do not silently correct one authoritative-looking artifact from another.
