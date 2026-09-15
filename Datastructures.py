# a=[1,2,3,4,3,2,1,3,4,243,234]
# a[2]=33
# a.append(66)
# a.append(660)
# a.insert(-1,"Hello")
# a.extend("Hello")
# a.remove(4.5)
# a.pop(2)
# a.pop()
# print(a.count(120))
# print(a.index(45))
# a.reverse()
# a.sort(reverse=True)
# print(a[4])
# print(a.index(1,3,7))

# Tuple 
# a=(1,2,3,2,1)
# a[2]=44
# print(a.index(14))

# person=["Ken",45,"FED"]
# name=person[0]
# age=person[1]
# role=person[2]

# name,age,role=person

# print(role)

# a=1,2,3,4,2
# a,b=5,6
# print(a)

# a="Hello world"
# a=(2,3,4,34,5456,342,5454)

# print(a[-4:]) # 4...last
# print(a[:4]) # 0,1,2,3
# print(a[2:5]) #2,3,4
# print(a[3:7])
# print(a[3:5]) # [34,5456]
# print(a[2:3]) #4

# print(len("321"))


# Set 

# s1={233,32,45,67,45,"Hello"}

# s1.add(23)
# s1.remove(233)

# print(s1)

# s1={2,3,4,5,6,7}
# s2={4,5,6,7,8,9,0}

# fs1=frozenset({1,2,3})

# fs1[2]

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s2.difference(s1))

# Dict 

person={
    "name":"Leo",
    "age":23,
    "role":"SASE",
    "isMarried":False,
    "surName":"Leo"
}

# person["favMovies"]=[24,96,3]
# person.pop("role")
# person.clear()
# print(person)
# person["role"]="FED"

# print(person.keys()) #dict_keys
# print(person.values()) #dict_values
# print(person.items())

# l1=[1,2,3,["four","five",["six","seven","eight"]]]

# print(len(l1))
# print(l1[-1][-1][-1][-1])