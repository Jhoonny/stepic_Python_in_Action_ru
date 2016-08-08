# from collections import Counter
from re import sub

def split_encode_series(string):
  c_last = string[0]
  ct = 1
  lst = []
  for c in string[1:]:
    if c != c_last:
      lst.append((ct, c_last))
      c_last, ct = c, 1

    else:
      ct += 1
  lst.append((ct, c_last))
  return lst
  # cnt = Counter(string)
  # return [(cnt[k], k) for k in cnt]

def encode_series(series):

  sir = ""
  for (k, v) in series:
    if k == 1:
      sir += str(v)
    else:
      sir += "{}{}".format(k, v)
  return sir
  # return ("".join(("{}{}".format(k, v) for (k, v) in series)))

def rle_encode(string):
  return encode_series(split_encode_series(string))

def main():
  # s = input().strip()
  # ser = split_encode_series(s)
  # print(ser)
  # s_n = encode_series(ser)
  # print(s_n)

  print(rle_encode(input().strip()))

if __name__ == '__main__':
  main()
