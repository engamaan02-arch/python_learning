def remove(l, word):
    n =[]
    for item in l:
        if item.strip() != word:
            n.append(item.strip())
    return n

l =[ "amaan" , " rohan " , "ammu" , "  udsy  "]
print(remove(l , "harry"))