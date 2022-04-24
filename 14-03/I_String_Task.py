s = input().casefold()
s = s.replace("a","")
s = s.replace("o","")
s = s.replace("y","")
s = s.replace("e","")
s = s.replace("u","")
s = s.replace("i","")
text =""
for i in s:
  text = text +"."+ i
 
print(text)