# Consider these two simple functions:
def foo(param="no"):  # if no parameter is entered set "no" as default
    return "yes"

def bar(param="no"): # if no parameter is entered set "no" as default
    return (param == "no") and (foo() or "no")

# What will the following function invocation return?
print(bar(foo()))
# no argument is provided so default is used (bar(foo("no")))
# foo() always returns "yes"
# (bar(foo())) evaluates to (bar("yes"))
# (bar()) returns True if both (param == "no") and (foo() or "no")
# Since (bar(foo())) evaluates to bar("yes") (param == "no") is False
# (foo() or "no") is never evaluated
# output is False
