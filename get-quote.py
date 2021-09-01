import random

def print_a_line():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)

  for i in range(rnd): 
    print(quotes[rnd])
    rnd = random.randint(0, last)

if __name__== "__main__":
  print_a_line()
