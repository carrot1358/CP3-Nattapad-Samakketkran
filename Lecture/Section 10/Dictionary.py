dict1 = {'name': 'carrot', 'Age': 21, }
print(dict1['name'])

dict1['Lastname'] = 'samakketkran'
print(dict1['name'], dict1['Lastname'])
dict1.clear()
dict1['name'] = 'ana'
print(dict1)

dict_eng= {'cow':'วัว','ant':'มด'}
print(dict_eng)

dict1.copy()
print(dict1.keys())

for i in dict_eng.keys():
    print(i)