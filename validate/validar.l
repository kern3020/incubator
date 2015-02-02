%{
#include <iostream>
using namespace std;
#define YY_DECL extern "C" int yylex()
%}
%%
[:]             { cout << "Found separator: " << yytext << endl; }
[0-9]+          { cout << "Found an integer:" << yytext << endl; }
[a-zA-Z0-9]+    { cout << "Found a string: " << yytext << endl; }
%%
main() {
	// lex through the input:
	yylex();
}
