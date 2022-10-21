import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('iris.data', sep=',', header=None)
data.columns = ['sepal_width',
                'sepal_length',
                'petal_width',
                'petal_length',
                'iris_species']


fig, ax = plt.subplots()  # boxplots
fig2, ax2 = plt.subplots()  # scatter plots
fig3, ax3 = plt.subplots(1, 2, figsize=(9, 4))  # combination

for axs in [ax, ax3[0]]:
    axs.boxplot(data.iloc[:,:4])
    axs.set(ylabel = '[cm]',
           xticklabels = data.columns[:4])

for axs in [ax2, ax3[1]]:
    for species_name in data['iris_species'].unique()[::-1]:
        iris_subset = data[data['iris_species'] == species_name]
        axs.scatter(iris_subset['sepal_length'],
                   iris_subset['sepal_width'],
                   label=species_name)
    axs.set(xlabel='sepal_length [cm]',
            ylabel='sepal_width [cm]')
    axs.legend(fontsize=8)

for i in range(2):
    ax3[i].spines['top'].set_visible(False)
    ax3[i].spines['right'].set_visible(False)

for figs in [fig, fig2, fig3]:
    figs.tight_layout()

fig.savefig('iris_boxplot.png', dpi=200)
fig2.savefig('petal_width_v_length_scatter.png', dpi=200)
fig3.savefig('multi_panel_figure.png', dpi=200)
