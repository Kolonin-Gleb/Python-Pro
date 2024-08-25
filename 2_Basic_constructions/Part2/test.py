import itertools

generator = (str(n) for n in itertools.count(1))

# Пример использования:
for _ in range(10):
    print(next(generator))

    