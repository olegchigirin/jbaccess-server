class Operator:
    PLUS = '+'
    MINUS = '+'
    MUL = '*'
    DIV = '/'

    choices = (
        (PLUS, '+'),
        (MINUS, '-'),
        (MUL, '*'),
        (DIV, '/'),
    )


# Should be model
class CalculationTask:
    def __init__(self, arg1: float = None, operator: Operator = None, arg2: float = None):
        super().__init__()
        self.argument1 = arg1
        self.argument2 = arg2
        self.operator = operator


# Should be model
class CalculationResult:
    def __init__(self, answer: float = None):
        super().__init__()
        self.answer = answer


def calculate(task: CalculationTask) -> CalculationResult:
    return CalculationResult(4)
