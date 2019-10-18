# Generated from subC.g4 by ANTLR 4.6
from antlr4 import *
from subCListener import subCListener

# This class handles type checking.
class subCListener3(ParseTreeListener):

    #use this dictionary to map symbols to an array
    #array should state type in first element: function/(const/pointer) int/(const/pointer) float/(const/pointer)char/....
    #the elements after the first depend on the type of the first element...
    #for function -> return type, [argument types], symbol table for function,...
    #for variable -> type, initvalue within corresponding scope's symbol table
    #   --> true & false will be of type "constint" with respectively 1 & 0 as initvalue
    #if initvalue is "None", it represents a function's parameter which can't be initialized
    symboldict = {}

    #error variable to indicate if code should be generated...
    error = False

    #since we need symboltables for each function, we need to keep a variable telling us which function we're dealing with
    __currentfunc = u""

   #use a dictionary with an array for the parents
    __scopesyms = symboldict
    __parents = []

    #keep a variable that indicates the initiator of a type check
    __initor = 0
    #keep another variable for the types that arise in the type check
    __type = []

    #will be passed by Visitor
    printscanparams = {}

    def __enterInitiator(self, ctx):
        if( self.__initor == 0 ):
            self.__initor = id(ctx)
        pass

    def __exitInitiator(self, ctx):
        if( self.__initor == id(ctx) ):
            self.__initor = 0
            self.__type = []
        pass

    # Enter a parse tree produced by subCParser#primaryexpr.
    def enterPrimaryexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#primaryexpr.
    def exitPrimaryexpr(self, ctx):
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#postfixexpr.
    def enterPostfixexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __argumentPassable(self, atype, ptype, ctx, i):
        if( atype == None or ptype == None ):
            return False
        if( ptype[-1] == '*' or ptype[-6:] == "*const" or "*)" in ptype or "*const)" in ptype ):
            if( atype[:5] != "const" and ptype[:5] == "const" ):
                ptype = ptype[5:]
            return atype == ptype
        elif( atype[-1] == '*' or atype[-6:] == "*const" or "*)" in atype or "*const)" in atype ):
            return atype == ptype
        else:
            #arrays or non-pointers
            #arrays should have the same type except for perhaps a const qualifier in rhs that can be ignored
            #only problem remains the dimensions of arrays, with open arrays this will cause trouble
            #non-pointers should be most trivial to compare, i.e. remove const qualifier in rhs & see if it matches right?
            if( ptype[:5] == "const" ):
                ptype = ptype[5:]
            if( atype[:5] == "const" ):
                atype = atype[5:]
            if( ']' in ptype[-1] or ']' in atype[-1] ):
                #mind open arrays
                while( ']' in ptype[-1] and ']' in atype[-1] ):
                    atype = atype.rsplit("[",1)[0] if ']' == atype[-1] else atype
                    ptype = ptype.rsplit("[",1)[0] if ']' == ptype[-1] else ptype
                return atype == ptype
            aval = self.__getStrength(atype)
            pval = self.__getStrength(ptype)
            if( aval == 0 or pval == 0 ):
                return False
            if( pval < aval ):
                print("\033[1;35mWarning\033[0m, %s @ line %d:"
                        " Possible loss of information from argument \'%s\' during implicit conversion of type \'%s\'"
                        " to parameter of type \'%s\'."
                        % (self.__currentfunc, ctx.start.line, ctx.getChild(i).getText(), atype, ptype) )
            return True
            pass
        pass

    def __checkArrayIndexTypeNadjustType(self, ctx, child, term, ftype, nt2pass):
        #child is an array index
        #check type child for 'int', other types should generate an error...
        itype = None
        if( "Terminal" in str(type(ctx.getChild(0))) ):
            nt2pass += 1
        if( term ):
            itype = self.__getType(child)
        else:
            itype = self.__type[-nt2pass]
        if( itype != None and itype.replace("const", "") != "int" ):
            self.error = True
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: Expecting array index of type \'int\'"
            " while type \'%s\' was given in \'%s\'."
                % (self.__currentfunc, ctx.start.line, itype, child.getText()) )
        if( '[' in ftype and ']' in ftype ):
            temp = ftype.split('[',1)
            temp2 = temp[1].split(']',1)
            ftype = temp[0] + temp2[1]
        else:
            self.error = True
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'[]\' is not defined for"
            " non-array type \'%s\'." % (self.__currentfunc, ctx.start.line, ftype) )
        #anything else we need to do here?
        return ftype

    def __buildArgumentsFromString(self, string, scanf, argtypes):
        mapper = {'d': "int", 'i': "int", 'c': "char", 's': "char*", 'f': "float" }
        for i in range(0, (len(string)-1)):
            if( string[i] == '%' and string[i+1] in ['d', 'i', 'c', 's', 'f']  ):
                if( i > 0 and string[i-1] == '%' ):
                    continue
                argtypes.append(mapper[string[i+1]])
                if( string[i+1] in ['d', 'i', 'c', 's', 'f'] and scanf ):
                    argtypes[len(argtypes)-1] += "*"

    def __initPostfix(self, ctx, child, index):
        ftype = None
        var = None
        argtypes = []
        error = False
        func = False
        if( "Terminal" in str(type(child)) ):
            ftype = self.__getType(child)
            var = self.__getVariableFromScope(child.getText())
            if( var != None and len(var) > 2 and var[0] == "function" ):
                self.__type.append(var[1])
                argtypes = var[2]
                func = True
            elif( var != None and len(var) > 2 ):
                self.__type.append(var[0])
            else:
                #meaning var == None cause var is always more than 2
                #except scopes but they're out of reach
                #thus dealing with constant or literal string which can't handle any of the postfix-expressions
                error = True
        else:
            ftype = self.__type[-index]
        return [ftype, argtypes, error, func]

    # Exit a parse tree produced by subCParser#postfixexpr.
    def exitPostfixexpr(self, ctx):
        if( ctx.getChildCount() > 1 ):
            #first child should be the primary expression, thus identifier, constant, string literal
            #or an expression between parentheses, in that case the node is not terminal and a type must arise some other way
            tnodes = self.__countTerminalNodes(ctx)
            ntnodes = ctx.getChildCount() - tnodes
            ret = self.__initPostfix(ctx, ctx.getChild(0), ntnodes)
            ftype = ret[0]
            argtypes = ret[1]
            func = ret[3]
            if( ret[2] ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Constants and string literals like \'%s\'"
                    " are not allowed in this context."
                    % (self.__currentfunc, ctx.start.line, ctx.getChild(0).getText()))
                self.__exitInitiator(ctx)
                return

            if( ftype == None ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Couldn't determine type of \'%s\'."
                        % (self.__currentfunc, ctx.start.line, ctx.getChild(0).getText()))
                self.__exitInitiator(ctx)
                return

            nt2pass = ntnodes+1
            offset = 1
            offset2 = 1 if func else 0
            varstring = False #for printf, if this is true, don't do anymore checks... real c doesn't give any feedback either
            psp = 0
            adjustType = False
            for i in range(1, ctx.getChildCount()):
                child = ctx.getChild(i)
                term = False
                if( "Terminal" not in str(type(child)) ):
                    nt2pass -= 1
                else:
                    term = True
                if( child.getText() in [".","->"] ):
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is related to \'struct\' types"
                            " which are currently not supported." % (self.__currentfunc, ctx.start.line, child.getText()))
                    self.__exitInitiator(ctx)
                    return
                if( ctx.getChild(0).getText() in ["scanf","printf"]  and i == 1 ):
                    #build your own argument types according to the provided string...
                    ty = self.__getType(child) if "Terminal" in str(type(child)) else self.__type[-nt2pass]
                    ty = ty[5:] if ty[:5] == "const" else ty
                    #if( ty != "char*" and "char[" not in ty and ty.count('[') != 1 and ty.count(']') != 1 ):
                    if( "char[" not in ty and ty.count('[') != 1 and ty.count(']') != 1 and "char*" != ty ):
                        print("Semantic \033[1;31merror\033[0m, %s @ line %d: \'%s\' requires first parameter to be of type"
                            " \'char*\' or \'char[]\' while type \'%s\' was given."
                            % (self.__currentfunc, ctx.start.line, ctx.getChild(0).getText(), ty))
                    scanf = (ctx.getChild(0).getText() == "scanf")
                    argtypes = []
                    self.__buildArgumentsFromString(child.getText(), scanf, argtypes)
                    offset += 1
                    offset2 -= 1
                    psp = self.printscanparams[str(ctx.start.line)+"-"+str(ctx.start.column)]+1 if "\"" not in child.getText() \
                            else 0
                elif( len(argtypes) > 0 and i < (len(argtypes)+offset) ):
                    #child is an argument
                    #check type of child vs argument type
                    argtype = None
                    if( term ):
                        argtype = self.__getType(child)
                    else:
                        argtype = self.__type[-(nt2pass+offset+offset2-1)]
                    if( not self.__argumentPassable(argtype, argtypes[i-offset], ctx, i) ):
                        self.error = True
                        print("Semantic \033[1;31merror\033[0m, %s @ line %d: Expecting argument of type \'%s\'"
                        " while \'%s\' of type \'%s\' was given."
                            % (self.__currentfunc, ctx.start.line, argtypes[i-offset], child.getText(), argtype) )
                    #now what? nothing?
                elif( child.getText() not in ["++","--"] and i > psp and not func ):
                    #child is an array index
                    #check type child for 'int', other types should generate an error...
                    #there is a different possibility here, for example an array of pointers to functions, then child is argument
                    #if we're still dealing with pointer types, generate error
                    if( "*)" in ftype or "*const)" in ftype ):
                        self.error = True
                        print("Semantic \033[1;31merror\033[0m, %s @ line %d: Indexing \'%s\' of type \'%s\'"
                        " which is a non-array type. For pointer types try using operator \'+=\' or \'-=\' to adjust the pointer."
                            % (self.__currentfunc, ctx.start.line, ctx.getChild(0), ftype) )
                    else:
                        ftype = self.__checkArrayIndexTypeNadjustType(ctx, child, term, ftype, nt2pass)
                        adjustType = True
                elif( child.getText() in ["++","--"] and self.__isConstQualified([ftype]) and i > psp and not func ):
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' can't be used on \'%s\'"
                            " which is \'const\' qualified."
                            % (self.__currentfunc, ctx.start.line, ctx.getChild(1).getText(), ctx.getChild(0).getText()) )
                #else fubar?
            #print self.__type
            if( ntnodes > 1 ):
                self.__type = self.__type[:-(ntnodes-1)]
            if( adjustType ):
                self.__type[-1] = ftype

        #else fubar...
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#unaryexpr.
    def enterUnaryexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __adjustType(self, op, ty, ctx):
        if( op == "&" ):
            #distinguish between arrays an non-arrays, then adjust type
            if( '[' in ty ):
                temp = ty.split('[', 1)
                ty = temp[0] + "(*)[" + temp[1]
            else:
                ty += "*"
        elif( op == "*" ):
            #check if pointer type is present, if so adjust type else generate error
            if( "(*)" in ty ):
                ty = ty.replace("(*)", "", 1)
            elif( "*" in ty and '[' not in ty ): #else we're trying to dereference an array which is not possible
                temp = ty[::-1]
                temp = temp.replace("*", "", 1)
                ty = temp[::-1]
            else:
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Can't dereference \'%s\' of non-pointer type \'%s\'."
                        % (self.__currentfunc, ctx.start.line, ctx.getChild(1).getText(), ty) )
        elif( op == "!" ):
            #adjust type to int (or bool?) since this translates into (variable == 0)
            #can we use this operator on arrays too? -> yes, but generate warning cause it will always evaluate to true
            #should this part of code be here at all? perhaps more like logicaland and logicalor?
            '''
            if( '[' in ty and "(*)" not in ty ):
                print("\033[1;35mWarning\033[0m, %s @ line %d:"
                        " Address of array \'%s\' will always evaluate to \'true\'."
                        % (self.__currentfunc, ctx.start.line, ctx.getChild(1).getText()) )
            '''
            ty = "int"
        #else '+' or '-' which we will handle later (for example, generate warning if a sign is placed in front of a pointer type)
        return ty

    __recursiveReturn = []

    def __recursiveSearchVariable(self, ctx):
        if( "Terminal" in str(type(ctx)) ):
            var = self.__getVariableFromScope(ctx.getText())
            if( var != None and var[0] != "function" ):
                self.__recursiveReturn.append(True)
            else:
                self.__recursiveReturn.append(False)
        else:
            for child in ctx.getChildren():
                self.__recursiveReturn.append(self.__recursiveSearchVariable(child))

    def __isVariable(self, child):
        #checks for unaryexpr if right child contains a node that represents a variable and no function...
        if( "Terminal" in str(type(child)) ):
            var = self.__getVariableFromScope(child.getText())
            if( var == None or var[0] == "function" ):
                return False
            return True
        else:
            self.__recursiveSearchVariable(child)
            res = (True in self.__recursiveReturn)
            self.__recursiveReturn = []
            return res
        return False

    # Exit a parse tree produced by subCParser#unaryexpr.
    def exitUnaryexpr(self, ctx):
        if( ctx.getChildCount() > 1 ):
            child0text = ctx.getChild(0).getText()
            child1term = ("Terminal" in str(type(ctx.getChild(1))))
            if( child0text == "sizeof" ):
                #first child should always be terminal
                #sizeof should return an 'int' no matter what the queried type is
                if( child1term ):
                    self.__type.append("int")
                else:
                    self.__type[-1] = "int"
            elif( child0text in ["&","*","+","-","!","++","--"] ):
                #'+' and '-' shouldn't change anything to the current type
                c1type = None
                if( child1term ):
                    c1type = self.__getType(ctx.getChild(1))
                    self.__type.append(c1type)
                else:
                    c1type = self.__type[-1]
                c1type = self.__adjustType(child0text, c1type, ctx)
                self.__type[-1] = c1type
                if( child0text in ["++","--"] and self.__isConstQualified([c1type]) ):
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' can't be used on \'%s\'"
                            " which is \'const\' qualified."
                            % (self.__currentfunc, ctx.start.line, child0text, ctx.getChild(1).getText()) )
                if( child0text in ["&","*","++","--"] and not self.__isVariable(ctx.getChild(1)) ):
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' can't be used on \'%s\'"
                            " which is not a variable."
                            % (self.__currentfunc, ctx.start.line, child0text, ctx.getChild(1).getText()) )
        #else fubar
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#castexpr.
    def enterCastexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#castexpr.
    def exitCastexpr(self, ctx):
        if( ctx.getChildCount() > 1 ):
            #last child should be the type to be casted
            #all other children, terminal or non-terminal, should represent a type to which is casted
            ret = self.__initPostfix(ctx, ctx.getChild((ctx.getChildCount()-1)), 1) #doing same stuff as we would in postfix
            ftype = ret[0]
            if( ftype == None ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Couldn't determine type of \'%s\'."
                        % (self.__currentfunc, ctx.start.line, ctx.getChild((ctx.getChildCount()-1)).getText()))
                self.__exitInitiator(ctx)
                return
            #do we really need to check all typecasts? only the last one really counts right? i.e. type-checking wise
            #cause in code-generation it might be needed to actually try & cast every type
            #can any errors occur here?
            #for i in range(0, (ctx.getChildCount()-1)):
            #    child = ctx.getChild((ctx.getChildCount()-2)-i)

            #what if there's an idiot who writes 'int (*)' as a cast-type, that will mess shit up...
            #for now, we'll silently overwrite '(*)' with '*' if there's no array-type present...
            temp = ctx.getChild(0).getText()
            if( "(*)" in temp and '[' not in temp ):
                temp = temp.replace("(*)", "*")
            if( len(self.__type) > 0 ):
                self.__type[-1] = temp
            else:
                self.__type.append(temp)
        #else fubar
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#mulexpr.
    def enterMulexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#mulexpr.
    def exitMulexpr(self, ctx):
        ret = self.__MulOrAdd(ctx)
        if( ret != None and ret[2] and ctx.getChildCount() > 1 and ctx.getChild(1).getText() == "%" ):
            lhs = ret[0].replace("const", "")
            rhs = ret[1].replace("const", "")
            if( lhs != "int" ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%%\' is only defined for type \'int\'."
                        " Must explicitly cast \'%s\' to type \'int\'." % (self.__currentfunc,
                        ctx.start.line, ctx.getChild(0).getText()) )
            if( rhs != "int" ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%%\' is only defined for type \'int\'."
                        " Must explicitly cast \'%s\' to type \'int\'." % (self.__currentfunc,
                        ctx.start.line, ctx.getChild(2).getText()) )
        self.__exitInitiator(ctx)
        pass


    def __MulOrAdd(self, ctx):
        if( ctx.getChildCount() < 1 ):
            self.error = True
            print("Unknown \033[1;31merror\033[0m @ line %d: Bad syntax." % (ctx.start.line))
            self.__exitInitiator(ctx)
            return
        lhs = ctx.getChild(0)
        rhs = ctx.getChild(ctx.getChildCount()-1)
        ret = self.__getTypes(ctx, lhs, rhs)
        lhstype = ret[0]
        rhstype = ret[1]
        noterm = ret[2]
        allterm = ret[3]

        ret2 = self.__lhsNrhsAddableOrMullable(lhstype, rhstype)
        restype = ret2[0]
        ok = ret2[1]
        if( not ok ):
            self.error = True
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is not defined between \'%s\'"
                    " of type \'%s\' and \'%s\' of type \'%s\'." % (self.__currentfunc,
                    ctx.start.line, ctx.getChild(1).getText(), lhs.getText(), lhstype, rhs.getText(), rhstype) )
        if( (self.__initor != id(ctx)) ):
            if( noterm ):
                 self.__type.pop()
            if( len(self.__type) > 0 and not allterm ):
                self.__type[-1] = restype
            else:
                self.__type.append(restype)
        return (lhstype, rhstype, ok)


    # Enter a parse tree produced by subCParser#addexpr.
    def enterAddexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __lhsNrhsAddableOrMullable(self, lhs, rhs):
        ok = False
        restype = "error"
        ltype = lhs.replace("const", "")
        rtype = rhs.replace("const", "")

        #Let's see how this goes
        if( '*' in ltype or '*' in rtype or "*)" in ltype or "*)" in rtype or
                '[' in ltype or '[' in rtype or "*const)" in ltype or "*const)" in rtype ):
            return (restype, ok)
        if( "void" in ltype or "void" in rtype ):
            return (restype, ok)

        if( "float" in ltype or "float" in rtype ):
            restype = "float"
        elif( "int" in ltype or "int" in rtype ):
            restype = "int"
        elif( "char" in ltype or "char" in rtype ):
            restype = "char"
        if( restype in ["float", "int", "char"] ):
            ok = True
        return (restype, ok)

    # Exit a parse tree produced by subCParser#addexpr.
    def exitAddexpr(self, ctx):
        self.__MulOrAdd(ctx)
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#shiftexpr.
    def enterShiftexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __getTypes(self, ctx, lhs, rhs):
        nrnodes = self.__countTerminalNodes(ctx)
        lhstype = None
        rhstype = None
        noterm = False
        allterm = False
        if( ctx.getChildCount() > 0 and nrnodes == ctx.getChildCount() ):
            lhstype = self.__getType(lhs)
            rhstype = self.__getType(rhs)
            allterm = True
            pass
        elif( nrnodes == (ctx.getChildCount()-1) and (len(self.__type) > 0) ):
            #determine which side is terminal, lhs or rhs?
            if( "Terminal" in str(type(ctx.getChild(0))) ):
                #lhs is terminal
                lhstype = self.__getType(lhs)
                rhstype = self.__type[-1]
                pass
            elif( "Terminal" in str(type(ctx.getChild(ctx.getChildCount()-1))) ):
                #rhs is terminal
                lhstype = self.__type[-1]
                rhstype = self.__getType(rhs)
                pass
            #else fubar
        elif( nrnodes == (ctx.getChildCount()-2) and (len(self.__type) > 1) ):
            #is this it?
            lhstype = self.__type[-2]
            rhstype = self.__type[-1]
            noterm = True
        #else fubar?
        return (lhstype, rhstype, noterm, allterm)

    # Exit a parse tree produced by subCParser#shiftexpr.
    def exitShiftexpr(self, ctx):
        if( ctx.getChildCount() < 1 ):
            self.error = True
            print("Unknown \033[1;31merror\033[0m @ line %d: Bad syntax." % (ctx.start.line))
            self.__exitInitiator(ctx)
            return
        lhs = ctx.getChild(0)
        rhs = ctx.getChild(ctx.getChildCount()-1)
        ret = self.__getTypes(ctx, lhs, rhs)
        lhstype = ret[0]
        rhstype = ret[1]
        noterm = ret[2]
        allterm = ret[3]

        if( lhstype.replace("const", "") != "int" ):
            self.error = True
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is only defined for type \'int\'."
                    " Must explicitly cast \'%s\' to type \'int\'." % (self.__currentfunc,
                    ctx.start.line, ctx.getChild(1).getText(), lhs.getText()) )
        if( rhstype.replace("const", "") != "int" ):
            self.error = True
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is only defined for type \'int\'."
                    " Must explicitly cast \'%s\' to type \'int\'." % (self.__currentfunc,
                    ctx.start.line, ctx.getChild(1).getText(), rhs.getText()) )
        if( (self.__initor != id(ctx)) ):
            if( noterm ):
                 self.__type.pop()
            if( len(self.__type) > 0 and not allterm ):
                self.__type[-1] = "int"
            else:
                self.__type.append("int")
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#relationalexpr.
    def enterRelationalexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __relationalTypesCheck(self, ctx, lhs, rhs, lhstype, rhstype):
        #void in either lhstype or rhstype should result in error
        #if pointer type, both need to be pointer types or array type... the type to which is pointer doesn't matter
        #if no pointer/array type, the other is also a common type, void excluded...
        #valid for relational and equality contexts
        op = ctx.getText()
        op = op.replace(lhs.getText(), "")
        op = op.replace(rhs.getText(), "")
        if( '*' in lhstype or '[' in lhstype ):
            if( not ('*' in rhstype or '[' in rhstype) ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is not defined between \'%s\' of type"
                    " \'%s\' and \'%s\' of type \'%s\'." % (self.__currentfunc,
                    ctx.start.line, op, lhs.getText(), lhstype, rhs.getText(), rhstype) )
            #else ok?
        else:
            if( "void" in lhstype or "void" in rhstype ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is not defined between \'%s\' of type"
                    " \'%s\' and \'%s\' of type \'%s\'." % (self.__currentfunc,
                    ctx.start.line, op, lhs.getText(), lhstype, rhs.getText(), rhstype) )
            #else ok?

    def __lhsNrhsTypes(self, ctx, lhs, rhs):
        #valid for relational, equality, logicaland and logicalor contexts
        lhstype = None
        rhstype = None
        tnodes = self.__countTerminalNodes(ctx)
        if( tnodes == ctx.getChildCount() ):
            lhstype = self.__getType(lhs)
            rhstype = self.__getType(rhs)
            self.__type.append("int")
        elif( "Terminal" in str(type(lhs)) ):
            lhstype = self.__getType(lhs)
            rhstype = self.__type[-1]
        elif( "Terminal" in str(type(rhs)) ):
            lhstype = self.__type[-1]
            rhstype = self.__getType(rhs)
        else:
            lhstype = self.__type[-2]
            rhstype = self.__type.pop()
        return [lhstype, rhstype]

    # Exit a parse tree produced by subCParser#relationalexpr.
    def exitRelationalexpr(self, ctx):
        self.__commonFunction01(ctx)
        self.__exitInitiator(ctx)
        pass

    def __commonFunction01(self, ctx):
        if( ctx.getChildCount() > 1 ):
            # '<=', '<', '>=', '>', '==' and '!=' all obey the same rules so just take first & last child and compare types
            lhs = ctx.getChild(0)
            rhs = ctx.getChild(ctx.getChildCount()-1)
            ret = self.__lhsNrhsTypes(ctx, lhs, rhs)
            lhstype = ret[0]
            rhstype = ret[1]
            #now check the types, and update __type[-1] with int representing a boolean result...
            self.__relationalTypesCheck(ctx, lhs, rhs, lhstype, rhstype)
            self.__type[-1] = "int"
        #else fubar

    # Enter a parse tree produced by subCParser#equalityexpr.
    def enterEqualityexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#equalityexpr.
    def exitEqualityexpr(self, ctx):
        self.__commonFunction01(ctx)
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#logicandexpr.
    def enterLogicandexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __addressTrueWarningCheck(self, ctx, child, ty):
        if( '[' in ty and "*)" not in ty ):
            print("\033[1;35mWarning\033[0m, %s @ line %d: Address of array \'%s\' will always evaluate to \'true\'."
                        % (self.__currentfunc, ctx.start.line, child.getText()) )

    def __voidTypeErrorCheck(self, ctx, child, ty):
        if( "void" in ty and not('*' in ty or '[' in ty) ):
            self.error = True
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is not defined for \'%s\' of type \'%s\'."
                % (self.__currentfunc, ctx.start.line, ctx.getChild(1).getText(), child.getText(), ty) )

    def __logicalTypesCheck(self, ctx, lhs, rhs, lhstype, rhstype):
        #void in either lhstype or rhstype should result in error
        #furthermore, types must be checked independently from each other...
        #every type is ok except generate warning for arrays indicating they always evaluate to true...
        #valid for logicaland and logicalor contexts
        self.__addressTrueWarningCheck(ctx, lhs, lhstype)
        self.__addressTrueWarningCheck(ctx, rhs, rhstype)
        self.__voidTypeErrorCheck(ctx, lhs, lhstype)
        self.__voidTypeErrorCheck(ctx, rhs, rhstype)


    def __commonFunction02(self, ctx):
        if( ctx.getChildCount() > 1 ):
            lhs = ctx.getChild(0)
            rhs = ctx.getChild(ctx.getChildCount()-1)
            ret = self.__lhsNrhsTypes(ctx, lhs, rhs)
            lhstype = ret[0]
            rhstype = ret[1]
            #now check the types, and update __type[-1] with int since this expression returns a boolean result...
            self.__logicalTypesCheck(ctx, lhs, rhs, lhstype, rhstype)
            self.__type[-1] = "int"
        #else fubar

    # Exit a parse tree produced by subCParser#logicandexpr.
    def exitLogicandexpr(self, ctx):
        self.__commonFunction02(ctx)
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#logicorexpr.
    def enterLogicorexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#logicorexpr.
    def exitLogicorexpr(self, ctx):
        self.__commonFunction02(ctx)
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#conditionalexpr.
    def enterConditionalexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __conditionalChecks(self, ctx, e1, e2, e1type, e2type):
        if( '*' in e1type or '[' in e1type or '*' in e2type or '[' in e2type ):
            if( e1type != e2type ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Conditional expression must have matching operand types"
                    " for pointer/array types while \'%s\' of type \'%s\' and \'%s\' of type \'%s\' were given."
                    % (self.__currentfunc, ctx.start.line, e1.getText(), e1type, e2.getText(), e2type) )
                return "void"
            else:
                return e1type
        else:
            if( ("void" in e1type or "void" in e2type) and not("void" in e1type and "void" in e2type) ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Incompatible operands"
                    " \'%s\' of type \'%s\' and \'%s\' of type \'%s\' were given in conditional expression."
                    % (self.__currentfunc, ctx.start.line, e1.getText(), e1type, e2.getText(), e2type) )
                return "void"
            else:
                e1val = self.__getStrength(e1type)
                e2val = self.__getStrength(e2type)
                if( e1val < e2val ):
                    return e2type
                else:
                    return e1type

    # Exit a parse tree produced by subCParser#conditionalexpr.
    def exitConditionalexpr(self, ctx):
        if( ctx.getChildCount() > 4):
            #first child should be of type int
            #third & fifth child should match in type else generate error
            #after all checks, adjust the type to the third/fifth type if they match, else set to void..or error? or incomplete?
            cond = ctx.getChild(0)
            e1 = ctx.getChild(2)
            e2 = ctx.getChild(4)
            tnodes = self.__countTerminalNodes(ctx) - 2 #account for '?' and ':'
            condtype = [self.__getType(cond), 0] if "Terminal" in str(type(cond)) else [self.__type[-tnodes], 1]
            e1type = self.__getType(e1) if "Terminal" in str(type(e1)) else self.__type[-(tnodes-condtype[1])]
            e2type = self.__getType(e2) if "Terminal" in str(type(e2)) else self.__type[-1]
            self.__voidTypeErrorCheck(ctx, cond, condtype[0])
            restype = self.__conditionalChecks(ctx, e1, e2, e1type, e2type)
            if( tnodes == 3 ): #should be 5 children total, minus two for '?' and ':' so 3 means all terminal
                self.__type.append(restype)
            elif( tnodes == 2 ):
                self.__type[-1] = restype
            elif( tnodes < 2 ):
                self.__type = self.__type[:-(2-tnodes)]
                self.__type[-1] = restype
        #else fubar
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#assignexpr.
    def enterAssignexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __getVariableFromScope(self, var):
        if( var in self.__scopesyms ):
            return self.__scopesyms[var]
        for i in reversed(self.__parents):
            if( var in i ):
                return i[var]
        return None

    def __isConstQualified(self, var):
        if( '*' in var[0] ):
            if( "*const" == var[0][-6:] or "*const)" in var ):
                return True
            else:
                return False
        else:
            if( "const" in var[0] ):
                return True
        return False

    def __countTerminalNodes(self, ctx):
        nrnodes = 0
        for child in ctx.getChildren():
            if( "Terminal" in str(type(child)) ):
                nrnodes += 1
        return nrnodes

    def __lhsAssignChecks(self, lhs, ctx):
        if( lhs == None ):
            #shouldn't be the case though, & if so, an error should already have been generated...
            self.error = True
            #clear whatever list is present?
            return
        if( ctx.getChild(0).getText() in ["true", "false"] ):
            self.error = True
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: \'%s\' is a keyword that can't be reassigned."
                    % (self.__currentfunc, ctx.start.line, ctx.getChild(0).getText()) )
            return
        #in this case we're definately not dealing with an array's value
        #if that would be the case then the lhs-node would not be terminal but postfix
        #so if the symbol table shows it's an array, then the pointer to start of array is meant here...
        #not dealing with dereferenced pointers either...
        if( self.__isConstQualified(lhs) ):
            self.error = True
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: \'%s\' is \'const\' qualified which can't be reassigned."
                    % (self.__currentfunc, ctx.start.line, ctx.getChild(0).getText()) )
            return

        if( lhs[0] == "function" ):
            self.error = True
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: \'%s\' is a function which can't be assigned."
                    % (self.__currentfunc, ctx.start.line, ctx.getChild(0).getText()) )
            return

    def __getStrength(self, val):
        if( "float" in val ):
            return 3
        elif( "int" in val ):
            return 2
        elif( "char" in val ):
            return 1
        elif( "void" in val ):
            return 0
        else: #shouldn't be the case though...
            return -1

    def __rhsAssignable2lhs(self, ctx, lhs, rhs):
        #now we need to match the types without interference from const qualifiers, array brackets or pointers
        #need a proper function since we need to mind that int can be assigned to float
        #the other way around should generate a warning at the very least, perhaps even error...
        if( lhs == None or rhs == None ):
            return False
        if( lhs[-1] == '*' or "*)" in lhs ): #Let's see how this goes...
            #assigning a pointer to some value
            #if rhs is also pointer, both must exactly match in type
            #else we need to check what type rhs is & determine if we can interpret the value as an adress...
            if( ctx.getChildCount() == 4 ):
                if( ctx.getChild(1).getText() in ["+","-"] and rhs == "int" ):
                    return True
                else:
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is not defined between \'%s\'"
                        " of type \'%s\' and \'%s\' of type \'%s\'." % (self.__currentfunc,
                        ctx.start.line, ctx.getChild(1).getText(), ctx.getChild(0).getText(), lhs,
                        ctx.getChild(3).getText(), rhs) )
                    return True
            else:
                return lhs == rhs
        else:
            #arrays or non-pointers
            #arrays should have the same type except for perhaps a const qualifier in rhs that can be ignored
            #only problem remains the dimensions of arrays, with open arrays this will cause trouble
            #non-pointers should be most trivial to compare, i.e. remove const qualifier in rhs & see if it matches right?
            if( lhs[-1] == ']' ):
                if( ctx.getChildCount() == 4 ):
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is not defined between \'%s\'"
                        " of type \'%s\' and \'%s\' of type \'%s\'." % (self.__currentfunc,
                        ctx.start.line, ctx.getChild(1).getText(), ctx.getChild(0).getText(), lhs,
                        ctx.getChild(3).getText(), rhs) )
                    return True
                return lhs == rhs #still mind the dimension-problem...
            if( ctx.getChildCount() == 4 and ctx.getChild(1).getText() in ["%","<<",">>"] ):
                if( lhs != "int" ):
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is only defined for type \'int\'."
                            " Must explicitly cast \'%s\' to type \'int\'." % (self.__currentfunc,
                            ctx.start.line, ctx.getChild(1).getText(), ctx.getChild(0).getText()) )
                if( rhs != "int" ):
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: Operator \'%s\' is only defined for type \'int\'."
                            " Must explicitly cast \'%s\' to type \'int\'." % (self.__currentfunc,
                            ctx.start.line, ctx.getChild(1).getText(), ctx.getChild(3).getText()) )
            lhsval = self.__getStrength(lhs)
            rhsval = self.__getStrength(rhs)
            if( lhsval < rhsval ):
                print("\033[1;35mWarning\033[0m, %s @ line %d:"
                        " Possible loss of information from \'%s\' during implicit conversion of type \'%s\'"
                        " to \'%s\' of type \'%s\'."
                        % (self.__currentfunc, ctx.start.line, ctx.getChild(ctx.getChildCount()-1).getText(),
                            rhs, ctx.getChild(0).getText(), lhs) )
            return True
            #return (lhs == rhs.replace("const", ""))

    def __representsInt(self, s):
        try:
            int(s, 0)
            return True
        except ValueError:
            return False

    def __representsFloat(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def __getType(self, val):
        valtype = None
        if( val.getText()[0] == '\"' ):
            #string literal
            valtype = "char[" + str(len(val.getText())-1) + "]"
        elif( val.getText()[0] == '\''):
            #character constant
            valtype = "char"
        elif( self.__representsInt(val.getText()) or self.__representsFloat(val.getText()) ):
            #numerical constant
            if( any(char in val.getText() for char in ['.','e','E']) ):
                valtype = "float"
            else:
                valtype = "int"
        elif( val.getText() in ["true","false"] ):
            valtype = "constint"
        elif( val.getText()[0].isalpha() or val.getText()[0] == '_' ):
            #identifier, what kind though.. function call? -> if arguments present, postfix should be next node
            #thus not passing here unless it's a function with no arguments, in which case checking return type is enough
            val = self.__getVariableFromScope(val.getText())
            if( val == None ):
                #shouldn't be the case though, & if so, an error should already have been generated...
                self.error = True
                return None
            if( len(val) > 2 and val[0] == "function" ): #function
                valtype = val[1]
            elif( len(val) > 2 or val ): #variable
                valtype = val[0]
            #else idk wtf happened but definitely fubar...
        return valtype


    # Exit a parse tree produced by subCParser#assignexpr.
    def exitAssignexpr(self, ctx):
        nrnodes = self.__countTerminalNodes(ctx)
        lhstype = None
        rhstype = None
        oneterm = False
        noterm = False
        if( ctx.getChildCount() > 0 and nrnodes == ctx.getChildCount() ):
            #lhs should be a variable located in symbol table -> type known
            lhs = self.__getVariableFromScope(ctx.getChild(0).getText())
            if( lhs == None or ctx.getChild(0).getText() in ["true","false"] ):
                self.__exitInitiator(ctx)
                return
            self.__lhsAssignChecks(lhs, ctx)
            lhstype = lhs[0]
            #rhs must be evaluated into either an identifier, constant or string literal
            #then we can deduce the type easily...
            #after all that, check if there's an additional operator & see it the operation is viable\
            rhs = ctx.getChild(ctx.getChildCount()-1)
            rhstype = self.__getType(rhs)
            self.__type.append("void")
        elif( nrnodes == (ctx.getChildCount()-1) and (len(self.__type) > 0) ):
            #determine which side is terminal, lhs or rhs?
            #check additional operator
            if( "Terminal" in str(type(ctx.getChild(0))) ):
                #lhs is terminal
                #this means lhs type is easily retrievable
                lhs = self.__getVariableFromScope(ctx.getChild(0).getText())
                if( lhs == None or ctx.getChild(0).getText() in ["true","false"] ):
                    self.__exitInitiator(ctx)
                    return
                self.__lhsAssignChecks(lhs, ctx)
                lhstype = lhs[0]
                #rhs must've been built up by now in __type
                rhstype = self.__type[-1]
                pass
            elif( "Terminal" in str(type(ctx.getChild(ctx.getChildCount()-1))) ):
                #lhs must've been built up by now in __type
                lhs = ctx.getChild(0)
                lhstype = self.__type[-1]
                #rhs is terminal
                #this means rhs type is easily retrievable
                rhs = ctx.getChild(ctx.getChildCount()-1)
                rhstype = self.__getType(rhs)
                pass
            #else fubar
            oneterm = True
            pass
        elif( nrnodes == (ctx.getChildCount()-2) and (len(self.__type) > 1) ):
            lhstype = self.__type[-2]
            rhstype = self.__type[-1]
            noterm = True
            if( not self.__isVariable(ctx.getChild(0)) ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: \'%s\' is not an assignable variable."
                    " \'%s\' of type \'%s\' can't be converted to \'%s\' of type \'%s\'."% (self.__currentfunc,
                    ctx.start.line, ctx.getChild(0).getText()) )
        #else fubar?

        if( not self.__rhsAssignable2lhs(ctx, lhstype, rhstype) ):
            self.error = True
            print("Semantic \033[1;31merror\033[0m, %s @ line %d: Type mismatch in assigment."
                    " \'%s\' of type \'%s\' can't be converted to \'%s\' of type \'%s\'."% (self.__currentfunc,
                    ctx.start.line, ctx.getChild(ctx.getChildCount()-1).getText(), rhstype,
                    ctx.getChild(0).getText(), lhstype) )
        if( (self.__initor != id(ctx)) and (oneterm or noterm) ):
            if( noterm ):
                self.__type.pop()
            if( len(self.__type) > 0 and oneterm ):
                self.__type[-1] = "void"
            else:
                self.__type.append("void")
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#expr.
    def enterExpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#expr.
    def exitExpr(self, ctx):
        #must remove all childcount-1 elements from __type and set the remaining element to 'void'
        if( ctx.getChildCount() > 1 ):
            self.__type = self.__type[:-(ctx.getChildCount()-1)]
            self.__type[-1] = "void"
        #else fubar
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#decl.
    def enterDecl(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#decl.
    def exitDecl(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#declspecifiers.
    def enterDeclspecifiers(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#declspecifiers.
    def exitDeclspecifiers(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#initdecltor.
    def enterInitdecltor(self, ctx):
        self.__enterInitiator(ctx)
        if( ctx.getChildCount() > 2 ):
            if( "Terminal" in str(type(ctx.getChild(0))) ):
                self.__initvar = self.__getVariableFromScope(ctx.getChild(0).getText())
        #else fubar
        pass

    def __adjustOpenArrayType(self, rtype):
        temp = self.__initvar[0]
        temp2 = rtype
        while( temp[-2:] == "[]" and temp2[-1] == ']' ):
            temp = temp[:-2]
            temp2 = temp2.rsplit('[',1)[0]
            while( '[' in temp and '[' in temp2 and temp.rsplit('[',1)[1] == temp2.rsplit('[',1)[1] ):
                temp = temp.rsplit('[',1)[0]
                temp2 = temp2.rsplit('[',1)[0]
        if( '[' not in temp and ']' not in temp and '[' not in temp2 and ']' not in temp2 and temp == temp2 ):
            self.__initvar[0] = rtype

    __initvar = None

    # Exit a parse tree produced by subCParser#initdecltor.
    def exitInitdecltor(self, ctx):
        if( ctx.getChildCount() > 2 ):
            lhs = ctx.getChild(0)
            rhs = ctx.getChild(2)
            rtype = self.__getType(rhs) if "Terminal" in str(type(rhs)) else self.__type[-1]
            ltype = self.__initvar[0]
            if( "[]" in ltype ):
                self.__adjustOpenArrayType(rtype)
            ltype = self.__initvar[0]
            if( self.__initvar[-1] == rhs.getText() ):
                print("\033[1;35mWarning\033[0m, %s @ line %d:"
                        " Variable \'%s\' is being initialized with itself."
                        % (self.__currentfunc, ctx.start.line, self.__initvar[-1]))
            if( not self.__rhsAssignable2lhs(ctx, ltype, rtype) ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Type mismatch in initialization expression."
                        " \'%s\' of type \'%s\' can't be converted to \'%s\' of type \'%s\'."% (self.__currentfunc,
                        ctx.start.line, rhs.getText(), rtype, self.__initvar[2], ltype) )
        #else fubar
        self.__initvar = None
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#typespecifier.
    def enterTypespecifier(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#typespecifier.
    def exitTypespecifier(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#typequal.
    def enterTypequal(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#typequal.
    def exitTypequal(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#declarator.
    def enterDeclarator(self, ctx):
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#declarator.
    def exitDeclarator(self, ctx):
        if( self.__initor != id(ctx) ):
            if( ctx.getChildCount() > 1 ):
                if( "Terminal" in str(type(ctx.getChild(1))) ):
                    var = self.__getVariableFromScope(ctx.getChild(1).getText())
                    if( var != None ):
                        self.__initvar = var
            #else fubar
        #else do nothing
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#ddeclarator.
    def enterDdeclarator(self, ctx):
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#ddeclarator.
    def exitDdeclarator(self, ctx):
        if( self.__initor != id(ctx) ):
            if( ctx.getChildCount() > 1 ):
                if( "Terminal" in str(type(ctx.getChild(0))) ):
                    var = self.__getVariableFromScope(ctx.getChild(0).getText())
                    if( var != None ):
                        self.__initvar = var
            #else fubar
        #else do nothing
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#pointer.
    def enterPointer(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#pointer.
    def exitPointer(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#paramdecl.
    def enterParamdecl(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#paramdecl.
    def exitParamdecl(self, ctx):
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

    def __getCommonType(self, ty):
        ty = ty[5:] if ty[:5] == "const" else ty
        ty = ty.split('[',1)[0]
        ty = ty.split('(',1)[0]
        ty = ty[:-5] if ty[-5:] == "const" else ty
        return ty

    # Exit a parse tree produced by subCParser#initializer.
    def exitInitializer(self, ctx):
        #todo: if we get here, we're definitely dealing with array initialization
        #adjust array sizes in case of open arrays & check if initializer array sizes match
        if( ctx.getChildCount() > 1 ):
            tnodes = self.__countTerminalNodes(ctx)
            ntnodes = ctx.getChildCount() - tnodes
            ltype = self.__getCommonType(self.__initvar[0])
            nt2pass = ntnodes
            types = []
            for i in range(0, ctx.getChildCount()):
                child = ctx.getChild(i)
                if( "Terminal" in str(type(child)) ):
                    types.append(self.__getType(child))
                else:
                    types.append(self.__type[-nt2pass])
                    nt2pass -= 1
            types = list(set(types))
            if( len(types) > 1 ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Multiple types \'%s\' where found in"
                        " array initializer \'%s\'." % (self.__currentfunc,
                        ctx.start.line, str(types), ctx.getText()) )
            if( ntnodes == 0 ):
                self.__type.append(types[0] + "[" + str(ctx.getChildCount()) + "]")
            else:
                if( ntnodes > 1 ):
                    self.__type = self.__type[:-(ntnodes-1)]
                self.__type[-1] = self.__type[-1].split('[',1)[0] + "[" + str(ctx.getChildCount()) + "][" \
                                + self.__type[-1].split('[',1)[1]
        #else fubar
        pass

    # Enter a parse tree produced by subCParser#statement.
    def enterStatement(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#statement.
    def exitStatement(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#labeled.
    def enterLabeled(self, ctx):
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#labeled.
    def exitLabeled(self, ctx):
        if( ctx.getChildCount()  > 2 ):
            if( ctx.getChild(0).getText() == "case" ):
                if( "Terminal" in str(type(ctx.getChild(1))) ):
                    self.__casetypes.append(self.__getType(ctx.getChild(1)))
                else:
                    self.__casetypes.append(self.__type[-1])
            elif( ctx.getChild(0).getText() == "default" ):
                self.__casetypes.append(self.__casetypes[-1])
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#compounds.
    def enterCompounds(self, ctx):
        if( len(self.__parents) == 1 and self.__funcscope ):
            self.__funcscope = False
        elif( self.__scopesyms.has_key(str(ctx.start.line)+"-"+str(ctx.start.column)) ):
            self.__parents.append(self.__scopesyms)
            self.__scopesyms = self.__scopesyms[str(ctx.start.line)+"-"+str(ctx.start.column)]
        pass

    # Exit a parse tree produced by subCParser#compounds.
    def exitCompounds(self, ctx):
        if( len(self.__parents) > 1 ):
            self.__scopesyms = self.__parents.pop()
        pass


    __tyindex = []
    __casetypes = []

    # Enter a parse tree produced by subCParser#selection.
    def enterSelection(self, ctx):
        if( ctx.getChildCount() > 2 ):
            if( "Terminal" not in str(type(ctx.getChild(1))) ):
                self.__tyindex.append(len(self.__type))
            self.__enterInitiator(ctx)
        pass

    def __switchable(self, ty):
        if( '[' in ty and "*)" not in ty ):
            return False
        elif( ty == "void" ):
            return False
        return True

    def __countLabeledStatements(self, node):
        count = 0
        for child in node.getChildren():
            if( "Labeled" in str(type(child)) ):
                count += 1
        return count

    # Exit a parse tree produced by subCParser#selection.
    def exitSelection(self, ctx):
        #if should be handled at code-generation, switch/case needs checks for void and corresponding types
        if( ctx.getChildCount() > 2 and ctx.getChild(0).getText() == "switch" ):
            ty = None
            if( "Terminal" in str(type(ctx.getChild(1))) ):
                ty = self.__getType(ctx.getChild(1))
            else:
                ty = self.__type[self.__tyindex.pop()]
            ty = ty[5:] if ty[:5] == "const" else ty
            if( not self.__switchable(ty) ):
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: \'%s\' of type \'%s\' is not viable in a \'switch\'"
                    " statment. Expecting a type that's convertable to integer type."
                    % (self.__currentfunc, ctx.start.line, ctx.getChild(1).getText(), ty) )
                self.__exitInitiator(ctx)
                return
            #check ty & compare to all types in cases...
            if( "Compounds" in str(type(ctx.getChild(2))) ):
                if( len(self.__casetypes) == self.__countLabeledStatements(ctx.getChild(2)) ):
                    for t in self.__casetypes:
                        if( not self.__switchable(t) ):
                            self.error = True
                            print("Semantic \033[1;31merror\033[0m, %s @ line %d: \'%s\' is not viable in a"
                            " \'case\' statment. Expecting a type that's convertable to integer type."
                                % (self.__currentfunc, ctx.start.line, ctx.getChild(1).getText(), t) )
                    self.__casetypes = self.__casetypes[:-ctx.getChildCount()]
                    defcount = 0
                    for child in ctx.getChild(2).getChildren():
                        if( child.getChild(0).getText() == "default" ):
                            defcount += 1
                        if( defcount > 1 ):
                            break
                    if( defcount > 1 ):
                        self.error = True
                        print("Semantic \033[1;31merror\033[0m, %s @ line %d: Can't have more than one default"
                            " label within a \'switch\' statement." % (self.__currentfunc, ctx.start.line) )
                else:
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: Not accepting anything other than case/default"
                        " statments after \'switch\' statement." % (self.__currentfunc, ctx.start.line) )
            else:
                self.error = True
                print("Semantic \033[1;31merror\033[0m, %s @ line %d: Expecting compound statement with cases after \'switch\'."
                    % (self.__currentfunc, ctx.start.line) )
        elif( ctx.getChildCount() > 2 ):
            ty = None
            if( "Terminal" in str(type(ctx.getChild(1))) ):
                ty = self.__getType(ctx.getChild(1))
            else:
                ty = self.__type[self.__tyindex.pop()]
            ty = ty[5:] if ty[:5] == "const" else ty
            self.__voidTypeErrorCheck(ctx, ctx.getChild(1), ty)
        self.__exitInitiator(ctx)


    # Enter a parse tree produced by subCParser#iteration.
    def enterIteration(self, ctx):
        if( ctx.getChild(0).getText() == "do" ):
            if( "Terminal" not in str(type(ctx.getChild(3))) ):
                self.__tyindex.append(len(self.__type))
        elif( ctx.getChild(0).getText() == "while" ):
            if( "Terminal" not in str(type(ctx.getChild(1))) ):
                self.__tyindex.append(len(self.__type))
        elif( ctx.getChild(0).getText() == "for" ):
            if( "Terminal" not in str(type(ctx.getChild(2))) ):
                self.__tyindex.append(len(self.__type))
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#iteration.
    def exitIteration(self, ctx):
        if( ctx.getChildCount() > 0 ):
            index = 1 if ctx.getChild(0).getText() == "while" else 3
            index = 2 if ctx.getChild(0).getText() == "for" else index
            ty = None
            if( "Terminal" in str(type(ctx.getChild(index))) ):
                ty = self.__getType(ctx.getChild(index))
            else:
                tyindex = self.__tyindex.pop()
                tyindex = tyindex if "Terminal" in str(type(ctx.getChild(1))) or \
                    ctx.getChild(0).getText() == "while"  else (tyindex+1)
                tyindex = -1 if "do" == ctx.getChild(0).getText() else tyindex
                ty = self.__type[tyindex]
            ty = ty[5:] if ty[:5] == "const" else ty
            self.__voidTypeErrorCheck(ctx, ctx.getChild(index), ty)
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#jump.
    def enterJump(self, ctx):
        if( ctx.getChildCount() > 0 ):
            if( ctx.getChild(0).getText() == "return" ):
                self.__enterInitiator(ctx)
            #elif goto part if we decide to implement...
        pass

    def __jumpable(self, ctx, br):
        runner = ctx.parentCtx
        while( runner != None ):
            if( "Iteration" in str(type(runner)) or
                    (br and "Selection" in str(type(runner)) and runner.getChild(0).getText() == "switch") ):
                return True
            runner = runner.parentCtx

    # Exit a parse tree produced by subCParser#jump.
    def exitJump(self, ctx):
        cc = ctx.getChildCount()
        if( cc > 0 ):
            if( ctx.getChild(0).getText() == "return" ):
                ty = "void"
                if( cc == 2 ):
                    expr = ctx.getChild(1)
                    if( "Terminal" in str(type(expr)) ):
                        ty = self.__getType(expr)
                    else:
                        ty = self.__type[-1]
                if( self.symboldict[self.__currentfunc][1] in ["void","constvoid"] and ty not in ["void","constvoid"] ):
                    print("\033[1;35mWarning\033[0m, %s @ line %d: Useless expression in return-statement."
                        % (self.__currentfunc, ctx.start.line) )
                elif( not self.__argumentPassable(ty, self.symboldict[self.__currentfunc][1], ctx, 1) and
                        not (self.symboldict[self.__currentfunc][1] in ["void","constvoid"] and ty in ["void","constvoid"]) ):
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: Expecting return-type \'%s\'"
                    " while type \'%s\' was given."
                        % (self.__currentfunc, ctx.start.line, self.symboldict[self.__currentfunc][1], ty) )
                self.__exitInitiator(ctx)
            elif( ctx.getChild(0).getText() in ["continue","break"] ):
                br = True if ctx.getChild(0).getText() == "break" else False
                if( not self.__jumpable(ctx, br) ):
                    string = "\'iteration\' or \'switch\'" if br else "\'iteration\'"
                    self.error = True
                    print("Semantic \033[1;31merror\033[0m, %s @ line %d: \'%s\' statement not in %s statment."
                        % (self.__currentfunc, ctx.start.line, ctx.getChild(0).getText(), string) )

            #elif goto part if we decide to implement...
        pass


    # Enter a parse tree produced by subCParser#program.
    def enterProgram(self, ctx):
        self.__scopesyms = self.symboldict
        pass

    # Exit a parse tree produced by subCParser#program.
    def exitProgram(self, ctx):
        print"\n\nSymbol Dictionary:\n-------------------"
        for i in self.symboldict:
            print i
            for j in self.symboldict[i]:
                print("\t%s" % j)
        pass


    # Enter a parse tree produced by subCParser#edecl.
    def enterEdecl(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#edecl.
    def exitEdecl(self, ctx):
        pass


    # Enter a parse tree produced by subCParser#include.
    def enterInclude(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#include.
    def exitInclude(self, ctx):
        pass

    __funcscope = False

    # Enter a parse tree produced by subCParser#functiondef.
    def enterFunctiondef(self, ctx):
        index = 0
        if( ctx.getChild(1).getChildCount() == 2 and "Declarator" in str(type(ctx.getChild(1))) ):
            index += 1

        if( ctx.getChild(1).getChildCount() == 0 ):
            self.__currentfunc = ctx.getChild(1).getText()
        else:
            if( ctx.getChild(1).getChild(index).getChildCount() > 0 ):
                self.__currentfunc = ctx.getChild(1).getChild(index).getChild(0).getText()
            else:
                #this must not happen though right?
                self.__currentfunc = ctx.getChild(1).getChild(index).getText()
        self.__parents.append(self.__scopesyms)
        self.__scopesyms = self.__scopesyms[self.__currentfunc][3]
        self.__funcscope = True
        pass

    # Exit a parse tree produced by subCParser#functiondef.
    def exitFunctiondef(self, ctx):
        self.__scopesyms = self.__parents.pop()
        self.__funcscope = False
        self.__currentfunc = u""
        pass


    # Enter a parse tree produced by subCParser#identifier.
    def enterIdentifier(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#identifier.
    def exitIdentifier(self, ctx):
        pass


