
import time
import threading
import multiprocessing
import asyncio



# 1 Threading

def process_order(order_id):
    time.sleep(1)

    result = 0
    for i in range(300000):
        result += (i * i) % 103

    print("Заказ", order_id, "обработан. Результат:", result)
    return result


def part1_threading():
    print("\n1. Threading")

    orders = [1, 2, 3, 4, 5]

    start = time.time()
    sync_results = []
    for order_id in orders:
        sync_results.append(process_order(order_id))
    end = time.time()

    print("Синхронное время:", round(end - start, 2), "сек.")

    start = time.time()
    threads = []

    for order_id in orders:
        thread = threading.Thread(target=process_order, args=(order_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()

    print("Threading время:", round(end - start, 2), "сек.")


# 2. Multiprocessing


def heavy_calculation(n):
    result = 0

    for i in range(n):
        result += (i * 2) % 97
        result += (i ** 2) % 113

    return result


def part2_multiprocessing():
    print("\n2. Multiprocessing")

    numbers = [3000000, 3000000, 3000000, 3000000]

    start = time.time()
    sync_results = []

    for n in numbers:
        sync_results.append(heavy_calculation(n))

    end = time.time()

    print("Последовательное время:", round(end - start, 2), "сек.")
    print("Результаты sync:", sync_results)

    start = time.time()

    with multiprocessing.Pool() as pool:
        mp_results = pool.map(heavy_calculation, numbers)

    end = time.time()

    print("Multiprocessing время:", round(end - start, 2), "сек.")
    print("Результаты multiprocessing:", mp_results)

    print("Результаты совпадают:", sync_results == mp_results)



# 3. Async


async def service_request(user_id):
    await asyncio.sleep(1)

    result = 0
    for i in range(500000):
        if i % 2 == 0:
            result += i % 123

    return user_id, result


async def part3_async():
    print("\n3. Async")

    start = time.time()

    tasks = []

    for user_id in range(1, 11):
        tasks.append(service_request(user_id))

    results = await asyncio.gather(*tasks)

    end = time.time()

    for user_id, result in results:
        print("Пользователь", user_id, "получил результат:", result)

    print("Async время:", round(end - start, 2), "сек.")



# 4. Смешанный сценарий


def universal_task(task_id):
    time.sleep(1)

    result = 0
    for i in range(500000):
        result += (i * task_id) % 101

    time.sleep(1)

    result = result + task_id

    print("Задача", task_id, "готова. Результат:", result)

    return result


def part4_mixed():
    print("\n4. Смешанный сценарий")

    task_ids = [1, 2, 3, 4, 5]

    start = time.time()
    sync_results = []

    for task_id in task_ids:
        sync_results.append(universal_task(task_id))

    end = time.time()

    print("Sync время:", round(end - start, 2), "сек.")
    print("Sync результаты:", sync_results)

    start = time.time()

    threads = []
    thread_results = [None] * len(task_ids)

    def run_task(index, task_id):
        thread_results[index] = universal_task(task_id)

    for index in range(len(task_ids)):
        thread = threading.Thread(target=run_task, args=(index, task_ids[index]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()

    print("Threading время:", round(end - start, 2), "сек.")
    print("Threading результаты:", thread_results)

    start = time.time()

    with multiprocessing.Pool() as pool:
        mp_results = pool.map(universal_task, task_ids)

    end = time.time()

    print("Multiprocessing время:", round(end - start, 2), "сек.")
    print("Multiprocessing результаты:", mp_results)

    print("Результаты sync и threading совпадают:", sync_results == thread_results)
    print("Результаты sync и multiprocessing совпадают:", sync_results == mp_results)



# Запуск всей программы


if __name__ == "__main__":
    part1_threading()
    part2_multiprocessing()
    asyncio.run(part3_async())
    part4_mixed()