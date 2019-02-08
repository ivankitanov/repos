# conditionals 1
# i_true = True
# i_false = False
# i_text = "I'm really a text"

# if iTrue is not True:
#     print(i_text)
# else:
#     print("wrong")
# if "really" in i_text:
#     print("{} is in the text.".format("really") )

#  conditionals 2
# def odd_check(number):
#     if num%2==0:
#       return "even"
#     else:
#       return "odd"

# num=46
# res=odd_check(num)
# print(res)

# conditionals 3
def check_list(username):
    if username in my_list:
        print(username)
    else:
        print("It's not in the list") 

my_list= ["John", "Jack", "Jhonny", "Jim"]
user=input("Enter a username: ")
check_list(user)
