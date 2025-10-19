def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = sum(n for n in range(1, number) if number % n == 0)
    number_type = {0: "perfect", -1: "deficient", 1: "abundant"}
    number_status = (aliquot_sum > number) - (aliquot_sum < number)
    return number_type.get(number_status)
