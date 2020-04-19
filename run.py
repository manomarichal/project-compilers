import os

print(os.path.abspath("./"))

os.system('find ./test_IO/CompilersBenchmark/CorrectCode -iname \'*.c\' -exec echo compiling {} \; -exec python ./src/main.py {} -n \;')
os.system('find ./test_IO/CompilersBenchmark/CorrectCode  -iname \'*.ll\' -exec echo running {} \; -exec lli {} \;')

print("\n"
      "---------------------------------------------------------\n"
      "Error detection tests below this line - supposed to fail!\n"
      "---------------------------------------------------------\n")

# os.system('find ./test_IO/CompilersBenchmark/SemanticErrors -iname \'*.c\' -exec echo compiling {} \; -exec python ./src/main.py {} \;')