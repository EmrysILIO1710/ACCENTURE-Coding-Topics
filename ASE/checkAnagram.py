# an anagram is a word formed by rearranging the letters of another word. input two words and check if they are anagrams.

word1 = input()
word2 = input()
word1 = list(word1)
word1.sort()
word2 = list(word2)
word2.sort()
if word1 == word2:
    print("yes")
else:
    print("no")