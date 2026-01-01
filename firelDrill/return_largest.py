word = 'Welcome','out','Weather','mobile','breakfast','journey'
longest = word[0] 
for word in word:
    if len(word) > len (longest):
        longest = word

print(longest)
print(len(longest))


