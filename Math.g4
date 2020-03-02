grammar Math;

INT : [0-9]+;
PLUS : '+' ;
MINUS : '-';
STAR : '*';
SLASH : '/';
LEFT_PAREN : '(';
RIGHT_PAREN : ')';
SEMICOLON : ';';
PERCENT : '%';
SMALLER_OP : '<';
GREATER_OP : '>';
EQUAL_OP : '==';
SMALLER_E_OP : '<=';
GREATER_E_OP : '>=';
NOT_EQUAL_OP : '!=';
AND_OP : '&&';
OR_OP : '||';
NOT_OP_OP : '!';
WS: [ \n\t\r]+ -> skip;


doc : ((bool_expr | math_expr) SEMICOLON)* EOF;
bool_expr : bool_expr (AND_OP | OR_OP | NOT_OP_OP) bool_expr | comp_expr;
comp_expr : math_expr (SMALLER_OP | GREATER_OP | EQUAL_OP | SMALLER_E_OP | GREATER_E_OP | NOT_EQUAL_OP) math_expr;
math_expr : LEFT_PAREN math_expr RIGHT_PAREN |
    math_expr STAR math_expr |
    math_expr SLASH math_expr |
    math_expr PERCENT math_expr |
    math_expr PLUS math_expr |
    math_expr MINUS math_expr |
    MINUS math_expr |
    PLUS math_expr |
    INT;