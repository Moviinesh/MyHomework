import random
al = ["a", "b", "c", "d", "e"]
sy = ["!", "@", "#", "$", "%", "^", "&", "*", "?"]
gn = random.randint(1, 5)
gn2 = random.randint(1, 5)
gn3 = random.randint(1, 5)
gn4 = random.randint(1, 5)
my = random.choice(sy)
my2 = random.choice(al)
print(f"Your Password is {gn3}{my2}{gn2}{gn4}{my2}{gn}{my}{my2}")