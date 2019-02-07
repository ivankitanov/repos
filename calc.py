def add(result):
  num =  float(input("Add number:"))
  return result+num


def substract(result):
  num = float(input("Substract number:"))
  return result-num


def multiply(result):

  num = float(input("Multiply with number:"))
  return result*num


def divide(result):
  num = float(input('Divide with number:'))
  return result/num 


res = float(input('Enter a number:'))
res=add(res)
res=substract(res)
res=multiply(res)
res=divide(res)
print("The result is: " + str(res))