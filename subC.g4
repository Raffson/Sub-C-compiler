grammar subC;

primaryexpr	:	identifier
		|	Constant
		|	Stringliteral
		|	'(' expr ')'
		;

postfixexpr	:	primaryexpr (('[' expr ']' | '('  (((assignexpr ',')+)? assignexpr)? ')' | ('.'|'->') identifier | ('++'|'--'))+)?
			/*primaryexpr
		| 	postfixexpr '[' expr ']'
		| 	postfixexpr '(' (((assignexpr ',')+)? assignexpr)? ')'
		| 	postfixexpr ('.'|'->') identifier
		| 	postfixexpr ('++'|'--')*/
		;

unaryexpr	:	postfixexpr
		|	('++'|'--') unaryexpr
		|	('&'|'*'|'+'|'-'|'!') castexpr
		|	'sizeof' (unaryexpr | '(' typename ')')
		;

castexpr	:	(('(' typename ')')+)? unaryexpr
		;

mulexpr		:	castexpr
		|	mulexpr ('*'|'/'|'%') castexpr
		;

addexpr		:	mulexpr
		|	addexpr ('+'|'-') mulexpr
		;

shiftexpr	:	addexpr
		|	shiftexpr ('<<'|'>>') addexpr
		;

relationalexpr	:	shiftexpr
		|	relationalexpr ('<' | '>') ('=')?  shiftexpr
		;

equalityexpr	:	relationalexpr
		|	equalityexpr ('==' | '!=') relationalexpr
		;

logicandexpr	:	equalityexpr
		|	logicandexpr '&&' equalityexpr
		;

logicorexpr	:	logicandexpr
		|	logicorexpr '||' logicandexpr
		;

conditionalexpr	:	(logicorexpr ('?' conditionalexpr ':' conditionalexpr)?)
		;

assignexpr	:	conditionalexpr
		|	unaryexpr (('*'|'+'|'-'|'/'|'%'|'>>'|'<<')? '=') assignexpr
		;

expr		:	(((assignexpr ',')+))? assignexpr
		;

decl		:	declspecifiers (((initdecltor ',')+)? initdecltor)? ';'
		;

declspecifiers	/*:	'typedef' declspecifiers? */
		:	typequal? typespecifier
		;

initdecltor	:	(declarator ('=' initializer)?)
		;

typespecifier	:	('void' | 'char' | 'float' | 'int')  /* | identifier) */
		;

typequal	:	'const'
		;

declarator	:	pointer ddeclarator
		|	ddeclarator
		;

ddeclarator	:	(identifier | '(' declarator ')') (('[' conditionalexpr? ']' | '(' ((((paramdecl ',')+)? paramdecl) | (((identifier ',')+) identifier))? ')')+)?
		;

pointer		:	('*' typequal? pointer?)
		;

paramdecl	:	(declspecifiers (declarator | abstractdecltor)?)
		;

typename	:	(declspecifiers (abstractdecltor)?)
		;

abstractdecltor	:	pointer
		|	pointer? dabstractdecltor
		;

dabstractdecltor:	('(' (abstractdecltor | (((paramdecl ',')+)? paramdecl))? ')' | '[' conditionalexpr? ']')+
		;

initializer	:	conditionalexpr
		|	'{' ((initializer ',')+)? initializer '}'
		;

statement	:	labeled
		|	compounds
		|	expr? ';'
		|	selection
		|	iteration
		|	jump
		;

labeled		:	((identifier ':') | ('case' conditionalexpr ':') | ('default' ':')) statement
		;

compounds	:	'{' ((decl | statement)+)? '}'
		;

selection 	:	'if' '(' expr ')' statement ('else' statement)?
		|	'switch' '(' expr ')' statement
		;

iteration	:	'while' '(' expr ')' statement
		|	'do' statement 'while' '(' expr ')' ';'
		|	'for' '(' expr ';' expr ';' expr ')' statement
		;

jump		:	('continue' | 'break' | 'return' expr?) ';'
		;

program		:	(edecl+)? EOF

Translunit edecl
edecl
		;

edecl		:	functiondef
		|	decl
		|	include
		;

include		:	'#' 'include' ('<stdio>' | '<stdio.h>' | '"stdio.h"')
			/* in the future we may want to support other includes...
			'#' 'include' '<' File '>'
		|	'#' 'include' '"' File '"' */
		;

functiondef	:	declspecifiers? declarator (decl+)? compounds
		;

identifier	:	Id
		;

Id		:	LETTER (LETTER | DIGIT)*
		;

Constant	:	DIGITS
		|	DIGIT
		|	OCTAL_D
		|	HEX_D
		|	(FRAC|DIGITS) EXP?
		|	'\'' CHAR '\''
		;

Stringliteral	:	'"' CHARSEQ? '"'
		;

File		:	(LETTER | DIGIT | '.')+
		;


/* Let's try to support unicode right away...
NONDIGIT	: [a-zA-Z_] ;
*/
fragment LETTER		: [a-zA-Z\u0080-\u00FF_] ;
fragment DIGITS		: [1-9] [0-9]* ;
fragment DIGIT		: [0-9];
fragment OCTAL_D	: '0' [0-7]+ ;
fragment HEX_D		: '0x' ([0-9]|[a-f]|[A-F])+ ;
fragment FRAC		: (DIGIT* '.' DIGIT+) | (DIGIT+ '.' DIGIT*) ;
fragment EXP		: [eE] '-'? DIGITS;
fragment CHARSEQ	: CHAR+;
fragment CHAR		: ~["\\\r\n]
			| '\\' ['"?abfnrtv\\]
			| '\\\n'   // Added line
			| '\\\r\n' // Added line
			;

COMMENT		:	'/*' .*? '*/'       -> skip ;
LINE_COMMENT	:	'//' .*? '\r'? '\n' -> skip ;

WS		:	[ \t\n\r]+ -> skip ;
