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

x = np.linspace(-3, 3, 30)
box_t = np.abs(x) <= 1 #(np.abs(x) < 1) * (1 - np.abs(x))
sin_t = np.abs(x) <= 1
convolved = np.convolve(sin_t, box_t / sum(box_t), 'same')
y_min = -0
y_max = +1.5
x_min = -3
x_max = +3

x_discrete = x * 10

file_prefix = 'example2_discrete_'

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

for plot_number, i in enumerate(np.linspace(-3, 3, 30)):
    # box_moved = np.abs(x - i) < 1
    box_moved = np.abs(x-i) < 1 #* np.exp(-(x-i))
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
    markerline, stemlines, baseline =plt.stem(x_discrete, box_moved, basefmt=' ', linefmt='g-')
    markerline.set_markerfacecolor('g')
    markerline.set_markeredgecolor('g')
    markerline, stemlines, baseline = plt.stem(x_discrete, sin_t,  basefmt=' ', linefmt='r-')
    markerline.set_markerfacecolor('r')
    markerline.set_markeredgecolor('r')
    plt.grid()
    plt.ylim(y_min, y_max)
    plt.axvline(x=i*10, c='g', label=f't={round(i,1)*10}', linestyle='--')
    if mult_valid_index_p > mult_valid_index_m:
        # plt.fill_between(x[mult_valid_index_m:mult_valid_index_p],
                         # x[mult_valid_index_m:mult_valid_index_p] * 0,
                         # multiplied[mult_valid_index_m:mult_valid_index_p],
                         # alpha=0.2,
                         # color='C1')
        # plt.plot(x[mult_valid_index_m:mult_valid_index_p],
                 # multiplied[mult_valid_index_m:mult_valid_index_p],
                 # linewidth=10.0,
                 # marker='o',
                 # linestyle=' ',
                 # c='orange')
        markerline, stemlines, baseline =plt.stem(x_discrete[mult_valid_index_m:mult_valid_index_p],
                 multiplied[mult_valid_index_m:mult_valid_index_p],)
        markerline.set_markerfacecolor('orange')
        markerline.set_markeredgecolor('orange')
        [s.set_color('orange') for s in stemlines]
    plt.legend()
    plt.xlim(x_min*10, x_max*10)
    tikzplotlib.save(
        join(dirname(__file__), file_prefix + f'box_moved_{plot_number}.tex'))
    plt.show()

    convolved_partial = convolved * (x <= i)
    plt.grid()
    plt.ylim(0, 1.5)
    plt.xlim(x_min*10, x_min*10)
    plt.axvline(x=i*10, c='b', label=f't={round(i,1)*10}', linestyle='--')
    # plt.fill_between(x, x * 0, multiplied, alpha=0.2, color='C1')
    # if mult_valid_index_p  > mult_valid_index_m:
    # plt.fill_between(x[mult_valid_index_m:mult_valid_index_p],
    # x[mult_valid_index_m:mult_valid_index_p] * 0,
    # multiplied[mult_valid_index_m:mult_valid_index_p],
    # alpha=0.2,
    # color='C1')
    if mult_valid_index_p  > mult_valid_index_m:
        markerline, stemlines, baseline =plt.stem(x_discrete, multiplied)
        markerline.set_markerfacecolor('orange')
        markerline.set_markeredgecolor('orange')
        [s.set_color('orange') for s in stemlines]
        try:
            plt.stem(x_discrete[:valid_index ],
                     convolved_partial[:valid_index ])
        except:
            pass
    plt.legend()
    plt.xlim(x_min*10, x_max*10)
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
