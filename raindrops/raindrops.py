def convert(number):
    result = ""
    table = {3: "Pling", 5: "Plang", 7: "Plong"}
    if number % 3 == 0:
        result += table.get(3, "")
    if number % 5 == 0:
        result += table.get(5, "")
    if number % 7 == 0:
        result += table.get(7, "")

    return result or str(number)



print(convert(105))

