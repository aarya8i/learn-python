# My first program to convert inches to centimeters
#
# @date 26/June/2022
# @author Aarya Aswadhati

# indexed by a tuple that returns the multiplier
conversion_table = {
    ("inches", "cm"): 2.54,
    ("feet", "m"): 0.30
}

def convert(base, to, question):
    multiplier = conversion_table[(base, to)];
    return question * multiplier


question = float(input("enter inches: "))
answer = convert("inches", "cm", question)
print("{:,.2f} inches is {:,.2f} centimeters".format(question, answer))
