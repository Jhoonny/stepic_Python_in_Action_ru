# Caesar cipher
ALF = ' abcdefghijklmnopqrstuvwxyz'


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
  muv = int(input().strip())
  string = input().strip()
  print('Result: "{}"'.format(caesar_coder(muv, string)))

if __name__ == '__main__':
  main()
