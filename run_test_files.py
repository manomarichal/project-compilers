import os

print(os.path.abspath("./"))

# os.system('find ./test_IO/working_examples -iname \'*.c\' -exec echo compiling {} \; -exec python ./src/main.py {} -n \;')
os.system('find ./test_IO/CompilersBenchmark/CorrectCode -iname \'*.c\' -exec echo compiling {} \; -exec python ./src/main.py {} -n \;')
