import os

import matplotlib.pyplot as plt
import seaborn as sns


def save(filename, _type):
    output_dir = 'plots'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(os.path.join(output_dir, filename)):
        os.makedirs(os.path.join(output_dir, filename))
    plt.savefig(os.path.join(output_dir, filename, f'{filename + _type}.png'))


def plot(_data, filename):
    # График эмпирической функции распределения
    sns.ecdfplot(data=_data)
    plt.title('Эмпирическая функция распределения мощности')
    plt.xlabel('Мощность')
    plt.ylabel('ECDF')
    if filename:
        save(filename, "_ecdf")
    else:
        plt.show()
    plt.clf()  # Очищаем фигуру после построения каждого графика
    plt.cla()  # Очищаем оси после построения каждого графика

    # Гистограмма
    sns.histplot(data=_data, bins=10, kde=True)
    plt.title('Гистограмма мощности')
    plt.xlabel('Мощность')
    plt.ylabel('Частота')
    if filename:
        save(filename, "_hist")
    else:
        plt.show()
    plt.clf()  # Очищаем фигуру после построения каждого графика
    plt.cla()  # Очищаем оси после построения каждого графика

    # Boxplot
    sns.boxplot(data=_data)
    plt.title('Boxplot мощности')
    plt.xlabel('Мощность')
    if filename:
        save(filename, "_boxplot")
    else:
        plt.show()
    plt.clf()  # Очищаем фигуру после построения каждого графика
    plt.cla()  # Очищаем оси после построения каждого графика

