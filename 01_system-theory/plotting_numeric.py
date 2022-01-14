#
# Copyright © 2020 Stephan Seitz <stephan.seitz@fau.de>
#
# Distributed under terms of the GPLv3 license.
"""

"""
from os.path import dirname, join

import matplotlib.pyplot as plt
import numpy as np
import tikzplotlib

x = np.linspace(-3, 3, 1000)
box_t = (x > 0) * np.exp(-x)#(np.abs(x) < 1) * (1 - np.abs(x))
sin_t = np.abs(x) < 1
convolved = np.convolve(sin_t, box_t / sum(box_t), 'same')
y_min = -0
y_max = +1.5
x_min = -3
x_max = +3

file_prefix = 'example2_'

# plt.subplot(1, 3, 1)
plt.plot(x, sin_t, linewidth=10.0, c='r')
plt.grid()
plt.ylim(y_min, 2)
plt.xlim(x_min, x_max)
tikzplotlib.save(join(dirname(__file__), file_prefix + 'triangle.tex'))
plt.show()

# plt.subplot(1, 3, 2)
plt.plot(x, box_t, linewidth=10.0, c='g')
plt.grid()
plt.ylim(y_min, 2)
plt.xlim(x_min, x_max)
tikzplotlib.save(join(dirname(__file__), file_prefix + 'box.tex'))
plt.show()

# plt.subplot(1, 3, 3)
plt.plot(x, convolved, linewidth=10.0)
plt.grid()
plt.ylim(y_min, 2)
plt.xlim(x_min, x_max)
tikzplotlib.save(join(dirname(__file__), file_prefix + 'convolved.tex'))
plt.show()

plt.plot(x, sin_t + box_t, linewidth=10.0)
plt.grid()
plt.ylim(y_min, 2)
plt.xlim(x_min, x_max)
tikzplotlib.save(join(dirname(__file__),
                      file_prefix + 'triangle_plus_box.tex'))
plt.show()

for plot_number, i in enumerate(np.linspace(-2.5, 2.5, 10)):
    # box_moved = np.abs(x - i) < 1
    box_moved = ((x-i) > 0) * np.exp(-(x-i))
    params = {'legend.fontsize': 30, 'legend.handlelength': 2}
    multiplied = box_moved * sin_t * (x <= i + 1)
    valid_index = 0
    while x[valid_index] <= i and valid_index < len(x) - 1:
        valid_index += 1
    mult_valid_index_m = 0
    while x[mult_valid_index_m] <= i - 1:
        mult_valid_index_m += 1

    mult_valid_index_p = 0
    while x[mult_valid_index_p] <= i + 1 and mult_valid_index_p < len(x) - 1:
        mult_valid_index_p += 1

    plt.rcParams.update(params)
    plt.plot(x, box_moved, linewidth=10.0, c='g')
    plt.plot(x, sin_t, linewidth=10.0, c='r')
    plt.grid()
    plt.ylim(y_min, y_max)
    plt.axvline(x=i, c='g', label=f't={round(i,2)}', linestyle='--')
    if mult_valid_index_p > mult_valid_index_m:
        plt.fill_between(x[mult_valid_index_m:mult_valid_index_p],
                         x[mult_valid_index_m:mult_valid_index_p] * 0,
                         multiplied[mult_valid_index_m:mult_valid_index_p],
                         alpha=0.2,
                         color='C1')
        plt.plot(x[mult_valid_index_m:mult_valid_index_p],
                 multiplied[mult_valid_index_m:mult_valid_index_p],
                 linewidth=10.0,
                 c='orange')
    plt.legend()
    plt.xlim(x_min, x_max)
    tikzplotlib.save(
        join(dirname(__file__), file_prefix + f'box_moved_{plot_number}.tex'))
    plt.show()

    convolved_partial = convolved * (x <= i)
    plt.grid()
    plt.ylim(0, 1.5)
    plt.xlim(-2.5, 2.5)
    plt.axvline(x=i, c='b', label=f't={round(i,2)}', linestyle='--')
    plt.fill_between(x, x * 0, multiplied, alpha=0.2, color='C1')
    # if mult_valid_index_p  > mult_valid_index_m:
    # plt.fill_between(x[mult_valid_index_m:mult_valid_index_p],
    # x[mult_valid_index_m:mult_valid_index_p] * 0,
    # multiplied[mult_valid_index_m:mult_valid_index_p],
    # alpha=0.2,
    # color='C1')
    plt.plot(x, multiplied, linewidth=10.0, c='orange')
    plt.plot(x[:valid_index - 1],
             convolved_partial[:valid_index - 1],
             linewidth=10.0)
    plt.legend()
    plt.xlim(x_min, x_max)
    tikzplotlib.save(
        join(dirname(__file__),
             file_prefix + f'convolved_partial_{plot_number}.tex'))
    plt.show()

    # plt.plot(x[mult_valid_index_m:mult_valid_index_p],
    # multiplied[mult_valid_index_m:mult_valid_index_p],
    # linewidth=10.0,
    # c='orange')
    # plt.grid()
    # plt.fill_between(x, x * 0, multiplied, alpha=0.2, color='C1')
    # plt.axvline(x=i, c='C1', label=f't={round(i,2)}', linestyle='--')
    # plt.ylim(0, 1)
    # plt.xlim(-2.5, 2.5)
    # plt.legend()
    # tikzplotlib.save(
    # join(dirname(__file__), f'multiplied_{plot_number}.tex'))
    # plt.show()
