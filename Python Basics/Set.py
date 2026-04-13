"""Set is Considered as an unordered DS and no indexing can be used to access
its mutable but need to delete the old one and then add new one"""
a={"chennai","mumbai","coimbatore","tripur","namakal"}
b={"coimbatore","bangalore","mumbai"}

c={1,2,3,4,5}
d={1,2,3,4,5,6,7}

print(a)
print(b)

print(c.isdisjoint(d))
print(c.issubset(d))
print(c.issuperset(d))
print(d.isdisjoint(c))
print(d.issubset(c))
print(d.issuperset(c))
print(a.union(b))
print(a.difference(b))
print(b.difference(a))
print(a.intersection(b))
a.add("Erode")
print(a)
a.remove("chennai")
print(a)
a.discard("coimbatore")
print(a)
a.discard("up") #Safe removal of the item
print(a)