import json
import math


if __name__ == '__main__':
    with open("data_2.json") as data_file:
        data_dict = json.load(data_file)

    if not isinstance(data_dict, dict):
        raise ValueError()

    x = data_dict.get('x', 0.0)
    y0 = data_dict.get('y0', 0.0)
    delta_max = data_dict.get('delta_max', 0.0)
    w_2_3 = data_dict.get('w_2_3', 0.0)
    w_1_2 = data_dict.get('w_1_2', 0.0)
    i = 0

    results = []

    while True:
        y1 = x
        x2 = y1
        y2 = 1 / (1 + math.exp(-x2 * w_1_2))
        x3 = y2
        y3 = 1 / (1 + math.exp(-x3 * w_2_3))
        y_mod = y3

        delta = abs((y0 - y_mod)/y0)

        results.append({
            'i': i,
            'y_mod': y_mod,
            'delta': delta,
            'w_2_3': w_2_3,
            'w_1_2': w_1_2
        })

        if delta < delta_max: break

        delta_3 = y_mod * (1 - y_mod) * (y0 - y_mod)

        delta_w_2_3 = x3 * delta_3

        w_2_3 += delta_w_2_3

        delta_2 = y1 * (1 - y2) * delta_3 * w_2_3

        delta_w_1_2 = x2 * delta_2

        w_1_2 += delta_w_1_2

        i += 1

    with open('results_2.json', 'w') as results_file:
        json.dump(results, results_file,indent=2)
