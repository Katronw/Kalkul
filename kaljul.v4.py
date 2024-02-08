import math
from sympy import symbols, Eq, solve
import re


def get_numbers_input(prompt):
    while True:
        value = input(prompt)
        numbers = value.split()
        if len(numbers) == 3 and all((num.lstrip('-').replace('.', '', 1).isdigit() or 
             (num.startswith('-') and num[1:].replace('.', '', 1).isdigit())) for num in numbers):
            return list(map(float, numbers))
        else:
            print("Ошибка! Пожалуйста, введите ровно три числа через пробел.")

def ask_continue_no3t():
    answer = input("Хотите ли вы продолжить операцию? (д/н): ")
    return answer.lower() == "н" or answer.lower() == "n"
    
 
def ask_continue():
    answer = input("Хотите ли вы продолжить операцию? (д/н): ")
    return answer.lower() == "д" or answer.lower() == "y"
    

def coom():
    print("Coming soon")

def ERROR():
    print("ВАШИ ДЕЙСТВИЯ ВЫЗВАЛИ ОШИБКУ\nERROR 404")


def get_input(prompt):
    value = input(prompt)
    while not re.match("^[-]?\d+(\.\d+)?\s*$", value):
        value = input(prompt)
    return float(value)

def get_fac(prompt):
    value = input(prompt)
    while not re.match("^[-]?\d+(\.\d+)?\s*$", value):
        value = input(prompt)
    return value

def factorial(n):
    pr = 1  
    for i in range(1, n+1):
        pr *= i
    print(f"!{n} = {pr}")

def kalkul():
    while True:
        operators = {
            0: ("* ", lambda x, y: x * y), 
            1: ("/", lambda x, y: x / y),
            2: ("+", lambda x, y: x + y),
            3: ("-", lambda x, y: x - y),
            4: ("**", lambda x, y: x ** y)
        }

        print(" (0)*\n (1)/\n (2)+\n (3)-\n (4)**\n (5)!\n (6)sin/arsin,cos/arcos,tan/artan")

        znak = get_input("> ")
        
        
        """answer = input("Хотите продолжить операцию? (д/н) ")"""
        
        
        if znak == 5:
            n = int(get_fac("> !"))
            factorial(n)
        elif znak < 5:
            num1 = get_input('Первая цифра = ')
            num2 = get_input('Вторая цифра = ')
            if znak in operators:
                operator, operation = operators[znak]
                result = operation(num1, num2)
                print(f"{num1} {operator} {num2} = {result}")

        elif znak == 6:
            print("(0)sin/arsin\n(1)cos/arcos\n(2)tan/artan")
            ugl = get_input("> ")
            if ugl == 0:
                print("(0)sin\n(1)arsin")
                u = get_input("> ")
                if u == 0:
                    sin_1 = get_input("sin ")
                    sin = math.sin(math.radians(sin_1))
                    print(f"sin{sin_1}° = {round(sin, 4)}")
                elif u == 1:
                    arsin_1 = float(input("arsin "))
                    arsin = math.degrees(math.asin(arsin_1))
                    print(f"arsin{arsin_1} = {round(arsin, 0)}°")
            elif ugl == 1:
                print("(0)cos\n(1)arcos")
                u = get_input("> ")
                if u == 0:
                    cos_1 = get_input("cos ")
                    cos = math.cos(math.radians(cos_1))
                    print(f"cos{cos_1}° = {round(cos, 4)}")
                if  u == 1:
                    arcos_1 = float(input("arcos "))
                    arcos = math.degrees(math.acos(arcos_1))
                    print(f"arcos{arcos_1} = {round(arcos, 0)}°")
            elif ugl == 2:
                print("(0)tan\n(1)artan")
                u = get_input("> ")
                if u == 0:
                    tan_1 = get_input("tan " )
                    tan = math.tan(math.radians(tan_1))
                    print(f"tan{tan_1}° = {round(tan, 4)}")
                elif u == 1:
                    artan_1 = float(input("artan "))
                    artan = math.degrees(math.atan(artan_1))
                    print(f"artan{artan_1} = {round(artan, 0)}")

            else:
                ERROR()
                break

        else:
            ERROR()
            break
     
        



        
        

def diskr():
    values = get_numbers_input("Введите числа через пробел\n> ")
    a, b, c = values
    print(f"a = {a} \nb = {b} \nc = {c}")
    b2 = float(b)**2
    a = float(a)
    c = float(c)
    d = float(int(b2 - 4 * a * c))

    D = f"D = {b2} - 4 * {a} * ({c}) = {d}"
    print(D)

    if d < 0 :
        print("It has no roots.")

    elif d == 0 :
        x = d/(2 * int(a))
        print ("x = " + str(x))

    elif d > 0:
        kor = math.sqrt(d)
        kor = float(round(kor, 1))
        b1 = int(b) * -1
        x1 = (float(b1) - float(kor)) / (2 * a)
        x2 = (float(b1) + float(kor)) / (2 * a)
        x1 = float(round(x1, 4))
        x2 = float(round(x2, 4))
        
        r = len("x1 = ")
        ty = f" =  {x1}"
        ty1 = len(ty)
        print( " " * r ,f"-{b} - {kor}") 
        df = len(f"-{b} - {kor}")
        n1 = int(r + df + ty1)
        q = n1/2 ; q= q/1.25
        q = int(round(q,0))

        print("x1 = " ,"-" * df , ty)
        print(" " * q + f"2 * {a}");print()
        
        
        r = len("x2 = ")
        ty = f" =  {x2}"
        ty1 = len(ty)
        print( " " * r ,f"-{b} + {kor}")
        df = len(f"-{b} - {kor}")
        n1 = int(r + df + ty1)
        q = n1/2 ; q= q/1.25
        q = int(round(q,0))

        print("x2 = ","-" * df , ty)
        print(" " * q + f"2 * {a}")

     
def solve_equation(equation_string):
    # Создаем символьные переменные
    x = symbols('x')

    # Разделяем уравнение на левую и правую части
    left, right = equation_string.split('=')

    # Преобразуем строки в уравнение
    equation = Eq(eval(left), eval(right))

    # Решаем уравнение
    solution = solve(equation, x)

    return solution

def ur():
 # Интерактивный калькулятор
 while True:
    user_input = input("Введите уравнение (для выхода введите 'q'): ")
    if user_input.lower() == 'q':
        break
    try:
        result = solve_equation(user_input)
        print("Решение уравнения:", result)
    except Exception as e:
        print("Ошибка:", e)   

def beta():
 ime = input("Enter your name: \n\n")


# correction made by AmyHubbertx
 for c in ime:

    c = c.upper()
    if (c == "A"):
        print("..######..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
    elif (c == "B"):
        print("..######..\n..#....#..\n..#####...\n..#....#..\n..######..\n\n")
    elif (c == "C"):
        print("..######..\n..#.......\n..#.......\n..#.......\n..######..\n\n")
    elif (c == "D"):
        print("..#####...\n..#....#..\n..#....#..\n..#....#..\n..#####...\n\n")
    elif (c == "E"):
        print("..######..\n..#.......\n..#####...\n..#.......\n..######..\n\n")
    elif (c == "F"):
        print("..######..\n..#.......\n..#####...\n..#.......\n..#.......\n\n")
    elif (c == "G"):
        print("..######..\n..#.......\n..#####...\n..#....#..\n..#####...\n\n")
    elif (c == "H"):
        print("..#....#..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
    elif (c == "I"):
        print("..######..\n....##....\n....##....\n....##....\n..######..\n\n")
    elif (c == "J"):
        print("..######..\n....##....\n....##....\n..#.##....\n..####....\n\n")
    elif (c == "K"):
        print("..#...#...\n..#..#....\n..##......\n..#..#....\n..#...#...\n\n")
    elif (c == "L"):
        print("..#.......\n..#.......\n..#.......\n..#.......\n..######..\n\n")
    elif (c == "M"):
        print("..#....#..\n..##..##..\n..#.##.#..\n..#....#..\n..#....#..\n\n")
    elif (c == "N"):
        print("..#....#..\n..##...#..\n..#.#..#..\n..#..#.#..\n..#...##..\n\n")
    elif (c == "O"):
        print("..######..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
    elif (c == "P"):
        print("..######..\n..#....#..\n..######..\n..#.......\n..#.......\n\n")
    elif (c == "Q"):
        print("..######..\n..#....#..\n..#.#..#..\n..#..#.#..\n..######..\n\n")
    elif (c == "R"):
        print("..######..\n..#....#..\n..#.##...\n..#...#...\n..#....#..\n\n")
    elif (c == "S"):
        print("..######..\n..#.......\n..######..\n.......#..\n..######..\n\n")
    elif (c == "T"):
        print("..######..\n....##....\n....##....\n....##....\n....##....\n\n")
    elif (c == "U"):
        print("..#....#..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
    elif (c == "V"):
        print("..#....#..\n..#....#..\n..#....#..\n...#..#...\n....##....\n\n")
    elif (c == "W"):
        print("..#....#..\n..#....#..\n..#.##.#..\n..##..##..\n..#....#..\n\n")
    elif (c == "X"):
        print("..#....#..\n...#..#...\n....##....\n...#..#...\n..#....#..\n\n")
    elif (c == "Y"):
        print("..#....#..\n...#..#...\n....##....\n....##....\n....##....\n\n")
    elif (c == "Z"):
        print("..######..\n......#...\n.....#....\n....#.....\n..######..\n\n")
    elif (c == " "):
        print("..........\n..........\n..........\n..........\n\n")
    elif (c == "."):
        print("----..----\n\n")
    

while True:
    print("Калькулятор (0)\nДискриминант (1)\nРешение уравнения(2)\nBETA(3)")
    spr1 = get_input("> ")

    if not ask_continue():
        break
    else:    
        
        if spr1 == 0:
            kalkul()

    
        elif spr1 == 1:
            diskr()
    
        elif spr1 ==2:
            ur()
        elif spr1 == 3:
            beta()
        
        else:
            ERROR()
            break

        if not ask_continue():
            break
