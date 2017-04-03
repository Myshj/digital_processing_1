import math

x1 = 0.5
x2 = 0.5
y0 = 0.5
delta_max = 0.1

w = {
    1: {
        "0_1": 0.5,
        "0_2": 0.5,
        "0_3": 0.5,
        "1_1": 0.5,
        "1_2": 0.5,
        "1_3": 0.5,
        "2_1": 0.5,
        "2_2": 0.5,
        "2_3": 0.5,

    },
    2: {
        "0_1": 0.5,
        "1_1": 0.5,
        "2_1": 0.5,
        "3_1": 0.5
    },
    3: {

    }
}

y = {
    1: {

    },
    2: {

    },
    3: {

    }
}

iteration = 0

while True:
    x_2_sum_1 = w[1]["0_1"] + x1 * w[1]["1_1"] + x2 * w[1]["2_1"]
    x_2_sum_2 = w[1]["0_2"] + x1 * w[1]["1_2"] + x2 * w[1]["2_2"]
    x_2_sum_3 = w[1]["0_3"] + x1 * w[1]["1_3"] + x2 * w[1]["2_3"]

    y[2][1] = 1 / (1 + math.exp(-x_2_sum_1))
    y[2][2] = 1 / (1 + math.exp(-x_2_sum_2))
    y[2][3] = 1 / (1 + math.exp(-x_2_sum_3))

    x_3_sum_1 = w[2]["0_1"] + y[2][1] * w[2]["1_1"] + y[2][2] * w[2]["2_1"] + y[2][3] * w[2]["3_1"]

    y[3][1] = 1 / (1 + math.exp(-x_3_sum_1))

    delta_mod = abs((y[3][1] - y0) / y0)

    if delta_mod <= delta_max:
        print(y[3][1])
        print(iteration)
        break

    delta_3_1 = y[3][1] * (1 - y[3][1]) * (y0 - y[3][1])

    delta_w_3_0_1 = delta_3_1
    delta_w_3_1_1 = delta_3_1 * y[2][1]
    delta_w_3_2_1 = delta_3_1 * y[2][2]
    delta_w_3_3_1 = delta_3_1 * y[2][3]

    w[2]["0_1"] += delta_w_3_0_1
    w[2]["1_1"] += delta_w_3_1_1
    w[2]["2_1"] += delta_w_3_2_1
    w[2]["3_1"] += delta_w_3_3_1

    delta_2_1 = y[2][1] * (1 - y[2][1]) * (w[1]["1_1"] * delta_3_1 + w[1]["2_1"] * delta_3_1)
    delta_2_2 = y[2][2] * (1 - y[2][2]) * (w[1]["1_2"] * delta_3_1 + w[1]["2_2"] * delta_3_1)
    delta_2_3 = y[2][3] * (1 - y[2][3]) * (w[1]["1_3"] * delta_3_1 + w[1]["2_3"] * delta_3_1)

    delta_w_2_0_1 = delta_2_1
    delta_w_2_1_1 = delta_2_1 * x1
    delta_w_2_1_2 = delta_2_2 * x1
    delta_w_2_1_3 = delta_2_3 * x1

    w[1]["0_1"] += delta_w_2_0_1
    w[1]["1_1"] += delta_w_2_1_1
    w[1]["1_2"] += delta_w_2_1_2
    w[1]["1_3"] += delta_w_2_1_3

    delta_w_2_0_2 = delta_2_1
    delta_w_2_2_1 = delta_2_1 * x2
    delta_w_2_2_2 = delta_2_2 * x2
    delta_w_2_2_3 = delta_2_3 * x2

    w[1]["0_2"] += delta_w_2_0_2
    w[1]["2_1"] += delta_w_2_2_1
    w[1]["2_2"] += delta_w_2_2_2
    w[1]["2_3"] += delta_w_2_2_3

    iteration += 1

    # print()
