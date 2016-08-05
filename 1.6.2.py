from re import *
def main():
  str = input()
  pattern = r'(\s)+'
  str = sub(pattern, "_", str)
  print(str)
if __name__ == "__main__":
  main()
