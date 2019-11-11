#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def p_verdura(n):
    p = (n - 7)*0.5
    return p


def p_carne(n):
    p = min((n-5)*(-0.3), 0)
    return p


def p_pesce(n):
    if n > 11.5:
        p = -2
    else:
        p = - 2*np.cos(0.55*n)
    return p


def p_legumi(n):
    p = 0.9*np.sqrt(n*2) - 2
    return p


def p_formaggi(n):
    p = min(0, (n-4)*(-0.3))
    return p


def p_uova(n):
    p = min(0, (n-7)*(-0.45))
    return p


def p_carboidrati(n):
    p = (n-7)*(1/7)
    return p


def p_frutta(n):
    p = (n-7)*(1/3)
    return p


def p_merendine(n):
    p = min(0, (n-2)*(-0.30))
    return p


def create_dataset():
    df = pd.DataFrame()
    for fun in fun_list:
        y = []
        for n in range(1401):
            y.append(fun(n*0.01))

        df[fun.__name__] = y

    df['x'] = [i*0.01 for i in range(1401)]

    return df


def plot(df, ax, func_name):
    ax.set_xlabel(func_name[2:], labelpad=0.1, alpha=0.9, fontsize=14)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_xlim(0, 14)
    ax.set_ylim(-4, 4)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_xticks(range(0, 15, 2))
    ax.set_yticks(range(-4, 5, 2))

    ax.plot(df['x'],
            df[func_name],
            sns.xkcd_rgb["dark red"],
            lw=2.5)


def plot_all():
    df = create_dataset()

    fig, axs = plt.subplots(4, 2)
    plt.subplots_adjust(hspace=0.300)
    coords = []
    for i in range(8):
        x = i % 2
        if x == 0:
            y = i//2
        coords.append((y, x))
    for n, i in enumerate(fun_list):

        plot(df, axs[coords[n]], i.__name__)

    plt.show()


def get_p(n_verdura, n_carne, n_pesce, n_legumi,
          n_formaggi, n_carboidrati, n_frutta, n_merendine):

    n_list = [n_verdura, n_carne, n_pesce, n_legumi,
              n_formaggi, n_carboidrati, n_frutta, n_merendine]
    total_p = 0
    for f, n in zip(fun_list, n_list):
        total_p += f(n)

    return total_p


fun_list = [p_verdura, p_carne, p_pesce, p_legumi,
            p_formaggi, p_carboidrati, p_frutta, p_merendine]

if __name__ == "__main__":
    plot_all()
