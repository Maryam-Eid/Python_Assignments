# 1
import os

os.chdir(r"C:\Users\Maryam\Desktop")

os.makedirs("Python")

file = open(r"Python\assign.py", "x")

for i in range(50):
    with open(fr"Python\text{i + 1}.txt", "a") as txt_file:
        txt_file.write(f"Elzero Web School => {i + 1}")
        if i == 24:
            txt_file.truncate(0)

os.rename(r"Python\text25.txt", r"Python\special-text.txt")

print("Current Working Directory: ", os.getcwd())
print("Opened File Path: ", os.path.dirname(os.path.abspath(file.name)))
print("Opened File Name: ", os.path.basename(file.name))
print("Files Count in Python Directory:", len(os.listdir("Python")))
print("#" * 20)

# 2
text1 = open(r"Python\text1.txt", "a")
text1.write("\nAppended => Elzero Web School " * 50)
text1.close()

# 3
text1 = open(r"Python\text1.txt", "r")
print("Number Of Lines is: ", len(text1.readlines()))
text1.seek(0)
print("Number Of Words is: ", sum(len(word.split()) for word in text1))
text1.seek(0)
print("Number Of Chars is: ", len(text1.read()))
text1.seek(0)
print("Number Of 'l' Char is: ", sum(char.count("l") for char in text1))

# 4
for i in range(10):
    os.remove(rf"Python\text{41 + i}.txt")
