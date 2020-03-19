import os

os.system('find ./test_IO/working_examples -iname \'*.ll\' -exec rm {} \;')
os.system('find ./test_IO/working_examples -iname \'*.dot\' -exec rm {} \;')
os.system('find ./test_IO/working_examples -iname \'*.png\' -exec rm {} \;')
