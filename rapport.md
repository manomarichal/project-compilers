# Project Compilers 2020 (C -> MIPS) 
## door Mano Marichal
### Algemene info:

Ik heb een paar scriptjes om de testfiles mooi uit te voeren:
- main.py: compileerd een enkele file & genereerd een dot en png file van de AST. Verdere uitleg onder **Installing and running - Compiling a file**
- run_benchmarks.py: genereert voor alle c files in **./test_IO/CompilersBenchmark** de llvm ir, mips, dotfiles en de ast als png
- run_test_files.py: genereert voor alle c files in **./test_IO/extra_tests** de llvm ir, mips, dotfiles en de ast als png
- clean.py: verwijdert alle gegenereerde files uit **./test_IO/**

**Overview of the features**

- [x] = implemented in MIPS
- [ ] = not implemented in MIPS 

### Mandatory features:
- [x] binary operations + , - , * , and /
- [x] binary operations > , < , and ==
- [x] unary operators + and -
- [x] char
- [x] int
- [x] float
- [x] pointers
- [x] pointer operations * and &
- [x] if
- [x] else
- [x] while
- [x] for
- [x] break
- [x] continue
- [x] global variables
- [x] functions
- [x] printf
- [x] scanf
- [x] arrays

### Optional features:
- [x] binary operator %
- [x] comparison operators >= , <= , and !=
- [x] logical operators && , || , and !
- [x] identifier Operations ++ and --
- [x] implicit Conversions (+ warnings for non-promotions)
- [ ] include comments in compiled LLVM
- [ ] switch
- [ ] case
- [ ] default
- [ ] arrays with variable size
- [ ] multi-dimensional arrays

### Notes: 
Omdat ik pas vrij laat te weten kwam dat ik alleen werkte, heb ik door tijdsproblemen hier en daar wat dingen niet volledig afgekregen:
- Arrays kunnen niet via een pointer worden aangesproken, en niet als function arguments gebruikt worden
- Ik support de string notatie voor char arrays niet (wel in de grammar en de ast, maar niet in MIPS)
- Ik support geen functies met meer dan 4 argumenten
- Er is geen support voor multi-declaraions (int a, b=3, c;)

