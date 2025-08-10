from flask import *
import math
import os
"""
значит я буду делать калькулятор,
но с кучей вещей которых нету в стандартном калькуляторе
(предустановдленный калькулятор на моем телефоне будеь использован как пример стандартного).
"""


equation = {
    1: ["new", "-", "3", "+", "cos", "(", "8", "*", "2", ")", "="],
    2: ["self", "/", "2", "^", "(", ["//", "2"], "9", ")", "="],
    3: ["new", "3", "^^", "3", "="],
    4: ["self", "^", "2", "+", "981264"]
}
results = [1938476, 271983455855]
e = math.e
pi = math.pi
operation_identification = ("self", "new", "+", "-", "*", "/", ["//", "2"], ["//", "3"], "**", "^^", "!", "?", "*10^", "(", ")", ["log", "10"], ["log", "e"], "sin", "cos", "tan", "cot", "sec", "csc", "=")
function_identification = (["log", "10"], ["log", "e"], "sin", "cos", "tan", "cot", "sec", "csc")


def delete():
    if equation[len(equation)][-1] not in ("new", "self"):
        equation[len(equation)].pop()
    elif equation[len(equation)][-1] == "self":
        equation[len(equation)][0] = "new"
# работает

# тест удаления (успешен)
"""
print(equation[4])
delete()
print(equation[4])
delete()
print(equation[4])
delete()
print(equation[4])
delete()
print(equation[4])
print(results)
"""

def clear():
    equation[len(equation)].clear()
    equation[len(equation)].append("new")
    if len(results) != 0:
        results.pop(-1)
# работает

# тест очистки (успешен)
"""
clear()
print(equation)
print(results)
"""

def clear_all():
    equation.clear()
    equation[1] = ["new"]
    results.clear()
# работает

# тест полной очистки (успешен)

clear_all()
print(equation)
print(results)


def number(n=0.0):
    if equation[len(equation)][-1] in operation_identification:
        equation[len(equation)].append(str(n))
    else:
        equation[len(equation)][-1] += str(n)
# работает

def point():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)][-1] += "."
    elif equation[len(equation)][-1] in operation_identification and equation[len(equation)][-1] is not "self":
        equation[len(equation)].append("0.")
# работает

def add():
    equation[len(equation)].append("+")
# работает

# тест добавления (успешен)
"""
number(32.747684)
add()
print(equation)
"""
# тест целых чисел и чисел с точкой (успешен)
"""
point()
number(1)
add()
number(7)
add()
number(8)
point()
number(5)
add()
number(9)
number(1)
number(0)
number(5)
print(equation)
"""

def subtract():
    equation[len(equation)].append("-")
# работает

def multiply():
    equation[len(equation)].append("*")
# работает

def divide():
    equation[len(equation)].append("/")
# работает

def to_the_power_of():
    equation[len(equation)].append("**")
# работает

def square_root():
    equation[len(equation)].append(["//", "2"])
# работает

def cube_root():
    equation[len(equation)].append(["//", "3"])
# работает

def to_the_tetration_of():
    equation[len(equation)].append("^^")
# работает

def squared():
    equation[len(equation)].append("**")
    equation[len(equation)].append("2")
# работает

def cubed():
    equation[len(equation)].append("**")
    equation[len(equation)].append("3")
# работает

def inversed():
    equation[len(equation)].append("**")
    equation[len(equation)].append("(")
    equation[len(equation)].append("-1")
# работает

def factorial():
    equation[len(equation)].append("!")
# работает

def termial():
    equation[len(equation)].append("?")
# работает

def add_euler():
    equation[len(equation)].append("e")
# работает

def add_pi():
    equation[len(equation)].append("pi")
# работает

def exponent():
    equation[len(equation)].append("*10^")
# работает

def sine():
    equation[len(equation)].append("sin")
    equation[len(equation)].append("(")
# работает

def cosine():
    equation[len(equation)].append("cos")
    equation[len(equation)].append("(")
# работает

def tangent():
    equation[len(equation)].append("tan")
    equation[len(equation)].append("(")
# работает

def cotangent():
    equation[len(equation)].append("cot")
    equation[len(equation)].append("(")
# работает

def secant():
    equation[len(equation)].append("sec")
    equation[len(equation)].append("(")
# работает

def cosecant():
    equation[len(equation)].append("csc")
    equation[len(equation)].append("(")
# работает

def parenthesis():
    parenthesis_open, parenthesis_close = 0, 0
    for i in equation[len(equation)]:
        if i == "(":
            parenthesis_open += 1
        elif i == ")":
            parenthesis_close += 1
    print(parenthesis_open, parenthesis_close)
    if parenthesis_open == parenthesis_close and equation[len(equation)][-1] in operation_identification:
        equation[len(equation)].append("(")
        print(1)
    elif parenthesis_open > parenthesis_close and equation[len(equation)][-1] in operation_identification:
        if equation[len(equation)][-1] is not ")":
            equation[len(equation)].append("(")
            print(2)
        else:
            equation[len(equation)].append(")")
            print(3)
    elif equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append(")")
        print(4)
# работает

def logarithm_base_10():
    equation[len(equation)].append(["log", "10"])
    equation[len(equation)].append("(")
# работает

def natural_logarithm():
    equation[len(equation)].append(["log", "e"])
    equation[len(equation)].append("(")
# работает

def tetration(a, b=1):
    if b == 1:
        return a
    else:
        return a ** tetration(a, b-1)
# работает

# тест скобок (успешен)
'''
parenthesis(); #1
parenthesis(); square_root(); #2
parenthesis(); number(3); multiply(); #3
logarithm_base_10(); #4
number(8713445871375.21654); parenthesis(); #4
parenthesis(); #3
to_the_tetration_of(); #2
sine(); #3
number(0.5); parenthesis(); #3
parenthesis(); #2
parenthesis() #1
showcase = ''
for a in equation[len(equation)]:
    if a is not "new":
        showcase += " "+str(a)
print(equation)
print(showcase)
#delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete(); delete();
#print(equation)
'''


def equals():
    try:
        current_eq = equation[len(equation)]
        filtered_eq = [item for item in current_eq if item not in ("new", "self", "=")]

        # Конвертуємо рівняння у рядок для обчислення
        eq_parts = []
        for item in filtered_eq:
            if isinstance(item, list):
                # Обробка спеціальних функцій (наприклад, ["log", "10"])
                if item[0] == "//":  # Обробка коренів
                    if item[1] == "2":
                        eq_parts.append("math.sqrt")
                    elif item[1] == "3":
                        eq_parts.append("math.cbrt")
                elif item[0] == "log":  # Обробка логарифмів
                    if item[1] == "10":
                        eq_parts.append("math.log10")
                    elif item[1] == "e":
                        eq_parts.append("math.log")
            elif item == "pi":
                eq_parts.append(str(math.pi))
            elif item == "e":
                eq_parts.append(str(math.e))
            elif item == "^^":
                eq_parts.append("**")  # Тетрація як звичайний ступінь (тимчасово)
            else:
                eq_parts.append(str(item))

        eq_str = "".join(eq_parts)

        eq_str = (
            eq_str.replace("sin(", "math.sin(")
            .replace("cos(", "math.cos(")
            .replace("tan(", "math.tan(")
            .replace("cot(", "(1/math.tan(")
            .replace("sec(", "(1/math.cos(")
            .replace("csc(", "(1/math.sin(")
        )

        # Додаємо закриваючі дужки для функцій
        open_brackets = eq_str.count("(")
        close_brackets = eq_str.count(")")
        eq_str += ")" * (open_brackets - close_brackets)

        print(f"Calculating: {eq_str}")  # Для налагодження

        result = eval(eq_str, {"math": math, "__builtins__": None})

        results.append(result)
        equation[len(equation)].append("=")
        equation[len(equation) + 1] = ["self"]
    except Exception as e:
        print(f"Calculation error: {e}")
        results.append("Error")


def render():
    # Initialize display variables
    current_eq = equation.get(len(equation), ["new"])
    last_result = results[-1] if results else "0"

    # Форматуємо відображення
    equation_display = ""
    for item in current_eq:
        if item in ("new", "self"):
            continue
        if isinstance(item, list):
            equation_display += "".join(str(x) for x in item) + " "
        else:
            equation_display += str(item) + " "

    equation_display = equation_display.strip() or "0"
    result_display = str(last_result) if last_result != "self" else "0"

    if request.method == "POST":
        key = request.form.get("key")

        # Number buttons
        if key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            number(int(key))

        # Basic operations
        elif key == ".":
            point()
        elif key == "+":
            add()
        elif key == "-":
            subtract()
        elif key == "*":
            multiply()
        elif key == "/":
            divide()

        # Advanced math operations
        elif key == "^":
            to_the_power_of()
        elif key == "√":
            square_root()
        elif key == "∛":
            cube_root()
        elif key == "^^":
            to_the_tetration_of()
        elif key == "!":
            factorial()
        elif key == "?":
            termial()
        elif key == "E":
            exponent()

        # Special functions
        elif key == "()":
            parenthesis()
        elif key == "e":
            add_euler()
        elif key == "pi":
            add_pi()
        elif key == "^-1":
            inversed()
        elif key == "^2":
            squared()
        elif key == "^3":
            cubed()

        # Trigonometric functions
        elif key == "sin":
            sine()
        elif key == "cos":
            cosine()
        elif key == "tan":
            tangent()
        elif key == "cot":
            cotangent()
        elif key == "sec":
            secant()
        elif key == "csc":
            cosecant()

        # Logarithmic functions
        elif key == "log":
            logarithm_base_10()
        elif key == "ln":
            natural_logarithm()

        # Control functions
        elif key == "delete":
            delete()
        elif key == "clear":
            clear()
        elif key == "clear all":
            clear_all()
        elif key == "=":
            equals()

        current_eq = equation.get(len(equation), ["new"])
        equation_display = ""
        for item in current_eq:
            if item in ("new", "self"):
                continue
            if isinstance(item, list):
                equation_display += "".join(str(x) for x in item) + " "
            else:
                equation_display += str(item) + " "

        equation_display = equation_display.strip() or "0"
        result_display = str(results[-1]) if results else "0"

    return render_template('project.html',
                         equation_display=equation_display,
                         result_display=result_display)



folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)

app.add_url_rule("/calculator", "calculator", render, methods=["post", "get"])
app.add_url_rule("/", "calculator", render, methods=["post", "get"])
app.add_url_rule("/render", "render", render, methods=["post", "get"])
app.config['SECRET_KEY'] = 'asdfasdasdfasdfasdfasdfasdasdfasdf'

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)