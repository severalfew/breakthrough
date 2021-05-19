import itertools
import numpy as np
import random
from tqdm import tqdm

restrictions = {
    "armor": ["inf", "mech", "reserve", "signal", "artillery"],
    "inf": ["reserve", "anti-tank", "recon", "signal"],
    "mech": ["inf", "reserve", "signal", "helicopter", "artillery"],
    "reserve": ["signal", "recon"],
    "anti-tank": ["armor", "mech"],
    "recon": ["signal"],
    "helicopter": ["armor", "anti-tank", "artillery"],
    # "signal": [],
    "artillery": ["inf", "reserve", "recon"],
    # "anti-air": ["fighter", "bomber"],
    # "fighter": ["helicopter", "bomber"],
    # "bomber": ["armor", "inf", "mech", "reserve", "anti-tank", "recon", "signal", "artillery"],
}

dice = {key: np.random.randint(1, 7, 6) for key in restrictions.keys()}

print(dice)
changes = 0

for i in tqdm(range(100000)):
    u1, u2 = random.sample(dice.keys(), 2)
    u1_should_win = u2 in restrictions[u1]
    if not u1_should_win:
        continue
    u1_wins = np.random.choice(dice[u1]) > np.random.choice(dice[u1])
    if u1_wins:
        dice[u1][random.choices(range(6), k=1, weights=dice[u1])] += 1
        changes += 1

print(changes)
print(dice)

# nsims = 10000
# for u1, u2, in itertools.combinations(dice.keys(), 2):
#     win_perc = sum((np.random.choice(dice[u1])) > np.random.choice(dice[u2]) for x in range(nsims))/nsims
#     print(u1, u2, win_perc)

highest = max(max(x) for x in dice.values())
factor = 1
for i in range(10):
    if i**6 > highest:
        break
    factor = i
for name, die in dice.items():
    print(name, sorted([max(1, int(x)) for x in np.log(die) / np.log([factor for i in range(len(die))])]))
