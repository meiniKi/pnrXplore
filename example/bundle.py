import sys
import os
from pathlib import Path
from pnrXplore import *
import pnrXplore
import json
from glob import glob

# ----------------- Load Data & Create Bundle ---------------------------------

data_path = Path("./example")
images_path = Path("./example/images")
bundle_path = Path("./example")

with open(data_path / "data.json", "r") as f:
    parsed_data = json.load(f)

bundle = PnrXploreBundle()

# ----------------- Overview Page ---------------------------------------------

psummary = pnrXplore.PnrXploreOverview(
    label="data_summary",
    key="data_overview",
    title="📈 Summary",
)

psummary.add_markdown(
    "This is a **minimal example** to demonstrate pnrXplore and pnrXplore-viewer. It showcases a subset of the available pages and components. Please note that the data used is only for demonstration purposes. To keep this example (and file sizes) small, renderings are only created every 25 iterations, which does not include the final solution. A dummy image replaces some renderings.<br /><br />"
)
psummary.add_markdown("Overview of the Most Relevant Data")

psummary.add_table(
    "Clocks",
    {
        "name": parsed_data["summary"]["clocks"]["names"],
        "freq": parsed_data["summary"]["clocks"]["freq"],
    },
    {"name": "Clock Name", "freq": "Frequency / MHz"},
)

psummary.add_table("Pre-Packing Utilization", parsed_data["summary"]["util_pre"])
psummary.add_table("Utilization", parsed_data["summary"]["util"])
psummary.add_table(
    "Placement",
    parsed_data["summary"]["place"],
    {"names": "", "data": "Value", "visu": ["LineChartColumn", "Progress"]},
)
psummary.add_table(
    "Routing",
    parsed_data["summary"]["route"],
    {"names": "", "data": "Value", "overused": ["LineChartColumn", "Progress"]},
)

bundle.add_page(psummary)


# ----------------- Notes Page ------------------------------------------------

bundle.add_page(
    pnrXplore.PnrXploreNotes(
        title="📝 Generic Notes",
        label="generic_notes",
        key="generic_notes",
        markdown="This example demonstrates how pnrXplore can be used.",
    )
)

bundle.add_page(
    pnrXplore.PnrXploreNotes(
        title="📝 Exciting News",
        label="exciting_news",
        key="another_notes_page",
        markdown="""There are some exciting insights in the next pages 🙌
```Python
#You can also paste some code here
def exciting_change_in_pnr():
    pass
```
        """,
    )
)


# ----------------- Placer Dashboard ------------------------------------------

page = PnrXplorePage(
    label="placer_plots",
    key="placer_dashboard",
    title="📌 Placer Plots",
)

iter_sel_key = "placer_dashboard_sel_iter"
group_sel_key = "placer_dashboard_sel_group"

page.add_component(
    pnrXplore.PnrXploreControlSliderSelect(
        label="Iteration",
        key=iter_sel_key,
        options=parsed_data["placer"]["iter_sel"],
    )
)

page.add_component(
    pnrXplore.PnrXploreControlBoxSelect(
        label="Group",
        key=group_sel_key,
        options=parsed_data["placer"]["group_names"],
    )
)

dashboard = pnrXplore.PnrXploreDashboard()

plot = pnrXplore.PnrXploreDashLine(
    label="HWPL",
    x=0,
    y=0,
    w=4,
    h=2,
    dragable=True,
    resizable=True,
    key="placer_hpwl_over_iter",
    color="hsl(182, 70%, 50%)",
    data_key="HPWL",
    data=[
        {"x": x, "y": y}
        for (x, y) in zip(
            parsed_data["placer"]["iter_labels"], parsed_data["placer"]["hpwl"]
        )
    ],
)
plot.add_dynamic_marker("x", value_key=iter_sel_key)
dashboard.add_item(plot)

plot = pnrXplore.PnrXploreDashLine(
    label="Phi",
    x=4,
    y=0,
    w=4,
    h=2,
    dragable=True,
    resizable=True,
    key="placer_energy_over_iter",
    color="hsl(182, 70%, 50%)",
    data_key="Phi",
    data=[
        {"x": x, "y": y}
        for (x, y) in zip(
            parsed_data["placer"]["iter_labels"], parsed_data["placer"]["phi"]
        )
    ],
)
plot.add_dynamic_marker("x", value_key=iter_sel_key)
dashboard.add_item(plot)

plot = pnrXplore.PnrXploreDashLine(
    label="Step Length",
    x=0,
    y=3,
    w=4,
    h=2,
    dragable=True,
    resizable=True,
    key="placer_steplen_over_iter",
    color="hsl(182, 70%, 50%)",
    data_key="Steplen",
    data=[
        {"x": x, "y": y}
        for (x, y) in zip(
            parsed_data["placer"]["iter_labels"], parsed_data["placer"]["steplen"]
        )
    ],
)
plot.add_dynamic_marker("x", value_key=iter_sel_key)
dashboard.add_item(plot)

plot = pnrXplore.PnrXploreDashLine(
    label="Overlaps",
    key="placer_overlap_over_iter",
    x=4,
    y=4,
    w=4,
    h=2,
    dragable=True,
    resizable=True,
)
plot.add_dynamic_marker("x", value_key=iter_sel_key)

for l in parsed_data["placer"]["group_names"]:
    plot.add_trace(
        data_key=l,
        color="hsl(182, 70%, 50%)",
        data=[
            {"x": x, "y": y}
            for (x, y) in zip(
                parsed_data["placer"]["iter_labels"],
                parsed_data["placer"]["overlaps"][l],
            )
        ],
    )
dashboard.add_item(plot)

dashboard.add_item(
    pnrXplore.PnrXploreDashStateImage(
        label="Render",
        x=9,
        y=10,
        w=3,
        h=3,
        dragable=True,
        resizable=True,
        key="placer_render_image",
        images=list(glob(str(images_path) + "/placement/*.png", recursive=True)),
        format_template="pos_%s_%03d.png",
        format_keys=[("str", group_sel_key), ("int", iter_sel_key)],
    )
)
page.add_component(dashboard)
bundle.add_page(page)


# ----------------- Placer Renderings -----------------------------------------

page = pnrXplore.PnrXplorePage(
    label="placer_renders",
    key="placer_images",
    title="📌 Placer Renders",
)

iter_sel_key = "placer_images_sel_iter"
group_sel_key = "placer_images_sel_group"

page.add_component(
    pnrXplore.PnrXploreControlSliderSelect(
        label="Iteration",
        key=iter_sel_key,
        options=parsed_data["placer_renders"]["iter_labels"],
    )
)

page.add_component(
    pnrXplore.PnrXploreControlBoxSelect(
        label="Group",
        key=group_sel_key,
        options=parsed_data["placer_renders"]["group_names"],
    )
)

dashboard = pnrXplore.PnrXploreDashboard()

# state = [("str", group_sel_key), ("int", iter_sel_key)]
state = []
# This is replaced by a dummy image, thus, no state is required

items_2d = [
    (
        "Phi 2D",
        0,
        0,
        2,
        2,
        "pstate_image_2d",
        images_path / "placeholder/placeholder.png",
        "placeholder.png",  # "phi_2d_%s_%03d.png",
        state,
    ),
    (
        "Fx 2D",
        2,
        0,
        2,
        2,
        "pstate_image_fx2d",
        images_path / "placeholder/placeholder.png",
        "placeholder.png",  # "fx_2d_%s_%03d.png",
        state,
    ),
    (
        "Fy 2D",
        4,
        0,
        2,
        2,
        "pstate_image_fy2d",
        images_path / "placeholder/placeholder.png",
        "placeholder.png",  # "fy_2d_%s_%03d.png",
        state,
    ),
    (
        "Density",
        4,
        2,
        2,
        2,
        "pstate_image_density",
        images_path / "placeholder/placeholder.png",
        "placeholder.png",  # "density_2d_%s_%03d.png",
        state,
    ),
]

items_3d = [
    (
        "Phi 3D",
        0,
        4,
        2,
        2,
        "pstate_image_phi3d",
        images_path / "placeholder/placeholder.png",
        "placeholder.png",  # "phi_3d_%s_%03d.png",
        state,
    ),
    (
        "Fx 3D",
        2,
        4,
        2,
        2,
        "pstate_image_fx3d",
        images_path / "placeholder/placeholder.png",
        "placeholder.png",  # "fx_3d_%s_%03d.png",
        state,
    ),
    (
        "Fy 3D",
        4,
        4,
        2,
        2,
        "pstate_image_fy3d",
        images_path / "placeholder/placeholder.png",
        "placeholder.png",  # "fy_3d_%s_%03d.png",
        state,
    ),
]

for i in items_2d + items_3d:
    dashboard.add_item(
        pnrXplore.PnrXploreDashStateImage(
            label=i[0],
            x=i[1],
            y=i[2],
            w=i[3],
            h=i[4],
            dragable=True,
            resizable=True,
            key=i[5],
            images=list(glob(str(i[6]) + "*", recursive=True)),
            format_template=i[7],
            format_keys=i[8],
        )
    )

page.add_component(dashboard)
bundle.add_page(page)

# ----------------- Router Dashboard -----------------------------------------

page = pnrXplore.PnrXplorePage(
    label="router_plots",
    key="router_dashboard",
    title="📌 Router Plots",
)

dashboard = pnrXplore.PnrXploreDashboard()

plot = pnrXplore.PnrXploreDashLine(
    label="Overuse",
    x=0,
    y=0,
    w=4,
    h=4,
    dragable=True,
    resizable=True,
    key="router_overuse_over_iter",
    color="hsl(182, 70%, 50%)",
    data_key="HPWL",
    data=[
        {"x": x, "y": y}
        for (x, y) in zip(
            parsed_data["placer_renders"]["iter_labels"],
            parsed_data["router"]["overuse"],
        )
    ],
)
dashboard.add_item(plot)

page.add_component(dashboard)
bundle.add_page(page)


# ----------------- Playground ------------------------------------------------
# Warning: not sand-boxed; this is insecure in untrusted environments!!!

default_code = """
print("Pages: {}".format(get_pages()))

d = get_page_data("pstatic_plots")


data = d["components"]["dashboard"][0]["item_content"]["data"][0]["data"]

x = [e["x"] for e in data]
y = [e["y"] for e in data]

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)
"""

bundle.add_page(
    pnrXplore.PnrXplorePlayground(
        title="🎨 Playground",
        label="playground",
        key="playground1",
        code=default_code,
    )
)

# ----------------- Nextpnr Viewer (experimental) -----------------------------

bundle.add_page(
    pnrXplore.PnrXploreNextpnrViewer(
        title="🔍 nextpnr Viewer",
        label="nextpnr_viewer",
        key="nextpnr_viewer",
        family="ecp5",
        device="25k",
        json_file=(data_path / "routed.json").absolute(),
    )
)

# ----------------- Write Bundle ----------------------------------------------

bundle.archive(bundle_path, format="tar", keep_tmp=False)
