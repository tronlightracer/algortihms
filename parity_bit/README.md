This is a codewars challenge but since the tests were failing I thought I'd add it to my github profile

The challenge can be found here:
https://www.codewars.com/kata/58409435258e102ae900030f/python

In telecomunications we use information coding to detect and prevent errors while sending data.

A parity bit is a bit added to a string of binary code that indicates whether the number of 1-bits in the string is even or odd. Parity bits are used as the simplest form of error detecting code, and can detect a 1 bit error.

In this case we are using even parity: the parity bit is set to 0 if the number of 1-bits is even, and is set to 1 if odd.

We are using them for the transfer of ASCII characters in binary (7-bit strings): the parity is added to the end of the 7-bit string, forming the 8th bit.

This algorithm returns a string with the parity bit sliced off and ensures that it's in the correct format of a byte with no errors. If there is error's it print to the consol "error".
