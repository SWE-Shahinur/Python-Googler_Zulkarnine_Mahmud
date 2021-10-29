with open("barak ovama.txt", mode="r") as b_file:
    for line in b_file.readlines():
        print(line.strip())

print("shahinur ",end="")
print("finised")
with open("barak ovama.txt", mode="r") as b_file:
    for line in b_file.readlines():
        words=line.strip().split(" ")#strip-string return kore
        print(words)
print("word finised")

with open("barak ovama.txt", mode="r") as b_file:
    worde_all=[]
    for line in b_file.readlines():
        words=line.strip().split()
        worde_all += words
    unique_word = set(worde_all)
    print(worde_all)
    print(len(worde_all))
    print(unique_word)
    print(len(unique_word))

    with open("unique_word.txt",mode="w") as write_file:
        for item in unique_word:
            write_file.write(item)
            write_file.write(" \n")

print("finised")