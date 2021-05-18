from .constants import COLORS, COUNTRIES, TEAMS
from .units import Unit, UNIT_SIZES, UNIT_TYPES
from .utility import resource_path
from matplotlib import pyplot as plt
from tqdm import tqdm
import matplotlib.patches as patches
import os

corps = [
    Unit(
        name="Landjut Command",
        size=UNIT_SIZES.corps,
        team=TEAMS.NATO,
        country=COUNTRIES["DK"],
        children=[
            Unit("Jutland Division", size=UNIT_SIZES.division, type=UNIT_TYPES.infantry),
            "Armored Division (Armor)"
        ],
        color="royalblue"
    ),
    Unit(
        name="I Netherlands Corps",
        size=UNIT_SIZES.corps,
        team=TEAMS.NATO,
        country=COUNTRIES["NL"],
        color="mediumblue"
    ),
    Unit(
        name="I German Corps",
        size=UNIT_SIZES.corps,
        team=TEAMS.NATO,
        country=COUNTRIES["DE"],
        color="lightsteelblue"
    ),
    Unit(
        name="I British Corps",
        size=UNIT_SIZES.corps,
        team=TEAMS.NATO,
        country=COUNTRIES["UK"],
        color="cornflowerblue"
    ),
    Unit(
        name="I Belgian Corps",
        size=UNIT_SIZES.corps,
        team=TEAMS.NATO,
        country=COUNTRIES["DK"],
        color="darkblue"
    ),
    Unit(
        name="III US Corps",
        size=UNIT_SIZES.corps,
        team=TEAMS.NATO,
        country=COUNTRIES["US"],
        color="dodgerblue"
    ),
    Unit(
        name="2nd Guards Tank Army",
        size=UNIT_SIZES.corps,
        team=TEAMS.PACT,
        country=COUNTRIES["USSR"],
        color="red"
    ),
    Unit(
        name="3rd Red Banner Army",
        size=UNIT_SIZES.corps,
        team=TEAMS.PACT,
        country=COUNTRIES["USSR"],
        color="brown"
    ),
    Unit(
        name="Nationale Volksarmee",
        size=UNIT_SIZES.corps,
        team=TEAMS.PACT,
        country=COUNTRIES["DDR"],
        color="indianred"
    ),
    Unit(
        name="Northern Group of Forces",
        size=UNIT_SIZES.corps,
        team=TEAMS.PACT,
        country=COUNTRIES["PL"],
        color="tomato"
    ),
    Unit(
        name="11th Guards Army Baltic Command",
        size=UNIT_SIZES.corps,
        team=TEAMS.PACT,
        country=COUNTRIES["USSR"],
        color="firebrick"
    ),
    Unit(
        name="1st Czechoslovak People's Army",
        size=UNIT_SIZES.corps,
        team=TEAMS.PACT,
        country=COUNTRIES["CZ"],
        color="salmon"
    ),
]

image_path = os.path.join(resource_path, "units")
os.makedirs(image_path, exist_ok=True)
gen = tqdm(corps)
for unit in gen:
    gen.set_description(unit.name)
    plt.figure(figsize=(2.5, 3.5))
    ax = plt.gca()
    ax.add_patch(patches.Rectangle(
        (0, 2.3),
        2.5,
        .4,
        facecolor=unit.color,
    ))
    ax.text(
        0.9,
        3.35,
        unit.name,
        ha='left',
        va='center',
        fontsize="small"
    )
    ax.text(
        0.9,
        3.1,
        str(unit.country.name),
        ha='left',
        va='center',
        fontsize="small"
    )
    plt.axhline(2.7, color='k')
    ax.text(
        .1,
        2.5,
        "Composition",
        ha='left',
        va='center',
        fontsize="small"
    )
    plt.axhline(2.3, color='k', alpha=.5)
    plt.imshow(
        COUNTRIES[unit.country.code].icon,
        extent=[0, .8, 2.7, 3.5]
    )

    for i, child in enumerate(unit.children):
        rgb = [x / 255 for x in getattr(COLORS, unit.team.name).value]
        size = 0
        for s in UNIT_SIZES:
            if s.name in child.lower():
                size = s.value
                break
        ax.text(
            .45,
            2.1 - .3 * i,
            f"[{size}] {child}",
            ha='left',
            va='center',
            fontsize="small"
        )
        ax.add_patch(patches.Rectangle(
            (.1, 2.025 - .3 * i),
            .3,
            .2,
            edgecolor="w",
            facecolor=unit.color,
        ))
        if "Infantry" in child:
            plt.plot([.1, .4], [2.025 - .3 * i, 2.225 - .3 * i], color="w")
            plt.plot([.1, .4], [2.225 - .3 * i, 2.025 - .3 * i], color="w")
        elif "Armor" in child:
            plt.plot([.2, .3], [2.075 - .3 * i, 2.075 - .3 * i], color="w")
            plt.plot([.2, .3], [2.175 - .3 * i, 2.175 - .3 * i], color="w")
            ax.add_patch(patches.Arc(
                (.2, 2.125 - .3 * i),
                .1,
                .1,
                theta1=90,
                theta2=270,
                color="w"
            ))
            ax.add_patch(patches.Arc(
                (.3, 2.125 - .3 * i),
                .1,
                .1,
                theta1=270,
                theta2=90,
                color="w"
            ))

    # ax.set_axis_off()
    plt.xlim(0, 2.5)
    plt.ylim(0, 3.5)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.savefig(f"{os.path.join(image_path, unit.name)}.png")
