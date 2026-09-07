---
name: research-display-revision
description: Revise research tables or figures while preserving supplied statistical results, model identities, significance rules and source provenance. Use for layout, labelling or packaging changes to existing result displays; new analyses and ordinary prose edits require a different workflow.
---

# Research display revision

Deliver the requested figure/table change with evidence that retained statistical content and meaning are preserved. Use the existing plotting or document tools appropriate to the format; this skill supplies the scientific comparison and handoff rules, not a new rendering engine.

## Lock the requested change

Read the user's chosen source display and aggregate results, plus relevant code or metadata. Record the input identity and intended output. If an actual source is unavailable, report that limit rather than reconstructing exact estimates from pixels. Preserve originals and work in the requested output location or a separate revision directory.

Distinguish layout changes, label corrections, display selection and statistical reruns. Act on existing authorization. A layout task does not imply permission to change populations, covariates, cutoffs, effect values, displayed inclusion or multiplicity rules. Continue independent layout work if a source issue blocks only a particular claim or panel.

## Preserve the content contract

Record a compact content contract, using existing metadata where available:

- source version/path and result identifiers or stable row keys;
- exposure, outcome, population, model, effect type, unit and reference where relevant;
- estimates, intervals, N/events, raw/adjusted P and significance family;
- included rows/features, display order, headings, captions, footnotes and numbering;
- output formats, intended size and the object types that need to remain editable.

Order changes operate on row identities, not row positions. Preserve missing/not-estimable states. Keep declared rounding separate from underlying numbers. Do not replace raw P with FDR or vice versa to make stars consistent across panels; a documented mixed rule must remain explicit.

Use [references/format-checks.md](references/format-checks.md) only for the target format's checks.

## Revise and check the final artifact

Prefer the original source code/template if it is usable; otherwise rebuild only the authorized display from verified aggregate data. Avoid running analysis code with installation or overwrite side effects merely to regenerate a figure. Statistical plots should remain data driven.

After saving, reopen/parse the output and compare retained values and model semantics against the content contract. For charts, also verify that plotted coordinates, CI endpoints, axis transforms, null/reference lines and row-label associations encode the source values; a copied metadata block or correct text alone is insufficient. For tables, compare values and formulas by stable keys, accounting only for authorized text/format changes.

Render the actual output at its intended size and inspect it for clipped labels, overlaps, unreadable text, missing symbols, aspect distortion and incorrect legends. If a rendering or target-app check is unavailable, record that dimension as unverified; do not use a structure PASS to fill the gap. Fix observed presentation defects and repeat only the affected checks.

## Handoff

Deliver the editable source, requested viewing/submission formats, source-data pointer, and a concise verification note. Distinguish input integrity, numeric/semantic preservation, visual checks, file openability and editable-object verification. File extensions alone do not establish editability or cross-application fidelity.

If core source results conflict, identify the exact conflict and leave the dependent statistical change pending; never manually repair generated core estimates. End with the actual files and any remaining limitations, not a claim that the scientific analysis has been validated.
