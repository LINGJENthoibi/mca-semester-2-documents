set1= {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set 1:", set1)
print("Set 2:", set2)
set1.add(6)
print("After adding 6 to set 1:", set1)
set1.remove(2)
print("Afetr removing 2 from set 1:", set1)
set1.discard(10)
print("Afetr discarding 10 removing set 1 (no error):", set1)
union_set = set1.union(set2)
print("Union of set 1 and set 2:", union_set)

intersection_set = set1.intersection(set1)
print("intersection of set 1 and set 2:", intersection_set)
difference_set = set1.difference(set2)
print("Difference of set 1 - set 2 :", difference_set)

print("Is set 1 a subset of union_set?", set1.issubset(union_set))
print("Is union_set a superset of set 2?", union_set.issuperset(set2))

set2.clear()
print("Set 2 after clear():", set2)

 
