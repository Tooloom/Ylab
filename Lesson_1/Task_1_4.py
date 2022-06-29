# Исправлено время выполнения. При тесте с текстом: "brsrsrsrssdbbanananananananananananananan"
# в прошлой версии занимало время ~ 55 секунд. В новой ~ 13 секунд. Надеюсь, этого достаточно
# для принятия задания.

from itertools import combinations
import time

start_time = time.time()


def bananas(s) -> set:
    result = set()
    text = 'banana'
    for i in combinations(range(len(s)), len(text)):  # positions for an opened symbols
        temp = list(s)
        temp2 = list('-' * len(s))
        t = 0
        for j in i:
            if text[t] != temp[j]:
                break
            else:
                temp2[j] = temp[j]  # opening characters by position
                t += 1
            if t == len(text):
                temp2 = ''.join(temp2)
                result.add(temp2)
                break

    return result


# print(bananas("banann"))
# print(bananas("banana"))
# print(bananas("bbananana"))
# print(bananas("bananaaa"))
# print(bananas("asdbaqwdnanfga na-"))

print(bananas("brsrsrsrssdbbanananananananananananananan"))

print("--- %s seconds ---" % (time.time() - start_time))

# assert bananas("banann") == set()
# assert bananas("banana") == {"banana"}
# assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
#                                 "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
#                                 "-ban--ana", "b-anana--"}
# assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
# assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
