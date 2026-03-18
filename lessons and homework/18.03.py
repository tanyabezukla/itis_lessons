import numpy as np
from functools import reduce
import math

temperatures = np.random.randint(-20, 40, 10000)
mean = np.mean(temperatures)
std = np.std(temperatures)


def temperature_stream(data):
    for t in data:
        yield t


def clean_data(stream):
    return filter(lambda x: -15 <= x <= 35, stream)


def transform_data(stream):
    # нормализация
    normalized = map(lambda x: (x - mean) / std, stream)
    # дополнительное преобразование
    transformed = map(lambda x: math.sin(x) + x**2, normalized)
    return transformed


# Генератор окон
def window_generator(stream, size=30):
    window = []
    for value in stream:
        window.append(value)
        if len(window) == size:
            yield window
            window = []


# Анализ окна
def analyze_window(window):
    return {
        "mean": np.mean(window),
        "median": np.median(window),
        "std": np.std(window),
        "min": np.min(window),
        "max": np.max(window)
    }


# Проверка аномалии
def is_anomalous(stats):
    return abs(stats["mean"]) > 1 or stats["std"] > 1


# поток
stream = temperature_stream(temperatures)

# очистка
clean_stream = clean_data(stream)

# преобразование
processed_stream = transform_data(clean_stream)

# окна
windows = window_generator(processed_stream)

# анализ всех окон
all_stats = list(map(analyze_window, windows))

# фильтрация окон
anomalies = list(filter(is_anomalous, all_stats))



def reducer(acc, x):
    count, sum_means, max_mean = acc
    return (
        count + 1,
        sum_means + x["mean"],
        max(max_mean, x["mean"])
    )

if anomalies:
    first = anomalies[0]["mean"]
    result = reduce(reducer, anomalies, (0, 0, first))
else:
    result = (0, 0, 0)

anomaly_count, sum_means, max_mean = result


print("Всего окон:", len(all_stats))
print("Аномальных окон:", anomaly_count)
print("Максимальное среднее значение:", max_mean)
print("Сумма средних значений:", sum_means)


