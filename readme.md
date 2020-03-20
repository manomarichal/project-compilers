# Project Compilers 2020
## Mano Marichal & Joren Van Borm

### Overview

We hebben alle mandatory dingen afgewerkt. Onderaan de readme kan je een overzicht zien van wat we allemaal gemaakt hebben.
Voor elk feature hebben we een testfile, in test_IO/working_examples Je kan voor al deze de llvm ir en ast dot / png files genereren met run.py.
clean.py Verwijdert alle gegenereerde files uit test_IO/working_examples. 

### Installing and running:
(assuming a linux-based system)

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

to deactivate it later, use the `deactivate` command

#### Install prerequisites:    
    
    pip3 install -r requirements.txt    
    
#### Run the test files  
    
    python3 run.py
 
#### Compiling a file  
    
    python3 ./src/main.py <filename> 

you can add the `-cf flag` after `<filename>` to enable constant folding
    
### Status:
#### Project 1)
- 2 Expression Parser
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
- 1 Variables:
    - 1.1 Grammar:
        - (mandatory) Types
            - [x] char
            - [x] int
            - [x] float
            - [x] pointer
        - (mandatory) Reserved words
            - [x] const
            - [x] int
            - [x] float
            - [x] char
        - [x] (mandatory) Variables
        - [x] (mandatory) Pointer Operations * and &
        - [x] (optional) Identifier Operations ++ and --
        - [x] (optional) Implicit Conversions (+ warnings for non-promotions)
- [x] 1.2 (mandatory) AST
- [x] 1.3 (mandatory) Visualization
- [ ] 1.4 (optional) Constant Propagation
- 2 Error Analysis
    - [x] 2.1 Syntax Errors
    - [x] 2.2 Semantic Errors
        - [x] undefined & uninitialised variables
        - [x] redeclared & redefined variables
        - [x] operations on incompatible types (dereferencing a non-ptr type)
        - [x] Assignment to an rvalue
        - [x] Assignment to a const variable
        - [x] Symbol table (scoped)

#### Project 3)
- 1 Variables
    - 1.1 Grammar
        - [x] (mandatory) Comments
        - [x] (mandatory) printf() for char, int & float (without metastring)
    - [x] 1.2 (mandatory) AST
    - [x] 1.3 (mandatory) Visualization
    - 2 (mandatory) LLVM
      - [x] (mandatory) Binary operations + , - , * , and /
      - [x] (mandatory) Binary operations > , < , and ==
      - [x] (mandatory) Unary operators + and -
      - [x] (mandatory) Brackets to overwrite the order of operations
      - [x] (mandatory) Printf
      - [x] (mandatory) Pointers + pointer operators
      - [x] (optional) Identifier Operations ++ and --
      - [x] (optional) Comments for each machine instruction
      - [x] (optional) Comparison operators >= , <= , and !=
      - [x] (optional) Logical operators && , || , and !
      - [x] (optional) Conversions (bool <> char <> int <> float)
      - [ ] (optional) Binary operator %
      - [ ] (optional) Include comments in compiled LLVM




