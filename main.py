import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import gamma
from sklearn.preprocessing import MinMaxScaler


def generate_gamma_sample(shape, rate, size):
    gamma_dist = gamma(shape, scale=1 / rate)
    return gamma_dist.rvs(size=size)


def compute_average(_data):
    return sum(_data) / len(_data)


def compute_dispersion(_data):
    _average = compute_average(_data)
    return sum([(x - _average) ** 2 for x in _data]) / (len(_data) - 1)


def compute_median(_data):
    temp_data = sorted(_data)
    n = len(temp_data)
    if n % 2 != 0:
        return temp_data[n // 2]
    else:
        return (temp_data[n // 2 - 1] + temp_data[n // 2]) / 2


# Задание параметров распределения
shape = 1
rate = 1
sample_size = 1000000  # размер каждой выборки

# Ввод количества выборок с клавиатуры
n = int(input("Введите количество выборок (n): "))


plt.hist(generate_gamma_sample(shape, rate, sample_size), bins=30, density=True, alpha=0.5, color='b')
# Настройка отображения
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.title('Гистограмма плотности гамма распределения')
plt.grid(True)
plt.savefig("histogram_gamma")
plt.show()
#
# # Инициализация массивов для хранения результатов
# averages = np.zeros(n)
# dispersions = np.zeros(n)
# medians = np.zeros(n)
# F_X_2 = np.zeros(n)
# F_X_n = np.zeros(n)
#
# # Генерация данных из стандартного нормального распределения
# n_data_normalized = np.random.normal(loc=0, scale=1, size=(n, sample_size))
#
# # Применение функции распределения нормального распределения для получения значений от 0 до 1
# # from scipy.stats import norm
# # n_data_normalized = norm.cdf(data)
#
# for i in range(n):
#     averages[i] = compute_average(n_data_normalized[i])
#
#     dispersions[i] = compute_dispersion(n_data_normalized[i])
#     medians[i] = compute_median(n_data_normalized[i])
#     F_X_2[i] = sorted(n_data_normalized[i])[1]
#     F_X_n[i] = max(n_data_normalized[i])
#
#
# # Вывод результатов
# print("Статистики для каждой выборки:")
# for i in range(n):
#     print(f"Выборка {i + 1}:")
#     print(f"Выборочное среднее: {averages[i]}")
#     print(f"Выборочная дисперсия: {dispersions[i]}")
#     print(f"Выборочная медиана: {medians[i]}\n")
#     # print(f"nF(X_2)={sample_size * F_X_2[i]}, Г(2,1)={generate_gamma_sample(2, 1, sample_size)}")
#     # print(f"nF(X_n)={sample_size * (1 - F_X_n[i])}, Г(1,1)={generate_gamma_sample(1, 1, sample_size)}")
#
#
# plt.hist(F_X_2, bins=30, density=True, alpha=0.5, color='b')
# # Настройка отображения
# plt.xlabel('Значение')
# plt.ylabel('Плотность вероятности')
# plt.title('Гистограмма плотности распределения nF(X_2)')
# plt.grid(True)
# plt.savefig('histogram_nF_x_2.png')
#
#
# plt.hist(F_X_n, bins=30, density=True, alpha=0.5, color='b')
# # Настройка отображения
# plt.xlabel('Значение')
# plt.ylabel('Плотность вероятности')
# plt.title('Гистограмма плотности распределения nF(X_n)')
# plt.grid(True)
# plt.savefig('histogram_nF_x_n.png')
# plt.show()
#
#
# plt.hist(averages, bins=30, density=True, alpha=0.5, color='b')
# # Настройка отображения
# plt.xlabel('Значение')
# plt.ylabel('Плотность вероятности')
# plt.title('Гистограмма плотности выборочного среднего')
# plt.grid(True)
# plt.savefig('histogram_average.png')
# plt.show()
#
# plt.hist(dispersions, bins=30, density=True, alpha=0.5, color='b')
# # Настройка отображения
# plt.xlabel('Значение')
# plt.ylabel('Плотность вероятности')
# plt.title('Гистограмма плотности дисперсии')
# plt.grid(True)
# plt.savefig('histogram_dispersion.png')
# plt.show()
#
# plt.hist(medians, bins=30, density=True, alpha=0.5, color='b')
# # Настройка отображения
# plt.xlabel('Значение')
# plt.ylabel('Плотность вероятности')
# plt.title('Гистограмма плотности медианы')
# plt.grid(True)
# plt.savefig('histogram_median.png')
# plt.show()
#
