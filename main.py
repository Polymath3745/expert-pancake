from helpers.calculator import Calculator

def main():
    arg1 = int(input("Enter value1: "))
    arg2 = int(input("Enter value2: "))

    calc = Calculator(arg1, arg2)
    x = calc.x
    y = calc.y

    print(f"The two arguments given: {x}, {y}")

if __name__ == '__main__':
    main()

