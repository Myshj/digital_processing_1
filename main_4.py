import math

x = 0.1
x0 = 1

w_1_2 = 0.1
w_0_2 = 0.1
w_2_3 = 0.1
w_0_3 = 0.1

y0 = 0.9

delta_max = 0.1

i = 0

while True:
    x_sum_2 = w_0_2 * x0 + w_1_2 * x
    y2 = 1 / (1 + math.exp(-x_sum_2))
    x_sum_3 = w_0_3 * x0 + w_2_3 * y2
    y3 = 1 / (1 + math.exp(-x_sum_3))

    delta_i = abs((y3 - y0) / y0)

    if delta_i <= delta_max:
        print(i)
        print(y3)
        break

    delta_3 = y3 * (1 - y3) * (y0 - y3)

    delta_2 = y2 * (1 - y2) * (w_0_2*delta_3 + w_1_2*delta_3)

    delta_w_0_3 = x0 * delta_3
    delta_w_2_3 = y2 * delta_3

    w_0_3 += delta_w_0_3
    w_2_3 += delta_w_2_3

    delta_w_0_2 = x0 * delta_2
    delta_w_1_2 = x * delta_2

    w_0_2 += delta_w_0_2
    w_1_2 += delta_w_1_2

    i += 1