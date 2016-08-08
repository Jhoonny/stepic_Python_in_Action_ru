from re import findall, match
def split_decode_series(string):
  lst = []
  for el in findall("(\d*)(\D)", string):
    if el[0]:
      lst.append((int(el[0]), el[1]))
    else:
      lst.append((1, el[1]))
  return lst

def decode_series(series):
  return "".join("" + v*k for (k, v) in series)

def rle_decode(string):
  return decode_series(split_decode_series(string))

def main():
  # s = input().strip()
  # ser = split_decode_series(s)
  # print(ser)
  # s_n = decode_series(ser)
  # print(s_n)

  print(rle_decode(input().strip()))

if __name__ == '__main__':
  main()
