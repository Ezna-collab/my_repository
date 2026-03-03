from model import CalculatorModel

m = CalculatorModel()

cases = [
    (['2','+','2']),
    (['3','x','4']),
    (['10','/','4']),
    (['sin','(','0',')']),
    (['π']),
    (['√','(','9',')']),
    (['log','(','100',')']),
]

for tokens in cases:
    out = m.calculate(tokens)
    print(f"{tokens} -> {out}")
