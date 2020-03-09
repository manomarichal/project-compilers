grammar Grammar;

INT : [0-9]+;

PLUS : '+' ;
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
NOT_OP : '!';
WS: [ \n\t\r]+ -> skip;


doc : ((bool_expr | math_expr) SEMICOLON)* EOF;

bool_expr : LEFT_PAREN bool_expr RIGHT_PAREN |
    NOT_OP bool_expr |
    bool_expr AND_OP bool_expr |
    bool_expr OR_OP bool_expr |
    comp_expr;

comp_expr : math_expr (SMALLER_OP | GREATER_OP | EQUAL_OP | SMALLER_E_OP | GREATER_E_OP | NOT_EQUAL_OP) math_expr;

math_expr : LEFT_PAREN math_expr RIGHT_PAREN |
    (MINUS | PLUS) math_expr |
    math_expr (STAR | SLASH | PERCENT) math_expr |
    math_expr (PLUS | MINUS) math_expr |
    INT;