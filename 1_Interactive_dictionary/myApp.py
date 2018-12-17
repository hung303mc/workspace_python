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
    ans = input("did you mean %s instead?Enter Y if yes, or N if no:" % tmp[0])
    if ans == "Y":
      return data[tmp[0]]
    elif ans == "N":
      return "couldn't find word "
    else:
      return "we couldn't know what you want"
  else:
    return "couldn't find word "

word = input("Enter word: ")

output = translate(word)
if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)
