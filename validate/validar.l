%{
#include <iostream>
using namespace std;
#define YY_DECL extern "C" int yylex()
%}
%%
[:]                     { cout << "Attribute separator: " << yytext << endl; }
"#"(.*[ \t]*.*)*[\n]+   { cout << "Found comment: " << yytext << endl; }
[0-9]+                  { cout << "Found an integer:" << yytext << endl; }
[a-zA-Z0-9_'\./\-\ ]+       { cout << "Found a string: " << yytext << endl; }
[\[]                    { cout << "List begins: " << yytext << endl; }
[\,]                    { cout << "List separator: " << yytext << endl; }
[\]]                    { cout << "List ends: " << yytext << endl; }

%%
main() {
	// lex through the input:
	yylex();
}
