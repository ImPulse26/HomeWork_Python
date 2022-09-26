# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('X Y Z f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = not (x or y or z) == (not x and not y and not z)
            print(x, y, z, bool(f))
