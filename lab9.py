import re


def task1(s):
    return bool(re.match(r'^[a-z0-9]+$', s))


def task2(s):
    return bool(re.search(r'[A-Z]', s))


def task3(s):
    return bool(re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', s))


def task4(s):
    return bool(re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$', s))


def task5(s):
    return bool(re.match(r'^\d{5}(-\d{4})?$', s))


def task6(s):
    return bool(re.match(r'^[a-z0-9_-]{6,12}$', s))


def task7(s):
    return bool(re.match(r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$', s))


def task8(s):
    return bool(re.match(r'^\d{3}-\d{2}-\d{4}$', s))


def task9(s):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$', s))


def task10(s):
    return bool(re.match(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$', s))


print(task1("hello123"))  
print(task2("Hello")) 
print(task3("192.168.1.1"))  
print(task4("12:34:56")) 
print(task5("12345"))  
print(task6("john_doe-123"))  
print(task7("4512-3456-7890-1234"))  
print(task8("123-45-6789")) 
print(task9("Passw0rd#"))  
print(task10("2001:0db8:85a3:0000:0000:8a2e:0370:7334")) 
