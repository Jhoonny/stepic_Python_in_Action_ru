#  under_score to UpperCamelCase

def main():
  str = input().strip()
  str = str.split("_")
  str_new = ""

  for s in str:
    str_new += s[0].upper() + s[1:]
  print(str_new)

if __name__ == "__main__":
  main()
