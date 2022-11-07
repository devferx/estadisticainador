data = [60,66,77,70,66,68,57,70,66,52,75,65,69,71,58,66,67,74,61,63,69,80,59,66,70,67,78,75,64,71,81,62,64,69,68,72,83,56,65,74,67,54,65,65,69,61,67,73,57,62,67,68,63,67,71,68,76,61,62,63,76,61,67,67,64,72,64,73,79,58,67,71,68,59,69,70,66,62,63,66]
cant = len(data)

minVal = 50
maxVal = 85
a = 5

print(">>>Intervalo")
for i in range(minVal, maxVal, a):
  if i + a  < maxVal:
    print(f'[{i}, {i + a})')
  else:
    print(f'[{i}, {i + a}]')


print(">>>Xc")
for i in range(minVal, maxVal, a):
  print((i + i+a) / 2)

print(">>>fi")
sum = 0
for i in range(minVal, maxVal, a):
  arr = list(filter(lambda x: x >= i and x < i+a, data))
  res = len(arr)
  sum += res

  print(res)

print("suma:", sum)

print("")

print(">>>hi")
sum = 0
for i in range(minVal, maxVal, a):
    arr = list(filter(lambda x: x >= i and x < i+a, data))
    res = round(len(arr) / cant, 3)
    sum += res

    print(res)

print(sum)

print("")

print(">>>hi%")
sum = 0
for i in range(minVal, maxVal, a):
    arr = list(filter(lambda x: x >= i and x < i+a, data))
    res = round(len(arr) / cant, 3) * 100
    sum += res

    print(res)

print(">>>Fi")
sum = 0
for i in range(minVal, maxVal, a):
  arr = list(filter(lambda x: x >= i and x < i+a, data))
  res = sum + len(arr)
  sum = res

  print(res)

print(">>>Hi%")
sum = 0
for i in range(minVal, maxVal, a):
    arr = list(filter(lambda x: x >= i and x < i+a, data))
    res = sum + round(len(arr) / cant, 3) * 100
    sum = res

    print(res)