import random

#main class
def classy():
  # print("Keep it logically awesome.") 

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last= 13
  # or can choose the next line. its same but diffrent expresion
  # last= len(quotes)-1

  rnd = random.randint(0,last)

  # before
  # print(quotes[13])

  numberofquotes = 2

  x=0
  while x < numberofquotes :
    print(quotes[rnd+x])
    x+=1

  else :
    print(numberofquotes)


if __name__== "__main__":
  classy()


