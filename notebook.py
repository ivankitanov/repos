def addToList(list):
    #adding to the list
    something=input('Please enter something in the list: ')
    list.append(something)


def updateList(list,x):
    #adding to the list
    if x>len(list):
        print("There is no index with that value!Update Aborted.")
    else :
        something=input('Please enter the updated value:')
        list[x]=something


def deleteElement(list,x):
    #adding to the list
    if x>len(list):
        print("There is no index with that value! Deletion Aborted.")
    else :
        del list[x]
        

notebook=[]
a="sth"
notebook.append(a)
a1="sth2"
notebook.append(a1)

addToList(notebook)
updateList(notebook,1)
deleteElement(notebook,3)
addToList(notebook)

# printing the contents of the list
for i in notebook:
  print(i)
