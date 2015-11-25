# Token cleaner

Turns an authentication token into a similar looking, but obviously
fake token.

This is useful for documentation or sample configuration files,
where you want to have a similar "look" but don't want to put a
real token.

Takes a real token like: "`b45HoPmm4HG`"
and makes a "fake" token that looks like "`a01BcDef2GH`"

## Usage:

    $ python clean.py b45HoPmm4HG
    a01BcDef2GH

## How it works:

We start by getting the input (using `sys.argv` for now). We also
define the `skip` array, which holds the characters we want to skip
and define a `clean` variable, which will hold our "cleaned"
output:

    dirty = sys.argv[1]
    skip = ['-', '/']
    clean = ''

Next we define a `list_spinner` [generator](http://stackoverflow.com/a/231855), which allows you to
"spin" through an array of elements, one by one, using the `next()`
method:

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

Finally, we iterate through each character in the "dirty" input to
produce a "cleaned" output, by detecting the type of input
character and selecting a replacement character from the `next()`
character in the list of the input character type:

    for char in dirty:
        if char in skip:
            rv = char
        elif char.islower():
            rv = letters.next()
        elif char.isupper():
            rv = letters.next().upper()
        elif char.isdigit():
            rv = numbers.next()
        else:
            rv = symbols.next()
        clean += str(rv)
    
    print(clean)