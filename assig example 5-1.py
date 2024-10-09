# quess 3
import string
def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence_letters = set(char.lower() for char in sentence if char.isalpha())
    return alphabet.issubset(sentence_letters)
test_sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Hello, world!",
    "Pack my box with five dozen liquor jugs.",
    "Sphinx of black quartz, judge my vow.",
    "This is not a pangram."
]
for sentence in test_sentences:
    print(f"'{sentence}' is a pangram: {is_pangram(sentence)}")

#ques 4
list1 = [1,3,4,45,66]
list2 = [29,25,4,99,66,44,3]
def overlapping(l1,l2):
    l1 = set(l1)
    l2 = set(l2)
    if(l1&l2):
        print("common elements : ", l1&l2)
        print("At least one member is common")
    else:
        print("NO member is common")
overlapping(list1,list2)

#ques 5
l=['vegetables','flowers','fruit','animlas','birds','ingredients']
def find_longest_word(l):
    for i in range(len(l)-1):
        longest=len(list(l[i]))
        if(len(list(l[i]))<len(list(l[i+1]))):
            longest=len(list(l[i+1]))
    print(f"length of the Longest in the list: {longest}")
find_longest_word(l)   

#ques 6
def fibonacci_sequence(n):
    fib_sequence = []
    a,b = 0,1
    for i in range(n):
        fib_sequence.append
        a,b =b, a+b
    return fib_sequence    
n = int(input("Enter the number of terms : "))
if n <= 0:
    print("please enter a positive integer:")
else:
    print(f"Fibonacci sequence up to {n} temrs : ({fibonacci_sequence(n)}")
    print(fibonacci_sequence(n))


