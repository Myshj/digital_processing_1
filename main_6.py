import math

x = {
    1: 3,
    2: 7
}

w_i_k = {
    1: {
        'a': {
            1: 1,
            2: 2
        },
        'b': {
            1: 3,
            2: 4
        },
        'c': {
            1: 0.5,
            2: 0.5
        }
    },
    2: {
        'a': {
            1: 2,
            2: 1
        },
        'b': {
            1: 7,
            2: 5
        },
        'c': {
            1: 0.5,
            2: 0.5
        }
    },
    3: {
        'a': {
            1: 0.5,
            2: 0.5
        },
        'b': {
            1: 0.5,
            2: 0.5
        },
        'c': {
            1: 0.5,
            2: 0.5
        }
    },
    4: {
        'a': {
            1: 0.5,
            2: 0.5
        },
        'b': {
            1: 0.5,
            2: 0.5
        },
        'c': {
            1: 0.5,
            2: 0.5
        }
    }
}

y = {
    'a': {
        1: 0.,
        2: 0.
    },
    'b': {
        1: 0.,
        2: 0.
    },
    'c': {
        1: 0.,
        2: 0.
    }
}

theta = {
    'a': 0.0,
    'b': 0.0,
    'c': 0.0
}

for i in range(1, 3):
    for k in ('a', 'b'):
        sum = 0.0
        for n in range(1, 3):
            sum += math.exp(
                (-w_i_k[n][k][i] - x[n]) * (-w_i_k[n][k][i] - x[n])
            )
        y[k][i] = sum

for k in ('a', 'b'):
    sum = 0.0

    for i in range(1, 3):
        sum += y[k][i]

    # sum /= 2
    theta[k] = sum

best_number = max(theta.values())

for k in theta.keys():
    if theta[k] == best_number:
        print(k)
