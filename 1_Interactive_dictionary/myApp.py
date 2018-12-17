import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
  word = word.lower()
  tmp = []
  if word in data:
    return data[word]
  else:
    tmp = get_close_matches(word, data.keys(), 1, 0.8)

  if len(tmp) > 0:
    print("did you mean %s instead? " % tmp[0])
    ans = input("Enter Y if yes, or N if no: ")
    if ans == "Y":
      return data[tmp[0]]
    elif ans == "N":
      return ("couldn't find word " + word)
  else:
    return ("couldn't find word " + word)

word = input("Enter word: ")

print(translate(word))
