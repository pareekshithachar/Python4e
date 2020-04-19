import re
name =input("enter file:")

if len(name)<1:
    name="regex_sum_426484.txt"
handle=open(name)
z= 0
x=list()
y=list()
for line in handle:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
    for i in range(len(x)):
        y.append(x[i])
for i in range(len(y)):
    z=z + int(y[i])
print(z)
