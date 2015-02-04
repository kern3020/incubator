%{
#include <cstdlib>
#include <iostream>
using namespace std;
#define YY_DECL extern "C" int yylex()
%}
%%
[ \t\n]                   ;  // ignore all whitespace
[:]                     { cout << "Attribute separator: " << yytext << endl; }
"#"(.*[ \t]*.*)*[\n]+   { cout << "Found comment: " << yytext << endl; }
[0-9]+                  { cout << "Found an integer:" << yytext << endl; }
[a-zA-Z0-9_'\./\-\ ]+       { cout << "Found a string: " << yytext << endl; }
[\[]                    { cout << "List begins: " << yytext << endl; }
[\,]                    { cout << "List separator: " << yytext << endl; }
[\]]                    { cout << "List ends: " << yytext << endl; }
.                       ;     
%%
int main(int argc, char *argv[]) {
  if (argc < 2) {
    cout << "usage: validar <bcbio-conf> " << endl;
    exit(1);
  }

  FILE *myfile = fopen(argv[1],"r");

  if (myfile) {
    // set lex to read from it instead of defaulting to STDIN:
    yyin = myfile;
    
    // lex through the input:
    yylex();
  } else {
    cout << "I can't open a.snazzle.file!" << endl;
    return -1;
  }

  return 0; 
}
