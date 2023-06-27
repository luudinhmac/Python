# dict
x = {
}
print(type(x))
k = {'key': 'mac', 2:5,4:6,5:9}
print(k)
print(k['key'])
k[1] = "macs"
print(k)
print(k.keys()) # print all keys
print(list(k.keys())) # print all key with list
print(k.values()) # print all values
del k['key'] # delete key values
print(k)

for key in k.keys():
    print(key, k[key])
    