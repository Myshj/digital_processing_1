import json
import math


if __name__ == '__main__':
    with open("data.json") as data_file:
        data_dict = json.load(data_file)

    if not isinstance(data_dict, dict):
        raise ValueError()

    x = data_dict.get('x', 0.0)
    y0 = data_dict.get('y0', 0.0)
    delta_max = data_dict.get('delta_max', 0.0)
    w = data_dict.get('w', 0.0)
    i = 0

    results = []

    while True:
        y_mod = 1 / (1 + math.exp(-x * w))

        delta = abs((y0 - y_mod)/y0)

        results.append({
            'i': i,
            'y_mod': y_mod,
            'delta': delta
        })

        if delta < delta_max: break

        delta_i = y_mod * (1 - y_mod) * (y0 - y_mod)

        delta_w = x * delta_i

        w += delta_w

        i += 1

    with open('results.json', 'w') as results_file:
        json.dump(results, results_file,indent=2)
