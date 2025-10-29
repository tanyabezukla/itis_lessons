from functools import reduce


people = [
    {"name": "Анна", "age": 19, "hobby": "рисование", "salary": 40000},
    {"name": "Илья", "age": 32, "hobby": "спорт", "salary": 85000},
    {"name": "Катя", "age": 24, "hobby": "фото", "salary": 60000},
    {"name": "Даня", "age": 17, "hobby": "игры", "salary": 0},
    {"name": "Олег", "age": 45, "hobby": "рыбалка", "salary": 120000},
    {"name": "Вика", "age": 28, "hobby": "чтение", "salary": 70000}
]


more_than_25 = list(filter(lambda x: x["age"] > 25, people))
# print(more_than_25)

salary_more = list(filter(lambda x: x["salary"] > 50000, people))
# print(salary_more)

copy_people = people.copy()
hobby_on_r = list(filter(lambda x: x["hobby"][0] == "р", copy_people))
# print(hobby_on_r)


all_names = list(map(lambda x: x["name"], people))
copy_people = people.copy()
[human.update({"salary": human["salary"]*1.1}) for human in copy_people]
new_list  = list(map(lambda x: {x["name"]: x["age"]}, people))

total_salary = reduce(lambda x, y: x + y["salary"], people, 0)
# print(total_salary)

average_age = (reduce(lambda x,y: x+ y["age"], people, 0)) / len(people)
# print(average_age)

max_salary = reduce(lambda x, y: y if y["salary"] > x["salary"] else x, people)
# print(max_salary)

sorted_by_age = sorted(people, key = lambda x: x["age"])
# print(sorted_by_age)

sorted_by_hobby_len = sorted(people, key = lambda x: len(x["hobby"]))
# print(sorted_by_hobby_len)

name_lenght_tuples = list(map(lambda x: x["name"], filter(lambda i: i["age"] > 20 and i["salary"] >  50000 and len(i["hobby"]) > 4, people)))
# print(name_lenght_tuples)


# ---------------------------------------------------------------------------------------------------
people_cities = [
    {"name": "Анна", "age": 19, "hobby": "рисование", "salary": 40000, "city": "Казань"},
    {"name": "Илья", "age": 32, "hobby": "спорт", "salary": 85000, "city": "Москва"},
    {"name": "Катя", "age": 24, "hobby": "фото", "salary": 60000, "city": "Казань"},
    {"name": "Даня", "age": 17, "hobby": "игры", "salary": 0, "city": "Казань"},
    {"name": "Олег", "age": 45, "hobby": "рыбалка", "salary": 120000, "city": "Москва"},
    {"name": "Вика", "age": 28, "hobby": "чтение", "salary": 70000, "city": "Казань"}
]

new_list2 = list(map(lambda i: {**i, "salary" : i["salary"]*1.15},  people_cities))
