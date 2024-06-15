### Лабораторна робота №13: Обробка даних за допомогою функцій з різними типами параметрів

**Мета роботи:**

*   Закріпити знання про функції в Python та їх параметри.
*   Навчитися застосовувати функції для вирішення різноманітних завдань обробки даних.
*   Ознайомитися з різними типами даних, такими як списки, генератори, словники та рядки, та навчитися працювати з ними за допомогою функцій.

**Опис завдання:**

Реалізувати набір функцій для обробки даних, використовуючи різні типи параметрів та повертаючи різні типи результатів:

1.  **`interpolate_missing(values: List[float]) -> List[float]`:** Інтерполює пропущені значення (`None`) у списку чисел, використовуючи середнє арифметичне сусідніх значень.
2.  **`fibonacci(n: int) -> Generator[int, None, None]`:** Генератор, що повертає числа Фібоначчі до n-го елемента.
3.  **`process_batches(data: List[int], batch_size: int) -> List[int]`:** Обробляє список чисел по пакетам (batch_size), повертаючи список максимальних значень у кожному пакеті.
4.  **`encode_string(s: str) -> str`:** Кодує рядок, використовуючи алгоритм RLE (Run-Length Encoding).
5.  **`decode_string(s: str) -> str`:** Декодує рядок, закодований за алгоритмом RLE.
6.  **`rotate_matrix(matrix: List[List[int]]) -> List[List[int]]`:** Обертає квадратну матрицю на 90 градусів за годинниковою стрілкою.
7.  **`regex_search(strings: List[str], pattern: str) -> List[str]`:** Повертає список рядків, які відповідають заданому регулярному виразу.
8.  **`merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]`:** Об'єднує два відсортованих списки в один відсортований список.
9.  **`is_prime(n: int) -> bool`:** Перевіряє, чи є число простим.
10. **`group_by_key(data: List[Dict[str, Any]], key: str) -> Dict[str, List[Any]]`:** Групує список словників за значенням ключа.
11. **`remove_outliers(data: List[int]) -> List[int]`:** Видаляє викиди (значення, що відхиляються від середнього більш ніж на два стандартних відхилення) зі списку чисел.

**Виконання роботи:**

1.  **Функція `interpolate_missing`:**
    *   Проходить по списку `values`.
    *   Якщо знаходить `None`, шукає найближчі ненульові значення зліва та справа.
    *   Замінює `None` середнім арифметичним знайдених значень.

2.  **Функція `fibonacci`:**
    *   Генерує числа Фібоначчі, починаючи з 0 та 1, доки не буде згенеровано `n` чисел.

3.  **Функція `process_batches`:**
    *   Розбиває список `data` на пакети розміром `batch_size`.
    *   Знаходить максимальне значення в кожному пакеті та додає його до списку `max_values`.

4.  **Функції `encode_string` та `decode_string`:**
    *   `encode_string` рахує повторювані символи та кодує їх у форматі "кількість+символ" (наприклад, "aaabbc" -> "3a2bc").
    *   `decode_string` робить зворотну операцію, розшифровуючи рядок, закодований за алгоритмом RLE.

5.  **Функція `rotate_matrix`:**
    *   Створює нову матрицю `rotated` такого ж розміру, як і вхідна.
    *   Заповнює `rotated`, копіюючи елементи з вхідної матриці, але змінюючи їх позиції відповідно до обертання на 90 градусів.

6.  **Функція `regex_search`:**
    *   Компілює регулярний вираз `pattern`.
    *   Повертає список рядків зі списку `strings`, які відповідають шаблону.

7.  **Функція `merge_sorted_arrays`:**
    *   Використовує два вказівники (`i` та `j`) для проходу по масивах `arr1` та `arr2`.
    *   Порівнює елементи під вказівниками та додає менший елемент до результуючого списку `merged`.
    *   Продовжує, доки не буде досягнуто кінця одного з масивів.
    *   Додає решту елементів з іншого масиву до `merged`.

8.  **Функція `is_prime`:**
    *   Перевіряє, чи є число `n` простим, шляхом перебору можливих дільників від 2 до кореня квадратного з `n`.

9.  **Функція `group_by_key`:**
    *   Створює словник `grouped`, де ключі - це унікальні значення ключа `key` зі списку словників `data`, а значення - списки відповідних значень `value`.

10. **Функція `remove_outliers`:**
    *   Обчислює середнє значення та стандартне відхилення списку `data`.
    *   Визначає нижню та верхню межі для викидів.
    *   Повертає новий список, що містить лише ті елементи з `data`, які знаходяться в межах цих меж.

**Результати:**

Функції успішно реалізовані та протестовані на прикладах, демонструючи їхню працездатність та коректність обробки даних.

**Висновки:**

У цій лабораторній роботі ми розглянули різні аспекти обробки даних за допомогою функцій у Python. Ми навчилися працювати з різними типами даних, такими як списки, генератори, словники та рядки, використовуючи різні типи параметрів та повертаючи різні типи результатів. Це дозволяє нам створювати гнучкі та ефективні функції для вирішення різноманітних завдань обробки даних.