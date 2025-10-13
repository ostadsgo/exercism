# def is_armstrong_number(number):
#     str_number = str(number)
#     len_number = len(str_number)
#     result_number = 0
#
#     for digit in str_number:
#         result_number += int(digit) ** len_number
#
#     return number == result_number




# def is_armstrong_number(number):
#     digits = [int(n) for n in str(number)]
#     res = [d ** len(digits) for d in digits]
#     return sum(res) == number

def is_armstrong_number(number):
    return sum(int(digit) ** len(str(number)) for digit in str(number)) == number
#

# def is_armstrong_number(number):
#     orginal_number = number
#     res = 0
#     n = len(str(number))
#     while number > 0:
#         number, digit = divmod(number, 10)
#         res += digit ** n
#
#     return res == orginal_number
