def decimal_to_binary(decimal_number):

    binary_rep = []
    while decimal_number >= 1:
        binary_rep.append(decimal_number % 2)
        decimal_number = decimal_number // 2
    binary_rep = binary_rep[::-1]
    return binary_rep


print("\n")
print(f"Your number in binary is: {decimal_to_binary(20)}")


def binary_to_decimal(binary_digits):
    list_of_numbers = []
    for i in range(len(binary_digits)):
        list_of_numbers.append(int(binary_digits[len(binary_digits) - i - 1]) * 2 ** i)

    return sum(list_of_numbers)


print("\n")
print(f"Your number in decimal is: {binary_to_decimal('10011')}")


def decimal_to_base(decimal_number, destination_base):
    result = []
    while decimal_number >= 1:
        result.append(decimal_number % destination_base)
        decimal_number = decimal_number // destination_base
    result = result[::-1]
    return result


print("\n")
print(f"Your number in the base you chose is: {decimal_to_base(20, 8)}")


def base_to_decimal(digits, original_base):
    output = []
    digits = digits[::-1]

    for i in range(len(digits)):
        output.append(int(digits[i]) * (original_base ** i))
    return sum(output)


print("\n")
print(f"Your number in the base you chose is: {base_to_decimal([2,4], 8)}")


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass
