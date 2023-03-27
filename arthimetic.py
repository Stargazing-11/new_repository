class Athimetic_Operations:
    def add(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Not integer instances")
        return x + y

    def subtract(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Not integer instances")
        return x - y
    def miultiply(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Not integer instances")
        return x * y
    def divide(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Not integer instances")
        if y == 0:
            raise ZeroDivisionError("Cannot divide a number by zero")
        return x / y