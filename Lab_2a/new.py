print("2.I -------------------------------->")
print("Перша константа", False)
print("Я знайшов команду", None)
print("Третя константа", True)
print("Вивід константи", __debug__)
########################################
print("2.II.1 -------------------------------->")
test = []
print(test,'is',bool(test))
test = [0]
print(test,'is',bool(test))
test = 0.0
print(test,'is',bool(test))
test = None
print(test,'is',bool(test))
test = True
print(test,'is',bool(test))
test = 'Easy string'
print(test,'is',bool(test))
######################################
print("2.II.2 -------------------------------->")
number = 5
print ('The binary equivalent of 5 is:', bin(number))
print("2.III.1 -------------------------------->")
list = ['hi', 'hello', 'good morning', 'how do you do']
for i in list:
  print(i)
print("2.III.2 -------------------------------->")
a=int(input())
b=int(input())
if a>b:
    print(a)
else:
    print(b)
print("2.III.3 -------------------------------->")
a, b, c = map(int, input().split())
m=a
if b<m:
    m=b
if c<m:
    m=c
print(m)
print("2.IV -------------------------------->")
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")
print("2.V -------------------------------->")
with open("README.md", "w") as f:
    f.write("some data")
print("2.VI -------------------------------->")
calc = lambda a, b, c: a+c
print(calc(4, '+', 67))

print("2.VI ----------->")
