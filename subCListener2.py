# Generated from subC.g4 by ANTLR 4.6
from antlr4 import *
from subCListener import subCListener
import re

types = [u"void", u"char", u"int", u"float", u"const", u"*"]

# This class handles part of the semantical analysis and constructs symbol tables.
class subCListener2(subCListener):

    #use this dictionary to map symbols to an array
    #array should state type in first element: function/(const/pointer) int/(const/pointer) float/(const/pointer)char/....
    #the elements after the first depend on the type of the first element...
    #for function -> return type, [argument types], symbol table for function,...
    #for variable -> type, initvalue within corresponding scope's symbol table, copy of key to make life easier
    #   --> true & false will be of type "constint" with respectively 1 & 0 as initvalue
    #if initvalue is "None", it represents a function's parameter which can't be initialized
    symboldict = {}

    #error variable to indicate if code should be generated...
    error = False

    #since we need symboltables for each function, we need to keep a variable telling us which function we're dealing with
    __currentfunc = u""

    #keeping a seperate dictionary for forward declarations of functions...
    #key(fwd declarated function's name) -> return type, [argument types]
    __fwddecls = {}


   #use a dictionary with an array for the parents
    __scopesyms = symboldict
    __parents = []

    # Enter a parse tree produced by subCParser#primaryexpr.
    def enterPrimaryexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#primaryexpr.
    def exitPrimaryexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#postfixexpr.
    def enterPostfixexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#postfixexpr.
    def exitPostfixexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#argexprlist.
    def enterArgexprlist(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#argexprlist.
    def exitArgexprlist(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#unaryexpr.
    def enterUnaryexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#unaryexpr.
    def exitUnaryexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#castexpr.
    def enterCastexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#castexpr.
    def exitCastexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#mulexpr.
    def enterMulexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#mulexpr.
    def exitMulexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#addexpr.
    def enterAddexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#addexpr.
    def exitAddexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#shiftexpr.
    def enterShiftexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#shiftexpr.
    def exitShiftexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#relationalexpr.
    def enterRelationalexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#relationalexpr.
    def exitRelationalexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#equalityexpr.
    def enterEqualityexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#equalityexpr.
    def exitEqualityexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#logicandexpr.
    def enterLogicandexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#logicandexpr.
    def exitLogicandexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#logicorexpr.
    def enterLogicorexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#logicorexpr.
    def exitLogicorexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#conditionalexpr.
    def enterConditionalexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#conditionalexpr.
    def exitConditionalexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#assignexpr.
    def enterAssignexpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#assignexpr.
    def exitAssignexpr(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#expr.
    def enterExpr(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#expr.
    def exitExpr(self, ctx):
        pass

    def __fwdDeclReturnTypeDrop(self, node, rt):
        #since a forward declaration doesn't require const-pointer consistency as in what we stated at line 526
        #we simply build up the return type & parameter list & look for the most viable option afterwards
        #this should be rather simple since ANSI C does not support function overloading...
        if( node.getChildCount() == 0 ):
            rt[0] += node.getText()
        else:
            if( "DdeclaratorContext" not in str(type(node)) ): #otherwise we go too far
                for child in node.getChildren():
                    self.__fwdDeclReturnTypeDrop(child, rt)

    def __fwdDeclParams(self, params, string):
        string = string.split(",")
        for i in string:
            index = -1
            typelen = -1
            for t in types:
                temp = i.rfind(t)
                if( temp > index ):
                    index = temp
                    typelen = len(t)
            if( index == -1 or typelen == -1 ):
                #generate error? or is the error caught in an earlier stage?
                pass
            params.append(i[:index+typelen])
            if( "[" in i ):
                j = i.split('[', 1)[1]
                params[len(params)-1] += "[" + j

    def __buildDeclType(self, dtype, string):
        index = 0
        typelen = 0
        string = string.split('=',1)[0]
        for t in types:
            temp = string.rfind(t)
            if( temp >= index ):
                index = temp
                typelen = len(t)
        if( index == 0 or typelen == 0 ):
            #generate error? or is the error caught in an earlier stage?
            pass
        dtype += string[:index+typelen]
        return dtype

    def __customSplit(self, string):
        stringarr = []
        bracketcount = 0
        last = 0
        for i in range(0, len(string)):
            if( string[i] == ',' and bracketcount == 0 ):
                if( last > 0 ):
                    stringarr.append(string[last:i])
                else:
                    stringarr.append(string[last:i])
                last = i+1
            elif( string[i] == '{' ):
                bracketcount += 1
            elif( string[i] == '}' ):
                bracketcount -= 1
        stringarr.append(string[last:])
        return stringarr

    def __buildInitializerList(self, vals): #still need to convert to integral types if necessary...
        ilist = []
        vals = vals[1:-1]
        last = 0
        multidim = False
        if( vals == "" ):
            return
        for i in range(0, len(vals)):
            if( vals[i] == '{' ):
                last = i
                multidim = True
            elif( vals[i] == '}'):
                ilist.append(self.__buildInitializerList(vals[last:i+1]))
                last = i
            elif( vals[i] == ',' and not multidim ):
                temp = vals[last:i]
                if( last > 0 ):
                    temp.replace(',', "")
                ilist.append(temp)
                last = i
        if( not multidim ):
            ilist.append(vals[last:].replace(',', "", 1))
        return ilist

    def __fixDimensions(self, vals):
        ilist = []
        last = 0
        last2 = 0
        if( None not in vals ):
            return vals
        for i in range(0, len(vals)):
            if( vals[i] == None and vals[last] != None ):
                ilist.append(vals[last:i])
                last = i
            elif( vals[i] == None and vals[last] == None ):
                ilist[last2:] = [ ilist[last2:] ]
                last = i
                last2 += 1
            elif( vals[i] != None and vals[last] == None ):
                last = i

        return ilist


    __found = False
    def __paramdeclPresent(self, ctx):
        for child in ctx.getChildren():
            if( "Paramdecl" in str(type(child)) ):
                self.__found = True
                return
            if( self.__found ):
                return
            if( child.getChildCount() > 0 ):
                self.__paramdeclPresent(child)

    def __representsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def __nonConstantArraySizes(self, ty):
        while( '[' in ty and ']' in ty ):
            arri = ty.split('[',1)[1].split(']',1)[0]
            if( not self.__representsInt(arri) and arri != "" ):
                return True
            ty = ty.split('[',1)[1].split(']')[1]
        return False

    # Enter a parse tree produced by subCParser#decl.
    def enterDecl(self, ctx):
        if( ctx.getChildCount() >= 3): #else we have ourselves a declspecifier on it's own which is useless...
            match = re.search(u'\(.*\)', ctx.getText())
            self.__found = False
            self.__paramdeclPresent(ctx)
            if( match is not None and '=' not in ctx.getText() and
                    ("()" in ctx.getText() or self.__found) ):
                returntype = [ctx.getChild(0).getText()]
                self.__fwdDeclReturnTypeDrop(ctx.getChild(1), returntype)
                funcname = ctx.getText()
                funcname = funcname.replace(returntype[0], u"")
                funcname = funcname[:-(len(funcname)-funcname.find(u"("))]
                if( funcname in ["true","false"] ):
                    print("Semantic \033[1;31merror\033[0m @ line %d: Function name can't be called \'%s\'."
                            % (ctx.start.line, funcname))
                    self.error = True
                    return
                if( '[' in returntype and not("*)" in returntype or "*const)" in returntype) ):
                    print("Semantic \033[1;31merror\033[0m @ line %d: Function \'%s\' can't return array type \'%s\'."
                            % (ctx.start.line, funcname, returntype))
                    self.error = True
                    return
                if( self.__fwddecls.has_key(funcname) ):
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m @ line %d: Redeclaration of forward declarated function \'%s\'."
                        % (ctx.start.line, ctx.getText()))
                else:
                    params = []
                    paramstring = ctx.getText()[ctx.getText().find(u"("):][1:][:-2] #remove everything in front of paramlist
                    #then remove the '(' and    ')' and ';' from the back
                    self.__fwdDeclParams(params, paramstring)
                    self.__fwddecls[funcname] = [returntype, params]
            else:
                decltypebase = ctx.getChild(0).getText()
                decltypebase = self.__buildDeclType(decltypebase, ctx.getChild(1).getText())
                variables = ctx.getText()
                variables = variables.replace(decltypebase, u"") #get rid of the declaration type
                variables = variables[:-1] #get rid of ';'
                variables = self.__customSplit(variables)
                for i in variables: #STILL NEED TO CHECK ARRAY'S SIZES IF THEY ARE VIABLE...
                    decltype = decltypebase
                    if( "(*" in decltype ):
                        i = i.replace("(*", "")
                    temp = i.split("=")
                    if( "[" in temp[0] ):
                        temp2 = temp[0].split('[', 1)
                        temp[0] = temp2[0]
                        while temp[0][-1] == ')':
                            decltype += ")"
                            temp[0] = temp[0][:-1]
                        decltype += "[" + temp2[1]
                        while temp[0][0] == '(':
                            decltype = decltype[:-1]
                            temp[0] = temp[0][1:]
                        while decltype[-1] == ')':
                            count = 0
                            for ic in range(0, (len(decltype)-1)):
                                char = decltype[len(decltype)-ic-2]
                                if( char == '(' and count == 0 ):
                                    decltype = decltype[:(len(decltype)-ic-2)] + decltype[(len(decltype)-ic-1):-1]
                                elif( char == '(' and count > 0 ):
                                    count -= 1
                                elif( char == ')' ):
                                    count += 1
                            if( count != 0 ):
                                break
                        if( self.__nonConstantArraySizes(decltype) ):
                            print("Semantic \033[1;31merror\033[0m @ line %d: Array sizes can't be variable"
                                " and must be integers in declaration of \'%s\'." % (ctx.start.line, temp[0]))
                            self.error = True
                            continue
                    if( temp[0] in ["true","false"] or not (temp[0].replace("_","a")).isalnum() ):
                        print("Semantic \033[1;31merror\033[0m @ line %d: Variable name can't be called \'%s\'."
                                % (ctx.start.line, temp[0]))
                        self.error = True
                        continue
                    if( decltype in ["void","constvoid"] ):
                        print("Semantic \033[1;31merror\033[0m @ line %d: Variable \'%s\' has incomplete type \'%s\'."
                                % (ctx.start.line, temp[0]))
                        self.error = True
                        continue

                    initval = 0
                    if( len(temp) == 2 ):
                        if( "{" in temp[1] ):
                            #here we build up the initializer list for arrays
                            initval = self.__buildInitializerList(temp[1])
                            initval = self.__fixDimensions(initval)
                            if( not initval ):
                                initval = None
                        else:
                            initval = temp[1]
                            if( (decltype[5:] if decltype[:5] == "const" else decltype) == "char[]" and '\"' in initval ):
                                decltype = decltype[:-1] + str(len(initval)-1) + "]"
                    if( self.__scopesyms.has_key(temp[0]) ):
                        self.error = True
                        print("Semantic \033[1;31merror\033[0m, %s @ line %d: Redeclaration of \'%s\'."
                            % (self.__currentfunc, ctx.start.line, temp[0]))
                    else:
                        self.__scopesyms[temp[0]] = [decltype, initval, temp[0]]
        else:
            print("\033[1;35mWarning\033[0m, %s @ line %d: \'%s\' is a useless declaration."
                    % (self.__currentfunc, ctx.start.line, ctx.getText()))
        pass

    # Exit a parse tree produced by subCParser#decl.
    def exitDecl(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#declspecifiers.
    def enterDeclspecifiers(self, ctx):
        '''if( "typedef" in ctx.getText() ):
            for i in range(1, ctx.getChildCount()):
                if( ctx.getChild(i).getChildCount() == 0):
                    print(ctx.getChild(i).getText())
        '''
        pass

    # Exit a parse tree produced by subCParser#declspecifiers.
    def exitDeclspecifiers(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#initdecltor.
    def enterInitdecltor(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#initdecltor.
    def exitInitdecltor(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#typespecifier.
    def enterTypespecifier(self, ctx):
        #print(ctx.getText())
        pass

    # Exit a parse tree produced by subCParser#typespecifier.
    def exitTypespecifier(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#specifierqualist.
    def enterSpecifierqualist(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#specifierqualist.
    def exitSpecifierqualist(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#typequal.
    def enterTypequal(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#typequal.
    def exitTypequal(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#declarator.
    def enterDeclarator(self, ctx):
        #print(ctx.getText())
        pass

    # Exit a parse tree produced by subCParser#declarator.
    def exitDeclarator(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#ddeclarator.
    def enterDdeclarator(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#ddeclarator.
    def exitDdeclarator(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#pointer.
    def enterPointer(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#pointer.
    def exitPointer(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#paramlist.
    def enterParamlist(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#paramlist.
    def exitParamlist(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#paramdecl.
    def enterParamdecl(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#paramdecl.
    def exitParamdecl(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#identifierlist.
    def enterIdentifierlist(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#identifierlist.
    def exitIdentifierlist(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#typename.
    def enterTypename(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#typename.
    def exitTypename(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#abstractdecltor.
    def enterAbstractdecltor(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#abstractdecltor.
    def exitAbstractdecltor(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#dabstractdecltor.
    def enterDabstractdecltor(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#dabstractdecltor.
    def exitDabstractdecltor(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#initializer.
    def enterInitializer(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#initializer.
    def exitInitializer(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#initializerlist.
    def enterInitializerlist(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#initializerlist.
    def exitInitializerlist(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#statement.
    def enterStatement(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#statement.
    def exitStatement(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#labeled.
    def enterLabeled(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#labeled.
    def exitLabeled(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#compounds.
    def enterCompounds(self, ctx):
        self.__parents.append(self.__scopesyms)
        if( len(self.__parents) == 1 and self.__currentfunc != u"" ):
            self.__scopesyms = self.__scopesyms[self.__currentfunc][3]
        else:
            self.__scopesyms[str(ctx.start.line)+"-"+str(ctx.start.column)] = {}
            self.__scopesyms = self.__scopesyms[str(ctx.start.line)+"-"+str(ctx.start.column)]
        pass

    # Exit a parse tree produced by subCParser#compounds.
    def exitCompounds(self, ctx):
        '''
        if( not bool(self.__scopesyms) ): #remove empty scopes -> this may interfere, watch closely
            for k,v in self.__parents[-1].items():
                if v == self.__scopesyms:
                    del self.__parents[-1][k]
        '''
        if( len(self.__parents) > 0 ):
            self.__scopesyms = self.__parents.pop()
        pass


    # Enter a parse tree produced by subCParser#selection.
    def enterSelection(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#selection.
    def exitSelection(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#iteration.
    def enterIteration(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#iteration.
    def exitIteration(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#jump.
    def enterJump(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#jump.
    def exitJump(self, ctx):
        pass

    # Enter a parse tree produced by subCParser#program.
    def enterProgram(self, ctx):
        self.symboldict[u"true"] = [u"constint", 1]
        self.symboldict[u"false"] = [u"constint", 0]
        pass

    # Exit a parse tree produced by subCParser#program.
    def exitProgram(self, ctx):
        if( u'main' not in self.symboldict ):
            print("Semantic \033[1;31merror\033: 'main' function is not present!")
            self.error = True
        '''
        print"\n\nSymbol Dictionary:\n-------------------"
        for i in self.symboldict:
            print i
            for j in self.symboldict[i]:
                print("\t%s" % j)
        '''
        pass


    # Enter a parse tree produced by subCParser#edecl.
    def enterEdecl(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#edecl.
    def exitEdecl(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#include.
    def enterInclude(self, ctx):
        if( ctx.getChild(2).getText() in ("<stdio>", "<stdio.h>", "stdio.h")):
            param = [u"constchar*format"]
            self.symboldict[u'printf'] = [u"function", u"void" , param]
            #format is a special one, need to find a way to implement this...
            #also, put it seperate or not? like "const char *", "format" or leave in 1?
            self.symboldict[u'scanf'] = [u"function", u"void" , param]
        pass

    # Exit a parse tree produced by subCParser#include.
    def exitInclude(self, ctx):
        pass

    __paramnum = 1

    def __initParam(self, node, paramlist, funcsymbols):
        ty = node.getChild(0).getText()
        temp = node.getChild(1)
        if( "Abstractdecltor" in str(type(temp)) ):
                ty += temp.getText()
                if( len(paramlist) <= paramindex ):
                    paramlist.append(u"")
                paramlist.append(ty)
                #no need to push to funcsymbols since there's no identifier (abstract declarator)
        else:
            while( temp.getChildCount() > 0 and "Identifier" not in str(type(temp.getChild(0)))
                    and "Terminal" not in str(type(temp)) ):
                if( (temp.getChild(0).getText() == "(" or "Declarator" in str(type(temp))) and temp.getChildCount() > 1 ):
                    ty += temp.getChild(0).getText()
                    temp = temp.getChild(1)
                else:
                    temp = temp.getChild(0)
            varname = temp.getChild(0).getText()
            ty += node.getText().replace(ty, "", 1).replace(varname, "", 1)
            paramlist.append(ty)
            line = node.start.line if "Terminal" not in str(type(node)) else node.parentCtx.start.line
            if( funcsymbols.has_key(varname) ):
                print("Semantic \033[1;31merror\033[0m @ line %d: Redeclaration of \'%s\'." %
                    (line, varname))
                self.error = True
                return
            funcsymbols[varname] = [paramlist[-1], None, self.__paramnum, varname]


    # Enter a parse tree produced by subCParser#functiondef.
    def enterFunctiondef(self, ctx):
        self.__paramnum = 1

        #Mind the 'main' function, we will not support commandline arguments nor a return type
        #generate warnings if it's the case and force void return type with no parameters...

        #first, check for NoneTypes so we are sure everything is ok... only valid for main...
        if( ctx.getChildCount() < 2 ):
            print("Unknown \033[1;31merror\033[0m @ line %d: Bad syntax." % (ctx.start.line-1))
            self.error = True
            return
        elif( ctx.getChild(1).getChildCount() == 0 ):
            print("Unknown \033[1;31merror\033[0m @ line %d: Bad syntax." % (ctx.getChild(1).start.line-1))
            self.error = True
            return
        elif( ctx.getChild(1).getChild(0).getChildCount() == 0 ):
            print("Unknown \033[1;31merror\033[0m @ line %d: Bad syntax." % (ctx.getChild(1).start.line-1))
            self.error = True
            return

        if( ctx.getChild(1).getChild(0).getChild(0).getText() == "main" ):
            if( self.symboldict.has_key(u"main") ):
                print("Semantic \033[1;31merror\033[0m @ line %d: \'main\' can only be defined once." %
                    (ctx.start.line) )
                self.error = True
                return
            if(  ctx.getChild(0).getText() != "void" ):
                print("\033[1;35mWarning\033[0m @ line %d: Function 'main' has an unsupported return type."
                        " Overwriting with 'void'." % ctx.getChild(0).start.line)
            if( ctx.getChild(1).getChild(0).getChildCount() > 3 ):
                print("\033[1;35mWarning\033[0m @ line %d: Function 'main' contains parameters"
                        " for command-line arguments which are not supported."
                        " Overwriting with no parameters." % ctx.getChild(1).getChild(0).start.line)
                temp = ctx.getChild(1).getChild(0).getChild(ctx.getChild(1).getChild(0).getChildCount()-1)
                for i in range(2, ctx.getChild(1).getChild(0).getChildCount()):
                    ctx.getChild(1).getChild(0).removeLastChild()
                ctx.getChild(1).getChild(0).addChild(temp)
            self.symboldict[ctx.getChild(1).getChild(0).getChild(0).getText()] = [u"function", u"void", [], {}]
            self.__currentfunc = u"main"
            return


        #all other functions...
        params = []
        funcsymbols = {} #needed to build up the first symbols, i.e. those in the paramlist
        index = 0 #if return type contains a pointer, we need to take the next child
        #also, if we have a const qualifier, pointer to pointer is not allowed... instead we need const type * const *
        if( ctx.getChild(1).getChildCount() > 1 and u"*" in ctx.getChild(1).getChild(0).getText() ):
            match = re.search(u'\*{2,}', ctx.getChild(1).getChild(0).getText())
            if( u"const" in ctx.getChild(0).getText() and match is not None ):
                replaced = match.group(0)
                replaced = replaced.replace(u"*", u"* const ")[:-7]
                print("Semantic \033[1;31merror\033 @ line %d: 'const' return type must also have 'const' pointer."
                    " Replace \'%s\' with \'%s\'"% (ctx.getChild(0).start.line, match.group(0), replaced))
                self.error = True
                #return #should we return straight away?
            index = 1

        #need more checks if it is not the main function...
        if( ctx.getChild(1).getChildCount() < (1+index) ):
            print("Unknown \033[1;31merror\033[0m @ line %d: Bad syntax." %
                    (ctx.getChild(1).start.line-1)) #for some reason, line is one too much
            self.error = True
            return
        elif( ctx.getChild(1).getChild(index).getChildCount() < 3 ):
            print("Unknown \033[1;31merror\033[0m @ line %d: Bad syntax." % (ctx.getChild(1).getChild(index).start.line-1))
            self.error = True
            return

        if( ctx.getChild(1).getChild(index).getChildCount() > 3 ): #meaning we need to build up the parameter types
            for i in range(2, ctx.getChild(1).getChild(index).getChildCount()-1):
                #need to go to a recursive function to dig out the parameter types...
                child = ctx.getChild(1).getChild(index).getChild(i)
                if( child.getText() == "," ):
                    self.__paramnum += 1
                else:
                    self.__initParam(child, params, funcsymbols)
        if( self.symboldict.has_key(ctx.getChild(1).getChild(index).getChild(0).getText()) ):
            print("Semantic \033[1;31merror\033[0m @ line %d: Redeclaration of \'%s\'." %
                    (ctx.start.line, ctx.getChild(1).getChild(index).getChild(0).getText()))
            self.error = True
            return
        if(  ctx.getChild(1).getChildCount() > 1 ):
            self.symboldict[ctx.getChild(1).getChild(index).getChild(0).getText()] = \
            [u"function", ctx.getChild(0).getText()+ctx.getChild(1).getChild(0).getText(), params, funcsymbols]
        else:
            self.symboldict[ctx.getChild(1).getChild(index).getChild(0).getText()] = \
            [u"function", ctx.getChild(0).getText(), params, funcsymbols]
        #print self.symboldict
        #print funcsymbols
        self.__currentfunc = ctx.getChild(1).getChild(index).getChild(0).getText()
        pass

    # Exit a parse tree produced by subCParser#functiondef.
    def exitFunctiondef(self, ctx):
        self.__currentfunc = u""
        pass


    def __notInScope(self, var):
        if( var in self.__scopesyms ):
            return False
        for i in reversed(self.__parents):
            if( var in i ):
                return False
        return True

    # Enter a parse tree produced by subCParser#identifier.
    def enterIdentifier(self, ctx):
        if( self.__notInScope(ctx.getText()) and (ctx.getText() not in self.__fwddecls)
                and (self.__currentfunc != u"")
                and (ctx.getText() not in self.symboldict[self.__currentfunc][3]) ):
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: \'%s\' was not declared!"
                    % (self.__currentfunc, ctx.start.line, ctx.getText()))
            self.error = True
        pass

    # Exit a parse tree produced by subCParser#identifier.
    def exitIdentifier(self, ctx):
        pass

