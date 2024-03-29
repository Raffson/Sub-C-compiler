# README: Sub-C Compiler

Author: Raffson

---

## Introduction
This project was made during the course 'Compilers' in the academic year 2016-2017. I decided to work alone even though it was recommended to work in groups of 2. The main reason was simply because I liked the challenge and I had considerably more time to spend on this course than most other students. Consequentially I did not want to get into situations where I would do most of the work and have someone else possibly mess up stuff because they can't follow along. Also the fact that we both would've had to understand all the code, I figured it would be easier if I did everything myself. I have to say, throughout the semester I sometimes found myself regretting that decision, but in the end everything turned out just fine.

## File structure and compiler usage
The root folder contains the grammar file (subC.g4) and all python files as well as the files generated by ANTLR4. The folder subcPrograms contains a number of samples that can be used to test the compiler. For each sample file, an AST has already been generated. Mind that the AST is overwritten every time the corresponding subC file is being used by the compiler.  
  To run the compiler simply execute the following command in terminal supposing that you're in the root folder:

```sh
$ python main.py <input-file>
```
A concrete example would be:

```sh
$ python main.py subcPrograms/alldemo.subc
```
Obviously having python installed is required in order for the compiler to work. Additionally for MacOSX and Linux 2 shell script were added, one to compile all .subc files within the subcPrograms folder and another one to run all .p files within the subcPrograms folder. A copy of the P-machine was added for convenience which you will have to compile with the provided makefile.

## Sample programs
Note: not all programs from the intermediate evaluation are present. This is simply because those aspects have already been tested and are useless at this point.

* arrayMath.subc  
This file tests mathematical operations on arrays of one dimension as well as 3-dimensional arrays. Also contains recursion & pass-by-reference situations.
* casedemo.subc  
This file tests switch-case statements simulating a simple calculator. 
* enigma.subc  
The flagship of all subC test-programs. This program simulates the enigma cipher as seen in the course "Codetheorie & Cryptografie". The program asks for a 3-letter key which indicates the starting position of the rotors. Then the program will ask for 3-digit string using numbers 0-7 that represents a rotor-combination. Additionally a 26-letter string will be asked representing the plugboard. If one wishes to connect two letters on the plugboard, simply swap the letters in your string (initially you start with ABCDEFGHIJKLMNOPQRSTUVWXZY, i.e. the alphabet in its normal order). At last a string is needed to encrypt/decrypt. Once that's done, the simulation will run & the resulting string will be printed. Aside from things that are already tested in other files, pointer arithmatic is one of the things tested. Also cast-expressions are thoroughly tested. A 2-dimensional stucture is being used by the variable that represents the selected rotors, thus that structure is also tested. Together with the tests in arrayMath.subc we can conclude that if it works for 1, 2 & 3 dimensions, the it will probably work for 4, 5, 6 & so on...
* factorialtest.subc  
As the name says, calculates the factorial (of 10) using a for-loop. Aside from that 2 other loops are presents just to test if the do-while & while statements work correctly. Also testing break statements here. Jump statement "continue" is not used in any of the files simply because "break" initially behaved like "continue" would thus this implicates "continue" works.
* gcd.subc  
Asks for 2 integers and calculates the greatest common divisor. This makes use of a for-loop and if-statement, thus testing those constructions. Within the if-statement's condition we test the "&&" operator as well as the "%" operator.
* printf.subc  
Mainly tests the "printf" function & the behaviour of argument passing to the printf function. Along the way most, if not all, operators are tested to verify its behaviour. Additionally nested if-statements are tested.
* recursivetest.subc  
Recursive program that calculates the 10th Fibonacci number.
* scanf.subc  
Tests the "scanf" function for integer, string, char and float. Also tests the use of global variables.
* swapper.subc  
Simple program that asks for two numbers & swaps them.

## Final status
The following is a brief list of implemented features:

* Iteration statements:
  * for
  * do-while
  * while   
* Selection statements:
  * if / if-else
  * switch
* Labeled statements:
  * case
  * default
* Operators: 
  * Binary: strongest type is result of expression
     * +, -, *, / (valid for common types except void)
     * %, <<, >> (valid for "int" only, no implicit cast available)
     * <, >, <=, >=, ==, !=, &&, ||  
     (valid for "int" only, implicit cast available)
  * Unary:
     * *, &, [ ], !, +, -, ++ (both pre & post), -- (both pre & post)  
  ++ and -- are only valid for common types except void
     * cast-operator (explicit type-cast)
     * sizeof-operator
  * Assignment:
     * =, +=, -=, *=, /=, %=, <<=, >>=  
  += and -= can be used for pointer arithmatic  
  same rules as binary operators apply
* Conditional expression:
  * *condition* ? *expr1* : *expr2*  
     where *expr1* & *expr2* are derived from a conditional expression in the grammar. *condition* is derived from a logical expression in the grammar.
* Functions:
  * definitions and calls obviously...
  * pass by value & pass by reference
* Jump statements:
  * return
  * break
  * continue
* Arrays:
  * open arrays
  * multi-dimensional arrays
  * array initialization
* "const" qualification
* Implicit type-casting
  * only applicable for common types (void excluded)
* printf & scanf

Due to the size of the project, some things that have been implemented may not have been mentioned simply because the list is too big. To summarize everything quickly, you can more or less compare the compiler with a regular C compiler except full support for dynamic memory, "volatile", "struct" & "union" types, typedefs, goto-statement with corresponding labels, pointers to functions, "enum", "extern", "static", "auto", "register", "double", "long", "(un)signed", "short", bitwise operations, "..." (ellipsis), xor and support for "<%" / "<:" aliases for "{" and "[" respectively.

## Symbol table
The symbol table is implemented as a ordered list (python's dictionary in this case) that maps a key, representing the variable, to an array that contains the relevant information. The first element of that array always represents the type of the variable. Depending on this type, the array contains the following infomation:  
 
* function:  
 * return type (string)
 * parameters (array)
 * symbol table for function (dictionary)
     * maps variables as follows:  
Key (variable's name) --> [ Type, initValue, Key ]  
If initValue is "None", it represents a parameter since these values have to be initialized depending in the arguments of the function-call. In addition to the first version an integer is stored between initValue and Key to indicate the order of the parameters. For variables that are not parameters an offset is added at the back of the array to calculate the position of the variable on the stack. As opposed to the first version, a variable is stored in its own scope. Scopes are now handled differently, i.e. they are also dictionaries like the symbol table. A special parameter type "constchar*format" is used in printf & scanf to identify its special needs.
* Any other type:  
As opposed to a function's symbol table, the global symbol table does not require a scope so the following mapping is used:  
Key (variable's name) --> [ Type, initValue, Key ]
Mind the fact that an address is appended during code-generation.
* Whenever a compound-statement is reached, a new dictionary is added and that dictionary becomes the active scope.

## Forward declaration table
Aside from the symbol table, a seperate table is used to maintain a list of forward declarated functions. This table has the following mapping:  
Key (function's name) --> [ returnType, [argTypes] ]  
Note that this table is not checked against the symbol table because if the parameter and/or return type(s) don't match, then the compiler will catch that problem during the type-checking part.

## Parser rules
subCListener2.py: Builds symbol table.

* enterDecl: adds variables to the corresponding symbol table or in case of a forward declarated function it is added to the forward declaration table
* enterProgram: adds true & false as constant integers to the global symbol table (still have to prevent in enterDecl that true & false be declared in a local scope)
* enterInclude: currently only checks for stdio and adds printf & scanf to the global symbol table
* enterFunctiondef: adds functions to the global symbol table and builds the necessary return & argument types

Reading from symbol tables is done from the following parser rules' functions:

* enterDecl: Reads from the corresponding symbol table to prevent redeclarations
* enterFunctiondef: Reads from the global symbol table to prevent redeclarations
* enterIdentfier: Reads from all symbol tables and forward declaration table to generate errors for undefined variables/functions
* exitProgram: Reads from the global symbol table to make sure the "main" function is present

subCVisitor2.py: Reduces the parsetree to an AST and outputs the AST to a .dot file.

* enterProgram: Jumps to a custom function that recursively reduces the parsetree to an AST.

subCListener3.py: Type-checking  

* Too many to rules to sum up. In short, every node in the AST takes types from a stack and pushes the resulting type back onto the stack to be used by the parent node. Along the way, all necessary type checks are performed.

subCListener4.py: Code generation

* Again too many to rules to sum up. The same strategy is used as in subCListener3.py except now also pieces of code are pushed/popped onto/off a seperate stack.

## Optimizations
No optimizations were implemented.

## Extra notes
* MAIN function:  
The main function does not support command-line arguments nor does it support a return type. If any of these are specified, they will be overwritten with no parameters (to avoid command-line arguments) and void as return type.

* INCLUDE directives:  
The following ways are available to include "stdio". This will give you to ability to use functions printf and scanf in your code:
 * \#include \<stdio>
 * \#incldue \<stdio.h>
 * \#include "stdio.h"  
* Scope of variables:  
Has changed compared to the first version due to a flaw in the design. At this point, every time a compound-statement is opened a new dictionary is created representing the scope of that compound-statement. The current scope is pushed to an array that will act as a stack and the new scope becomes the current scope. Upon exitting the compound-statement the last scope is popped from the array and assigned to the current scope.

* printf & scanf:  
 Input of strings is stored on the heap, thus being somewhat dynamic. The first argument can be either a string literal or a variable. In the latter case, no type checking is performed (just like in a real ANSI C compiler) & thus the programmer is expected to know what he's doing.