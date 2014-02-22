import sys
import string

dirty = sys.argv[1]
clean = ''

def list_spinner(input_list, initial_offset=0):
    offset = initial_offset
    while True:
        if (offset + 1) > len(input_list):
            offset = initial_offset
        yield(input_list[offset])
        offset += 1

letters = list_spinner(list(string.ascii_lowercase))
numbers = list_spinner(list(string.digits))
symbols = list_spinner(list(string.punctuation))

for char in dirty:
    if char.islower():
        rv = letters.next()
    elif char.isupper():
        rv = letters.next().upper()
    elif char.isdigit():
        rv = numbers.next()
    else:
        rv = symbols.next()
    clean += str(rv)

print(clean)
