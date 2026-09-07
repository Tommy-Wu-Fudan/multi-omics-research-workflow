---
name: research-result-trace
description: Audit research claims in manuscripts, methods or review reports, tables and figures against supplied aggregate results or implementation evidence, including model, population, units, multiplicity and version. Use for source-to-claim consistency checks; ordinary grammar edits and new statistical analyses do not need this workflow.
---

# Research result trace

Produce an evidence-linked consistency audit using the supplied artifacts. The task is to establish what each claim is supported by, not to choose new statistical methods or silently repair core results.

## Establish the comparison

Use the user's named manuscript and result package. If identities conflict, record each candidate and inspect lineage (manifest, code/config, result table, run record); do not select a final version from filename, modification time, memory, or a previous audit's PASS alone. Ask only if resolving that conflict is required for the dependent task; continue checks that remain determinate.

Read the minimum relevant aggregate tables and methodological evidence. Exact values come from source tables, not chart coordinates, OCR, or prose. Record original paths and locators; use hashes for the files actually audited when practical. Do not copy individual-level records into the audit.

## Trace claims

For each substantive claim, establish a result identity: exposure/contrast, outcome, population, model/covariates, effect kind, unit, reference, analysis version and multiplicity family. Only require fields relevant to that claim; missing necessary metadata yields unresolved, not an invented default.

Compare estimate, confidence limits, N/events, effect direction, raw P and adjusted P separately. Preserve displayed precision: a rounded value is compatible if the source rounds to that value under the declared rule; inequalities such as P < 0.001 are bounds, not exact numbers. Do not recompute inferential P values from rounded confidence limits.

When handling complex displays or model claims, read [references/decision-cases.md](references/decision-cases.md) for the relevant comparison.

Use these dispositions:

- `supported`: all required source fields support the claim within stated precision.
- `mismatch`: an identified source contradicts a value or semantic claim; cite both locations.
- `unresolved`: required provenance or model metadata is missing/ambiguous.
- `out-of-scope`: checking it requires a new analysis, unavailable participant data, or external scientific validation beyond this audit.

These are audit dispositions, not scientific evidence grades. A supported statement may still describe a weak, exploratory or biased analysis. Source scripts prove implementation text; a report proves what it recorded; actual completed outputs and their lineage are needed for an execution claim. A script's unused option is not evidence it ran.

## Deliver

Write a compact ledger (CSV or Markdown) with claim ID/location, source path and precise locator, result identity, disposition, observed comparison, and required correction/evidence. Report supported controls as well as actionable mismatches so the audit does not manufacture problems. Keep genuine source conflicts visible.

Unless editing was requested, leave all inputs unchanged and supply suggested corrections in the report. If editing was requested, change only authorized manuscript/display content from verified sources and verify the final file. Never modify generated core statistical results by hand.

State what was checked, what was not rerun, and what remains unresolved. Do not turn a consistency check into a new study, a publication approval, or a declaration of causal validity.
