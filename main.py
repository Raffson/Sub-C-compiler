import sys
from antlr4 import *
from subCLexer import subCLexer
from subCParser import subCParser
from subCListener2 import subCListener2
from subCVisitor2 import subCVisitor2
from subCListener3 import subCListener3
from subCListener4 import subCListener4

def main(argv):
    input = FileStream(argv[1])
    lexer = subCLexer(input)
    stream = CommonTokenStream(lexer)
    parser = subCParser(stream)
    tree = parser.program()
    if( parser._syntaxErrors ):
        print("Syntax erros exist in \'%s\'. Failed to generate code..."%argv[1])
        return
    listener = subCListener2()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    visitor = subCVisitor2()
    visitor.visit(tree)
    #visitor.visit(tree)
    if( not listener.error ):
        listener2 = subCListener3()
        listener2.symboldict = listener.symboldict
        listener2.printscanparams = visitor.printscanparams
        walker.walk(listener2, tree)
        if( not listener2.error ):
            listener3 = subCListener4()
            listener3.symboldict = listener2.symboldict
            listener3.printscanparams = visitor.printscanparams
            walker.walk(listener3, tree)
            if( listener3.error ):
                #generate error message, delete any file that was already generated...
                print("Error during code generation...")
                pass
            else:
                print("Code generation complete...")
        else:
            print("Fatal errors exist in current code. Failed to generate code...")
    else:
        print("Fatal errors exist in current code. Failed to generate code...")

if __name__ == '__main__':
    main(sys.argv)
