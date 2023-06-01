def average_closure():
    numbers = []
    total = 0
    def add_number(number):
        nonlocal total
        numbers.append(number)
        total += number
    def get_average():
        if not numbers:
            return None
        return total / len(numbers)
    return add_number, get_average

add_number, get_average = average_closure()
add_number(5)
add_number(10)
add_number(15)
print(get_average())
