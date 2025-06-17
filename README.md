# Это простой командный блокнот калькулятор для Python, который поддерживает основные арифметические операции: сложение, вычитание, умножение и деление.

# Использование
Чтобы запустить калькулятор из командной строки, используйте:
python main.py <operation> <number1> <number2>
<operation>: одно из 'add', 'subtract', 'multiply' или 'divide'.
<number1> и <number2>: числа, которые будут использоваться в операции.

# Например:
python main.py add 10 5
Тестирование
Тесты написаны с помощью pytest и unittest и могут быть выполнены, выполнив следующие команды:

# Для pytest
pytest test_calculator.py

# Для unittest
python -m unittest test_calculator_unitte