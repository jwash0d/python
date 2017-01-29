def word_count(string):
  dictionary = {}
  string_list = string.lower().split()
  for item in string_list:
    if item in dictionary:
      dictionary [item] += 1
    else:
      dictionary [item] = 1 ##or string not sure.... hmmm.
  return dictionary


d = word_count("James is the very very best")
print(d)