# Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return  # with the {} on a different line the code is unreachable
    {
        'prop1': "hi there",
    }

print(first())    # returns {'prop1': 'hi there'}
print(second())   # returns None