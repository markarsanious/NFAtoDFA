grammar task_2_1;

start:  (expr NEWLINE)* ;

expr:   aaa
    |   add
    |   inc
    ;

aaa:    COMMAND ;

add:    COMMAND REG MEMORY
    |   COMMAND MEMORY REG
    |   COMMAND REG REG
    |   COMMAND MEMORY IMMEDIATE
    |   COMMAND REG IMMEDIATE
    ;

inc:    COMMAND REG
    |   COMMAND MEMORY
    ;



NEWLINE : [\r\n]+ ;
COMMAND     : ('AAA' | 'ADD' | 'INC') ;
REG :     ('AX' | 'BX' | 'CX' | 'DX') ;
MEMORY :    ('[AX]') ;
IMMEDIATE : [0-9]+
          | ('0' | '1')+'b';