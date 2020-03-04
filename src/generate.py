from os import system

system("java -jar antlr-4.8-complete.jar -Dlanguage=Python2 -no-listener -visitor -o ./antlr src/Math.g4")
