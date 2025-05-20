# TODO: Write the functions for arithmatic operations here
# These functions should cover Task 2
from operator import truediv
history = []


def add(num1, num2):
  try:
    add_result = float(num1) + float(num2)
    add_history=f"{float(num1)} + {float(num2)} = {float(add_result)}"
    print(add_history)
    history.append(add_history)
  except:
    return reset()

def subtract(num1, num2):
    sub_result = float(num1) - float(num2)
    sub_history=f"{float(num1)} - {float(num2)} = {float(sub_result)}"
    print(sub_history)
    history.append(sub_history)


def multiply(num1, num2):
    mul_result = float(num1) * float(num2)
    mul_history=f"{float(num1)} * {float(num2)} = {float(mul_result)}"
    print(mul_history)
    history.append(mul_history)


def divide(num1, num2):
   try:
    if (float(num2) == 0):
        print("float division by zero")
        zero_div_history=f"{float(num1)} / {float(num2)} = None"
        print(zero_div_history)
        history.append(zero_div_history)
    else:
        div_result = float(num1) / float(num2)
        div_history=f"{float(num1)} / {float(num2)} = {float(div_result)}"
        print(div_history)
        history.append(div_history)
   except:
       return reset()

def power(num1, num2):
    pow_result = float(num1) ** float(num2)
    pow_history=f"{float(num1)} ^ {float(num2)} = {float(pow_result)}"
    print(pow_history)
    history.append(pow_history)


def remainder(num1, num2):
    rem_result = float(num1) % float(num2)
    rem_history=f"{float(num1)} % {float(num2)} = {float(rem_result)}"
    print(rem_history)
    history.append(rem_history)


# -------------------------------------
# TODO: Write the select_op(choice) function here
# This function sould cover Task 1 (Section 2) and Task 3
def take_input1():
    num1 = input("Enter first number: ")
    if '$' in num1:
        print(num1)
        return 0
    elif '#' in num1:
        print(num1)
        return terminate()
    else:
        print(num1)
        return num1
def take_input2():
    num2 = input("Enter second number: ")
    if '$' in num2:
        print(num2)
        return 0
    elif '#' in num2:
        print(num2)
        return terminate()
    else:
        print(num2)
        return num2

def reset():
    return

def terminate():
    print("Done. Terminating")
    exit()
def history_recall():
  if not history:
      print('No past calculations to show')
  else:
    for i in history:
        print(i)
    return

def select_op(choice):
    if (choice == '+'):
        num1 = take_input1()
        if (num1 == 0):
            return
        num2 = take_input2()
        if (num2 == 0):
            return
        add(num1, num2)
    elif (choice == '-'):
        num1 = take_input1()
        if (num1 == 0):
            return
        num2 = take_input2()
        if (num2 == 0):
            return
        subtract(num1, num2)
    elif (choice == '*'):
        num1 = take_input1()
        if (num1 == 0):
            return
        num2 = take_input2()
        if (num2 == 0):
            return
        multiply(num1, num2)
    elif (choice == '/'):
        num1= take_input1()
        if (num1 == 0):
            return
        num2 = take_input2()
        if (num2 == 0):
            return
        divide(num1, num2)
    elif (choice == '^'):
        num1= take_input1()
        if (num1 == 0):
            return
        num2 = take_input2()
        if (num2 == 0):
            return
        power(num1, num2)
    elif (choice == '%'):
        num1= take_input1()
        if (num1 == 0):
            return
        num2 = take_input2()
        if (num2 == 0):
            return
        remainder(num1, num2)
    elif (choice == '#'):
        return terminate()
    elif (choice == '$'):
        return reset()
    elif (choice == '?'):
        return history_recall()
    else:
        print("Unrecognized operation")


# End the select_op(choice) function here
# -------------------------------------
# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        exit()