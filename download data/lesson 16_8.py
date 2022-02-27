import json

filename = 'data/6064e16ed34eff1443414d84.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:

    json.dump(all_eq_data, f, indent=4)