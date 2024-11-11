from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def evaluate_expression(expression):
    lexer = Lexer(expression)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    return interpreter.interpret()


def main():
    test_expressions = [
        "(2 + 3) * 4",        # очікуваний результат 20
        "7 * (3 + 2) / 5",    # очікуваний результат 7.0
        "10 + 2 * 6",         # очікуваний результат 22
        "100 * 2 + 12",       # очікуваний результат 212
        "100 * (2 + 12)",     # очікуваний результат 1400
        "100 * (2 + 12) / 14" # очікуваний результат 100.0
    ]

    for expr in test_expressions:
        try:
            result = evaluate_expression(expr)
            print(f"{expr} = {result}")
        except Exception as e:
            print(f"Помилка обчислення виразу {expr}: {e}")


if __name__ == "__main__":
    main()
