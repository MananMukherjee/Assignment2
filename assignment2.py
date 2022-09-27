#a file named newfile.txt with 'hello' written in it is created and saved
#r+ and w+ both re open to reading as well as writing
with open('newfile.txt','r+') as g:
  print(g.write("Manan"))            #returns the string length of the new string
with open('newfile.txt','r+') as l:
  print(l.read())                    #replaces the old string with the new one
with open('newfile.txt','w+') as h:
  print(h.write("Mukherjee"))        #replaces the string 'Manan' with 'Mukherjee', but displays the number of characters in the string as the result
with open('newfile.txt','w+') as k:  #shows nothing, since w+ deletes the previous values everytime it's called
  print(k.read())
with open('newfile.txt','a+') as i:  #appends the word python to thhe previous string, but displays only the number of characters in new string
  print(i.write("python")) 
with open('newfile.txt','a+') as m:  #shows nothing, since a+ deletes the previous values everytime it's called
  print(i.read())

#program for calculator
# a file named 'calculator' has been created for storing the values
print("enter two numbers:")
x= float(input())
y= float(input())
print("Type the operation name in lowercase alphabets only,i.e, add, subtract, multiply or divide:")
z= input()
with open("calculator.txt","a") as k:
  if z=='add':
    k.write(str(x+y))
  elif z=='subtract':
    k.write(str(x-y))
  elif z=='multiply':
    k.write(str(x*y))
  elif z=='divide':
    k.write(str(x/y))
