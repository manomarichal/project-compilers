grammar Grammar;

CHAR: '\''[ -~] '\'';
INT : [0-9]+;
FLOAT : [0-9]+'.'[0-9]+;
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
CHAR_TYPE: 'char';
CONST: 'const';
ASSIGN_OP: '=';
PLUS : '+' ;
AMP : '&' ;
MINUS : '-';
STAR : '*';
SLASH : '/';
PERCENT : '%';
LEFT_PAREN : '(';
RIGHT_PAREN : ')';
SEMICOLON : ';';
SMALLER_OP : '<';
GREATER_OP : '>';
EQUAL_OP : '==';
SMALLER_E_OP : '<=';
GREATER_E_OP : '>=';
NOT_EQUAL_OP : '!=';
AND_OP : '&&';
OR_OP : '||';
INCR: '++';
DECR: '--';
NOT_OP : '!';
ID : [a-z]+;
WS: [ \n\t\r]+ -> skip;


doc : ((decl | expr) SEMICOLON)* EOF;

typeObj:  CONST? (INT_TYPE | FLOAT_TYPE | CHAR_TYPE) (CONST? STAR)* CONST?;

identifier: ID;

decl:  typeObj identifier ASSIGN_OP expr;

literal: INT | FLOAT | CHAR;

expr : LEFT_PAREN expr RIGHT_PAREN |
    expr (DECR | INCR) |
    (DECR | INCR) expr |
    (MINUS | PLUS) expr |
    (NOT_OP) expr |
    expr (STAR | SLASH | PERCENT) expr |
    expr (PLUS | MINUS) expr |
    expr (SMALLER_OP | SMALLER_E_OP) expr |
    expr (GREATER_OP | GREATER_E_OP) expr |
    expr (EQUAL_OP | NOT_EQUAL_OP) expr |
    expr AND_OP expr |
    expr OR_OP expr |
    <assoc=right> expr ASSIGN_OP expr |
    identifier |
    literal;