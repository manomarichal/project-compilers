import os

os.system('find ./test_IO/working_examples -iname \'*.c\' -exec echo compiling {} \; -exec python ./src/main.py {} \;')
os.system('find ./test_IO/working_examples -iname \'*.ll\' -exec echo running {} \; -exec lli {} \;')