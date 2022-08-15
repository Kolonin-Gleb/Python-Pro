# hash_as_key()
'''
def hash_as_key(objects):
    d = {}
    for obj in objects:
        if d.get(hash(obj)) == None:
            d[hash(obj)] = obj
        else:
            d[hash(obj)] = [d[hash(obj)]] + [obj]
    return d

data = [1, 2, 3, 4, 5, 5, 5]
print(hash_as_key(data))
# {1: 1, 2: 2, 3: 3, 4: 4, 5: [5, 5]}

data = [-1, -2, -3, -4, -5]
print(hash_as_key(data))
# {-2: [-1, -2], -3: -3, -4: -4, -5: -5}
'''

# expression = '2**2 + 10'
# print(eval(expression)) # eval - возращает результат своего исполнения!

# a, b = 10, 0
# expression = 'if a or b: print(a + b)'
# print(eval(expression))

# Как это работает?
# code = '100 + 10 + 1'
# print(exec(code))
# print(eval(code))

# Математические выражения
'''
import sys
results = [eval(inp) for inp in sys.stdin]

print(max(results))
'''

# Минимум и максимум значений функции (y) среди целых точек на промежутке 
'''
2*x**2 + 5*x + 7
-1 5
Sample Output 1:

Минимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно 4
Максимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно 82


func = input()
diapason = input().split()

y = []
for x in range(int(diapason[0]), int(diapason[1])+1):
    y.append(eval(func.replace('x', f"({x})")))

print(f"Минимальное значение функции {func} на отрезке [{'; '.join(diapason)}] равно {min(y)}")
print(f"Максимальное значение функции {func} на отрезке [{'; '.join(diapason)}] равно {max(y)}")

'''
