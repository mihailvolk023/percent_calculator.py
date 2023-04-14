# percent_calculator.py

number = float(input("Введите число: "))
percent = float(input("Введите процент: "))

result = number * (percent / 100)

print(percent, "% от", number, "равно", round(result, 2))
