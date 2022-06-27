# My first program to convert inches to centimeters
#
# @date 26/June/2022
# @author Aarya Aswadhati

variable = float(input("enter inches: "))
answer = 2.54 * variable
print("{:,.2f} inches is {:,.2f} centimeters".format(variable, answer))
