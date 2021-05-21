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
import sys


def dist(n1, n2):
    return np.sqrt((n1['x'] - n2['x']) ** 2 + (n1['y'] - n2['y']))


G = nx.DiGraph()

location_path = os.path.join(resource_path, "locations")

nodes = []
for file in os.listdir(location_path):
    with open(os.path.join(location_path, file), "r") as fp:
        data = json.load(fp)
        G.add_node(data["city"], **data)
        nodes.append(data["city"])

pos = nx.get_node_attributes(G, "x")
for key, value in pos.items():
    pos[key] = (value, G.nodes[key]["y"])

tri = Delaunay(np.array(list(pos.values())))
for simplex in tri.simplices:
    for n1, n2 in itertools.permutations(simplex, r=2):
        if "neighbors" not in G.nodes[nodes[n1]]:
            G.nodes[nodes[n1]]['neighbors'] = []
        if n2 not in G.nodes[nodes[n1]]["neighbors"]:
            G.nodes[nodes[n1]]["neighbors"].append(nodes[n2])

with open(os.path.join(resource_path, "location.json"), "w") as fp:
    json.dump(data, fp)

for i, node in enumerate(nodes):
    for neighbor in G.nodes[node]["neighbors"]:
        G.add_edge(node, neighbor)


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
        extent=[node["x"] - .25, node["x"] - .1, node["y"] - .075, node["y"] + .075]
    )


plt.figure(figsize=(20, 20))
for node in G.nodes:
    draw_location(ax=plt.gca(), node=G.nodes[node])
nx.draw_networkx_edges(
    G,
    pos=pos,
    alpha=.5,
    min_source_margin=10,
    min_target_margin=10,
)
plt.show()
