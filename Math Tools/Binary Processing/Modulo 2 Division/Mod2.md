# Modulo 2 Division (Binary Polynomial Division)

This code performs **modulo‑2 division** – binary division with no carry, using XOR instead of subtraction. It is the basis of **CRC (Cyclic Redundancy Check)** error‑detection codes.  

**Only generates and shows the remainder.**

## How it works

1. The dividend is padded with `(divisor length - 1)` zeros on the right.
2. The padded dividend is scanned bit by bit from the left.
   - If the current bit is `1`, the divisor is XORed into the padded dividend starting at that position.
   - If the current bit is `0`, no XOR is performed.
3. After processing all original dividend bits, the last `(divisor length - 1)` bits form the **remainder**.

The binary numbers are given as integers that contain only the digits `0` and `1`. Internally they are converted to strings.

## Example Usage

    val1 = 1010101010110010100101000111001000101011001000000011110000001010100000000001011001010000101000000000000000000001010100110011101110001111
    val2 = 1011
    
    remainder = modulo2_division(val1, val2)
    print("Remainder:", remainder)

- `val1` – a long binary sequence (the message).
- `val2 = 1011` – a 4‑bit generator polynomial (degree 3).
- The remainder is a 3‑bit binary CRC check value.

The output is a string of `0` and `1` characters, for example: `Remainder: 101`.

## Important

- The input arguments must be integers whose decimal digits are **only** `0` and `1`.  
- Do not pass ordinary decimal numbers like `1234` – they would be misinterpreted.
