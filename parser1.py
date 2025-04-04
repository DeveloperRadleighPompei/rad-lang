from lark import Lark

grammar = """
program: statements ";"
statements: statement | statement statements
statement: declaration | assignment | if_statement | loop | function_def | function_call
type: "INT" | "DEC" | "STR" | "BOOL"
declaration: type identifier "=" expression
assignment: identifier "=" expression
if_statement: "if" "(" expression ")" "{" statements "}"
loop: "while" "(" expression ")" "{" statements "}"
function_def: type identifier "(" parameter_list ")" "{" statements "}"
parameter_list: parameter | parameter "," parameter_list
parameter: type identifier
function_call: identifier "(" arguments ")"
arguments: expression | expression "," arguments
expression: term | expression "+" term | expression "-" term
          | expression "*" term | expression "/" term
term: number | identifier | "(" expression ")"
identifier: letter | identifier letter | identifier digit
number: digit | digit number
letter: "a".."z" | "A".."Z"
digit: "0".."9"
"""

with open("test.rad", "r") as f:
    input_text = f.read()

parser = Lark(grammar, start="program", parser="earley")

try:
    tree = parser.parse(input_text)
    print("Parsing succeeded")
    print(tree.pretty())
except Exception as e:
    print("Parsing failed:", e)
