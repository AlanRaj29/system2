
#Dictionary Keys

a = input("Enter the input:")
def dic_len(b):
    dic = {}
    for i in b:
        c = dic.keys()
        if i in c:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic
print(dic_len(a))
