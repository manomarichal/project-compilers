from os import system

system("java -jar antlr-4.8-complete.jar -Dlanguage=Python2 -visitor -o ./antlr Math.g4")
