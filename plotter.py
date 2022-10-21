"""This script takes in the CSV file iris.data and creates boxplots for the
overall iris properties, along with scatter plots of sepal_length vs
sepal_width per iris_species.

"""
import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = pd.read_csv('iris.data', sep=',', header=None)
    data.columns = ['sepal_width',
                    'sepal_length',
                    'petal_width',
                    'petal_length',
                    'iris_species']

    fig1, ax1 = plt.subplots()  # boxplots
    fig2, ax2 = plt.subplots()  # scatter plots
    fig3, ax3 = plt.subplots(1, 2, figsize=(9, 4))  # combination

    for axs in [ax1, ax3[0]]:
        col_subset = data.columns[:4]
        axs.boxplot(data[col_subset])
        axs.set(ylabel='[cm]',
                xticklabels=col_subset)

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

    for figs in [fig1, fig2, fig3]:
        figs.tight_layout()

    fig1.savefig('iris_boxplot.png')
    fig2.savefig('petal_width_v_length_scatter.png')
    fig3.savefig('multi_panel_figure.png')


if __name__ == '__main__':
    main()
