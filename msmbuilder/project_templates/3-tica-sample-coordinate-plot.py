import seaborn as sns
from matplotlib import pyplot as plt

sns.set_style('ticks')
colors = sns.color_palette()

from msmbuilder.dataset2 import load
from msmbuilder.utils import load as dload
import numpy as np

meta, ttrajs = load('meta.pandas.pickl', 'ttrajs')
txx = np.concatenate(list(ttrajs.values()))

inds = dload("tica-dimension-0-inds.pickl")
straj = []
for traj_i, frame_i in inds:
    straj += [ttrajs[traj_i][frame_i, :]]
straj = np.asarray(straj)


def plot_sampled_traj(ax):
    ax.hexbin(txx[:, 0], txx[:, 1],
              cmap=sns.cubehelix_palette(as_cmap=True),
              mincnt=1,
              bins='log',
              alpha=0.8,
              )

    ax.plot(straj[:, 0], straj[:, 1], 'o-', label='Sampled')

    ax.set_xlabel("tIC 1", fontsize=16)
    ax.set_ylabel("tIC 2", fontsize=16)
    ax.legend(loc='best')


fig, ax = plt.subplots(figsize=(7, 5))
plot_sampled_traj(ax)
fig.tight_layout()
fig.savefig('tica-dimension-0-heatmap.pdf')
