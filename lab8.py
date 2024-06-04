import json


# Task 1: JSON Parsing and Data Retrieval
def task1(file_path, age_threshold):
    with open(file_path, 'r') as file:
        data = json.load(file)
    names_above_threshold = [person['name'] for person in data if person.get('age', 0) > age_threshold]
    return names_above_threshold


# Task 2: Data Transformation and JSON Serialization
def task2(data_list, file_path):
    with open(file_path, 'w') as file:
        json.dump(data_list, file)


# Task 3: JSON Schema Validation
def task3(schema, file_paths):
    non_conforming_files = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = json.load(file)
        try:
            validate(instance=data, schema=schema)
        except ValidationError:
            non_conforming_files.append(file_path)
    return non_conforming_files


# Task 4: Nested JSON Data Handling
def task4(file_path, key):
    def extract_key(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    yield v
                else:
                    yield from extract_key(v)
        elif isinstance(obj, list):
            for item in obj:
                yield from extract_key(item)

    with open(file_path, 'r') as file:
        data = json.load(file)
    values = list(extract_key(data))
    return values


# Task 5: Updating JSON Data
def task5(file_path, category, update_function):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for item in data:
        if item.get('category') == category:
            update_function(item)

    with open(file_path, 'w') as file:
        json.dump(data, file)
