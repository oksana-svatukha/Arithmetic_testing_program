# Програма арифметичного тестування

# Вступ
"""Ця програма генерує та виводить арифметичні завдання для тестування. Користувач вводить відповіді, а програма надає звіт про час та кількість помилок."""

### Використання

"""Генерація Завдань"""

"""Програма генерує випадкові арифметичні завдання з операторами "+", "-", "*", "/" та операндами в межах від 2 до 13."""

import random
import time

OPERATORS = ["+", "-", "/", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 13
TOTAL_PROBLEMS = 3


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = int(eval(expr))
    return expr, answer

wrong = 0
input("Press enter tp start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("____________________-")
print("Nice work! You finished in", total_time, "seconds!")