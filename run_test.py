import os

file = "test.c"
file_path = "./test_IO/" + file
os.system("python3 ./src/main.py " + file_path + " -n")
asm_file_path = file_path[0:len(file_path) - 2] + ".asm"
os.system("java -jar Mars4_5.jar " + asm_file_path)

