# Write a library that supports validating and formatting post codes for UK. The details of which post codes are
# valid and which are the parts they consist of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_
# United_Kingdom#Formatting. The API that this library provides is your choice.
#
# I used the regex provided by the goverment

import re

def checkPostCodeUK(code):
    result = re.match(r'^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$', code)
    result1 = re.match(r'^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) {0,1}[0-9][A-Za-z]{2})$', code)
    if result or result1:
        return True
    else:
        return False

#Tests
#print(checkPostCodeUK("s23 ase"))
#print(checkPostCodeUK("EC1A 1BB"))
#print(checkPostCodeUK("W1A 0AX"))
#print(checkPostCodeUK("M1 1AE"))
#print(checkPostCodeUK("B33 8TH"))
#print(checkPostCodeUK("CR2 6XH"))
#print(checkPostCodeUK("DN55 1PT"))
#print(checkPostCodeUK(""))
#print(checkPostCodeUK("!!!!!!!"))
#print(checkPostCodeUK("$@"))
