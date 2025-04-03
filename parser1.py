from lark import Lark, exceptions

grammar = '''
%import common.WS
%ignore WS

program: statements

statements: statement | statement statements

statement: declaration 
         | assignment 
         | if_statement 
         | loop 
         | function_def 
         | function_call

type: "INT" | "DEC" | "STR" | "BOOL"

declaration: type identifier "=" expression ";"

assignment: identifier "=" expression ";"

if_statement: "if" "(" expression ")" "{" statements "}"

loop: "while" "(" expression ")" "{" statements "}"

function_def: type identifier "(" parameter_list ")" "{" statements "}"

parameter_list: parameter | parameter "," parameter_list

parameter: type identifier

function_call: identifier "(" arguments ")" ";"

arguments: expression | expression "," arguments

expression: term 
          | expression "+" term 
          | expression "-" term
          | expression "*" term 
          | expression "/" term

term: number | identifier | "(" expression ")"

identifier: letter | identifier letter | identifier digit

number: digit | digit number

letter: "a".."z" | "A".."Z"

digit: "0".."9"
'''

parser = Lark(grammar)

test_string = "if (x + y) { x = x + 1; }"

try:
    parser.parse(test_string)
    print("The string follows the <program> rule!")
except exceptions.ParseError:
    print("The string does not follow the <program> rule.")
