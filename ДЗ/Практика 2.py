# st = {1, 2, 3, 4, 5}
# st.add(12-5)
# print(st)
#
# a = {8, 10, 2, 4, 6}
# b = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# c = a | b
# d = b - a
# e = a & b
# print(b.remove(0))
# print(c)
# print(d)
# print(e)

d = dict(one=1, two=2, three=3)

print(d)

phonebook = {"Петров Петр": "+79102222222"}
phonebook["Иванов Сергей"] = "+79101111111"
print(phonebook["Иванов Сергей"])

phonebook["Петров Петр"] = "+79103333333"
print(phonebook)

print(phonebook.get("Васильев Василий", "Номер не найден"))
print(phonebook.keys())
print(phonebook.values())
print(id(object))
# print("79102222222" is "79103333333")
# print(help([object]))
print(type(object))
# print(isinstance(object, class or type or tuple))


a = 5.43
print(type(a) is int)
print(isinstance(a, (int, float)))
print(str(True))
print(str(a))
print(int(a))
print(int(True))
print(float(a))
print(bool(None), bool(0), bool(0.0), bool(""), bool({}))
print(bool(5), bool({1: "первый"}))
print(tuple([1, 2, 3]))

b = dict(one=1, two=2, three=2)
print(list(d.keys()))
print(set(d.values()))

x = [53, 68, ["А", "В", "С"]]
x1 = x  # Поверхностная копия (через присваивание)
x2 = x[:]  # Глубокая копия (создается при срезе)
x2.append([1,5])
x3 = x.copy()
print(x1)
print(x2)
print(x3)
print(id(x), id(x1), id(x2), id(x3))
print(x1 is x, x2 is x, x3 is x)


q = 5
w = q
print(q, w)
print(id(q), id(w))
e = 5
print(id(q), id(e))

q = 10
print(id(q), id(e))

r = [1, 2, 3]
t = [1, 2, 3]
y = r
print(id(r), id(t), id(y))
r[0] = 5
print(r, t, y)

lst = [1, 8, 2, 5, 0, 3]
print(sorted(lst))
print(sorted(lst, reverse=True))
phones = {'Иван': '+74951111111',  'Сергей': '+74951111113',  'Кирилл': '+74951111112'}
print(sorted(phones))

elements = [(1, "Н", "Водород"), (8, "O", "Кислород"), (53, "I", "Йод")]
print(sorted(elements, key=lambda item: item[2]))

nums = [123, 100, 1001, 234, 515]
print(sorted(nums, key=lambda item: item % 10, reverse=True))
print(min(nums))
print(a in nums)
# print(nums.index(a[1, start[3, end]]))
print(nums.count(123))
print(sorted(nums, key=None, reverse=False))
print(len(nums))
print(123 in nums)
print(122 in nums)

nums += [321, 432]
print(nums)

nums *= 2
print(nums)
print(min(nums), max(nums))
print(nums.index(1001))
print(nums.count(3))
print(sorted(nums))
# elements_lower = elements.lower
# print(elements_lower)

s = "ЭТО просТо ТеКст"
print(ord(s[0]))
print(chr(1069))
print(s.upper(), s.lower(), s.title(), s.capitalize())
print(s.find("О"))
print(s.replace("О", "о"))
lst = s.split()
print(lst)
print("-".join(lst))

age = 20
name = "Максим"
print("Меня зовут {}, мне {} лет.".format(name, age))
print("Меня зовут {0}, мне {1} лет.".format(name, age))
print("{name}, ходит на {subject} каждую пятницу.".format(subject="Мат. анализ", name="Иван"))
print("За 1 рубль дают {0:.4f}$".format(1/100))

li = [8, 7, 5.5, 1000, 3.50, 200]
li.insert(2, 100)
li.append(5.5)
li += [0, 0]
print(li)
v = li.pop(0)
print(v)
print(li)
li.sort()
print(li)
li.remove(1000)
print(li)
del li[1:4]
print(li)

# tuple()
z = tuple("text")
print(z)
z[0] = "n"
print(z)
tuple(range(10))

grn = input("Введите госномер ТС (транспортного средства): ").upper()

if grn == "%RUS":
    print("Удалите RUS из ГРН")
if grn == " ":
    print("Вы правильно ввели ГРН")