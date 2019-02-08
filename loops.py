# numbers= ["43", "42", "41", "44", "47", "1", "8"]
# def odd_or_even():
#     even=[]
#     odd=[]
#     for number in numbers:
#     if number%2==0:
#         even.append(number)
#     else:
#         odd.append(number)
#     print("The even numbers are: ")
#     for num1 in even:
#         print num1
#     print("The odd numbers are: ")
#     for num1 in even:
#         print num1
# odd_or_even()        

#  print name
def func():
    name=input("What's your name? ")
    cont=True
    while(cont):
        for letter in name:
            print(letter)
        choice = input("Do you want to see the letters (y/n)? ")
        if(choice=="n"):
            cont = False
func()

