import array

my_array = array.array('i', [1, 2, 3, 4, 5])
max_element = my_array[0]
for num in my_array:
    if num > 0:
        print('положительное')
    else:
        print('отрицательное')