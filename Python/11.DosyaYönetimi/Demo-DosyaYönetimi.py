# Not Uygulaması
def notes_calculte(line):
    line = line[:-1]
    list = line.split(":")

    studentName= list[0]
    notes= list[1].split(',')

    not1 = int(notes[0])
    not2 = int(notes[1])
    not3 = int(notes[2])

    average = (not1+not2+not3)/3

    if average>90 and average<=100 :
        letter = "AA"
    elif average>=85 and average <= 89 :
        letter = "BA"
    elif average>=65 :
        letter = "CC"
    else :
        letter = "FF"

    return studentName + ": " + letter + "\n"
    
def averages_read():
    with open("question_notes.txt","r",encoding="utf-8") as file:
        for line in file : 
            print(notes_calculte(line))

def input_notes():
    name = input("Student name: ")
    lastName = input("Student last name: ")
    not1 = input("Student Notes 1: ")
    not2 = input("Student Notes 2: ")
    not3 = input("Student Notes 3: ")

    with open("question_notes.txt","a",encoding="utf-8") as file:
        file.write(name+" "+ lastName+ ":"+not1+","+not2+","+not3+ "\n") 

def register_notes():
    with open("question_notes.txt","r",encoding="utf-8") as file:
        list=[]
        for i in file:
            list.append(notes_calculte(i))

        with open("results.txt","w",encoding="utf-8") as file2:
            for i in list:
                file2.write(i)

while True:
    process = input('1-Read Notes\n2-Input Notes\n3-Register Notes\n4-Exit\n')

    if process == "1":
        averages_read()
    elif process == "2":
        input_notes()
    elif process == "3":
        register_notes()
    else:
        break
