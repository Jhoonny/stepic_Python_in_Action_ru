text = ("{0} and {1} sat in the tree.\n"
"{0} had fallen, {1} was stolen.\n"
"What's remaining in the tree?\n")

def main():
  a = input().strip()
  b = input().strip()

  print(text.format(a, b))

if __name__ == "__main__":
  main()
