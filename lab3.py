def task1(my_list):
    my_list.insert(1, -5)
    min_element = min(my_list)
    max_element = max(my_list)
    my_list.insert(2, [1, 2, 3])
    my_list.append("Your Full Name")
    list_length = len(my_list)
    return my_list, min_element, max_element, list_length

def task2(A, B, C):
    total_cost = sum([quantity * price for quantity, price in zip(B, C)])
    average_price = sum(C) / len(C)
    most_stocked_item = A[B.index(max(B))]
    return total_cost, average_price, most_stocked_item

def task3():
    A1 = []
    A2 = []
    for x in range(-25, 26):
        if x > 0:
            A1.append(x)
        else:
            A2.append(x)
    return A1, A2

def task4(my_string):
    count = 0
    for char in my_string:
        if char == 'a':
            count += 1
    return count

def task5(my_string):
    modified_str = my_string.replace("GOOD", "NICE")
    word_count = len(my_string.split())
    return modified_str, word_count

def task6():
    total_sum = sum(range(1, 6))
    return total_sum

def task7(my_list):
    result = [num for num in my_list if num % 7 == 0 and num % 5 == 0]
    return result





