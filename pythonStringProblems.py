# Reverse a string
# newstring = "Sonali"
# print(newstring[::-1])

# takes a sentence and counts the number of upperCases lowercases alphabets and digits
# sentence = input("Enter Sentence:")
# upper,lower,alpha,digit = 0,0,0,0
# for x in sentence:
#     if x.isupper():
#         upper += 1
#     if x.islower():
#         lower+=1
#     if x.isalpha():
#         alpha+=1
#     if x.isdigit():
#         digit+=1
   
# print("There are {}:upper  {}:lower,{}:alphabetic and {}:digits in given sentence".format(upper,lower,alpha,digit ))

#PALINDROME OR NOT

# newstr = input("Enter a string:")

# rev = newstr[::-1]
# if newstr == rev:
#     print("{} is a palindrome string".format(newstr))
# else:
#     print("{} is not a palindrome string".format(newstr))


# a,b,c,d = 0,0,0,0
# for x in newstr:
#     if x == "a":
#         a+= 1
#     if x == "b":
#         b+= 1
#     if x == "c":
#         c+= 1
#     if x == "d":
#         d+= 1

# maximum = max(a,b,c,d)

# def convertPi(str):
#     if len(str)==0:
#         return
#     if str[0] == "p" and str[1] == "i":
#         print("3.14")
#         res = str[2:]
#         convertPi(res)
#     else:
#         print(str[0])
#         convertPi(str[1:])
    
# convertPi("pippxcpifdmfbdpinmnpi")


# Remove all duplicates from the string

# def remove_duplicates(str):

#         if len(str)==0:
#                 return ""
        
#         ch = str[0]
#         ans = remove_duplicates(str[1:0])

#         if ch==ans[0]:
#                 return ans;
        
#         return ch+ans

# remove_duplicates("ssoonali")


# move all x to end of the string

# def x_to_end(str):
#     if len(str) == 0:
#         return ""
#     ch = str[0]
#     ans = x_to_end(str[1:])
#     if ch == "x":
#         return ans+ch
#     return ch+ans


# print(x_to_end("sxoxnxaxlxi"))


# generate all substring of a string

# def substr(str,ans):
#     if len(str)==0:
#         print(ans)
#         return

#     ch = str[0]
#     res = str[1:]
#     substr(res,ans);
#     substr(res,ans+ch)

# print(substr("sonali",""))

# num= 123456789
# numlist = []
# while num>0:
#     mod = num % 10
#     numlist.append(mod)
#     num = num // 10
# print(numlist[::-1]) #start:last:step



# newList= [[1,2,3],[3,2,1],[9,8,7],[7,8,9]]

# for x in range(len(newList)):
#     for y in range(len(newList[x])):
#         print(newList[x][y],end=" ")








# newString = "sonali"


    