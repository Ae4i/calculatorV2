from flask import *
import math
import os
"""
значит я буду делать калькулятор,
но с кучей вещей которых нету в стандартном калькуляторе
(предустановдленный калькулятор на моем телефоне будеь использован как пример стандартного).
"""
folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)

equation = {
    1: ["new", "-", "3", "+", "cos(", "8", "*", "2", ")", "="],
    2: ["self", "/", "2", "^", "(", ["//", "2"], "9", ")", "="],
    3: ["new", "3", "^^", "3", "="],
    4: ["self", "+", "981264"]
}
results = {
    1: 1938476,
    3: 271983455855
}
e = math.e
pi = math.pi
operation_identification = ("self", "new", "+", "-", "*", "/", ["//", "2"], ["//", "3"], "^", "^^", "!", "?", "*10^", "(", ")", ["log", "10"], ["log", "e"], "sin", "cos", "tan", "cot", "sec", "csc", "=")
function_identification = [["log", "10"], ["log", "e"], "sin", "cos", "tan", "cot", "sec", "csc"]


def delete():
    if equation[len(equation)][-1] is not "new" or not "self":
        # сделать для обнаружения функций здесь
        if equation[len(equation)][-1] is "(" or ")" and equation[len(equation)][-2] in function_identification:
            equation[len(equation)].remove(equation[len(equation)][-1])
            equation[len(equation)].remove(equation[len(equation)][-1])
        else:
            equation[len(equation)].remove(equation[len(equation)][-1])
    elif equation[len(equation)][-1] is "self":
        equation[len(equation)].clear()
        equation[len(equation)].append("new")


def clear():
    equation[len(equation)].clear()
    equation[len(equation)].append("new")
    results.remove(results[-1])


def clear_all():
    equation.clear()
    equation[1] = ["new"]
    results.clear()


def number(n=0.0):
    if equation[len(equation)][-1] in operation_identification:
        equation[len(equation)].append(str(n))


def add():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("+")


def subtract():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("-")


def multiply():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("*")


def divide():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("/")


def to_the_power_of():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("^")


def square_root():
    if equation[len(equation)][-1] in operation_identification:
        equation[len(equation)].append(["//", "2"])
    else:
        equation[len(equation)].append("*")
        equation[len(equation)].append(["//", "2"])


def cube_root():
    if equation[len(equation)][-1] in operation_identification:
        equation[len(equation)].append(["//", "3"])
    else:
        equation[len(equation)].append("*")
        equation[len(equation)].append(["//", "3"])


def to_the_tetration_of():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("^^")


def squared():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("^")
        equation[len(equation)].append("2")


def cubed():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("^")
        equation[len(equation)].append("3")


def inversed():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("^")
        equation[len(equation)].append("-1")



def factorial():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("!")


def termial():
    if equation[len(equation)][-1] not in operation_identification:
        equation[len(equation)].append("?")


def add_euler():
    if equation[len(equation)][-1] in operation_identification:
        equation[len(equation)].append("e")
    else:
        equation[len(equation)].append("*")
        equation[len(equation)].append("e")


def add_pi():
    if equation[len(equation)][-1] in operation_identification:
        equation[len(equation)].append("pi")
    else:
        equation[len(equation)].append("*")
        equation[len(equation)].append("pi")


def exponent():
    equation[len(equation)].append("*10^")


def sine():
    equation[len(equation)].append("sin")
    equation[len(equation)].append("(")


def cosine():
    equation[len(equation)].append("cos")
    equation[len(equation)].append("(")


def tangent():
    equation[len(equation)].append("tan")
    equation[len(equation)].append("(")


def cotangent():
    equation[len(equation)].append("cot")
    equation[len(equation)].append("(")


def secant():
    equation[len(equation)].append("sec")
    equation[len(equation)].append("(")


def cosecant():
    equation[len(equation)].append("csc")
    equation[len(equation)].append("(")


def parenthesis():
    parenthesis_open, parenthesis_close = 0, 0
    for i in equation[len(equation)]:
        if i == "(":
            parenthesis_open += 1
        elif i == ")":
            parenthesis_close += 1
    if parenthesis_open == parenthesis_close:
        equation[len(equation)].append("(")
    elif equation[len(equation)][-1] is "(":
        equation[len(equation)].append("(")
    else:
        equation[len(equation)].append(")")


def logarithm_base_10():
    equation[len(equation)].append(["log", "10"])
    equation[len(equation)].append("(")


def natural_logarithm():
    equation[len(equation)].append(["log", "e"])
    equation[len(equation)].append("(")


def tetration(a, b=1):
    for i in range(b-1):
        a = a**a
    return a

print(tetration(3, 3))
print(tetration(3, 2))
print(tetration(3))
def equals():
    # the calculations happen here (это очень тяжело)
    if equation[len(equation)][0] is "new":
        result = int(equation[len(equation)][0])
        for i in range(len(equation[len(equation)])-2):
            if equation[len(equation)][i+2] is "+" and equation[len(equation)][i+3] not in operation_identification:
                if "." in equation[len(equation)][i+3].split():
                    result += float(equation[len(equation)][i+3])
                else:
                    result += int(equation[len(equation)][i+3])
            elif equation[len(equation)][i+2] is "-" and equation[len(equation)][i+3] not in operation_identification:
                if "." in equation[len(equation)][i+3].split():
                    result -= float(equation[len(equation)][i+3])
                else:
                    result -= int(equation[len(equation)][i+3])
            elif equation[len(equation)][i+2] is "*" and equation[len(equation)][i+3] not in operation_identification:
                if "." in equation[len(equation)][i+3].split():
                    result *= float(equation[len(equation)][i+3])
                else:
                    result *= int(equation[len(equation)][i+3])
            elif equation[len(equation)][i+2] is "/" and equation[len(equation)][i+3] not in operation_identification:
                if "." in equation[len(equation)][i+3].split():
                    result /= float(equation[len(equation)][i+3])
                else:
                    result /= int(equation[len(equation)][i+3])
            elif equation[len(equation)][i+2] is "^" and equation[len(equation)][i+3] not in operation_identification:
                if "." in equation[len(equation)][i+3].split():
                    result **= float(equation[len(equation)][i+3])
                else:
                    result **= int(equation[len(equation)][i+3])
            elif equation[len(equation)][i+2] is "^-1":
                result **= -1
            elif equation[len(equation)][i+2] is "^2":
                result **= 2
            elif equation[len(equation)][i+2] is "^3":
                result **= 3
            elif equation[len(equation)][i+2] is ["//", "2"] and equation[len(equation)][i+3] not in operation_identification:
                if equation[len(equation)][i+1] in operation_identification and equation[len(equation)][i+1] not in function_identification:
                    if equation[len(equation)][i+1] is "*":
                        if "." in equation[len(equation)][i+3].split():
                            result *= math.sqrt(float(equation[len(equation)][i+3]))
                        else:
                            result *= math.sqrt(int(equation[len(equation)][i+3]))
                    elif equation[len(equation)][i+1] is "+":
                        if "." in equation[len(equation)][i+3].split():
                            result += math.sqrt(float(equation[len(equation)][i+3]))
                        else:
                            result += math.sqrt(int(equation[len(equation)][i+3]))
                    elif equation[len(equation)][i+1] is "/":
                        if "." in equation[len(equation)][i+3].split():
                            result /= math.sqrt(float(equation[len(equation)][i+3]))
                        else:
                            result /= math.sqrt(int(equation[len(equation)][i+3]))
                    elif equation[len(equation)][i+1] is "-":
                        if "." in equation[len(equation)][i+3].split():
                            result -= math.sqrt(float(equation[len(equation)][i+3]))
                        else:
                            result -= math.sqrt(int(equation[len(equation)][i+3]))
                    elif equation[len(equation)][i+1] is "^":
                        if "." in equation[len(equation)][i+3].split():
                            result **= float(equation[len(equation)][i+3])
                        else:
                            result **= int(equation[len(equation)][i+3])
                    elif equation[len(equation)][i+1] is "^^":
                        if "." in equation[len(equation)][i+3].split():
                            result = tetration(result, float(equation[len(equation)][i+3]))
                        else:
                            result = tetration(result, int(equation[len(equation)][i+3]))
            elif equation[len(equation)][i+2] is "*10^" and equation[len(equation)][i+3] not in operation_identification:
                if "." in equation[len(equation)][i+3].split():
                    result *= 10**float(equation[len(equation)][i+3])
                else:
                    result *= 10**int(equation[len(equation)][i+3])




    results[len(equation)] = result
    equation[len(equation)].append("=")
    equation[len(equation)+1] = ["self"]



@app.route('/')
def render():
    return render_template('project.html')


port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)

app.add_url_rule("/calculator", "calculator", render, methods=["post", "get"])
app.config['SECRET_KEY'] = 'asdfasdasdfasdfasdfasdfasdasdfasdf'
app.run()
