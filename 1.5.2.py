
def main():
  search_note = "A"
  note = input().strip().split(" ")
  coun = 0
  for i in note:
    if i == search_note:
      coun += 1

  print('{:.2f}'.format(coun/len(note)))

if __name__ == "__main__":
  main()
