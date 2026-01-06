### Modulo 2 Division

val1 = 1010101010110010100101000111001000101011001000000011110000001010100000000001011001010000101000000000000000000001010100110011101110001111
val2 = 1011

def modulo2_division(dividend, divisor):
    
    # Convert to strings for easier manipulation
    s_dividend = str(dividend)
    s_divisor = str(divisor)
    len_dividend = len(s_dividend)
    len_divisor = len(s_divisor)

    # Append zeros to the dividend
    padded_dividend = s_dividend + '0' * (len_divisor - 1)
    padded_dividend = list(padded_dividend)
    s_divisor = list(s_divisor)

    # Perform modulo 2 division
    for i in range(len_dividend):
        if padded_dividend[i] == '1':  # Only perform division if the leading bit is 1
            for j in range(len_divisor):
                # XOR operation
                padded_dividend[i + j] = '0' if padded_dividend[i + j] == s_divisor[j] else '1'
    # The remainder is the last (len_divisor - 1) bits
    remainder = ''.join(padded_dividend[-(len_divisor - 1):])
    return remainder

remainder = modulo2_division(val1, val2)
print("Remainder:", remainder)