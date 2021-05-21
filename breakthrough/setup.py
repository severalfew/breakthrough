from tqdm import tqdm
import geocoder
import json
import os
import pandas as pd


def retrieve_locations():
    location_csv = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources", "locations.csv")
    df = pd.read_csv(location_csv)
    df.sort_values(["team", "country", "name"]).to_csv(location_csv, index=False)
    gen = tqdm(df.iterrows(), total=len(df))
    for i, row in gen:
        location_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "resources", "locations", row["name"] + ".json"
        )
        try:
            with open(location_file, "r") as fp:
                data = json.load(fp)
        except FileNotFoundError:
            data = geocoder.osm(row['name']).osm
        try:
            data["city_size"] = row["city_size"]
        except:
            breakpoint()
        data["team"] = row["team"]
        data["country"] = row["country"]
        if "city" not in data.keys():
            data["city"] = row['name']
        data['display_x'] = data['x'] * 138.15846723809852 - 466.7843618496411
        data['display_y'] = data['y'] * 223.7003946611845 - 11293.081791485833
        for key in list(data.keys()):
            if ":" in key:
                data[key.replace(":", "_")] = data.pop(key)
        with open(location_file, "w") as fp:
            json.dump(data, fp)


if __name__ == "__main__":
    setup_funcs = tqdm([retrieve_locations])
    for func in setup_funcs:
        setup_funcs.set_description(func.__name__)
        func()
