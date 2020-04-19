import os

os.system('find ./test_IO/CompilersBenchmark/CorrectCode -iname \'*.c\' -exec echo compiling {} \; -exec python ./src/main.py {} \;')
os.system('find ./test_IO/CompilersBenchmark/CorrectCode  -iname \'*.ll\' -exec echo running {} \; -exec lli {} \;')

print("Error detection tests below this line - supposed to fail!\n"
      "---------------------------------------------------------")

# os.system('find ./test_IO/error_examples -iname \'*.c\' -exec echo compiling {} \; -exec python ./src/main.py {} \;')