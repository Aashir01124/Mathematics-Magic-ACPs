while 1:
    def binary_to_decimal(binary_str):
        decimal_value = 0
        power = 0

        for bit in reversed(binary_str):
            if bit == '1':
                decimal_value += 2 ** power
            power += 1

        return decimal_value

    binary_input = input("Enter a binary number: ")
    decimal_output = binary_to_decimal(binary_input)

    print("The decimal value of binary", binary_input, "is", decimal_output)