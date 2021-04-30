from .constants import COLORS, COUNTRIES
from .utility import resource_path
from scipy.spatial import Delaunay
from tqdm import tqdm
import itertools
import json
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os


def dist(n1, n2):
    return np.sqrt((n1['x'] - n2['x']) ** 2 + (n1['y'] - n2['y']))


G = nx.DiGraph()

location_path = os.path.join(resource_path, "location.json")

nodes = []
with open(location_path, "r") as fp:
    data = json.load(fp)
    for node in data:
        G.add_node(node["city"], **node)
        nodes.append(node["city"])

pos = nx.get_node_attributes(G, "x")
for key, value in pos.items():
    pos[key] = (value, G.nodes[key]["y"])

# tri = Delaunay(np.array(list(pos.values())))
# for simplex in tri.simplices:
#     for n1, n2 in itertools.permutations(simplex, r=2):
#         if "neighbors" not in data[n1].keys():
#             data[n1]["neighbors"] = []
#         if n2 not in data[n1]["neighbors"]:
#             data[n1]["neighbors"].append(int(n2))
#
# with open(location_path, "w") as fp:
#     json.dump(data, fp)

for i, node in enumerate(data):
    for neighbor in node['neighbors']:
        G.add_edge(node['city'], nodes[neighbor])


def draw_location(ax, node):
    ax.add_patch(patches.Rectangle(
        (node['x'] - .1, node['y'] - .075),
        .375,
        .15,
        facecolor=[x / 255 for x in getattr(COLORS, node["team"]).value]
    ))
    ax.text(
        node['x'] - .0625,
        node['y'],
        f"{node['city']}\n{node['country']} {node['city_size']}",
        ha='left',
        va='center',
        fontsize="xx-small"
    ),
    plt.imshow(
        COUNTRIES[node['country']].icon,
        extent=[node["x"]-.25, node["x"]-.1, node["y"]-.075, node["y"]+.075]
    )


plt.figure(figsize=(20, 20))
for node in data:
    draw_location(ax=plt.gca(), node=node)
nx.draw_networkx_edges(
    G,
    pos=pos,
    alpha=.5,
    min_source_margin=10,
    min_target_margin=10,
)
plt.show()
