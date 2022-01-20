import random

def classy():
  # print("Keep it logically awesome.") 

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last= 13
  # or can choose the next line. its same but diffrent expresion
  # last= len(quotes)-1

  rnd = random.randint(0,last)

  # print(quotes[13])
  print(quotes[rnd])

if __name__== "__main__":
  classy()
