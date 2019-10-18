# Generated from subC.g4 by ANTLR 4.6
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by subCParser.

class subCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by subCParser#primaryexpr.
    def visitPrimaryexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by subCParser#postfixexpr.
    def visitPostfixexpr(self, ctx):
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


    # Visit a parse tree produced by subCParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


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


