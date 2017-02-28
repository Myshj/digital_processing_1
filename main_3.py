import math


w = [
    0.1,
    1
]

x = [
    1,
    3
]

y0 = 0.5

delta_max = 0.1

iteration = 0

while True:
    x_sum = 0.0

    for it in range(0, len(x)):
        x_sum += x[it]*w[it]

    y_mod = 1 / (1 + math.exp(-x_sum))

    delta_mod = abs((y0 - y_mod) / y0)

    if delta_mod <= delta_max:
        print(y_mod)
        print(iteration)
        break

    delta_i = y_mod * (1 - y_mod) * (y0 - y_mod)

    delta_w = [
        x_i * delta_i for x_i in x
    ]

    for it in range(0, len(w)):
        w[it] += delta_w[it]

    iteration += 1