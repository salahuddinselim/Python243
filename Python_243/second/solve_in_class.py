def func(name, age):
  age100 = 2024+(100-age)
  print(age100)

def reverse(my_list):
  a_list=my_list
  a_list.reverse()
  sum=0
  print(a_list)
  for x in my_list:
    sum+=x
  avg=sum/len(my_list)
  print("Average is: ",avg)


def checkpalindrome(str):
  n = ""
  for x in str:
    n=x+n
   
  if str ==n :
    print("Palindrome")
  else:
    print("Not Palindrome")


def main():
  name=input("Enter your name: ")
  age=int(input("Enter your age: "))
  func(name,age)

  str=input("Enter the string: ")
  checkpalindrome(str)
  
  my_list=[]
  n = int(input("Enter your limit: "))
  for x in range (0,n):
    m=int(input())
    my_list.append(m)
  reverse(my_list)



main()