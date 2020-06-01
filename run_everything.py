import os

os.system('python3 clean.py')
files = os.listdir('./test_IO/extra_tests')
files.sort()
for file in files:
    file_path = "./test_IO/extra_tests/" + file
    print("compiling " + file)
    os.system("python3 ./src/main.py " + file_path + ' -n')

files = os.listdir('./test_IO/CompilersBenchmark/CorrectCode')
files.remove('.DS_Store')
files.sort()
for file in files:
    file_path = "./test_IO/CompilersBenchmark/CorrectCode/" + file
    print("compiling " + file)
    os.system("python3 ./src/main.py " + file_path + ' -n')


# os.system('find ./test_IO/working_examples -iname \'*.c\' -exec echo compiling {} \; -exec python ./src/main.py {} -n \;')
# os.system('find ./test_IO/CompilersBenchmark/CorrectCode -iname \'*.c\' -exec echo compiling {} \; -exec python3 ./src/main.py {} -n \;')
# os.system('find ./test_IO/CompilersBenchmark/CorrectCode -iname \'*.asm\' -exec echo running {} \; -exec cat {} \;-exec java -jar Mars4_5.jar {} \;')

