import os

os.system('python3 clean.py')
files = os.listdir('./test_IO/CompilersBenchmark/CorrectCode')
print(os.path.abspath("./"))
for file in files:
    input("")
    os.system("clear")
    file_path = "./test_IO/CompilersBenchmark/CorrectCode/" + file
    print("\n##########################\nfile: " + file)
    os.system("cat " + file_path)
    print("compiling " + file)
    os.system("python3 ./src/main.py " + file_path + " -n")
    asm_file_path =  file_path[0:len(file_path)-2] + ".asm"
    print("running " + asm_file_path)
    os.system("java -jar Mars4_5.jar " + asm_file_path)



# os.system('find ./test_IO/working_examples -iname \'*.c\' -exec echo compiling {} \; -exec python ./src/main.py {} -n \;')
# os.system('find ./test_IO/CompilersBenchmark/CorrectCode -iname \'*.c\' -exec echo compiling {} \; -exec python3 ./src/main.py {} -n \;')
# os.system('find ./test_IO/CompilersBenchmark/CorrectCode -iname \'*.asm\' -exec echo running {} \; -exec cat {} \;-exec java -jar Mars4_5.jar {} \;')

