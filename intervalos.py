data = [
  12, 10, 9, 11, 15, 16, 9, 10, 10, 11, 12, 13,14,15, 11, 11, 12, 16, 17, 17,16,16, 15, 14,
  12, 11, 11, 11, 12, 12, 12, 15, 13, 14, 16, 15, 18, 19, 18, 10, 11, 12, 12, 11, 13, 13,
  15, 13, 11, 12
]
cant = len(data)


minVal = 9
maxVal = 20
a = 2

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

print(">>>Hi")
sum = 0
for i in range(minVal, maxVal, a):
  arr = list(filter(lambda x: x >= i and x < i+a, data))
  res = sum + round(len(arr) / cant, 3)
  sum = res

  print(res)

print(">>>Hi%")
sum = 0
for i in range(minVal, maxVal, a):
    arr = list(filter(lambda x: x >= i and x < i+a, data))
    res = sum + round(len(arr) / cant, 3) * 100
    sum = res

    print(res)