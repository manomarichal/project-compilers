grammar Grammar;

CHAR : '\''[ -~] '\'';
INT : [0-9]+;
FLOAT : [0-9]+'.'[0-9]+;
INT_TYPE : 'int';
FLOAT_TYPE : 'float';
CHAR_TYPE : 'char';
CONST : 'const';
IF_KW : 'if';
ELSE_KW : 'else';
SWITCH_KW : 'switch';
CASE_BRANCH : 'case';
DEFAULT_BRANCH : 'default';
FOR_KW : 'for';
WHILE_KW : 'while';
BREAK_KW : 'break';
CONT_KW : 'continue';
VOID_KW : 'void';
RETURN_KW: 'return';
COMMA: ',';
ASSIGN_OP : '=';
PLUS : '+' ;
AMP : '&' ;
MINUS : '-';
STAR : '*';
SLASH : '/';
PERCENT : '%';
LEFT_PAREN : '(';
RIGHT_PAREN : ')';
LEFT_C_BRACE : '{' ;
RIGHT_C_BRACE: '}';
SEMICOLON : ';';
COLON : ':';
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
PRINT : 'printf';
ID : [_a-zA-Z][_a-zA-Z0-9]*;
WS: [ \n\t\r]+ -> skip;
COMMENT_SINGLE: '//'~('\r'|'\n')* -> skip;
COMMENT_MULTI: '/*' .*? '*/' -> skip;


doc : block? EOF;

block: statement+;

typeObj:  CONST? (INT_TYPE | FLOAT_TYPE | CHAR_TYPE) (CONST? STAR)* CONST?;

identifier: ID;

statement: functionDecl | (general_expr | control) SEMICOLON | construct;

control: BREAK_KW | CONT_KW;

functionDecl: typeObj identifier LEFT_PAREN ( (typeObj identifier) (COMMA typeObj identifier)* )? RIGHT_PAREN stateOrScope;

functionCall: identifier LEFT_PAREN ( (general_expr) (COMMA general_expr)* )? RIGHT_PAREN;

// TODO: I don't really know the rules here (eg. for(int a=0; ...) allowed but not if(int a=0) or while(int a=0) according to online compiler)
parenCond: LEFT_PAREN general_expr RIGHT_PAREN;

stateOrScope: statement | scopeConstr;

construct: ifConstr | switchConstr | forConstr | whileConstr | scopeConstr;

scopeConstr: LEFT_C_BRACE block RIGHT_C_BRACE;

ifConstr: IF_KW parenCond stateOrScope (ELSE_KW stateOrScope)?;

switchConstr: SWITCH_KW parenCond LEFT_C_BRACE caseBranch* defaultBranch? RIGHT_C_BRACE;

caseBranch: CASE_BRANCH literal COLON block;

defaultBranch: DEFAULT_BRANCH COLON block;

forConstr: FOR_KW LEFT_PAREN general_expr SEMICOLON general_expr SEMICOLON general_expr RIGHT_PAREN stateOrScope;

whileConstr: WHILE_KW parenCond  stateOrScope;


general_expr: (RETURN_KW)? (decl | expr | printf | functionCall); // TODO: fix naming (this should be the simpler name)

decl:  typeObj identifier ASSIGN_OP expr |
    typeObj identifier;

literal: INT | FLOAT | CHAR;

expr : LEFT_PAREN expr RIGHT_PAREN |
    expr (DECR | INCR) |
    (DECR | INCR) expr |
    (MINUS | PLUS) expr |
    (AMP | STAR) expr |
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
    literal |
    functionCall;

printf : PRINT LEFT_PAREN (literal | identifier) RIGHT_PAREN; // TODO: print any (general) expression