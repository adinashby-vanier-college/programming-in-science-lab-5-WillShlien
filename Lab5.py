# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n == 1:
        return "*"

    square = "*" * n + "\n"
    for i in range(n - 2):
        square += "*" + " " * (n-2) + "*\n"
    square += "*" * n
    return square

# 1
# 12
# 123
# 1234
def number_pattern(n):
    counter = 1
    num_string = ""
    result = ""

    while counter <= n:
        num_string += str(counter)
        if counter != n:
            result += num_string + "\n"
        else:
            result += num_string
        counter += 1

    return result

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result = 0
    counter = 0
    while counter <= n:
        result += counter
        counter += 1
    return result

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    counter = 1
    result = ""

    while counter <= n:
        spaces = " " * (n - counter)
        stars = "*" * (counter * 2 - 1)
        if counter != n:
            result += spaces + stars + "\n"
        else:
            result += spaces + stars
        counter += 1

    return result