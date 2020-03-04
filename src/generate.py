from os import system

system("java -jar antlr-4.8-complete.jar -Dlanguage=Python3 -no-listener -visitor -o src/antlr src/Math.g4")
