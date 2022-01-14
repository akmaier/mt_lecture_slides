#
# Copyright © 2020 Stephan Seitz <stephan.seitz@fau.de>
#
# Distributed under terms of the GPLv3 license.
"""

"""
from itertools import chain
from os.path import dirname, join

import matplotlib.pyplot as plt
import numpy as np
import tikzplotlib


# from https://stackoverflow.com/questions/4258106/how-to-calculate-a-fourier-series-in-numpy#4266499
def fourier_series_coeff_numpy(f, T, N, return_complex=False):
    """Calculates the first 2*N+1 Fourier series coeff. of a periodic function.

    Given a periodic, function f(t) with period T, this function returns the
    coefficients a0, {a1,a2,...},{b1,b2,...} such that:

    f(t) ~= a0/2+ sum_{k=1}^{N} ( a_k*cos(2*pi*k*t/T) + b_k*sin(2*pi*k*t/T) )

    If return_complex is set to True, it returns instead the coefficients
    {c0,c1,c2,...}
    such that:

    f(t) ~= sum_{k=-N}^{N} c_k * exp(i*2*pi*k*t/T)

    where we define c_{-n} = complex_conjugate(c_{n})

    Refer to wikipedia for the relation between the real-valued and complex
    valued coeffs at http://en.wikipedia.org/wiki/Fourier_series.

    Parameters
    ----------
    f : the periodic function, a callable like f(t)
    T : the period of the function f, so that f(0)==f(T)
    N_max : the function will return the first N_max + 1 Fourier coeff.

    Returns
    -------
    if return_complex == False, the function returns:

    a0 : float
    a,b : numpy float arrays describing respectively the cosine and sine coeff.

    if return_complex == True, the function returns:

    c : numpy 1-dimensional complex-valued array of size N+1

    """
    # From Shanon theoreom we must use a sampling freq. larger than the maximum
    # frequency you want to catch in the signal.
    f_sample = 2 * N
    # we also need to use an integer sampling frequency, or the
    # points will not be equispaced between 0 and 1. We then add +2 to f_sample
    t, dt = np.linspace(0, T, f_sample + 2, endpoint=False, retstep=True)

    y = np.fft.rfft(f(t)) / t.size

    if return_complex:
        return y
    else:
        y *= 2
        return y[0].real, y[1:-1].real, -y[1:-1].imag

# file_prefix = 'zigzag_'
file_prefix = 'boxfourier_'

def zigzag(t):
    if file_prefix == 'zigzag_':
        return np.remainder(t - np.pi , 2*np.pi) - np.pi 
    elif 'boxfourier_':
        t = t - np.pi/4
        return np.remainder(np.abs(t), np.pi)*np.sign(t) < (np.pi / 2)*np.sign(t)



if file_prefix == 'zigzag_':
    y_min = -4
    y_max = +4
elif 'boxfourier_':
    y_min = -0.1
    y_max = +1.6
x_min = -2 * np.pi
x_max = +2 * np.pi


t = np.linspace(x_min, x_max, 1000)

plt.plot(t, zigzag(t), linewidth=5.0, c='C0')
plt.grid()
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)
tikzplotlib.save(join(dirname(__file__), file_prefix + 'signal.tex'))
plt.savefig(join(dirname(__file__), file_prefix + 'signal.pdf'))
plt.show()

T = np.pi *2
N = 1000
a0, a, b = fourier_series_coeff_numpy(zigzag, T=T, N=N)

N_plot = 15
plt.plot(np.linspace(1, N_plot, N_plot),
         a[:N_plot],
         c='C1',
         marker='o',
         label='Coefficients for $\cos(2\pi i k t/T)$',
         linestyle='')
plt.plot(np.linspace(1, N_plot, N_plot),
         b[:N_plot],
         c='C2',
         marker='o',
        label='Coefficients for $\sin(2\pi i k t/T)$',
         linestyle='')
plt.grid()
plt.legend()
plt.xlabel('i')
if file_prefix.startswith('zigzag'):
    plt.ylim(-2.2, 2.2)
elif file_prefix.startswith('boxfourier'):
    plt.ylim(-1.2, 1.2)
tikzplotlib.save(join(dirname(__file__), file_prefix + 'coefficients.tex'))
plt.savefig(join(dirname(__file__), file_prefix + 'coefficients.pdf'))
plt.show()

# f(t) ~= a0/2+ sum_{k=1}^{N} ( a_k*cos(2*pi*k*t/T) + b_k*sin(2*pi*k*t/T) )
sins = []
coss = []
for k in range(1, N):
    sins.append(np.sin(t * k * 2 * np.pi / T))
    coss.append(np.cos(t * k * 2 * np.pi / T))

for N_max in chain(range(1, 13), [20, 29, 70]):
    reco = a0 / 2 + sum(a[i] * coss[i] + b[i] * sins[i]
                        for i in range(0, N_max))

    plt.figure()
    plt.plot(t, zigzag(t), linewidth=2.0, c='C0')
    plt.plot(t, reco, linewidth=2.0, c='C3', label=f'N={N_max}')
    plt.grid()
    plt.legend()
    plt.xlabel('t')
    plt.ylim(y_min, y_max)
    tikzplotlib.save(join(dirname(__file__),
                          file_prefix + f'reco_{N_max}.tex'))
    plt.draw()
    plt.savefig(join(dirname(__file__), file_prefix + f'reco_{N_max}.pdf'))
    plt.figure()

    plt.plot(t,
             t/t * a0/2,
             c='C1',
             linewidth=2.0,
             label='$a_0$' )
    for i in range(N_max):
        plt.plot(t,
                 b[i] * sins[i],
                 c=f'C{i+2}',
                 linewidth=2.0,
                 label='$b_{%i}$' % (i + 1))
    plt.grid()
    if N_max < 10:
        plt.legend()
    plt.xlabel('t')
    plt.ylim(y_min, y_max)
    tikzplotlib.save(join(dirname(__file__), file_prefix + f'sin_{N_max}.tex'))
    plt.draw()
    plt.savefig(join(dirname(__file__), file_prefix + f'sin_{N_max}.pdf'))

    plt.figure()
    plt.plot(t,
             t/t * a0/2,
             c='C1',
             linewidth=2.0,
             label='$a_0$' )
    for i in range(N_max):
        plt.plot(t,
                 a[i] * coss[i],
                 c=f'C{i+2}',
                 linewidth=2.0,
                 label='$a_{%i}$' % (i + 1))
    plt.grid()
    if N_max < 10:
        plt.legend()
    plt.xlabel('t')
    plt.ylim(y_min, y_max)
    tikzplotlib.save(join(dirname(__file__), file_prefix + f'cos_{N_max}.tex'))
    plt.draw()
    plt.savefig(join(dirname(__file__), file_prefix + f'cos_{N_max}.pdf'))
