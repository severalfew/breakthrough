from .constants import COUNTRIES
from .utility import resource_path
import json
import matplotlib.pyplot as plt
import os

with open(os.path.join(resource_path, "location.json"), "r") as fp:
    data = json.load(fp)

for location in data:
    plt.figure(figsize=(2.5, 3.5))
    ax = plt.gca()
    ax.text(
        0.9,
        3.35,
        f"{location['city']}, {location['country']}",
        ha='left',
        va='center',
        fontsize="small"
    )
    ax.text(
        0.9,
        3.1,
        location['addr_state'],
        ha='left',
        va='center',
        fontsize="small"
    )
    ax.text(
        0.9,
        2.85,
        f"Size: {location['city_size']}",
        ha='left',
        va='center',
        fontsize="small"
    )

    plt.imshow(
        COUNTRIES[location['country']].icon,
        extent=[0, .8, 2.7, 3.5]
    )
    # ax.set_axis_off()
    plt.xlim(0, 2.5)
    plt.ylim(0, 3.5)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
    break
