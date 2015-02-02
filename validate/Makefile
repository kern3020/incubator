SRC_LEX=validar.l

validar: lex.yy.c
	g++ lex.yy.c -lfl -o validar

clean: 
	rm lex.yy.c validar *~

lex.yy.c: validar.l
	flex validar.l
