sett = {1,2,3,4}
sett.add(3)
sett. remove(1)
print(sett)

a = {1,2}
b = {3,4}
c = a|b
print(c)
print (len(sett))

S = [{1,2},{3,4},{5,6,7},{1,4},{2,5}]

s=set()

for i in S:
    s = s | i

print(s)

d = {4,7}
e = {3,5,7}
x = d&e
print(x)    

t = [{0,1,5},{1,2,5,9},{1,2,3,4,5}, {2,5,6,7,8}]

s = t[0]

for i in t:
    s = s&i
print (s)    

"""r = d - e
print(r)

r = e - d
print(r)"""