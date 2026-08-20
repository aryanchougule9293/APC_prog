from array import array

# append()
a = array('i', [10, 20, 30])
a.append(40)
print("append():", a)


# buffer_info()
a = array('i', [10, 20, 30])
print("buffer_info():", a.buffer_info())


# byteswap()
a = array('i', [10, 20, 30])
a.byteswap()
print("byteswap():", a)


# count()
a = array('i', [10, 20, 10, 30, 10])
print("count():", a.count(10))


# extend()
a = array('i', [10, 20, 30])
a.extend([40, 50])
print("extend():", a)


# frombytes()
a = array('i')
b = array('i', [10, 20, 30]).tobytes()
a.frombytes(b)
print("frombytes():", a)


# fromfile()
with open("data.bin", "wb") as f:
    array('i', [10, 20, 30]).tofile(f)

a = array('i')
with open("data.bin", "rb") as f:
    a.fromfile(f, 3)

print("fromfile():", a)


# fromlist()
a = array('i', [10, 20])
a.fromlist([30, 40, 50])
print("fromlist():", a)


# fromunicode()
a = array('u')
a.fromunicode("Hello")
print("fromunicode():", a)


# index()
a = array('i', [10, 20, 30, 40])
print("index():", a.index(30))


# insert()
a = array('i', [10, 20, 40])
a.insert(2, 30)
print("insert():", a)


# pop()
a = array('i', [10, 20, 30, 40])
x = a.pop()
print("pop():", x)
print(a)


# remove()
a = array('i', [10, 20, 30, 40])
a.remove(30)
print("remove():", a)


# reverse()
a = array('i', [10, 20, 30, 40])
a.reverse()
print("reverse():", a)


# tobytes()
a = array('i', [10, 20, 30])
print("tobytes():", a.tobytes())


# tofile()
a = array('i', [10, 20, 30])

with open("array.bin", "wb") as f:
    a.tofile(f)

print("tofile(): Data written to array.bin")


# tolist()
a = array('i', [10, 20, 30])
print("tolist():", a.tolist())


# tounicode()
a = array('u', "Python")
print("tounicode():", a.tounicode())
