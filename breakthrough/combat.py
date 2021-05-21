import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from tqdm import tqdm


class Infantry:
    def __init__(self, size=4):
        self.units = [6] * size
        self.die = [1, 2, 3, 4, 5, 6]

    def roll(self):
        rolls = zip([np.random.choice(self.die) for x in self.units], self.units)
        self.units = [x for x, y in rolls if x < y]
        return self.units


class Armor:
    def __init__(self, size=4):
        self.units = [6] * size
        self.die = [1, 2, 3, 4, 5, 6, 7, 8]

    def roll(self):
        rolls = zip([np.random.choice(self.die) for x in self.units], self.units)
        self.units = [x for x, y in rolls if x <= y]
        return self.units


results_inf = []
results_armor = []
for i in tqdm(range(10000)):
    count_inf = 0
    inf = Infantry()
    while len(inf.units):
        inf.roll()
        count_inf += 1
    armor = Armor()
    results_inf.append(count_inf)
    count_armor = 0
    while len(armor.units):
        armor.roll()
        count_armor += 1
    results_armor.append(count_armor)

sns.kdeplot(results_inf, label="Infantry", bw_adjust=3)
sns.kdeplot(results_armor, label="Armor", bw_adjust=3)
plt.legend()
plt.show()
