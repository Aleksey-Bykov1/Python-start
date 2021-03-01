src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_src = set()
tmp = set()

for i in src:
    if i not in tmp:
        unique_src.add(i)
    else:
        unique_src.discard(i)
    tmp.add(i)

unique_src_ord = [i for i in src if i in unique_src]
print(unique_src_ord)
