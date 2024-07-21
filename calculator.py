from art import logo
print(logo)

def addition(number_1, number_2):
 return number_1 + number_2

def substraction(number_1, number_2):
 return number_1 - number_2

def multiplication(number_1, number_2):
 return number_1 * number_2

def division(number_1, number_2):
 return number_1 / number_2

operations = {"+":addition,
              "-":substraction,
              "*":multiplication,
              "/":division
}


cont = True
while cont:
  number_1 = float(input("First Number: "))
  number_2 = float(input("Second Number: "))
  for operator in operations:
    print(operator)
  selected_operator = input("Pick one operator.")
  calculating_function = operations[selected_operator]
  result = round(calculating_function(number_1, number_2),4) 
  print(f"{number_1}{selected_operator}{number_2}={result}")
  answer = input("Continue?")
  if answer.lower() != 'yes':
   cont = False   