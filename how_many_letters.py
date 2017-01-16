inp = input("Enter a file to see (only txt files):- ")
file = open(inp)
inp2 = input("Letter to count:- ")
letters = dict()

for line in file:
    words = line.split()
    for word in words:
        for letter in word:
            if letter == inp2.upper() or letter == inp2.lower():
                letters[letter.lower()] = letters.get(letter.lower(), 0) + 1

final_answer = letters.items()

for kee,val in final_answer:
    print("The letter", kee, "appears", val, "times.")