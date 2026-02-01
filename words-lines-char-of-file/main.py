# Program that reads a text file and prints the number of lines, words, and characters in it.

def characters():
    with open("1.txt", "r") as f: 
        character_count = 0
        data = f.read()
        for i in data:
            if i == "\n" or i == " ":
                continue
            character_count += 1
        return character_count

def words():
    with open("1.txt", "r") as f:
        data = f.read().split()
        return len(data)

def lines():
    count = 0
    with open("1.txt", 'r') as f:

        while True:
            line = f.readline()
            if not line:
                return count
            count += 1
    

print(f"Lines in File: {lines()} ")
print(f"Words in File: {words()}")
print(f"Characters in File: {characters()}")