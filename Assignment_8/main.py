children = [
    {"name": "Alice", "age": 2, "height": 95},
    {"name": "Bob", "age": 4, "height": 105},
    {"name": "Charlie", "age": 3, "height": 110},
    {"name": "David", "age": 5, "height": 102},
    {"name": "Eve", "age": 6, "height": 99}]
eligible_children = []
criteria = lambda a,b: a > 3 and b > 100
for child in children:
    if(criteria(child["age"], child["height"])):
        eligible_children.append(child)
print("Eligible children for the fun park: ",eligible_children)