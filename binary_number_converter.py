def decimalToBinary(num):
    if num >= 0:
        binary_string = bin(num)[2:]  # Convert to binary and strip the '0b' prefix
        return binary_string
    else:
        return "Number must be a positive integer."

def binaryToDecimalFull(binary_string):
    try:
        return int(binary_string, 2)  # Convert from binary string to decimal
    except ValueError:
        return "Invalid binary string."

# Example of using the extended features
print(decimalToBinary(14))  # Example for a larger number
print(binaryToDecimalFull('1110'))  # Should print: 14



