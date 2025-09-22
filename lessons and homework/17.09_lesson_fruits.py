fruits = (input('Enter fruits: ')).split(', ')
capitalized_fruits = []
for fruit in fruits:
    capitalized_fruits.append(fruit.capitalize())
    

without_repeats = list(set(capitalized_fruits))

#print(sorted(without_repeats))

fruit_count = {}
for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = fruits.count(fruit)
    else:
        continue


#print(f'Количество каждого фрукта: {fruit_count}')

#most_common = max(fruit_count)
#print(most_common)

most_common = ''
maxcount = 0
for key, value in fruit_count.items():
    if value > maxcount:
        maxcount = value
        most_common = key

#print(most_common)


tuple_fruits = tuple(set(capitalized_fruits))

#print(tuple_fruits)
        
list_of_fruits = ['Mango', 'Banana', 'Pineapple']
found_fruits = [fruit for fruit in list_of_fruits if fruit in tuple_fruits]
if len(found_fruits)!= 0 :
    print('Found fruits: '.join(found_fruits), '\n')
else:
    print('Not found')


'''n = int(input('vvedite n '))

k = 0
for j in sorted(without_repeats):
    k += 1
    print(j)
    if k == n+1:
        break'''
