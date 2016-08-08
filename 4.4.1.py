# Caesar cipher
# ALF = ' abcdefghijklmnopqrstuvwxyz'

ALF = [chr(el) for el in range(0x1F600, 0x1F64F+1)]

def caesar_coder(muv, string):
  s = ""
  for c in string:
    if c in ALF:
      new_index = ALF.index(c) + muv
      if new_index >= len(ALF) or new_index < -len(ALF):
        new_index = new_index % len(ALF)
      s += ALF[new_index]

  return s


def caser_decoder(muv, string):
  pass


def main():
  # print(len(ALF))
  muv = int(input().strip())
  string = input().strip()
  print('Result: "{}"'.format(caesar_coder(muv, string)))

if __name__ == '__main__':
  main()
