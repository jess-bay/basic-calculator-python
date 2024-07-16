# functions needed - add, subtract, multiply, divide

#simple: 
# def add(a, b):
#   return a + b

def add(a, b): 
  answer = a + b
  print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def subtract(a, b): 
  answer = a - b
  print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def multiply(a, b): 
  answer = a * b
  print(str(a) + " x " + str(b) + " = " + str(answer) + "\n")

def divide(a, b): 
  answer = a / b
  print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

# print the options - add, subtract, multiply, divide, exit
while True:
  print("A. Addition")
  print("B. Subtraction")
  print("C. Multiplication")
  print("D. Division")
  print("E. Exit")

  choice = input("input your choice: ")
  if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    add(a, b)
  elif choice == "b" or choice =="B":
    print("Subtraction")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    subtract(a, b)
  elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    multiply(a, b)
  elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    divide(a, b)
  elif choice == "e" or choice == "E":
    print("Exit")
    quit()


# get values
# call functions with values retrieved
# while loop to continue the program until exit