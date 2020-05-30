import os

os.system('python3 clean.py')
files = os.listdir('./test_IO/extra_tests')
files.sort()
print(os.path.abspath("./"))
for file in files:
    os.system("clear")
    file_path = "./test_IO/extra_tests/" + file
    print("##########################\nfile: " + file)
    os.system("cat " + file_path)
    print("\n##########################\ncompiling " + file)
    os.system("python3 ./src/main.py " + file_path)
    asm_file_path =  file_path[0:len(file_path)-2] + ".asm"
    print("\n##########################\nrunning " + asm_file_path)
    os.system("java -jar Mars4_5.jar " + asm_file_path)
    print("##########################")
    input("")




# os.system('find ./test_IO/working_examples -iname \'*.c\' -exec echo compiling {} \; -exec python ./src/main.py {} -n \;')
# os.system('find ./test_IO/CompilersBenchmark/CorrectCode -iname \'*.c\' -exec echo compiling {} \; -exec python3 ./src/main.py {} -n \;')
# os.system('find ./test_IO/CompilersBenchmark/CorrectCode -iname \'*.asm\' -exec echo running {} \; -exec cat {} \;-exec java -jar Mars4_5.jar {} \;')

