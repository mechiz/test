class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value


class Calculator:
    def __init__(self, init_value):
        self.value = init_value

    def add(self, val):
        self.value += val

cal = Calculator(0)
cal.add(3)
cal.add(4)

print(cal.value)