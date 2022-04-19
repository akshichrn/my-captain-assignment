string = input("enter the string")
res= {}
  
for keys in string:
    res[keys] = res.get(keys, 0) + 1
  

print ("Count of all characters in the string is : \n"
                                             +  str(res))
