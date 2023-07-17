r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)

try:
    Rectangle(10, "2")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(10, 2)
    r.width = -10
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(10, 2)
    r.x = {}
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    Rectangle(10, 2, 3, -1)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

r1 = Rectangle(3, 2)
print(r1.area())

r2 = Rectangle(2, 10)
print(r2.area())

r3 = Rectangle(8, 7, 0, 0, 12)
print(r3.area())

r1 = Rectangle(4, 6)
r1.display()

print("---")

r1 = Rectangle(2, 2)
r1.display()

r1 = Rectangle(4, 6, 2, 1, 12)
print(r1)

r2 = Rectangle(5, 5, 1)
print(r2)

r1 = Rectangle(2, 3, 2, 2)
r1.display()

print("---")

r2 = Rectangle(3, 2, 1, 0)
r2.display()

r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(89)
print(r1)

r1.update(89, 2)
print(r1)

r1.update(89, 2, 3)
print(r1)

r1.update(89, 2, 3, 4)
print(r1)

r1.update(89, 2, 3, 4, 5)
print(r1)

r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(height=1)
print(r1)

r1.update(width=1, x=2)
print(r1)

r1.update(y=1, width=2, x=3, id=89)
print(r1)

r1.update(x=1, height=2, y=3, width=4)
print(r1)

r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(height=1)
print(r1)

r1.update(width=1, x=2)
print(r1)

r1.update(y=1, width=2, x=3, id=89)
print(r1)

r1.update(x=1, height=2, y=3, width=4)
print(r1)
