from collections import Counter

types = [type(x).__name__ for x in my_list]
type_counts = Counter(types)

print(type_counts)
