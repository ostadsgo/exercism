def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    number_of_steps = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        number_of_steps += 1
    return number_of_steps



