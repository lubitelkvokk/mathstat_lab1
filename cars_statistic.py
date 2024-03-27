import csv

import numpy as np

import plot_by_data


def compute_average(_data):
    return sum(_data) / len(_data)


def compute_dispersion(_data):
    _average = compute_average(_data)
    sm = 0
    for x in _data:
        sm += (x - _average) ** 2
    return sum([(x - _average) ** 2 for x in _data]) / (len(_data) - 1)


def compute_median(_data):
    temp_data = sorted(_data)
    n = len(temp_data)
    if n % 2 != 0:
        return temp_data[n // 2]
    else:
        return (temp_data[n // 2 - 1] + temp_data[n // 2]) / 2


def compute_iqr(_data):
    q1 = np.percentile(_data, 25)
    q3 = np.percentile(_data, 75)
    return q3 - q1


# Создаем список для хранения данных из CSV файла
data = []

# Читаем данные из CSV файла и сохраняем их в список
with open("cars93.csv", encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=",")
    for row in file_reader:
        data.append(row)

# Теперь вы можете использовать данные из списка data в любом месте вашей программы
# Например, для подсчета количества автомобилей каждого производителя
cars = {}
types = {}

for row in data:
    manufacturer = row["Manufacturer"]
    type = row["Type"]
    if manufacturer in cars:
        cars[manufacturer] += 1
    else:
        cars[manufacturer] = 1

    if type in types:
        types[type] += 1
    else:
        types[type] = 1

print(cars)

# Находим ключ с максимальным значением
max_key = max(cars, key=cars.get)

print("Производитель с наибольшим количеством автомобилей:", max_key)
print("Количество автомобилей:", cars[max_key])

# Находим ключ с максимальным значением
min_key = min(cars, key=cars.get)

print("Производитель с наибольшим количеством автомобилей:", min_key)
print("Количество автомобилей:", cars[min_key])

print("Статистические данные всей выборки автомобилей:")
horsepowers = [int(row["Horsepower"]) for row in data]
print(f'\tВыборочное среднее: {compute_average(horsepowers)}')
print(f'\tВыборочная дисперсия: {compute_dispersion(horsepowers)}')
print(f'\tВыборочная медиана: {compute_median(horsepowers)}')
print(f"\tМежквартильный размах: {compute_iqr(horsepowers)}")

plot_by_data.plot(horsepowers, "general")

print(types)
for type in types.keys():
    print(f"Статистические данные всей выборки автомобилей типа {type}:")
    horsepowers_for_curr_type = []
    for car in data:
        if car["Type"] == type:
            horsepowers_for_curr_type.append(int(car["Horsepower"]))

    plot_by_data.plot(horsepowers_for_curr_type, type)
    print(horsepowers_for_curr_type)
    print(f'\tВыборочное среднее: {compute_average(horsepowers_for_curr_type)}')
    print(f'\tВыборочная дисперсия: {compute_dispersion(horsepowers_for_curr_type)}')
    print(f'\tВыборочная медиана: {compute_median(horsepowers_for_curr_type)}')
    print(f"\tМежквартильный размах: {compute_iqr(horsepowers_for_curr_type)}")
