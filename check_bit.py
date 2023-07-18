def is_set(number: int, bit: int) -> int:
    for i in range(bit):
        number >>= 1
    if number & 1:
        return 1
    return 0


try:
    number1 = int(input("Enter an integer : "))
    number2 = int(input("Enter an other integer : "))
    print(is_set(number1, number2))
except ValueError:
    print("Invalid input. Please enter only integers.")
