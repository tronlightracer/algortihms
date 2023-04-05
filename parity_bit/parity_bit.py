test1 = "01011001"
test2 = "01011010"
test3 = "10100011 00111001 11001100"


def parity_bit_checker(binary: str):
    binaries = binary.split()
    empty_str = ""
    for bit in binaries:
        if bit[-1] == "0" and bit[0:-1].count("1") % 2 == 0:
            empty_str = empty_str + bit[0:-1] + " "
        elif bit[-1] == "1" and bit[0:-1].count("1") % 2 != 0:
            empty_str = empty_str + bit[0:-1] + " "
        else:
            print("error")
    # slices off the last character which is a space which will fail the coding challenge
    return empty_str[0:-1]


print(parity_bit_checker(test1))
print(parity_bit_checker(test2))
print(parity_bit_checker(test3))
