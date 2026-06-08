grammar MiniGo;

// =====================================================
// Parser rules
// =====================================================


root
    : PACKAGE IDENTIFIER SEMI topDeclarationList EOF
    ;

topDeclarationList
    : (variableDecl | typeDecl | funcDecl)*
    ;

variableDecl
    : VAR singleVarDecl SEMI
    | VAR LPAREN innerVarDecls? RPAREN SEMI
    ;

innerVarDecls
    : singleVarDecl SEMI (singleVarDecl SEMI)*
    ;

singleVarDecl
    : identifierList declType ASSIGN expressionList
    | identifierList ASSIGN expressionList
    | singleVarDeclNoExps
    ;

singleVarDeclNoExps
    : identifierList declType
    ;

typeDecl
    : TYPE singleTypeDecl SEMI
    | TYPE LPAREN innerTypeDecls? RPAREN SEMI
    ;

innerTypeDecls
    : singleTypeDecl SEMI (singleTypeDecl SEMI)*
    ;

singleTypeDecl
    : IDENTIFIER declType
    ;

funcDecl
    : funcFrontDecl block SEMI
    ;

funcFrontDecl
    : FUNC IDENTIFIER LPAREN funcArgDecls? RPAREN declType?
    ;

funcArgDecls
    : singleVarDeclNoExps (COMMA singleVarDeclNoExps)*
    ;

declType
    : LPAREN declType RPAREN
    | IDENTIFIER
    | sliceDeclType
    | arrayDeclType
    | structDeclType
    ;

sliceDeclType
    : LBRACK RBRACK declType
    ;

arrayDeclType
    : LBRACK INTLITERAL RBRACK declType
    ;

structDeclType
    : STRUCT LBRACE structMemDecls? RBRACE
    ;

structMemDecls
    : singleVarDeclNoExps SEMI (singleVarDeclNoExps SEMI)*
    ;

identifierList
    : IDENTIFIER (COMMA IDENTIFIER)*
    ;

expressionList
    : expression (COMMA expression)*
    ;

expression
    : primaryExpression
        #primaryExpressionOnly

    | PLUS expression
        #unaryPlusExpression

    | MINUS expression
        #unaryMinusExpression

    | NOT expression
        #unaryNotExpression

    | CARET expression
        #unaryBitNotExpression

    | expression multiplicativeOp expression
        #multiplicativeExpression

    | expression additiveOp expression
        #additiveExpression

    | expression relationalOp expression
        #relationalExpression

    | expression AND expression
        #logicalAndExpression

    | expression LOGICAL_OR expression
        #logicalOrExpression
    ;

multiplicativeOp
    : STAR
    | DIV
    | MOD
    | LSHIFT
    | RSHIFT
    | AMP
    | BIT_CLEAR
    ;

additiveOp
    : PLUS
    | MINUS
    | PIPE
    | CARET
    ;

relationalOp
    : EQUALS
    | NOT_EQUALS
    | LT
    | LTE
    | GT
    | GTE
    ;

primaryExpression
    : operand (selector | index | arguments)*
    | appendExpression
    | lengthExpression
    | capExpression
    ;

operand
    : literal
    | IDENTIFIER
    | LPAREN expression RPAREN
    ;

literal
    : INTLITERAL
    | FLOATLITERAL
    | RUNELITERAL
    | RAWSTRINGLITERAL
    | INTERPRETEDSTRINGLITERAL
    ;

index
    : LBRACK expression RBRACK
    ;

arguments
    : LPAREN expressionList? RPAREN
    ;

selector
    : DOT IDENTIFIER
    ;

appendExpression
    : APPEND LPAREN expression COMMA expression RPAREN
    ;

lengthExpression
    : LEN LPAREN expression RPAREN
    ;

capExpression
    : CAP LPAREN expression RPAREN
    ;

statementList
    : statement*
    ;

block
    : LBRACE statementList RBRACE
    ;

statement
    : PRINT LPAREN expressionList? RPAREN SEMI
    | PRINTLN LPAREN expressionList? RPAREN SEMI
    | RETURN expression? SEMI
    | BREAK SEMI
    | CONTINUE SEMI
    | simpleStatement SEMI
    | block SEMI
    | switchStmt SEMI
    | ifStatement SEMI
    | loop SEMI
    | typeDecl
    | variableDecl
    ;

simpleStatement
    : nonEmptySimpleStatement?
    ;

nonEmptySimpleStatement
    : assignmentStatement
    | expressionList DECLARE_ASSIGN expressionList
    | expression (INC | DEC)?
    ;

assignmentStatement
    : expressionList ASSIGN expressionList
    | expression assignmentOp expression
    ;

assignmentOp
    : PLUS_ASSIGN
    | AMP_ASSIGN
    | MINUS_ASSIGN
    | PIPE_ASSIGN
    | STAR_ASSIGN
    | CARET_ASSIGN
    | LSHIFT_ASSIGN
    | RSHIFT_ASSIGN
    | BIT_CLEAR_ASSIGN
    | MOD_ASSIGN
    | DIV_ASSIGN
    ;

ifStatement
    : IF (nonEmptySimpleStatement SEMI)? expression block (ELSE (ifStatement | block))?
    ;

loop
    : FOR block
    | FOR expression block
    | FOR nonEmptySimpleStatement? SEMI expression? SEMI nonEmptySimpleStatement? block
    ;

switchStmt
    : SWITCH (nonEmptySimpleStatement SEMI)? expression? LBRACE expressionCaseClauseList RBRACE
    ;

expressionCaseClauseList
    : expressionCaseClause*
    ;

expressionCaseClause
    : expressionSwitchCase COLON statementList
    ;

expressionSwitchCase
    : CASE expressionList
    | DEFAULT
    ;

// =====================================================
// Lexer rules
// =====================================================

// Keywords
PACKAGE     : 'package';
VAR         : 'var';
TYPE        : 'type';
FUNC        : 'func';
STRUCT      : 'struct';

IF          : 'if';
ELSE        : 'else';
FOR         : 'for';
SWITCH      : 'switch';
CASE        : 'case';
DEFAULT     : 'default';

BREAK       : 'break';
CONTINUE    : 'continue';
RETURN      : 'return';

PRINT       : 'print';
PRINTLN     : 'println';

APPEND      : 'append';
LEN         : 'len';
CAP         : 'cap';

// Operators and punctuation
DECLARE_ASSIGN      : ':=';

PLUS_ASSIGN         : '+=';
MINUS_ASSIGN        : '-=';
STAR_ASSIGN         : '*=';
DIV_ASSIGN          : '/=';
MOD_ASSIGN          : '%=';
AMP_ASSIGN          : '&=';
PIPE_ASSIGN         : '|=';
CARET_ASSIGN        : '^=';
LSHIFT_ASSIGN       : '<<=';
RSHIFT_ASSIGN       : '>>=';
BIT_CLEAR_ASSIGN    : '&^=';

EQUALS              : '==';
NOT_EQUALS          : '!=';
LTE                 : '<=';
GTE                 : '>=';

AND                 : '&&';
LOGICAL_OR          : '||';

INC                 : '++';
DEC                 : '--';

LSHIFT              : '<<';
RSHIFT              : '>>';
BIT_CLEAR           : '&^';

ASSIGN              : '=';
LT                  : '<';
GT                  : '>';

PLUS                : '+';
MINUS               : '-';
STAR                : '*';
DIV                 : '/';
MOD                 : '%';

AMP                 : '&';
PIPE                : '|';
CARET               : '^';
NOT                 : '!';

LPAREN              : '(';
RPAREN              : ')';
LBRACE              : '{';
RBRACE              : '}';
LBRACK              : '[';
RBRACK              : ']';

COMMA               : ',';
SEMI                : ';';
COLON               : ':';
DOT                 : '.';

// Literals
FLOATLITERAL
    : DECIMALS DOT DECIMALS? EXPONENT?
    | DOT DECIMALS EXPONENT?
    | DECIMALS EXPONENT
    ;

INTLITERAL
    : DECIMAL_LIT
    | BINARY_LIT
    | OCTAL_LIT
    | HEX_LIT
    ;

RUNELITERAL
    : '\'' (ESCAPED_VALUE | ~['\\\r\n]) '\''
    ;

RAWSTRINGLITERAL
    : '`' ~[`]* '`'
    ;

INTERPRETEDSTRINGLITERAL
    : '"' (ESCAPED_VALUE | ~["\\\r\n])* '"'
    ;

IDENTIFIER
    : LETTER (LETTER | UNICODE_DIGIT)*
    ;

// Comments and whitespace
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

// Fragments
fragment LETTER
    : [a-zA-Z_]
    ;

fragment UNICODE_DIGIT
    : [0-9]
    ;

fragment DECIMALS
    : [0-9] ('_'? [0-9])*
    ;

fragment DECIMAL_LIT
    : '0'
    | [1-9] ('_'? [0-9])*
    ;

fragment BINARY_LIT
    : '0' [bB] ('_'? [01])+
    ;

fragment OCTAL_LIT
    : '0' [oO]? ('_'? [0-7])+
    ;

fragment HEX_LIT
    : '0' [xX] ('_'? HEX_DIGIT)+
    ;

fragment HEX_DIGIT
    : [0-9a-fA-F]
    ;

fragment EXPONENT
    : [eE] [+-]? DECIMALS
    ;

fragment ESCAPED_VALUE
    : '\\' (
          [abfnrtv\\'"]
        | [0-7] [0-7] [0-7]
        | 'x' HEX_DIGIT HEX_DIGIT
        | 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
        | 'U' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
      )
    ;