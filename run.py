import os

os.system('find ./test_IO/examples -iname \'*.c\' -exec python ./src/main.py {} \;')
# os.system('find ./test_IO/examples -iname \'*.ll\' -exec lli {} \;')