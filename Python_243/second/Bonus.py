def create_list():
  sum=0
  myset = {}
  mylist = []
  my_tuple=()
  n = int(input("Enter the limit: "))
  for x in range(0,n) :
    ele = int(input())
    mylist.append(ele)
  myset = set(mylist)
  mylist.sort()
  print("sorted list: ",mylist)
  for x in mylist:
    sum+=x
  print(sum)
  my_tuple=tuple(mylist)
  print("Largest: ",my_tuple[n-1],"Smallest: ",my_tuple[0])
  num=int(input("Enter the number you want to search: "))
  if num in myset:
    print("Found")
  else:
    print("not found")
  dic = {"1":1,"2":4,"3":9,"5":25,"4":16}
  s = sorted(dic)
  print(s)


def main():
  create_list()




main()