
val = []

val.append([])
val.append(float('inf'))
val.append(0.0)
val.append("""""")
val.append(0)
val.append(float('nan'))
val.append('True')
val.append(object())
val.append(True)
val.append({})
val.append([None, None])
val.append([None])
val.append(False)

for i in range(len(val)):
  if not val[i]:
    print("{} - {}".format(i+1, val[i]))
