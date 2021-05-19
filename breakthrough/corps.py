from .constants import COLORS, COUNTRIES, TEAMS
from .units import Unit, UNIT_SIZES, UNIT_TYPES
from .utility import resource_path
from matplotlib import pyplot as plt
from tqdm import tqdm
import matplotlib.patches as patches
import os

division = UNIT_SIZES.division
battallion = UNIT_SIZES.battallion
brigade = UNIT_SIZES.brigade
regiment = UNIT_SIZES.regiment
corps = UNIT_SIZES.corps

infantry = UNIT_TYPES.infantry
artillery = UNIT_TYPES.artillery
armor = UNIT_TYPES.armor
air_defense = UNIT_TYPES.air_defense
airborne = UNIT_TYPES.airborne

nato = TEAMS.NATO
pact = TEAMS.PACT

de = COUNTRIES['DE']
dk = COUNTRIES['DK']
nl = COUNTRIES['NL']
uk = COUNTRIES['UK']

corps = [
    Unit(
        name="Landjut Command",
        size=UNIT_SIZES.corps,
        team=TEAMS.NATO,
        country=COUNTRIES["DK"],
        children=[
            Unit("Jutland Division", division, nato, dk, type=infantry),
            Unit("33rd Artillery Battalion", battallion, nato, dk, type=artillery),
            Unit("650th Rocket Artillery Battalion", battallion, nato, dk, type=artillery),
            Unit("600th Air Defence Regiment", regiment, nato, dk, type=air_defense),
            Unit("Jutland Battle Group", brigade, nato, dk, type=armor),
            Unit("1st Infantry Brigade", brigade, nato, dk, type=infantry),
            Unit("6th Panzergrenadier Division", division, nato, dk, type=infantry),
            Unit("Territorial Command Schleswig-Holstein", brigade, nato, dk, type=infantry)
        ],
        color="royalblue"
    ),
    Unit(
        name="I Netherlands Corps",
        size=corps,
        team=TEAMS.NATO,
        country=COUNTRIES["NL"],
        color="mediumblue",
        children=[
            Unit("1e Divisie", division, nato, nl, type=infantry),
            Unit("3rd Panzer Division", division, nato, nl, type=armor),
            Unit("4e Divisie", division, nato, nl, type=infantry),
            Unit("5e Divisie", division, nato, nl, type=infantry),
            Unit("101e Infanteriebrigade", brigade, nato, nl, type=infantry),
            Unit("1 Corps Artillery", brigade, nato, nl, type=artillery),
        ]
    ),
    Unit(
        name="I German Corps",
        size=corps,
        team=TEAMS.NATO,
        country=COUNTRIES["DE"],
        color="lightsteelblue",
        children=[
            Unit("1st Panzer Division", division, nato, de, type=armor),
            Unit("7th Panzer Division", division, nato, de, type=armor),
            Unit("11th Panzergrenadier Division", division, nato, de, type=infantry),
            Unit("27th Airborne Brigade", brigade, nato, de, type=airborne)
        ]
    ),
    Unit(
        name="I British Corps",
        size=corps,
        team=TEAMS.NATO,
        country=COUNTRIES["UK"],
        color="cornflowerblue",
        children=[
            Unit("1st Armoured Division", division, nato, uk, type=armor),
            Unit("2nd Infantry Division", division, nato, uk, type=infantry),
            Unit("3rd Armoured Division", division, nato, uk, type=armor),
            Unit("4th Armoured Division", division, nato, uk, type=armor),
        ]
    ),
    Unit(
        name="I Belgian Corps",
        size=corps,
        team=TEAMS.NATO,
        country=COUNTRIES["DK"],
        color="darkblue"
    ),
    Unit(
        name="III US Corps",
        size=corps,
        team=TEAMS.NATO,
        country=COUNTRIES["US"],
        color="dodgerblue"
    ),
    Unit(
        name="2nd Guards Tank Army",
        size=corps,
        team=TEAMS.PACT,
        country=COUNTRIES["USSR"],
        color="red"
    ),
    Unit(
        name="3rd Red Banner Army",
        size=corps,
        team=TEAMS.PACT,
        country=COUNTRIES["USSR"],
        color="brown"
    ),
    Unit(
        name="Nationale Volksarmee",
        size=corps,
        team=TEAMS.PACT,
        country=COUNTRIES["DDR"],
        color="indianred"
    ),
    Unit(
        name="Northern Group of Forces",
        size=corps,
        team=TEAMS.PACT,
        country=COUNTRIES["PL"],
        color="tomato"
    ),
    Unit(
        name="11th Guards Army Baltic Command",
        size=corps,
        team=TEAMS.PACT,
        country=COUNTRIES["USSR"],
        color="firebrick"
    ),
    Unit(
        name="1st Czechoslovak People's Army",
        size=corps,
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
        size = child.size.value
        ax.text(
            .45,
            2.1 - .28 * i,
            f"[{size}] {child}",
            ha='left',
            va='center',
            fontsize="x-small"
        )
        ax.add_patch(patches.Rectangle(
            (.1, 2.025 - .28 * i),
            .3,
            .2,
            edgecolor="w",
            facecolor=unit.color,
        ))
        if child.type == infantry:
            plt.plot([.1, .4], [2.025 - .28 * i, 2.225 - .28 * i], color="w")
            plt.plot([.1, .4], [2.225 - .28 * i, 2.025 - .28 * i], color="w")
        elif child.type == armor:
            plt.plot([.2, .3], [2.075 - .28 * i, 2.075 - .28 * i], color="w")
            plt.plot([.2, .3], [2.175 - .28 * i, 2.175 - .28 * i], color="w")
            ax.add_patch(patches.Arc(
                (.2, 2.125 - .28 * i),
                .1,
                .1,
                theta1=90,
                theta2=270,
                color="w"
            ))
            ax.add_patch(patches.Arc(
                (.3, 2.125 - .28 * i),
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
