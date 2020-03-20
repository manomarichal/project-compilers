import os

os.system('find ./test_IO/ -iname \'*.ll\' -exec rm {} \;')
os.system('find ./test_IO/ -iname \'*.dot\' -exec rm {} \;')
os.system('find ./test_IO/ -iname \'*.png\' -exec rm {} \;')
