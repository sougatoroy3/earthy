'''Problem

You are required to enter a word that consists of 
and  that denote the number of Zs and Os respectively. 
The input word is considered similar to word zoo if 2x=y

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar
to word zoo but not the words such as zzooo and zzzooooo.

Input format
First line: A word that starts with several Zs and continues
by several Os.Note: The maximum length of this word must be 20

Output format

Print Yes if the input word can be considered as the string zoo
otherwise, print No.
'''

word=input()
x=word.count('z')
y=word.count('o')
print(x,y)
if x*2==y:
    print('Yes')
else:
    print('No')