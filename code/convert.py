# My first program to convert inches to centimeters
#
# @date 26/June/2022
# @author Aarya Aswadhati
#
# Change Log:
# - 08/July/2022: prepare code to get ready to parse
#

# indexed by a tuple that returns the multiplier
conversion_table = {
    ("inches", "cm"): 2.54,
    ("feet", "m"): 0.30
}

def convert(base, to, units):
    multiplier = conversion_table[(base, to)]
    return units * multiplier

#  parse a question into parts...
#  see posts/004-problems-patterns-and-parsing.md

convertdict = {
    "cm": "A"
    "to": "B"
    "in": "C"
    "inches": "D"
    "centimeters": "E"
    " ": "␢"
}
def parse(question):
    print("you asked \"{}\", working on it...".format(question))
    #1. break the question into tokens; tokens are separated by whitespace
    #2. break tokens further if needed; e.g 1cm needs to be *split* into a number and a string
    #3. if input is parseable then a tuple should be returned as below:
    #   e.g: if question is "1cm to in"
    #        then the output on success will be (true, ["cm", "in", 1])
    #4. if input is not parseable (i.e not understandable) then a tuple
    #   as below is returned:
    #        (false, "not in my domain of expertise to answer that question")
    tokens = question.split()
    print("'{}' has {} tokens, will keep working on it".format(question, len(tokens)))


# 1. describe what this program does for the user
# 2. prompt the user type in their request
print("this program converts from one measurement system to another... for example, inches to centimeters")
question = raw_input("what's your question? ")
parts = parse(question)