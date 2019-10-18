# Generated from subC.g4 by ANTLR 4.6
from antlr4 import *
from subCVisitor import subCVisitor
import re
import sys
import os.path

# This class handles AST generation. See line 284 for starting point.

class subCVisitor2(subCVisitor):

    __f = None

    # Visit a parse tree produced by subCParser#primaryexpr.
    def visitPrimaryexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#postfixexpr.
    def visitPostfixexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#argexprlist.
    def visitArgexprlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#unaryexpr.
    def visitUnaryexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#castexpr.
    def visitCastexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#mulexpr.
    def visitMulexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#addexpr.
    def visitAddexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#shiftexpr.
    def visitShiftexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#relationalexpr.
    def visitRelationalexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#equalityexpr.
    def visitEqualityexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#logicandexpr.
    def visitLogicandexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#logicorexpr.
    def visitLogicorexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#conditionalexpr.
    def visitConditionalexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#assignexpr.
    def visitAssignexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#decl.
    def visitDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#declspecifiers.
    def visitDeclspecifiers(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#initdecltor.
    def visitInitdecltor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#typespecifier.
    def visitTypespecifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#specifierqualist.
    def visitSpecifierqualist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#typequal.
    def visitTypequal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#declarator.
    def visitDeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#ddeclarator.
    def visitDdeclarator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#pointer.
    def visitPointer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#paramdecl.
    def visitParamdecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#identifierlist.
    def visitIdentifierlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#typename.
    def visitTypename(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#abstractdecltor.
    def visitAbstractdecltor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#dabstractdecltor.
    def visitDabstractdecltor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#initializer.
    def visitInitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#initializerlist.
    def visitInitializerlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#labeled.
    def visitLabeled(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#compounds.
    def visitCompounds(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#selection.
    def visitSelection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#iteration.
    def visitIteration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#jump.
    def visitJump(self, ctx):
        return self.visitChildren(ctx)

    printscanparams = {}

    def __getParamCount(self, node):
        params = 0
        cparen = 0
        for child in node.getChildren():
            if( child.getText() == "(" ):
                cparen += 1
            elif( child.getText() == ")" ):
                cparen -= 1
                if( cparen == 0 ):
                    break
            elif( child.getText() == "," and cparen == 1 ):
                #this way we don't count the first parameter which is ok..we can always account for it later...
                params += 1
        return params

    def __skipNodes(self, node):
        ret = node
        while( True ):
            ccount = 0
            index = 0
            printscan = True if "Postfix" in str(type(ret)) and \
                   ret.getChildCount() > 0 and ret.getChild(0).getText() in ["printf","scanf"] else False
            if( printscan ):
                self.printscanparams[str(ret.start.line)+"-"+str(ret.start.column)] = self.__getParamCount(ret)
            for i in range(0, ret.getChildCount()):
                child = ret.getChild(i)
                if( (child.getText() in [";",",","{","}","(",")","[","]"] and "Dabstractdecltor" not in str(type(ret))
                        or child.getText() in [";",",","{","}"] and "Dabstractdecltor" in str(type(ret))
                        or "Jump" in str(type(ret)))
                        and "Compounds" not in str(type(ret)) ):
                    continue
                ccount += 1
                index = i
            if( ccount == 1 ):
                ret = ret.getChild(index)
                continue
            else:
                return ret

    def __adjustNodes(self, node, c, cc):
        for i in range(0, len(node.children)):
            if( node.children[i] is cc ):
                index = i
                node.children[i] = c
                node.children[i].parentCtx = node
                cc.parentCtx = None
                break

    __nodes = []

    def __recursiveASTbuilder(self, node, s1):
        childs = []
        childnodes = []
        for child in node.getChildren():
            if( not self.skip ):
                childcopy = child
                child = self.__skipNodes(child)
                if( child is not childcopy ):
                    self.__adjustNodes(node, child, childcopy)
                '''
                if( "Pointer" in str(type(node)) ):
                    continue
                if( (child.getText() in
                        [";",",","{","}","(",")","+","-","/","%","=",">","<","<<",">>","==","!=","&&","||",":","[","]",
                            "switch", "if", "else", "case", "default", "for", "while", "do", "#", "include"]
                        and "Pointer" not in str(type(node)))
                        and "Dabstractdecltor" not in str(type(node))
                        or ("Mulexpr" in str(type(node)) and child.getText() == "*")
                        or ("Jump" in str(type(node)) and node.getChildCount() == 3 and child.getText() == "return") ):
                    continue
                '''
                if( (child.getText() in
                        [";",",","{","}","(",")","[","]"]
                        and "Dabstractdecltor" not in str(type(node))) ):
                    continue
            s2 = str(type(child)).split(".")
            s2 = s2[len(s2)-1][:-2]
            s2 = s2.replace("Context", "")
            copy = s2
            re.sub(r'[^a-zA-Z0-9_]+', '', s2)
            if( s2 == "" ):
                s2 = "node"
            if( s2 == "TerminalNodeImpl" ):
                copy = child.getText()
                copy = copy.replace("\"", "\\\"")
            '''
            elif( not self.skip ):
                if( s2 in ["Assignexpr", "Relationalexpr", "Equalityexpr", "Logicandexpr", "Logicorexpr"] ):
                    copy = child.getChild(1).getText()
                    if( child.getChildCount() == 4 ):
                        copy += child.getChild(2).getText()
                elif( s2 == "Initdecltor" ):
                    copy = child.getChild(1).getText()
                elif( s2 in ["Mulexpr", "Addexpr", "Shiftexpr", ]  ):
                    copy = child.getChild(1).getText()
                elif( s2 == "Selection" ):
                    copy = child.getChild(0).getText()
                    if( child.getChildCount() == 7 ):
                        copy += "  else"
                elif( s2 == "Labeled" ):
                    copy = child.getChild(0).getText()
                elif( s2 == "Iteration" ):
                    copy = child.getChild(0).getText()
                    if( copy == "do" ):
                        copy += "  while"
                elif( s2 == "Jump" ):
                    copy = child.getChild(0).getText()
                elif( s2 == "Include" ):
                    copy = "#include"
                elif( s2 == "Ddeclarator" ):
                    copy = "Direct Declarator"
                elif( s2 == "Pointer" ):
                    copy = child.getText()
            '''
            counter = 0
            while( (s2+str(counter)) in self.__nodes ):
                counter += 1
            s2 += str(counter)
            self.__nodes.append(s2)
            if( child.getChildCount() > 0 ):
                childs.append(s2)
                childnodes.append(child)
            self.__f.write("\t%s [label=\"%s\"];\n" % (s2, copy))
            self.__f.write("\t%s -- %s;\n" % (s1, s2))

        index = 0
        for child in childnodes:
            if( child.getChildCount() > 0 ): #not needed anymore right?
                start = childs[index]
                self.__recursiveASTbuilder(child, start)
                index += 1

        lv = 0
        while( lv < len(node.children) ):
            child = node.children[lv]
            if( child.getText() in [";",",","{","}","(",")","[","]"] and "Dabstractdecltor" not in str(type(node))
                        or child.getText() in [";",",","{","}"] and "Dabstractdecltor" in str(type(node)) ):
                node.children[lv].parentCtx = None
                del node.children[lv]
                continue
            lv += 1


    skip = False
    run = 0
    # Visit a parse tree produced by subCParser#program.
    def visitProgram(self, ctx):
        File = sys.argv[1].rsplit('.', 1)[0]
	print File
        if( self.run > 0 ):
            self.skip = True
            self.__f = open(File+"-AST2.dot","w")
        else:
            self.__f = open(File+"-AST.dot","w")
            self.run += 1
        self.__f.write("graph AST {\n")
        start = str(type(ctx)).split(".")
        start = start[len(start)-1][:-2]
        start = start.replace("Context", "")
        self.__nodes.append(start)
        self.__recursiveASTbuilder(ctx, start)
        #self.visitChildren(ctx)
        self.__f.write("}\n")
        self.__f.close()



    # Visit a parse tree produced by subCParser#edecl.
    def visitEdecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#include.
    def visitInclude(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#functiondef.
    def visitFunctiondef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


