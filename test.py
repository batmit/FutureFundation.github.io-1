estoque = {
    'batata': [2, 1.90],
    'alface': [10, 2.10],
    'cebola': [20, 1.30],

}

for c, n in estoque.values():
    print(c, n)
for c, n in estoque.items():
    print(c)
    print(n[0], n[1])