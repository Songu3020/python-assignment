sample = input("Enter word: ")
print()
speak ="ing"
abc = "ly"
empty = ""  
length = len(sample)
if sample.endswith(speak):
   print(sample, abc)
if length > 3:
   print(sample,speak)
elif length == 3:
  print(sample,speak )
else:
    print(empty)
 

