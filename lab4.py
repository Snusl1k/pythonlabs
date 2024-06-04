def task1(a, b, c):
  max_of_first_two = max(a, b)

  return max(max_of_first_two, c)

def task2(list1):
  
  return sum(list1)

def task3(list1):
  
  for num in list1:
    product *= num

  
  return product

def task4(text):
 
  return text[::-1]

def task5(n):
  
  if not isinstance(n, int) or n < 0:
    raise ValueError("Input must be a non-negative integer.")

  
  if n == 0:
    return 1

  
  else:
    return n * task5(n-1)

def task6(num):
  
  return 25 <= num <= 50

def task7(text):
  
  upper_count = 0
  lower_count = 0

  
  for char in text:
    if char.isupper():
      upper_count += 1
    elif char.islower():
      lower_count += 1

  
  return upper_count, lower_count

def task8(list1):

  return list(set(list1))

def task9(list1):
 
  even_list = []

  
  for num in list1:
    
    if num % 2 == 0:
    
      even_list.append(num)

  
  return even_list

def task10(num_rows):

  if num_rows <= 0:
    raise ValueError("Number of rows must be positive.")

  
  pascal_triangle = [[1], [1, 1]]


  for i in range(2, num_rows):
    new_row = [1]
    for j in range(1, i):
      
      new_row.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
    new_row.append(1)
    pascal_triangle.append(new_row)

  
  return max(pascal_triangle[-1])
