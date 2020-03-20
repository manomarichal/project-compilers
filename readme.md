# Project Compilers 2020
## Mano Marichal & Joren Van Borm

### Overview

We hebben alle mandatory dingen afgewerkt. Onderaan de readme kan je een overzicht zien van wat we allemaal gemaakt hebben.
Voor elk feature hebben we een testfile, in test_IO/working_examples/. Je kan voor al deze de llvm ir, dotfiles en ast visualization genereren met run.py.
clean.py verwijdert alle gegenereerde files uit test_IO/working_examples/. 

### Installing and running:

#### Clone git repository   
    
    git clone https://github.com/shano19/compilers-2020.git
 
#### Install **pip** 

    sudo apt-get install python3-pip

#### Install **virtualenv** using pip3

    sudo pip3 install virtualenv 

#### Create virtual environment 

    virtualenv venv 
  
#### Active virtual environment:    
    
    source venv/bin/activate

#### Install prerequisites:    
    
    pip3 install -r requirements.txt    
    
#### Run the test files  
    
    python3 run.py
    
 
#### Compiling a file  
    
    python3 ./src/main.py <filename> 

you can add the -c flag to indicate that constant folding should be used
    
### Status:
#### Project 1)
- 2.1 Grammar:
  -  [x] (mandatory) Binary operations + , - , * , and /
  -  [x] (mandatory) Binary operations > , < , and ==
  -  [x] (mandatory) Unary operators + and -
  -  [x] (mandatory) Brackets to overwrite the order of operations
  -  [x] (optional) Binary operator %
  -  [x] (optional) Comparison operators >= , <= , and !=
  -  [x] (optional) Logical operators && , || , and !
- [x] 2.2 (mandatory) AST
- [x] 2.3 (mandatory) Visualization
- [x] 2.4 (optional) Constant folding

#### Project 2)
- 1.1 Grammar:
    - [x] (mandatory) Types
        - [x] int
        - [x] float
        - [x] char
        - [x] pointer
    - [x] (mandatory) Reserved words
        - [x] const
        - [x] int
        - [x] float
        - [x] char
    - [x] (mandatory) Variables
    - [x] (optional) Identifier Operations ++ and --
    - [x] (optional) Implicit Conversions
- [x] 1.2 (mandatory) AST
- [x] 1.3 (mandatory) Visualization
- [x] 1.4 (optional) Constant Propagation
- [x] 2.1 (mandatory) Syntax errors
- [x] 2.2 (mandatory) Semantic errors

#### Project 3)
- 1.1 Grammar
    - [x] (mandatory) Comments
    - [ ] (optional) Not ignoring comments
    - [x] (mandatory) Printf
- [x] 1.2 (mandatory) AST
- [x] 1.3 (mandatory) Visualization
- [x] 2 (mandatory) LLVM
  -  [x] (mandatory) Binary operations + , - , * , and /
  -  [x] (mandatory) Binary operations > , < , and ==
  -  [x] (mandatory) Unary operators + and -
  -  [x] (mandatory) Brackets to overwrite the order of operations
  -  [x] (mandatory) Printf
  -  [x] (mandatory) Pointers + pointer operators
  -  [x] (optional) Identifier Operations ++ and --
  -  [x] (optional) Comments for each machine instruction
  -  [ ] (optional) Binary operator %
  -  [x] (optional) Comparison operators >= , <= , and !=
  -  [x] (optional) Logical operators && , || , and !
  -  [x] (optional) Constant folding
  -  [x] (optional) Implicit conversions (bool <> char <> int <> float)




