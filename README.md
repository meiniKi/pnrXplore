# pnrXplore

pnrXplore is a Python package to bundle data from CAD and EDA physical design implementation (e.g., place & route) for pnrXplore-viewer. Take a look at [pnrXplore-viewer](https://github.com/meiniKi/pnrXplore-viewer) for more information.

> [!TIP]
> More information can be found [here](https://github.com/meiniKi/pnrXplore-viewer).


## Quick Start

The best starting point is the provided example in [bundle.py](example/bundle.py). Running the example provides a bundle that can be uploaded to the viewer.

Optional: install the package in a virtual environment, as in the snippet below.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python example/bundle.py
```

### Templates

<table>
<tr>
<th>Description</th>
<th>Code</th>
</tr>

<tr> <td>
<b>Overview:</b> Summary page template to overview the most relevant data.
</td> <td>

```python
p = PnrXploreOverview(
    label="data_summary",
    key="data_overview",
    title="📈 Placement Summary"
)

p.add_markdown("Summary")
p.add_table("Title", data, vis)
```
</td> </tr>


<tr> <td>
<b>Notes:</b> Page for notes such as the key ideas or modifications in the implementation run. It supports Markdown syntax elements, such as tables. The text can be edited by pnrXplore-viewer.
</td> <td>

```python
PnrXploreNotes(
    title="📝 Notes",
    label="generic_notes",
    key="generic_notes",
    markdown="Initial Markdown text."
)
```
</td> </tr>


<tr> <td>
<b>Playground:</b> Python playground to run Python code in pnrXplore-viewer. It can print or plot data on the provided bundle during discussions or explorations. Note that the execution environment currently is not sandboxed and, thus, cannot be used in untrusted environments.
</td> <td>

```python
PnrXplorePlayground(
    title="🎨 Playground",
    label="playground",
    key="playground1",
    code=default_code
)
```
</td> </tr>


<tr> <td>
<b>nextpnr Viewer:</b> Render the FPGA architecture layout and overlay the implemented design by embedding nextpnr-viewer.
</td> <td>

```python
PnrXploreNextpnrViewer(
    title="🔍 nextpnr Viewer",
    label="nextpnr_viewer",
    key="nextpnr_viewer",
    family="ecp5",
    device="25k",
    json_file="routed.json"
)
```
</td> </tr>
</table>

### Components

<table>
<tr>
<th>Description</th>
<th>Code</th>
</tr>

<tr> <td>
<b>Slider:</b> Slider to, e.g., select a system state.
</td> <td>

```python
PnrXploreControlSliderSelect(
    label="Iteration",
    key=iter_sel_key,
    options=slider_options
)
```
</td> </tr>

<tr> <td>
<b>Drop-down List:</b> Drop-down to, e.g., select a system state.
</td> <td>

```python
PnrXploreControlBoxSelect(
    label="Group",
    key=group_sel_key,
    options=select_options
)
```
</td> </tr>

<tr> <td>
<b>Line Plot:</b> Dashboard item to plot data in a line plot. It is initialized with a specific size and position. Optionally, markers can be overlayed to show the currently selected state.
</td> <td>

```python
p = PnrXploreDashLine(
    label="HWPL", x=0, y=0, w=4, h=2,
    dragable=True,
    resizable=True,
    key="placer_hpwl_over_iter",
    color="hsl(182, 70%, 50%)",
    data_key="HPWL",
    data=data
)
p.add_dynamic_marker("x", value_key=iter_sel_key)
```
</td> </tr>

<tr> <td>
<b>State Image:</b> An image that corresponds to the selected state, e.g., a rendering.
</td> <td>

```python
pnrXplore.PnrXploreDashStateImage(
    label="Render", x=9, y=10, w=3, h=3,
    dragable=True,
    resizable=True,
    key="placer_render_image",
    images=images_list,
    format_template="pos_%s_%03d.png",
    format_keys=[("str", group_sel_key), ("int", iter_sel_key)])
```

</td> </tr>

</table>

For more examples see [bundle.py](example/bundle.py).