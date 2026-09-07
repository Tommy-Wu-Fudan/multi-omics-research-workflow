# Targeted format checks

## Tables / workbooks

Identify the intended data worksheet by its title and structure, not just its tab name; helper model-log sheets should not become separate publication tables. Snapshot cell values, formulas, table notes, row identities and the relevant format properties before merging or reordering.

Compare numeric/formula content separately from authorized textual edits and layout. A changed ZIP hash or style ID does not imply changed statistics. Formula preservation does not prove recalculation; record whether cached results or native recalculation were verified. Check row/column sizes, merged cells, footnotes and index navigation in the rendered output.

Renumbering needs an old-to-new mapping for worksheet titles, Index, manuscript callouts and supplemental captions. Only remove sheets or rows when the request authorizes that selection. Large omics tables may be better delivered as spreadsheets rather than thousands of printed PDF pages.

## Statistical figures

For ratio estimates, verify the log-axis mapping and the null value 1; for beta/difference scales verify the stated transform and null value. Match each plotted interval and marker to the correct source row after ordering. Preserve clipped-interval indicators when the display range cannot show a full interval.

Volcano/heatmap legends must specify which statistic drives color or stars. Check model-specific exceptions, units, log bases, threshold inequalities and whether selection represents the full set or a subset. Inclusive overlap counts and mutually exclusive intersections are different data.

## SVG, PDF, PPT and document packaging

Inspect object types: native text, paths/shapes, raster pictures and linked assets. Fonts converted to paths are not text-editable; a raster inside SVG/PPT is not internally vector-editable. Describe mixed output accurately. Test a target application's import only if that behavior is required and the app is available.

Embedding figures in Word requires legible actual size, preserved aspect ratio, correct caption/source association, valid links/bookmarks and page breaks. Preserve citation/revision fields if they are part of the requested artifact. A successful parse or native pagination check is not a full visual inspection.
