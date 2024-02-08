input1 = input("software title:")
input2 = input("License number:")

file1 = open("datadir\licenses.txt", "a")


file1.write(input1)
file1.write(":")
file1.write(input2 + "\n")
   #         ")

file1.write("---" + "\n")
   #        ")

file1.close
