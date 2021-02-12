import bintrees

t = bintrees.RBTree([(5, 'Alfa'), (2, 'Bravo'), (7, 'Charlie'), (3, 'Delta'),
(6, 'Echo')])

print(t[2])

print("min: ",t.min_item()," max: ",t.max_item())

t.insert(9,'Golf')
print(t)

print("min key: ",t.min_key()," max key: ",t.max_key())

t.discard(3)
print(t)

a = t.pop_min()
print(t)

b = t.pop_max()
print(t)
