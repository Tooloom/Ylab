# Ошибка была в том, что при, допустим, значении 5 - выдавало 0.
# Также, был цикл с перебором всех чисел, когда нужно лишь перебирать кратные 5.
# Не были учтены кратные степени 5. При n = 25 - должны прибавляться два нуля, а не 1. При 125 - 3 нуля и т.д.


def zeros(n):
    t = 0
    while n // 5 != 0:
        t = t + n // 5
        n = n // 5
    return t


print(zeros(0))
print(zeros(5))
print(zeros(6))
print(zeros(25))
print(zeros(30))
print(zeros(125))

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
