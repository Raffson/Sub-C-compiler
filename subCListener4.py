# Generated from subC.g4 by ANTLR 4.6
from antlr4 import *
from subCListener import subCListener
import sys

# This class handles code-generation.
# A lot of work is similar to the type-checking part though we passed all errors in the previous run
# Thus we can skip all parts that have already been checked...
class subCListener4(ParseTreeListener):

    #use this dictionary to map symbols to an array
    #array should state type in first element: function/(const/pointer) int/(const/pointer) float/(const/pointer)char/....
    #the elements after the first depend on the type of the first element...
    #for function -> return type, [argument types], symbol table for function,...
    #for variable -> type, intvalue within corresponding scope's symbol table
    #   --> true & false will be of type "constint" with respectively 1 & 0 as initvalue
    #if initvalue is "None", it represents a function's parameter which can't be initialized
    symboldict = {}
    #will adjust symboldict by adding baseaddresses for variables during declaration

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

    #variable that tells us which code of stdio must be included, 0 is none, 1 is printf, 2 is scanf, 3 is both
    __stdioref = 0

    #variable to maintain the number of labels, using ihnttnftf with the number
    #ihnttnftf as in "i hope none takes this name for their function" cause otherwise labels will conflict...
    __nrl = 0
    __l = "ihnttnftf"

    #variable to keep blocks of instructions that have to be organized by parent nodes like function calls, if statements, etc.
    __instrs = []

    #variable for offset in stackframe after parameters, must be reset on every function definition's entry...
    __offaddr = 0
    __offaddrs = []

    #variable for nesting depth
    __nd = 0

    def __enterInitiator(self, ctx):
        if( self.__initor == 0 ):
            self.__initor = id(ctx)
        pass

    def __recursiveArrayPrint(self, var):
        for i in range(0, len(var)):
            if( type(var[i]) ==  str or type(var[i]) == unicode ):
                self.__f.write("%s" % var[i])
            else:
                self.__recursiveArrayPrint(var[i])

    def __exitInitiator(self, ctx):
        if( self.__initor == id(ctx) ):
            self.__initor = 0
            self.__type = []
            for i in range(0, len(self.__instrs)):
                if( type(self.__instrs[i]) ==  str ):
                    self.__f.write("%s" % self.__instrs[i])
                else:
                    self.__recursiveArrayPrint(self.__instrs[i])
            self.__instrs = []
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

    def __inAssignableContext(self, node):
        temp = node
        if( temp.parentCtx != None ):
            temp2 = temp.parentCtx
            if( "Postfixexpr" in str(type(temp2)) ):
                var = self.__getVariableFromScope(temp2.getChild(0).getText())
                if( var != None and (var[0][0] == "function" or '[' in var[0][0]) ):
                    return True
            elif( any(x in str(type(temp2)) for x in ["Labeled","Selection"]) ):
                return (temp2.getChild(1) == temp)
            elif( "Iteration" in str(type(temp2)) ):
                ft = temp2.getChild(0).getText()
                if( ft == "for" ):
                    return (temp in [temp2.getChild(1),temp2.getChild(2)])
                elif( ft == "do" ):
                    return (temp == temp2.getChild(3))
                elif( ft == "while" ):
                    return (temp == temp2.getChild(1))
            elif( "Jump" in str(type(temp2)) ):
                return (temp2.getChild(0).getText() == "return")
            elif( "Compounds" in str(type(temp2)) ):
                return False
            return True
        else:
            return False

    def __checkArrayIndexTypeNadjustType(self, ctx, child, term, ftype, nt2pass):
        #child is an array index
        itype = None
        if( "Terminal" in str(type(ctx.getChild(0))) ):
            nt2pass += 1
        if( term ):
            itype = self.__getType(child)
        else:
            itype = self.__type[-nt2pass]
        if( '[' in ftype and ']' in ftype ):
            temp = ftype.split('[',1)
            temp2 = temp[1].split(']',1)
            ftype = temp[0] + temp2[1]
        #else caught in previous run
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
        func = False
        if( "Terminal" in str(type(child)) ):
            ftype = self.__getType(child)
            var = self.__getVariableFromScope(child.getText())
            if( var != None and len(var[0]) > 2 and var[0][0] == "function" ):
                self.__type.append(var[0][1])
                argtypes = var[0][2]
                func = True
            elif( var != None and len(var[0]) > 2 ):
                self.__type.append(var[0][0])
            else:
                #caught in previous run
                pass
        else:
            ftype = self.__type[-index]
        return [ftype, argtypes, func]

    def __isVariable(self, node, term):
        return ( term and (self.__getVariableFromScope(node.getText()) != None) )

    def __getBaseAddress(self, node, term):
        #mind arguments... they have no address appended...
        if( term ):
            ret = self.__getVariableFromScope(node.getText())
            if( ret != None and ret[0][0] != "function"):
                var = ret[0]
                nd = ret[1]
                if( var[1] != None ):
                    if( node.getText() in self.symboldict ):
                        return [var[-1], nd, False, True]
                    return [var[-1], nd, False, False]
                else:
                    return [var[-2], nd, True, False]
            #else fubar
        #else fubar

    def __getTypeP(self, ty):
        if( ty[-1] == '*' or ty[:-6] == "*const" or "*)" in ty or "*const)" in ty ):
            return "a"
        elif( "int" in ty ):
            return "i"
        elif( "float" in ty ):
            return "r"
        elif( "char" in ty ):
            return "c"
        elif( "void" in ty ):
            return "a"

    def __isFunction(self, node, isvar):
        if( isvar ):
            return (self.__getVariableFromScope(node.getText())[0][0] == "function")
        return False

    def __getArraySize(self, argtype):
        argcop = argtype
        temp = 1
        while( '[' in argcop and ']' in argcop and "[]" not in argcop ):
            spl = argcop.rsplit('[',1)
            temp *= int(spl[1].split(']')[0], 0)
            argcop = spl[0]
        return temp

    def __generateOffsetCode(self, child, instr, ftype, term):
        arrsize = self.__getArraySize(ftype)
        if( term ):
            #generate code for offset...
            isvar = self.__isVariable(child, True)
            if( isvar ):
                #load the variable, offset address...
                ret = self.__getBaseAddress(child, True)
                baddr = ret[0]
                nd = ret[1]
                isarg = ret[2]
                glob = ret[3]
                typi = self.__getTypeP(self.__getType(child))
                #must do something different in case of argument...
                if( self.__inExprContextFollowedByConditionalContext(child) ):
                    nd += 1
                conv = ""
                if( typi != "i" ):
                    conv = ("conv %s i\n"%typi)
                if( isarg ):
                    instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nconv i a\nind %s\n%sixa %d\n"
                            % (nd, nd, (baddr+5), typi, conv, arrsize))
                elif( glob ):
                    instr.append("ldo %s %d\n%sixa %d\n" % (typ, baddr, typ, conv, arrsize) )
                else:
                    instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\nind %s\n%sixa %d\n"
                            % (nd, nd, baddr, typi, conv, arrsize))
            else:
                #must be a integer contant...
                instr.append("ldc i %s\nixa %d\n"
                        % (child.getText(), arrsize))
        else:
            #code was generated for offset...
            instr.append("insert")
            instr.append("ixa %d\n"%arrsize)


    def __check4IndirectionsNreplace(self, ctx, child, instr, op, opp, fterm, pre):
        #check for indirection & replace
        if( fterm ):
            var = self.__getVariableFromScope(child.getText())
            if( var != None and var[0][0] != "function" ):
                ret = self.__getBaseAddress(child, True)
                baddr = ret[0]
                nd = ret[1]
                isarg = ret[2]
                glob = ret[3]
                typ = self.__getTypeP(var[0][0])
                if( self.__inExprContextFollowedByConditionalContext(ctx) ):
                    nd += 1
                if( isarg ):
                    instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nconv i a\n"
                                % (nd, nd, (baddr+5)) )
                elif( glob ):
                    instr.append("ldc a %d\n" % (baddr))
                else:
                    instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\n"
                                % (nd, nd, baddr) )
                if( pre ):
                    instr.append("dpl a\ndpl a\nind %s\n%s %s 1\nsto %s\nind %s\n"
                            % (typ, op, typ, typ, typ) )
                else:
                    instr.append("dpl a\ndpl a\nind %s\n%s %s 1\nsto %s\nind %s\n%s %s 1\n"
                            % (typ, op, typ, typ, typ, opp, typ) )
            else:
                #shouldn't happend though...
                print("\033[1;35mWarning\033[0m, %s @ line %d:"
                " Useless usage of operator \'%s\' in expression \'%s\'."
                    % (self.__currentfunc, ctx.start.line, op, ctx.getText()) )
        else:
            lasttyp = None
            if( "ind" in instr[-1] ):
                lasttyp = instr[-1].replace("ind ","").replace("\n","")
                instr[-1] = instr[-1].rsplit(("ind %s\n"%lasttyp),1)[0]
            else:
                lasttyp = self.__getTypeP(self.__type[-1])
            if( pre ):
                instr.append("dpl a\ndpl a\nind %s\n%s %s 1\nsto %s\nind %s\n"
                        % (lasttyp, op, lasttyp, lasttyp, lasttyp) )
            else:
                instr.append("dpl a\ndpl a\nind %s\n%s %s 1\nsto %s\nind %s\n%s %s 1\n"
                        % (lasttyp, op, lasttyp, lasttyp, lasttyp, opp, lasttyp) )

    def __lhsAssignDecendant(self, ctx):
        temp = ctx
        stoppers = ["Compounds","Iteration","Selection","Labeled","Jump","Expr"]
        while( temp.parentCtx != None ):
            if( "Assignexpr" in str(type(temp.parentCtx)) and temp == temp.parentCtx.getChild(0) ):
                return True
            elif( any(x in str(type(temp.parentCtx)) for x in stoppers) ):
                return False
            temp = temp.parentCtx
        return False

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
            func = ret[2]
            instr = []
            addrs = []
            arglen = 6 #position of first argument in reference of stackframe, 5 is used to indicate end of parameters

            if( "Terminal" not in str(type(ctx.getChild(0))) ):
                instr.append("insert")

            nt2pass = ntnodes+1 if "Terminal" in str(type(ctx.getChild(0))) else ntnodes
            offset = 1
            first = True
            offset2 = 1 if func else 0
            psp = 0
            adjustType = False
            for i in range(1, ctx.getChildCount()):
                child = ctx.getChild(i)
                term = False
                if( "Terminal" not in str(type(child)) ):
                    nt2pass -= 1
                else:
                    term = True
                if( ctx.getChild(0).getText() in ["scanf","printf"] and i == 1 ):
                    #build your own argument types according to the provided string...
                    scanf = (ctx.getChild(0).getText() == "scanf")
                    if( scanf and self.__stdioref < 2 ):
                        self.__stdioref = 2
                    elif( not scanf and self.__stdioref == 2 ):
                        self.__stdioref = 3
                    elif( not scanf and self.__stdioref < 1 ):
                        self.__stdioref = 1
                    argtypes = []
                    self.__buildArgumentsFromString(child.getText(), scanf, argtypes)
                    offset += 1
                    offset2 -= 1
                    psp = self.printscanparams[str(ctx.start.line)+"-"+str(ctx.start.column)]+1 if "\"" not in child.getText() \
                            else 0
                    if( ctx.getChild(0).getText() in ["printf","scanf"] ):
                        instr.append("ldc i 1\n")
                        arglen += 1
                elif( (len(argtypes) > 0 and i < (len(argtypes)+offset)) or i <= psp ):
                    #child is an argument
                    argtype = None
                    if( term ):
                        argtype = self.__getType(child)
                    else:
                        argtype = self.__type[-(nt2pass+offset+offset2-1)]
                    typa = self.__getTypeP(argtype)
                    typp = self.__getTypeP(argtypes[i-offset]) if psp == 0 else typa
                    if( '[' in argtype and not("*)" in argtype or "*const)" in argtype) ):
                        arrsize = self.__getArraySize(argtype)
                        #if( typa == "c" ): #account for \0 terminator
                        #    arrsize += 1
                        #put argument on stack, though how do we find the address?
                        #find out common type, is it a variable or constant?
                        if( term and child.getText()[0] == '\"' ): #constant (string literal)
                            addrs.append("ldc i %d\n" % (arglen+len(argtypes)))
                            for j in child.getText()[1:-1]:
                                if( j != '\n' and j != '\t' ):
                                    instr.append("ldc c %d\n" % ord(j))
                                else:
                                    ordval = 10 if j == '\n' else 9
                                    instr.append("ldc c %d\n" % ordval)
                                if( typa != typp ):
                                    instr.append("conv %s %s\n" % (typa, typp))
                                arglen += 1
                            instr.append("ldc c 0\n")
                            arglen += 1
                        elif( term ):
                            #must be an array in scope then right?
                            addrs.append("ldc i %d\n" % (arglen+len(argtypes)))
                            ret2 = self.__getBaseAddress(child, term)
                            baddr = ret2[0]
                            nd = ret2[1]
                            isarg = ret2[2]
                            glob = ret2[3]
                            if( self.__inExprContextFollowedByConditionalContext(ctx) ):
                                nd += 1
                            for j in range(0, arrsize):
                                if( isarg ):
                                    instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nldc i %d\nadd i\nconv i a\nind %s\n"
                                            % (nd, nd, (baddr+5), j, typa))
                                elif( glob ):
                                    instr.append("ldo %s %d\n" % (typa, baddr) )
                                else:
                                    instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\nind %s\n"
                                            % (nd, nd, (baddr+j), typa))
                                if( typa != typp ):
                                    instr.append("conv %s %s\n" % (typa, typp))
                                arglen += 1
                        else:
                            #not terminal, so code should've been generated already...
                            #but is that all? hasn't there jus been generated an address that we have to carry on with?
                            #yup-> must now load up stuff with that adress...
                            #indexed array, dereferenced pointer leading to array, what else?
                            addrs.append("ldc i %d\n" % (arglen+len(argtypes)))
                            instr.append("insert")
                            instr.append("movs %d\n"%arrsize)
                            arglen += arrsize
                    else:
                        #type of length 1, find exact type, variable or constant, then push onto stack
                        isvar = self.__isVariable(child, term)
                        if( term and not isvar ): #all constants different from string literal
                            addrs.append("ldc i %d\n" % (arglen+len(argtypes)))
                            typ = self.__getTypeP(self.__getType(child))
                            if( typ == "c" ):
                                temp = child.getText().replace('\'', "")
                                if( temp != '\n' and temp != '\t' ):
                                    instr.append("ldc %s %d\n" % (typa, ord(temp)))
                                else:
                                    ordval = 10 if j == '\n' else 9
                                    instr.append("ldc %s %d\n" % (typa, ordval))
                            else:
                                if( child.getText() in ["true","false"] ):
                                    val = 1 if child.getText() == "true" else 0
                                    instr.append("ldc i %d\n" % val)
                                else:
                                    instr.append("ldc %s %s\n" % (typa, child.getText()))
                            arglen += 1
                        elif( term and isvar ): #all variables in scope, incl parameterless functions... must handle seperately
                            isfunc = self.__isFunction(child, isvar)
                            addrs.append("ldc i %d\n" % (arglen+len(argtypes)))
                            if( isfunc ):
                                #must generate the code here and now cause the node is terminal...
                                instr.append("mst 0\nldc i 6\ncup 1 %s\n" % child.getText())
                                arglen += 1
                            else:
                                ret2 = self.__getBaseAddress(child, term)
                                baddr = ret2[0]
                                nd = ret2[1]
                                isarg = ret2[2]
                                glob = ret2[3]
                                if( self.__inExprContextFollowedByConditionalContext(ctx) ):
                                    nd += 1
                                if( isarg ):
                                    instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nconv i a\nind %s\n"
                                            % (nd, nd, (baddr+5), typa))
                                elif( glob ):
                                    instr.append("ldo %s %d\n" % (typa, baddr) )
                                else:
                                    instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\nind %s\n"
                                            % (nd, nd, baddr, typa))
                                arglen += 1
                        else:
                            #not terminal, function calls, dereferenced pointers, indexed array with common type as result...
                            #general expressions (+,-,*,/,%,<,>,=,==,!=,<=,>=,<<,>>,&,*,!,++,--) that lead to a result...
                            #insert the generated code on this position...
                            addrs.append("ldc i %d\n" % (arglen+len(argtypes)))
                            instr.append("insert")
                            arglen += 1
                        if( typa != typp ):
                            instr.append("conv %s %s\n" % (typa, typp))
                elif( child.getText() not in ["++","--"] and i > psp ):
                    #child is an array index
                    ftype = self.__checkArrayIndexTypeNadjustType(ctx, child, term, ftype, nt2pass)
                    #need to know what we're dealing with... is first child terminal or not, else code was already generated...
                    #is this child terminal or not, otherwise again code was generated...
                    #if terminal first child, we need a base address, not sure about the rest..
                    #if this child is terminal, then it's fairly simple...
                    typ = self.__getTypeP(ftype)
                    if( "Terminal" in str(type(ctx.getChild(0))) ):
                        if( first ): #loading the base address of what should be an array should only be done once...
                            #append to instr-> load address of variable (should be an array)
                            #take base adress of first child, which should be a variable
                            ret = self.__getBaseAddress(ctx.getChild(0), True)
                            baddr = ret[0]
                            nd = ret[1]
                            isarg = ret[2]
                            glob = ret[3]
                            if( self.__inExprContextFollowedByConditionalContext(ctx) ):
                                nd += 1
                            if( isarg ):
                                instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nconv i a\n"
                                        % (nd, nd, (baddr+5)))
                            elif( glob ):
                                instr.append("ldc a %d\n" % (baddr) )
                            else:
                                instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\n"
                                        % (nd, nd, baddr))
                            first = False
                        self.__generateOffsetCode(child, instr, ftype, term)
                    else:
                        #code should've been generated, use an insert...
                        #if this child is terminal, generate code for offset
                        #else code was generated for offset...
                        self.__generateOffsetCode(child, instr, ftype, term)
                    if( '[' not in ftype and not self.__lhsAssignDecendant(ctx) ):
                        instr.append("ind %s\n" % typ)
                    adjustType = True
                elif( child.getText() in ["++","--"] and i > psp ):
                    #this is definitely a variable, possibly (de)referenced or indexed array, or array element address...
                    #if first child is terminal, get type and generate code...
                    #else code was generated, still need to get type...
                    #guessing same stuff must happen in both cases?
                    #   ->ALMOST, if terminal, check for indirection & replace,
                    #           else, check instr-block of previous child (so depending if previous child was terminal or not)
                    op = "inc" if child.getText() == "++" else "dec"
                    opp = "inc" if op == "dec" else "dec"
                    if( "Terminal" in str(type(ctx.getChild(0))) ):
                        self.__check4IndirectionsNreplace(ctx, ctx.getChild(0), instr, op, opp, True, False)
                    else:
                        #check instr-block of previous child (so depending if previous child was terminal or not)
                        prevchild = ctx.getChild(i-1)
                        if( "Terminal" in str(type(prevchild)) ):
                            self.__check4IndirectionsNreplace(ctx, ctx.getChild(0), instr, op, opp, False, False)
                        else:
                            #prev child not terminal, meaning nt2pass is still referring to the prev child's instr-block
                            pcinstr = self.__instrs[-(nt2pass)]
                            self.__check4IndirectionsNreplace(ctx, ctx.getChild(0), pcinstr, op, opp, False, False)
                #else fubar?
            if( func ):
                #end of arguments
                if( ctx.getChild(0).getText() not in ["printf", "scanf"] ):
                    arglen += len(argtypes)
                    addrs.insert(0, ("ldc i %d\n" % arglen))
                else:
                    addrs = []
                    c1term = True if "Terminal" in str(type(ctx.getChild(1))) else False
                    if( c1term and self.__isVariable(ctx.getChild(1), c1term) ):
                        #must find variable & load up string... type is either char[] or char*
                        c1type = self.__getType(ctx.getChild(1))
                        ret = self.__getBaseAddress(ctx.getChild(1), True)
                        baddr = ret[0]
                        nd = ret[1]
                        isarg = ret[2]
                        glob = ret[3]
                        arrsize = self.__getArraySize(c1type) + 1
                        if( self.__inExprContextFollowedByConditionalContext(ctx) ):
                            nd += 1
                        if( isarg ):
                            #just load address & let printf/scanf do the rest...
                            instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nconv i a\n"
                                    % (nd, nd, (baddr+5)))
                        elif( glob ):
                            instr.append("ldc a %d\n" % (baddr) )
                        else:
                            #just load address & let printf/scanf do the rest...
                            instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\n"
                                    % (nd, nd, baddr))
                        arglen += 1
                        #just load address & let printf/scanf do the rest...
                        instr.insert(0, ("ldc i 1\n"))
                    elif( c1term and '\"' == ctx.getChild(1).getText()[0] ):
                        strarg = ctx.getChild(1).getText()
                        strarg = strarg[1:-1] if '\"' == strarg[0] else strarg
                        instr.append("ldc c 0\n")
                        arglen += 1
                        looper = 0
                        for i in range(0, len(strarg)):
                            temp = strarg[len(strarg)-1-looper]
                            if( looper < (len(strarg)-1) ):
                                if( strarg[len(strarg)-1-looper] == 'n' and strarg[len(strarg)-2-looper] == '\\' ):
                                    temp = '\n'
                                    looper += 1
                                elif( strarg[len(strarg)-1-looper] == 't' and strarg[len(strarg)-2-looper] == '\\' ):
                                    temp = '\t'
                                    looper += 1
                            if( temp != '\n' and temp != '\t' ):
                                instr.append("ldc c %d\n" % ord(temp))
                            else:
                                ordval = 10 if temp == '\n' else 9
                                instr.append("ldc c %d\n" % ordval)
                            arglen += 1
                            looper += 1
                            if( looper >= len(strarg) ):
                                break
                        instr.insert(0, ("ldc i 0\n"))
                    elif( not c1term ):
                        #address was calculated earlier, use that to load up the string...
                        #using return value address of this function stack as temp var for loop-address
                        #using current function's return value address (i.e. at MP)
                        # to temporarily keep the start address that was calculated earlier
                        #so top of stack contains address to a char type, no matter what... (in this case)
                        #address was loaded... let printf/scanf do the rest...
                        arglen += 1
                        instr.insert(0, ("ldc i 1\n"))
                    #else fubar

                self.__combineInstructionsPostfix(ctx, ntnodes, instr, addrs, arglen, True, ftype)
            else:
                self.__combineInstructionsPostfix(ctx, ntnodes, instr, addrs, arglen, False,ftype)
            if( ntnodes > 1 ):
                self.__type = self.__type[:-(ntnodes-1)]
            if( adjustType ):
                self.__type[-1] = ftype
        #else fubar...
        self.__exitInitiator(ctx)
        pass

    def __combineInstructionsPostfix(self, ctx, ntnodes, instr, addrs, arglen, func, ftype):
        nt2pass = ntnodes
        for i in range(0, len(instr)):
            if( instr[i] == "insert" ):
                instr[i] = self.__instrs[-nt2pass]
                nt2pass -= 1
        if( func ):
            addrs.insert(0, "mst 0\n")
            instr.append("cup %d %s\n" % ((arglen-5), ctx.getChild(0).getText()))
        if( ftype != "void" and not self.__inAssignableContext(ctx) ):
            typ = self.__getTypeP(ftype)
            instr.append("conv %s b\nldc b f\nand\nconv b c\nout c\n" % (typ))
        if( ntnodes > 0 ):
            self.__instrs = self.__instrs[:-ntnodes]
        self.__instrs.append(addrs + instr)


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
        elif( op == "!" ):
            ty = "int"
        #else '+' or '-' which we will handle later (for example, generate warning if a sign is placed in front of a pointer type)
        return ty

    def __getStringValue(self, string):
        value = 0
        looper = 0
        for i in range(0, len(string)):
            if( (looper < (len(string)-1)) and string[looper] == '\\' and string[looper+1] == 'n' ):
                value += 10
                looper += 1
            else:
                value += ord(string[looper])
            looper += 1
            if( looper >= len(string) ):
                break
        return value

    def __generateCode4Load(self, ctx, instr, child1term, otype, notormin):
        if( child1term ):
            var = self.__getVariableFromScope(ctx.getChild(1).getText())
            typ = self.__getTypeP(otype)
            if( var != None and ctx.getChild(1).getText() not in ["true","false"] ):
                if( var[0][0] == "function" ): #parameterless function
                    instr.append("mst 0\nldc i 6\ncup 1 %s\n" % ctx.getChild(1).getText())
                else:
                    ret = self.__getBaseAddress(ctx.getChild(1), True)
                    baddr = ret[0]
                    nd = ret[1]
                    isarg = ret[2]
                    glob = ret[3]
                    if( self.__inExprContextFollowedByConditionalContext(ctx) ):
                        nd += 1
                    if( isarg ):
                        instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nconv i a\nind %s\n"
                                    % (nd, nd, (baddr+5), typ) )
                    elif( glob ):
                        instr.append("ldo %s %d\n" % (typ, baddr) )
                    else:
                        instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\nind %s\n"
                                    % (nd, nd, baddr, typ) )
            elif( notormin ):
                text = ctx.getChild(1).getText()
                if( "\"" in text ):
                    value = self.__getStringValue(text[1:-1])
                    instr.append("ldc i %d\n" % (typ, value))
                    return "i"
                elif( "\'" in text ):
                    if( text == "\'\\n\'" ):
                        instr.append("ldc c %s\n" % "\'\\n\'")
                    else:
                        instr.append("ldc c %d\n" % ord(text[1]))
                elif( text in ["true","false"] ):
                    val = 1 if text == "true" else 0
                    instr.append("ldc i %d\n" % val)
                else:
                    #must be numerical constant...
                    if( self.__representsInt(text) and typ == "i" ):
                        instr.append("ldc %s %d\n" % (typ, int(text, 0)))
                    elif( self.__representsFloat(text) and typ == "r" ):
                        instr.append("ldc %s %f\n" % (typ, float(text)))
            else:
                #shouldn't happend though...
                print("\033[1;35mWarning\033[0m, %s @ line %d:"
                " Useless usage of operator \'%s\' in expression \'%s\'."
                    % (self.__currentfunc, ctx.start.line, ctx.getChild(0).getText(), ctx.getText()) )
        return None

    # Exit a parse tree produced by subCParser#unaryexpr.
    def exitUnaryexpr(self, ctx):
        instr = []
        if( ctx.getChildCount() > 1 ):
            child0text = ctx.getChild(0).getText()
            child1term = ("Terminal" in str(type(ctx.getChild(1))))
            if( child0text == "sizeof" ):
                #first child should always be terminal
                #sizeof should return an 'int' no matter what the queried type is
                c1type = None
                if( child1term ):
                    c1type = self.__getType(ctx.getChild(1))
                    self.__type.append("int")
                else:
                    c1type = self.__type[-1]
                    self.__type[-1] = "int"
                if( '[' in c1type and "*)" not in c1type and "*const)" not in c1type ):
                    arrsize = self.__getArraySize(c1type)
                    #arrsize = (arrsize+1) if "char" in c1type else arrsize
                    instr.append("ldc i %d"%arrsize)
                    #for open-array arguments this is a problem...
                else:
                    instr.append("ldc i 1")
            elif( child0text in ["&","*","+","-","!","++","--"] ):
                #'+' and '-' shouldn't change anything to the current type
                c1type = None
                if( child1term ):
                    c1type = self.__getType(ctx.getChild(1))
                    self.__type.append(c1type)
                else:
                    c1type = self.__type[-1]
                otype = c1type
                c1type = self.__adjustType(child0text, c1type, ctx)
                self.__type[-1] = c1type
                if( child0text in ["++","--"] ):
                    op = "inc" if child0text == "++" else "dec"
                    opp = "inc" if op == "dec" else "dec"
                    if( child1term ):
                        self.__check4IndirectionsNreplace(ctx, ctx.getChild(1), instr, op, opp, True, True)
                    else:
                        pcinstr = self.__instrs[-1]
                        self.__check4IndirectionsNreplace(ctx, ctx.getChild(1), pcinstr, op, opp, False, True)
                elif( child0text == "&" ):
                    #if child1 is terminal, must generate that code too...
                    #else, code was generated & we must remove the indirection...
                    if( child1term ):
                        var = self.__getVariableFromScope(ctx.getChild(1).getText())
                        if( var != None and var[0][0] != "function" ):
                            ret = self.__getBaseAddress(ctx.getChild(1), True)
                            baddr = ret[0]
                            nd = ret[1]
                            isarg = ret[2]
                            glob = ret[3]
                            if( self.__inExprContextFollowedByConditionalContext(ctx) ):
                                nd += 1
                            if( isarg ):
                                instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nconv i a\n"
                                            % (nd, nd, (baddr+5)) )
                            elif( glob ):
                                instr.append("ldc a %d\n" % (baddr) )
                            else:
                                instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\n"
                                            % (nd, nd, baddr) )
                        else:
                            #shouldn't happend though...
                            print("\033[1;35mWarning\033[0m, %s @ line %d:"
                            " Useless usage of reference operator \'&\' in expression \'%s\'."
                                % (self.__currentfunc, ctx.start.line, ctx.getText()) )
                    else:
                        if(  "ind " in self.__instrs[-1][-1] ):
                            self.__instrs[-1][-1] = self.__instrs[-1][-1].rsplit("ind ", 1)[0]
                        else:
                            print("\033[1;35mWarning\033[0m, %s @ line %d:"
                            " Useless usage of reference operator \'&\' in expression \'%s\'."
                                % (self.__currentfunc, ctx.start.line, ctx.getText()) )
                elif( child0text == "*" ):
                    self.__generateCode4Load(ctx, instr, child1term, otype, False)
                    typd = self.__getTypeP(c1type)
                    if( not self.__lhsAssignDecendant(ctx) and '[' not in c1type ):
                        instr.append("ind %s\n" % typd)
                elif( child0text == "!" ):
                    res = self.__generateCode4Load(ctx, instr, child1term, otype, True)
                    typo = self.__getTypeP(otype) if res == None else "i"
                    instr.append("conv %s b\nnot\nconv b i\n" % typo)
                elif( child0text == "+" ):
                    #Do nothing right?
                    pass
                elif( child0text == "-" ):
                    res = self.__generateCode4Load(ctx, instr, child1term, otype, True)
                    typo = self.__getTypeP(otype) if res == None else "i"
                    if( typo not in ["i","r"] ):
                        instr.append("conv %s i\nneg %s\nconv i %s\n" % (typo, typo, typo))
                    else:
                        instr.append("neg %s\n" % typo)
                    #perhaps generate warnings here if dealing with pointers or array addresses?
            c1type = None
            if( child1term ):
                c1type = self.__getType(ctx.getChild(1))
            else:
                c1type = self.__type[-1]
            if( c1type != "void" and not self.__inAssignableContext(ctx) ):
                typ = self.__getTypeP(c1type)
                instr.append("conv %s b\nldc b f\nand\nconv b c\nout c\n" % (typ))
            if( child1term ):
                self.__instrs.append(instr)
            else:
                self.__instrs[-1] = self.__instrs[-1] + instr
        else:
            self.__instrs.append(instr)
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#castexpr.
    def enterCastexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    # Exit a parse tree produced by subCParser#castexpr.
    def exitCastexpr(self, ctx):
        instr = []
        if( ctx.getChildCount() > 1 ):
            #last child should be the type to be casted
            #all other children, terminal or non-terminal, should represent a type to which is casted
            ret = self.__initPostfix(ctx, ctx.getChild((ctx.getChildCount()-1)), 1) #doing same stuff as we would in postfix
            ftype = ret[0]
            isfunc = ret[2]
            ftyp = self.__getTypeP(ftype)
            temp = ctx.getChild(0).getText()
            if( "(*)" in temp and '[' not in temp ):
                temp = temp.replace("(*)", "*")
            if( len(self.__type) > 0 ):
                self.__type[-1] = temp
            else:
                self.__type.append(temp)
            #code gen
            last = ctx.getChild((ctx.getChildCount()-1))
            lterm = True if "Terminal" in str(type(last)) else False
            if( lterm ):
                if( isfunc ):
                    instr.append("mst 0\nldc i 6\ncup 1 %s\n" % last.getText())
                else:
                    ret = self.__getBaseAddress(last, True)
                    if( ret != None ):
                        baddr = ret[0]
                        nd = ret[1]
                        isarg = ret[2]
                        glob = ret[3]
                        if( self.__inExprContextFollowedByConditionalContext(ctx) ):
                            nd += 1
                        if( isarg ):
                            instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nconv i a\nind %s\n"
                                        % (nd, nd, (baddr+5), ftyp) )
                        elif( glob ):
                            instr.append("ldo %s %d\n" % (ftyp, baddr) )
                        else:
                            instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\nind %s\n"
                                        % (nd, nd, baddr, ftyp) )
                    elif( last.getText() in ["true","false"] ):
                        val = 1 if last.getText() == "true" else 0
                        instr.append("ldc i %d\n" % val)
                    else:
                        self.__generateLoadConstantCode(instr, last.getText(), ftyp, ftyp)
            else:
                instr = self.__instrs[-1]
            lastyp = ftyp
            for i in reversed(range(0, (ctx.getChildCount()-1))):
                child = ctx.getChild(i)
                ctype = None
                ctype = child.getText()
                typ = self.__getTypeP(ctype)
                instr.append("conv %s %s\n" % (lastyp,typ))
                lastyp = typ
            if( temp != "void" and not self.__inAssignableContext(ctx) ):
                typ = self.__getTypeP(temp)
                instr.append("conv %s b\nldc b f\nand\nconv b c\nout c\n" % (typ))
            if( lterm ):
                self.__instrs.append(instr)
            else:
                self.__instrs[-1] = instr
        #else fubar
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#mulexpr.
    def enterMulexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __generateLoadConstantCode(self, instr, text, typ, rtyp, rhshift):
        #should be terminal node!
        if( "\'" in text ):
            if( text == "\'\\n\'" ):
                instr.append("ldc c %s\n" % "\'\\n\'")
            else:
                instr.append("ldc c %d\n" % ord(text[1]))
        elif( "\"" in text ):
            text = text[1:-1]
            for i in range(0, len(text)):
                if( text[i] == "\'\\n\'" ):
                    instr.append("ldc c %s\n" % "\'\\n\'")
                else:
                    instr.append("ldc c %s\n" % ord(text[i]))
        else:
            #must be numerical constant...
            if( self.__representsInt(text) and typ == "i" ):
                val = int(text, 0)
                if( rhshift ): #2^rhs
                    val = 2**val
                instr.append("ldc i %d\n" % (val))
            elif( self.__representsFloat(text) and typ == "r" ):
                instr.append("ldc r %f\n" % (float(text)))

    def __inExprContextFollowedByConditionalContext(self, node):
        temp = node
        while( temp.parentCtx != None ):
            temp = temp.parentCtx
            if( "Expr" in str(type(temp)) ):
                if( "Conditionalexpr" in str(type(temp.parentCtx)) ):
                    return True
            elif( "Compounds" in str(type(temp)) ): #at this point the conditions for True can't be met anymore...
                return False
        return False

    def __generateLoadCode(self, node, instr, typ, restype, offset, rhshift):
        if( "Terminal" in str(type(node)) ):
            ret2 = self.__getBaseAddress(node, True)
            if( ret2 == None ): #parameterless function call or constant...
                if( self.__isFunction(node, self.__isVariable(node, True)) ):
                    instr.append("mst 0\nldc i 6\ncup 1 %s\n" % node.getText() )
                else:
                    self.__generateLoadConstantCode(instr, node.getText(), typ, restype, rhshift)
            elif( node.getText() in ["true","false"] ):
                val = 1 if node.getText() == "true" else 0
                instr.append("ldc i %d\n" % val)
            else:
                baddr = ret2[0]
                nd = ret2[1]
                isarg = ret2[2]
                glob = ret2[3]
                if( self.__inExprContextFollowedByConditionalContext(node) ):
                    nd += 1
                if( isarg ):
                    instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nconv i a\nind %s\n"
                                % (nd, nd, (baddr+5), typ) )
                elif( glob ):
                    instr.append("ldo %s %d\n" % (typ, baddr) )
                else:
                    instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\nind %s\n"
                                % (nd, nd, baddr, typ) )
                if( rhshift ): #2^rhs
                    exitcase = (self.__l+str(self.__nrl))
                    mainloop = (self.__l+str(self.__nrl+1))
                    instr.append("ldc i 1\n%s:\nlda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\n ind i\n"
                            "ldc i 0\nequ i\nfjp %s\nsli i\nujp %s\n"
                            % (mainloop, nd, nd, self.__offaddr+1, (self.__l+str(self.__nrl+2)), exitcase))
                    instr.append("%s:\nlda %d 0\nconv a i\nlod i %d 5\nadd i\nldc i %d\nadd i\nconv i a\ndpl a\n ind i\n"
                            "dec i 1\nsto i\nldc i 2\nmul i\nujp %s\n%s:\n"
                            % ((self.__l+str(self.__nrl+2)), nd, nd, self.__offaddr+1, mainloop, exitcase))
                    self.__nrl += 3
        else:
            instr[:] = instr[:] + self.__instrs[-offset]
        if( typ != restype ):
            instr.append("conv %s %s\n" % (typ, restype))


    # Exit a parse tree produced by subCParser#mulexpr.
    def exitMulexpr(self, ctx):
        instr = []
        ret = self.__MulOrAdd(ctx)
        modulo = False
        if( ret != None and ctx.getChildCount() > 1 and ctx.getChild(1).getText() == "%" ):
            #prepare other stuff?
            modulo = True
        #code gen
        self.__generateMulAddCode(ctx, instr, ret, modulo, False)
        self.__exitInitiator(ctx)
        pass

    def __generateMulAddCode(self, ctx, instr, ret, modulo, add):
        typl = self.__getTypeP(ret[0])
        typr = self.__getTypeP(ret[1])
        restyp = self.__getTypeP(self.__type[-1])
        rescop = restyp
        restyp = restyp if restyp in ["i","r"] else "i"
        lhs = ctx.getChild(0)
        rhs = ctx.getChild((ctx.getChildCount()-1))
        lhsterm = True if "Terminal" in str(type(lhs)) else False
        rhsterm = True if "Terminal" in str(type(rhs)) else False
        offset = 1 if not lhsterm else 0
        offset = (offset+1) if not rhsterm else offset
        self.__generateLoadCode(lhs, instr, typl, restyp, offset, False)
        offset = 1 if not rhsterm else 0
        instrlen = 0
        if( modulo ):
            instr = instr + instr
            instrlen = len(instr)
        self.__generateLoadCode(rhs, instr, typr, restyp, offset, False)
        temp = []
        if( modulo ):
            temp = instr[instrlen:]
            #code for modulo, restyp must be "i"
            instr.append("div i\n")
            instr = instr + temp
            instr.append("mul i\nsub i\n")
        else:
            op = "mul" if ctx.getChild(1).getText() == "*" else "div"
            if( add ):
                op = "add" if ctx.getChild(1).getText() == "+" else "sub"
            instr.append("%s %s\n" % (op, restyp))
            if( rescop != restyp ):
                instr.append("conv %s %s\n" % (restyp, rescop))
        #must check if we're in assignable context.. otherwise we'll need to adjust offaddr
        if( self.__type[-1] != "void" and not self.__inAssignableContext(ctx) ):
            typ = self.__getTypeP(self.__type[-1])
            instr.append("conv %s b\nldc b f\nand\nconv b c\nout c\n" % (typ))
        if( lhsterm and rhsterm ):
            self.__instrs.append(instr)
        elif( not(lhsterm or rhsterm) ):
            self.__instrs = self.__instrs[:-1]
        if( not lhsterm or not rhsterm ):
            self.__instrs[-1] = instr
        #print self.__instrs


    def __MulOrAdd(self, ctx):
        lhs = ctx.getChild(0)
        rhs = ctx.getChild(ctx.getChildCount()-1)
        ret = self.__getTypes(ctx, lhs, rhs)
        lhstype = ret[0]
        rhstype = ret[1]
        noterm = ret[2]
        allterm = ret[3]

        ret2 = self.__lhsNrhsAddableOrMullable(lhstype, rhstype)
        restype = ret2[0]
        if( (self.__initor != id(ctx)) ):
            if( noterm ):
                 self.__type.pop()
            if( len(self.__type) > 0 and not allterm ):
                self.__type[-1] = restype
            else:
                self.__type.append(restype)
        return (lhstype, rhstype)


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
        ret = self.__MulOrAdd(ctx)
        #code gen
        instr = []
        self.__generateMulAddCode(ctx, instr, ret, False, True)
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
        lhs = ctx.getChild(0)
        rhs = ctx.getChild(ctx.getChildCount()-1)
        ret = self.__getTypes(ctx, lhs, rhs)
        lhstype = ret[0]
        rhstype = ret[1]
        noterm = ret[2]
        allterm = ret[3]
        if( (self.__initor != id(ctx)) ):
            if( noterm ):
                 self.__type.pop()
            if( len(self.__type) > 0 and not allterm ):
                self.__type[-1] = "int"
            else:
                self.__type.append("int")
        #code gen
        instr = []
        typl = self.__getTypeP(lhstype)
        typr = self.__getTypeP(rhstype)
        restyp = "i"
        lhsterm = True if "Terminal" in str(type(lhs)) else False
        rhsterm = True if "Terminal" in str(type(rhs)) else False
        offset = 1 if not lhsterm else 0
        offset = (offset+1) if not rhsterm else offset
        self.__generateLoadCode(lhs, instr, typl, restyp, offset, False)
        offset = 1 if not rhsterm else 0
        self.__generateLoadCode(rhs, instr, typr, restyp, offset, True)
        op = "mul" if ctx.getChild(1).getText() == "<<" else "div"
        instr.append("%s %s\n" % (op, restyp))
        #must check if we're in assignable context.. otherwise we'll need to adjust offaddr
        if( not self.__inAssignableContext(ctx) ): #type is always int...
            instr.append("conv i b\nldc b f\nand\nconv b c\nout c\n")
        if( lhsterm and rhsterm ):
            self.__instrs.append(instr)
        elif( not(lhsterm or rhsterm) ):
            self.__instrs = self.__instrs[:-1]

        if( not lhsterm or not rhsterm ):
            self.__instrs[-1] = instr
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#relationalexpr.
    def enterRelationalexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __lhsNrhsTypes(self, ctx, lhs, rhs):
        #valid for relational, equality, logicaland and logicalor contexts
        lhstype = None
        rhstype = None
        tnodes = self.__countTerminalNodes(ctx)
        lterm = False
        rterm = False
        if( tnodes == ctx.getChildCount() ):
            lhstype = self.__getType(lhs)
            rhstype = self.__getType(rhs)
            lterm = True
            rterm = True
            self.__type.append("int")
        elif( "Terminal" in str(type(lhs)) ):
            lhstype = self.__getType(lhs)
            rhstype = self.__type[-1]
            lterm = True
        elif( "Terminal" in str(type(rhs)) ):
            lhstype = self.__type[-1]
            rhstype = self.__getType(rhs)
            rterm = True
        else:
            lhstype = self.__type[-2]
            rhstype = self.__type.pop()
        return [lhstype, rhstype, lterm, rterm]

    # Exit a parse tree produced by subCParser#relationalexpr.
    def exitRelationalexpr(self, ctx):
        self.__commonFunction01(ctx)
        self.__exitInitiator(ctx)
        pass

    def __getRelEqOp(self, ctx):
        op = ""
        if( ctx.getChildCount() == 4 ):
            op = "geq" if ctx.getChild(1).getText() == ">" else "leq"
        elif( ctx.getChildCount() == 3 ):
            if( ctx.getChild(1).getText() == "<" ):
                op = "les"
            elif( ctx.getChild(1).getText() == ">" ):
                op = "grt"
            elif( ctx.getChild(1).getText() == "==" ):
                op = "equ"
            elif( ctx.getChild(1).getText() == "!=" ):
                op = "neq"
        return op


    def __commonFunction01(self, ctx):
        if( ctx.getChildCount() > 1 ):
            # '<=', '<', '>=', '>', '==' and '!=' all obey the same rules so just take first & last child and compare types
            lhs = ctx.getChild(0)
            rhs = ctx.getChild(ctx.getChildCount()-1)
            ret = self.__lhsNrhsTypes(ctx, lhs, rhs)
            lhstype = ret[0]
            rhstype = ret[1]
            lterm = ret[2]
            rterm = ret[3]
            self.__type[-1] = "int"

            #code gen?
            instr = []
            typl = self.__getTypeP(lhstype)
            typr = self.__getTypeP(rhstype)
            restyp = "i"
            offset = 1 if not lterm else 0
            offset = (offset+1) if not rterm else offset
            self.__generateLoadCode(lhs, instr, typl, restyp, offset, False)
            offset = 1 if not rterm else 0
            self.__generateLoadCode(rhs, instr, typr, restyp, offset, False)
            op = self.__getRelEqOp(ctx)
            instr.append("%s i\n" % (op))
            instr.append("conv b i\n")
            #must check if we're in assignable context.. otherwise we'll need to adjust offaddr
            if( not self.__inAssignableContext(ctx) ): #type is always int...
                instr.append("conv i b\nldc b f\nand\nconv b c\nout c\n")
            if( lterm and rterm ):
                self.__instrs.append(instr)
            elif( not(lterm or rterm) ):
                self.__instrs = self.__instrs[:-1]

            if( not lterm or not rterm ):
                self.__instrs[-1] = instr

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

    def __commonFunction02(self, ctx):
        if( ctx.getChildCount() > 1 ):
            lhs = ctx.getChild(0)
            rhs = ctx.getChild(ctx.getChildCount()-1)
            ret = self.__lhsNrhsTypes(ctx, lhs, rhs)
            lhstype = ret[0]
            rhstype = ret[1]
            lterm = ret[2]
            rterm = ret[3]
            self.__type[-1] = "int"
            #code gen?
            instr = []
            typl = self.__getTypeP(lhstype)
            typr = self.__getTypeP(rhstype)
            restyp = "i"
            offset = 1 if not lterm else 0
            offset = (offset+1) if not rterm else offset
            self.__generateLoadCode(lhs, instr, typl, restyp, offset, False)
            instr.append("conv i b\n")
            offset = 1 if not rterm else 0
            self.__generateLoadCode(rhs, instr, typr, restyp, offset, False)
            instr.append("conv i b\n")
            op = "and" if ctx.getChild(1).getText() == "&&" else "or"
            instr.append("%s\n" % (op))
            instr.append("conv b i\n")
            #must check if we're in assignable context.. otherwise we'll need to adjust offaddr
            if( not self.__inAssignableContext(ctx) ): #type is always int...
                instr.append("conv i b\nldc b f\nand\nconv b c\nout c\n")
            if( lterm and rterm ):
                self.__instrs.append(instr)
            elif( not(lterm or rterm) ):
                self.__instrs = self.__instrs[:-1]
            if( not lterm or not rterm ):
                self.__instrs[-1] = instr
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
            return e1type
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
            ntnodes = ctx.getChildCount() - self.__countTerminalNodes(ctx)
            condtype = [self.__getType(cond), 0] if "Terminal" in str(type(cond)) else [self.__type[-ntnodes], 1]
            e1type = self.__getType(e1) if "Terminal" in str(type(e1)) else self.__type[-(ntnodes-condtype[1])]
            e2type = self.__getType(e2) if "Terminal" in str(type(e2)) else self.__type[-1]
            restype = self.__conditionalChecks(ctx, e1, e2, e1type, e2type)
            if( ntnodes > 1 ):
                self.__type = self.__type[:-(ntnodes-1)]
                self.__type[-1] = restype
            instr = []
            typc = self.__getTypeP(condtype[0])
            type1 = self.__getTypeP(e1type)
            type2 = self.__getTypeP(e2type)
            typr = self.__getTypeP(restype)
            condterm = ("Terminal" in str(type(cond)))
            e1term = ("Terminal" in str(type(e1)))
            e2term = ("Terminal" in str(type(e2)))
            offset = 1 if not condterm else 0
            offset = (offset+1) if not e1term else offset
            offset = (offset+1) if not e2term else offset
            begin1 = (self.__l+str(self.__nrl))
            begin2 = (self.__l+str(self.__nrl+1))
            if( restype == "void" ): #or not within an assignable context...
                instr.append("ujp %s\n%s:\n" % (begin2, begin1))
                self.__nrl += 2
            self.__generateLoadCode(cond, instr, typc, typc, offset, False)
            offset = (offset-1) if not condterm else offset
            instr.append("conv %s b\nfjp %s\n" % (typc, (self.__l+str(self.__nrl))))
            temp = self.__nrl
            self.__nrl += 2
            self.__generateLoadCode(e1, instr, type1, typr, offset, False)
            offset = (offset-1) if not e1term else offset
            instr.append("ujp %s\n%s:\n" % ((self.__l+str(temp+1)), (self.__l+str(temp))))
            self.__generateLoadCode(e2, instr, type2, typr, offset, False)
            instr.append("%s:\n" % (self.__l+str(temp+1)))
            if( restype == "void" ): #or not within an assignable context...
                instr.append("retp\n%s:\nmst 0\nldc i 6\ncup 1 %s\n" % (begin2, begin1))
            if( restype != "void" and not self.__inAssignableContext(ctx) ):
                instr.append("conv %s b\nldc b f\nand\nconv b c\nout c\n" % typr)
            if( ntnodes > 0 ):
                self.__instrs = self.__instrs[:-ntnodes]
            self.__instrs.append(instr)
        #else fubar
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#assignexpr.
    def enterAssignexpr(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __getVariableFromScope(self, var):
        if( var in self.__scopesyms ):
            return [self.__scopesyms[var], 0]
        nd = 1
        for i in reversed(self.__parents):
            if( var in i ):
                return [i[var], nd]
            nd += 1
        return None

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

    def __countTerminalNodes(self, ctx):
        nrnodes = 0
        for child in ctx.getChildren():
            if( "Terminal" in str(type(child)) ):
                nrnodes += 1
        return nrnodes

    def __getType(self, val):
        valtype = None
        if( val.getText()[0] == '\"' ):
            #string literal
            valtype = "char[" + str(len(val.getText())-2) + "]"
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
            val = val[0] if val != None else val
            if( val == None ):
                #shouldn't be the case though, & if so, an error should already have been generated...
                self.error = True
                return None
            if( len(val) > 2 and val[0] == "function" ): #function
                valtype = val[1]
            elif( len(val) > 2 ): #variable
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
            lhs = self.__getVariableFromScope(ctx.getChild(0).getText())[0]
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
                lhs = self.__getVariableFromScope(ctx.getChild(0).getText())[0]
                lhstype = lhs[0]
                #rhs must've been built up by now in __type
                rhstype = self.__type[-1]
            elif( "Terminal" in str(type(ctx.getChild(ctx.getChildCount()-1))) ):
                #lhs must've been built up by now in __type
                lhs = ctx.getChild(0)
                lhstype = self.__type[-1]
                #rhs is terminal
                #this means rhs type is easily retrievable
                rhs = ctx.getChild(ctx.getChildCount()-1)
                rhstype = self.__getType(rhs)
            #else fubar
            oneterm = True
        elif( nrnodes == (ctx.getChildCount()-2) and (len(self.__type) > 1) ):
            #is this it?
            lhstype = self.__type[-2]
            rhstype = self.__type[-1]
            noterm = True
        #else fubar?

        if( (self.__initor != id(ctx)) and (oneterm or noterm) ):
            if( noterm ):
                self.__type.pop()
            if( len(self.__type) > 0 and (oneterm or noterm) ):
                self.__type[-1] = "void"
            else:
                self.__type.append("void")

        #code gen
        instr = []
        lhs = ctx.getChild(0)
        rhs = ctx.getChild(ctx.getChildCount()-1)
        typl = self.__getTypeP(lhstype)
        typr = self.__getTypeP(rhstype)
        lterm = True if "Terminal" in str(type(lhs)) else False
        rterm = True if "Terminal" in str(type(rhs)) else False
        offset = 1 if not lterm else 0
        offset = (offset+1) if not rterm else offset
        self.__generateLoadCode(lhs, instr, typl, typl, offset, False)
        if( ("ind %s\n"%typl) in instr[-1] and not instr[-1].rsplit(("ind %s\n"%typl), 1)[1] ):
            instr[-1] = instr[-1].rsplit(("ind %s\n"%typl), 1)[0]
        if( ctx.getChildCount() == 4 ):
            op = ctx.getChild(1).getText()
            if( op in ["*","<<","/",">>"] ):
                offset = 2 if not rterm else 1
                self.__generateLoadCode(lhs, instr, typl, typl, offset, False)
                temp = typl
                if( temp not in ["i","r"] ):
                    instr.append("conv %s i\n" % typl)
                self.__generateLoadCode(rhs, instr, typr, temp, 1, (op == "<<" or op == ">>"))
                opstr = "mul" if op in ["*","<<"] else "div"
                instr.append("%s %s\n" % (opstr, temp))
                if( temp != typl ):
                    instr.append("conv %s %s\n" % (temp, typl))
            elif( op == "%" ):
                #type should've been checked for int only
                offset = 2 if not rterm else 1
                self.__generateLoadCode(lhs, instr, typl, typl, offset, False)
                self.__generateLoadCode(lhs, instr, typl, typl, offset, False)
                self.__generateLoadCode(rhs, instr, typr, typl, 1, False)
                instr.append("div i\n")
                self.__generateLoadCode(rhs, instr, typr, typl, 1, False)
                instr.append("mul i\nsub i\n")
            elif( op in ["+","-"] ):
                offset = 2 if not rterm else 1
                self.__generateLoadCode(lhs, instr, typl, typl, offset, False)
                temp = typl
                if( temp not in ["i","r"] ):
                    instr.append("conv %s i\n" % typl)
                    temp = "i"
                self.__generateLoadCode(rhs, instr, typr, temp, 1, False)
                opstr = "add" if op == "+" else "sub"
                instr.append("%s %s\n" % (opstr, temp))
                if( temp != typl ):
                    instr.append("conv %s %s\n" % (temp, typl))
        else:
            temp = []
            self.__generateLoadCode(rhs, temp, typr, typl, 1, False)
            if( "char[" in rhstype and rhstype.count('[') == 1 ):
                counter = 0
                for t in temp:
                    instr.append("dpl a\ninc a %d\n%ssto c\n"%(counter, t))
                    counter += 1
                instr.append("inc a %d\nldc c 0\nsto c\n"%counter)
            else:
                instr = instr + temp
        if( not ("char[" in rhstype and rhstype.count('[') == 1) ):
            instr.append("sto %s\n" % typl)
        if( lterm and rterm ):
            self.__instrs.append(instr)
        elif( not(lterm or rterm) ):
            self.__instrs = self.__instrs[:-1]
        if( not lterm or not rterm ):
            self.__instrs[-1] = instr
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
            instr = []
            ntnodes = ctx.getChildCount() - self.__countTerminalNodes(ctx)
            nt2pass = ntnodes
            for i in range(0, ctx.getChildCount()):
                child = ctx.getChild(i)
                if( "Terminal" in str(type(child)) ):
                    var = self.__getVariableFromScope(child.getText())
                    #should only be parameterless functions...
                    if( var != None and var[0][0] == "function" and len(var[0][2]) == 0 ):
                        instr.append("mst 0\nldc i 6\ncup 1 %s\n" % child.getText())
                else:
                    instr = instr + self.__instrs[-nt2pass]
                    nt2pass -= 1
            if( ntnodes > 0 ):
                self.__instrs = self.__instrs[:-(ntnodes)]
            self.__instrs.append(instr)
        #else fubar
        self.__exitInitiator(ctx)
        pass


    def __findVariable(self, node):
        #can only be used by decl context, else it's mess up stuff...
        if( node.getChildCount() == 0 and node.getText().replace('_','a').isalnum()
                and self.__getVariableFromScope(node.getText()) != None ):
            return self.__getVariableFromScope(node.getText())[0]
        else:
            for child in node.getChildren():
                if( "Terminal" in str(type(child)) ):
                    if( child.getText().replace('_','a').isalnum() ):
                        return self.__findVariable(child)
                else:
                    return self.__findVariable(child)

    # Enter a parse tree produced by subCParser#decl.
    def enterDecl(self, ctx):
        self.__enterInitiator(ctx)
        pass

    def __countInitNodes(self, ctx):
        ic = 0
        for child in ctx.getChildren():
            if( "Initdecltor" in str(type(child)) ):
                ic += 1
        return ic

    def __isLastDecl(self, node):
        parent = node.parentCtx
        for i in range(0, len(parent.children)):
            if( node == parent.children[i] ):
                if( i < (len(parent.children)-1) ):
                    if( "Functiondef" in str(type(parent.children[i+1])) ):
                        return True
                    else:
                        return False
        return False

    # Exit a parse tree produced by subCParser#decl.
    def exitDecl(self, ctx):
        instr = []
        if( ctx.getChildCount() > 1 ):
            #must mind forward declarated functions...
            for i in range(1, ctx.getChildCount()):
                child = ctx.getChild(i)
                var = self.__findVariable(child)
                if( var != None and var[0] == "function" ):
                    self.__instrs = []
                    if( self.__currentfunc == u"" ):
                        if( self.__isLastDecl(ctx) ):
                            instr.append("mst 0\nldc i 6\ncup 1 main\nhlt\n")
                    self.__exitInitiator(ctx)
                    return
                var.append(self.__offaddr)
                self.__offaddr += 1
                typ = self.__getTypeP(var[0]) #shouldn't be a function...
                val = "0.0" if typ == "r" else "0"
                if( '[' in var[0] and not("*)" in var[0] or "*const)" in var[0]) ):
                    #array, adjust offaddr, either initialize all on 0 or let initdecltor initialize...
                    asize = self.__getArraySize(var[0])
                    #asize = asize+1 if ("char" in var[0] and var[0].count('[') == 1) else asize
                    self.__offaddr += (asize-1)
                    if( "Initdecltor" not in str(type(child)) ):
                        for j in range(0, asize):
                            instr.append("ldc %s %s\n" % (typ,val))
                    else:
                        instr.append("insert")
                else:
                    #non-array, if child is different from initdecltor, initval is just 0 and we can load a constant
                    #else we need to let initdecltor generate the code, or at least adjust the value...
                    if( "Initdecltor" not in str(type(child)) ):
                        instr.append("ldc %s %s\n" % (typ,val))
                    else:
                        instr.append("insert")
        initnodes = self.__countInitNodes(ctx)
        initcop = initnodes
        if( initcop > 0 ):
            for i in range(0, len(instr)):
                if( "insert" == instr[i] ):
                    instr = instr[:i] + self.__instrs[-initnodes] + instr[i+1:]
                    initnodes -= 1
            self.__instrs = self.__instrs[:-initcop]
        if( self.__currentfunc == u"" ):
            if( self.__isLastDecl(ctx) ):
                instr.append("mst 0\nldc i 6\ncup 1 main\nhlt\n")
        self.__instrs.append(instr)
        self.__exitInitiator(ctx)
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
                self.__initvar = self.__getVariableFromScope(ctx.getChild(0).getText())[0]
        #else fubar

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

    __initvar = None

    # Exit a parse tree produced by subCParser#initdecltor.
    def exitInitdecltor(self, ctx):
        instr = []
        if( ctx.getChildCount() > 2 ):
            lhs = ctx.getChild(0)
            rhs = ctx.getChild(2)
            rtype = self.__getType(rhs) if "Terminal" in str(type(rhs)) else self.__type[-1]
            ltype = self.__initvar[0]
            typl = self.__getTypeP(ltype)
            typr = self.__getTypeP(rtype)
            if( "[]" in ltype ):
                self.__adjustOpenArrayType(rtype)
            ltype = self.__initvar[0]
            if( "Terminal" in str(type(rhs)) ):
                if( self.__isVariable(rhs, True) ):
                    if( self.__isFunction(rhs, True) ):
                        #parameterless function, at least it should be..otherwhise rhs is not term
                        instr.append("mst 0\nldc i 6\ncup 1 %s\n" % rhs.getText())
                    else:
                        #if array, need to loop
                        #else, get base address & go
                        # if typl != typr then we need a conversion from typr to typl
                        ret = self.__getBaseAddress(rhs, True)
                        baddr = ret[0]
                        nd = ret[1]
                        isarg = ret[2]
                        glob = ret[3]
                        if( '[' in ltype and not("*)" in ltype or "*const)" in ltype) ):
                            #array stuff...
                            arrsize = self.__getArraySize(ltype)
                            arrsize = (arrsize + 1) if "char" in ltype else arrsize
                            for i in range(0, arrsize):
                                if( isarg ):
                                    instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\ninc i %d\nconv i a\nind %s\n"
                                            % (nd, nd, (baddr+5), i, typr))
                                elif( glob ):
                                    instr.append("ldc a %d\ninc a %d\nind %s\n" % (baddr, i, typr) )
                                else:
                                    instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\ninc i %d\nconv i a\nind %s\n"
                                                % (nd, nd, baddr, i, typr) )
                                if( typr != typl ):
                                    #shouldn't happen though...
                                    instr.append("conv %s %s\n" % (typr, typl))
                        else:
                            #non-array stuff...
                            if( isarg ):
                                instr.append("lda %d 0\nconv a i\nlod i %d %d\nadd i\nconv i a\nind %s\n"
                                        % (nd, nd, (baddr+5), typr))
                            elif( glob ):
                                instr.append("ldo %s %d\n" % (typr, baddr) )
                            else:
                                instr.append("lda %d 0\nconv a i\nlod i %d 5\nadd i\ninc i %d\nconv i a\nind %s\n"
                                            % (nd, nd, baddr, typr) )
                            if( typr != typl ):
                                instr.append("conv %s %s\n" % (typr, typl))
                else:
                    #load constant
                    if( rhs.getText()[0] == '\"' ): #constant (string literal)
                        st = rhs.getText()[1:-1]
                        looper = 0
                        for j in range(0, len(st)):
                            if( looper < (len(st)-1) and st[looper] == '\\' and st[looper+1] == 'n' ):
                                instr.append("ldc c \'\\n\'\n")
                                instr.append("ldc c 13\n")
                                looper +=1
                            else:
                                instr.append("ldc c %d\n" % ord(st[looper]))
                            if( typr != typl ):
                                instr.append("conv %s %s\n" % (typr, typl))
                            looper += 1
                            if( looper >= len(st) ):
                                break
                        instr.append("ldc c 0\n")
                    else:
                        temp = rhs.getText() if self.__representsInt(rhs.getText()) \
                                or self.__representsFloat(rhs.getText()) else rhs.getText()[1:-1]
                        if( temp != "\\n" ):
                            if( '\'' in rhs.getText() ):
                                temp = ord(temp)
                                instr.append("ldc %s %s\n" % (typr, temp))
                            elif( self.__representsInt(temp) ):
                                temp = int(temp, 0)
                                instr.append("ldc %s %d\n" % (typr, temp))
                            elif( self.__representsFloat(temp) ):
                                temp = float(temp)
                                instr.append("ldc %s %f\n" % (typr, temp))
                        else:
                            instr.append("ldc %s %s\n" % (typr, "\'\\n\'"))
                        if( typr != typl ):
                            instr.append("conv %s %s\n" % (typr, typl))
            else:
                instr.append("insert")
                #mind arrays! each element must be converted, not only the last one..
                #wait actually, arrays should match in type whatsoever right? so only common types can/could be converted
                if( typr != typl ):
                    instr.append("conv %s %s\n" % (typr, typl))

        #else fubar
        rhsterm = True if ctx.getChildCount() > 2 and "Terminal" in str(type(ctx.getChild(2))) else False
        for i in range(0, len(instr)):
            if( "insert" == instr[i] ): #should only occur once & __instrs[-1] is what we need...
                instr = instr[:i] + self.__instrs[-1] + instr[i+1:]
        if( not rhsterm ):
            self.__instrs = self.__instrs[:-1]
        else:
            self.__type.append(self.__initvar[0])
        self.__instrs.append(instr)
        self.__initvar = None
        self.__exitInitiator(ctx)


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
                        self.__initvar = var[0]
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
                        self.__initvar = var[0]
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
            if( ntnodes == 0 ):
                self.__type.append(types[0] + "[" + str(ctx.getChildCount()) + "]")
            else:
                if( ntnodes > 1 ):
                    self.__type = self.__type[:-(ntnodes-1)]
                self.__type[-1] = self.__type[-1].split('[',1)[0] + "[" + str(ctx.getChildCount()) + "][" \
                                + self.__type[-1].split('[',1)[1]
            instr = []
            typl = self.__getTypeP(ltype)
            typr = self.__getTypeP(self.__getCommonType(types[0]))
            nt2pass = ntnodes
            for i in range(0, ctx.getChildCount()):
                child = ctx.getChild(i)
                if( "Terminal" in str(type(child)) ):
                    self.__generateLoadCode(child, instr, typr, typl, 0, False)
                else:
                    instr = instr + self.__instrs[-nt2pass]
                    nt2pass -= 1
            if( ntnodes > 0 ):
                self.__instrs = self.__instrs[:-ntnodes]
            self.__instrs.append(instr)
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

    __caseinstrs = []

    # Exit a parse tree produced by subCParser#labeled.
    def exitLabeled(self, ctx):
        instr = []
        if( ctx.getChildCount() == 4 ):
            ty = None
            if( "Terminal" in str(type(ctx.getChild(1))) ):
                ty = self.__getType(ctx.getChild(1))
            else:
                ty = self.__type[-2]
            typ = self.__getTypeP(ty)
            offset = 1 if "Terminal" in str(type(ctx.getChild(2))) else 2
            offset = (offset+1) if ctx.getChildCount() == 5 and "Terminal" not in str(type(ctx.getChild(4))) else offset
            self.__generateLoadCode(ctx.getChild(1), instr, typ, "i", offset, False)
            self.__caseinstrs.append(instr)
            instr = []
            instr.append("insertlabel")
            if( "Terminal" in str(type(ctx.getChild(3))) ):
                typ = self.__getTypeP(self.__getType(ctx.getChild(3)))
                self.__generateLoadCode(ctx.getChild(3), instr, typ, typ, 0, False)
            else:
                instr = instr + self.__instrs[-1]
        elif( ctx.getChildCount() == 3 ):
            instr.append("default")
            if( "Terminal" in str(type(ctx.getChild(2))) ):
                typ = self.__getTypeP(self.__getType(ctx.getChild(2)))
                self.__generateLoadCode(ctx.getChild(2), instr, typ, typ, 0, False)
            else:
                instr = instr + self.__instrs[-1]
        ntnodes = ctx.getChildCount() - self.__countTerminalNodes(ctx)
        if( ntnodes > 0 ):
            self.__instrs = self.__instrs[:-ntnodes]
            self.__type = self.__type[:-ntnodes]
        self.__instrs.append(instr)
        self.__type.append("void")
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#compounds.
    def enterCompounds(self, ctx):
        self.__enterInitiator(ctx)
        if( len(self.__parents) == 1 and self.__funcscope ):
            self.__funcscope = False
        elif( self.__scopesyms.has_key(str(ctx.start.line)+"-"+str(ctx.start.column)) ):
            self.__parents.append(self.__scopesyms)
            self.__scopesyms = self.__scopesyms[str(ctx.start.line)+"-"+str(ctx.start.column)]
            self.__offaddrs.append(self.__offaddr)
            self.__offaddr = 0
            pass

    # Exit a parse tree produced by subCParser#compounds.
    def exitCompounds(self, ctx):
        if( len(self.__parents) > 1 ):
            self.__scopesyms = self.__parents.pop()
        if( len(self.__offaddrs) > 1 ):
            self.__offaddr = self.__offaddrs.pop()
        ntnodes = ctx.getChildCount() - self.__countTerminalNodes(ctx)
        instr = []
        temp = (self.__l+str(self.__nrl))
        temp2 = (self.__l+str(self.__nrl+1))
        self.__nrl += 2
        temp3 = None
        if( "Selection" not in str(type(ctx.parentCtx)) ):
            temp3 = (self.__l+str(self.__nrl))
            self.__nrl += 1
        else:
            temp3 = self.__exitcases[-1]

        if( "Functiondef" not in str(type(ctx.parentCtx)) ):
            instr.append("ldc i 0\nmst 0\nldc i 6\ncup 1 %s\ndpl i\nldc i 1\nneq i\nfjp %s\n"
                    "ldc i 2\nequ i\nfjp %s\nretf\n%s:\nujp %s\n%s:\nconv i b\nconv b c\nout c\nujp %s\n%s:\n"
                    % ((self.__l+str(self.__nrl)), temp, temp2, temp2, temp3,
                        temp, self.__exitcases[-1], (self.__l+str(self.__nrl))))
            self.__nrl += 1
        for i in range(0, ctx.getChildCount()):
            child = ctx.getChild(i)
            if( "Terminal" not in str(type(child)) ):
                instr = instr + self.__instrs[-ntnodes]
                ntnodes -= 1
            else:
                typ = self.__getTypeP(self.__getType(child))
                self.__generateLoadCode(child, instr, typ, typ, 0, False)
        if( "Functiondef" not in str(type(ctx.parentCtx)) ):
            instr.append("retp\n")
        if( "Selection" not in str(type(ctx.parentCtx)) ):
            instr.append(("%s:\n"%temp3))
        ntnodes = ctx.getChildCount() - self.__countTerminalNodes(ctx)
        if( ntnodes > 0 ):
            self.__instrs = self.__instrs[:-ntnodes]
            self.__type = self.__type[:-ntnodes]
        self.__type.append("void")
        self.__instrs.append(instr)
        self.__exitInitiator(ctx)
        pass


    __tyindex = []
    __exitcases = []

    # Enter a parse tree produced by subCParser#selection.
    def enterSelection(self, ctx):
        if( ctx.getChildCount() > 2 ):
            if( "Terminal" not in str(type(ctx.getChild(1))) ):
                self.__tyindex.append(len(self.__type))
            self.__exitcases.append(self.__l+str(self.__nrl))
            self.__nrl += 1
            self.__enterInitiator(ctx)
        pass

    def __countLabeledStatements(self, node):
        count = 0
        for child in node.getChildren():
            if( "Labeled" in str(type(child)) ):
                count += 1
        return count

    # Exit a parse tree produced by subCParser#selection.
    def exitSelection(self, ctx):
        #if should be handled at code-generation, switch/case needs checks for void and corresponding types
        instr = []
        if( ctx.getChildCount() > 2 ):
            switch = ("switch" == ctx.getChild(0).getText())
            ty = None
            if( "Terminal" in str(type(ctx.getChild(1))) ):
                ty = self.__getType(ctx.getChild(1))
            else:
                ty = self.__type[self.__tyindex.pop()]
            ty = ty[5:] if ty[:5] == "const" else ty
            typ = self.__getTypeP(ty)
            offset = 1 if "Terminal" in str(type(ctx.getChild(2))) else 2
            offset = (offset+1) if ctx.getChildCount() == 5 and "Terminal" not in str(type(ctx.getChild(4))) else offset
            if( switch ):
                #we need to account for the switched variable since the stack is now at nesting level +1
                #generateLoadCode will call getBaseAddress which will go fubar because we already left the Compounds
                self.__parents.append(self.__scopesyms)
                key = str(ctx.getChild(2).start.line)+"-"+str(ctx.getChild(2).start.column)
                self.__scopesyms = self.__scopesyms[key]
                self.__generateLoadCode(ctx.getChild(1), instr, typ, "i", offset, False)
                self.__scopesyms = self.__parents.pop()
            if( switch ):
                #must check last array of __instrs and take the first element to compare what we just loaded with the case..
                #notice that 3rd child can never be terminal, should always be compounds with jumps and labeled
                temp = self.__instrs[-1]
                for i in reversed(range(0, len(temp))):
                    val = temp[i]
                    if( val == "insertlabel" ):
                        caseinstr = self.__caseinstrs.pop()
                        if( "insertlabel" not in temp[:i] ):
                            temp = temp[:i] + instr + ["dpl i\n"] + caseinstr \
                                + [("equ i\nfjp %s\n" % (self.__l+str(self.__nrl-1)))] + temp[i+1:]
                            self.__nrl += 1
                        else:
                            temp[i] = ("%s:\n" % (self.__l+str(self.__nrl)))
                            temp = temp[:i+1] + ["lod i 0 6\n"] + caseinstr \
                                + [("equ i\nfjp %s\n" % (self.__l+str(self.__nrl-1)))] + temp[i+1:]
                            self.__nrl += 1
                    elif( val == "default" ):
                        temp[i] = ("%s:\n" % (self.__l+str(self.__nrl)))
                        self.__nrl += 1
                temp[-1] = ("retp\n%s:\n" % (self.__exitcases[-1]))
                instr = temp
            else:
                comp1 = True if "Compounds" in str(type(ctx.getChild(2))) else False
                haselse = True if ctx.getChildCount() == 5 else False
                comp2 = True if haselse and "Compounds" in str(type(ctx.getChild(4))) else False
                offset = 1 if "Terminal" in str(type(ctx.getChild(2))) else 2
                if( ctx.getChildCount() == 5 ):
                    offset = offset if ("Terminal" in str(type(ctx.getChild(4)))) else (offset+1)
                self.__generateLoadCode(ctx.getChild(1), instr, typ, "b", offset, False)
                c1 = (self.__l+str(self.__nrl)) if haselse else self.__exitcases[-1]
                c2 = self.__exitcases[-1]
                self.__nrl  = (self.__nrl+1) if haselse else self.__nrl
                if( comp1 ):
                    offset = 2 if haselse and "Terminal" not in str(type(ctx.getChild(4))) else 1
                    temp = self.__instrs[-offset]
                    temp.insert(0, ("fjp %s\n" % c1))
                    temp.insert(0, instr)
                    temp.append("%s:\n" % c1)
                    instr = temp
                else:
                    offset = 2 if (haselse and "Terminal" not in str(type(ctx.getChild(4)))) else 1
                    if( haselse ):
                        instr = instr + [("fjp %s\n"%c1)] + self.__instrs[-offset] \
                            + [("ujp %s\n%s:\n"%((c2),c1))]
                    else:

                        instr = instr + [("fjp %s\n"%c1)] + self.__instrs[-offset] + [("%s:\n"%c1)]
                if( haselse ):
                    if( comp2 ):
                        temp = self.__instrs[-1]
                        temp.append("%s:\n" % c2)
                        instr = instr + temp
                    else:
                        if( "Terminal" in str(type(ctx.getChild(4))) ):
                            temp = []
                            self.__generateLoadCode(ctx.getChild(4), temp, typ, typ, 0, False)
                            instr = instr + temp + [("%s:\n"%c2)]
                        else:
                            instr = instr + self.__instrs[-1] + [("%s:\n"%c2)]
                #print ("%s:\n" % c2)
        ntnodes = ctx.getChildCount() - self.__countTerminalNodes(ctx)
        if( ntnodes > 0 ):
            self.__instrs = self.__instrs[:-ntnodes]
            self.__type = self.__type[:-ntnodes]
        self.__instrs.append(instr)
        self.__type.append("void")
        self.__exitcases.pop()
        self.__exitInitiator(ctx)
        pass

    __begincases = []

    # Enter a parse tree produced by subCParser#iteration.
    def enterIteration(self, ctx):
        self.__enterInitiator(ctx)
        if( ctx.getChild(0).getText() == "do" ):
            if( "Terminal" not in str(type(ctx.getChild(3))) ):
                self.__tyindex.append(len(self.__type))
        elif( ctx.getChild(0).getText() == "while" ):
            if( "Terminal" not in str(type(ctx.getChild(1))) ):
                self.__tyindex.append(len(self.__type))
        elif( ctx.getChild(0).getText() == "for" ):
            if( "Terminal" not in str(type(ctx.getChild(2))) ):
                self.__tyindex.append(len(self.__type))
        self.__exitcases.append(self.__l+str(self.__nrl))
        self.__begincases.append(self.__l+str(self.__nrl+1))
        self.__nrl += 2
        pass

    def __getIterationOffset4Condition(self, ctx):
        if( ctx.getChildCount > 2 ):
            loop = ctx.getChild(0).getText()
            if( loop == "do" ):
                return 1
            elif( loop == "while" ):
                if( "Terminal" in str(type(ctx.getChild(2))) ):
                    return 1
                else:
                    return 2
            elif( loop == "for" ):
                temp = 3
                temp = (temp-1) if "Terminal" in str(type(ctx.getChild(4))) else temp
                temp = (temp-1) if "Terminal" in str(type(ctx.getChild(3))) else temp
                return temp

    def __getChildTypeP(self, ctx, child):
        #for iteration's for-case
        if( "Terminal" in str(type(child)) ):
            return self.__getTypeP(self.__getType(child))
        else:
            offset = 0
            for i in reversed(range(0, ctx.getChildCount())):
                c = ctx.getChild(i)
                if( "Terminal" not in str(type(child)) ):
                    offset += 1
                if( c == child ):
                    return self.__getTypeP(self.__type[-offset])

    # Exit a parse tree produced by subCParser#iteration.
    def exitIteration(self, ctx):
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

        instr = []
        condinstr = []
        typc = self.__getTypeP(ty)
        offset = self.__getIterationOffset4Condition(ctx)
        self.__generateLoadCode(ctx.getChild(index), condinstr, typc, "b", offset, False)
        initinstr = []
        lvinstr = []
        loop = ctx.getChild(0).getText()
        if( loop == "for" ):
            ityp = self.__getChildTypeP(ctx, ctx.getChild(1))
            self.__generateLoadCode(ctx.getChild(1), initinstr, ityp, ityp, (offset+1), False)
            lvtyp = self.__getChildTypeP(ctx, ctx.getChild(3))
            self.__generateLoadCode(ctx.getChild(3), lvinstr, lvtyp, lvtyp, (offset-1), False)
        binstr = []
        blockoffs = 1 if ctx.getChild(0).getText() in ["for","while"] else 2
        blockoffs = 1 if ctx.getChild(0).getText() == "do" and "Terminal" in str(type(ctx.getChild(3))) else blockoffs
        blockindex = 1 if ctx.getChild(0).getText() != "do" else 3
        if( "Terminal" in str(type(ctx.getChild(ctx.getChildCount()-blockindex))) ):
            btyp = self.__getTypeP(self.__getType(ctx.getChild(blockindex)))
            self.__generateLoadCode(ctx.getChild(blockindex), binstr, btyp, btyp, 0, False)
        else:
            binstr = self.__instrs[-blockoffs]
        if( loop == "do" ):
            instr = [("%s:\n"%self.__begincases[-1])] + binstr + \
                    condinstr + [("not\nfjp %s\n%s:\n"%(self.__begincases[-1], self.__exitcases[-1]))]
        elif( loop == "while" ):
            instr = [("%s:\n"%self.__begincases[-1])] + condinstr + [("fjp %s\n"%self.__exitcases[-1])] + \
                    binstr + [("ujp %s\n%s:\n"%(self.__begincases[-1], self.__exitcases[-1]))]
        elif( loop == "for" ):
            skipl = (self.__l+str(self.__nrl))
            self.__nrl += 1
            instr = initinstr + [("ujp %s\n%s:\n"%(skipl,self.__begincases[-1]))] + lvinstr + [("%s:\n"%skipl)] + \
                    condinstr + [("fjp %s\n"%self.__exitcases[-1])] + binstr + \
                    [("ujp %s\n%s:\n"%(self.__begincases[-1], self.__exitcases[-1]))]
        ntnodes = ctx.getChildCount() - self.__countTerminalNodes(ctx)
        if( ntnodes > 0 ):
            self.__instrs = self.__instrs[:-ntnodes]
            self.__type = self.__type[:-ntnodes]
        self.__instrs.append(instr)
        self.__type.append("void")
        self.__exitcases.pop()
        self.__begincases.pop()
        self.__exitInitiator(ctx)
        pass


    # Enter a parse tree produced by subCParser#jump.
    def enterJump(self, ctx):
        if( ctx.getChildCount() > 0 ):
            if( ctx.getChild(0).getText() == "return" ):
                self.__enterInitiator(ctx)
            #elif goto part if we decide to implement...
        pass

    def __inCompoundsFollowedByIterationContext(self, ctx):
        temp = ctx
        while( temp.parentCtx != None ):
            if( "Compounds" in str(type(temp)) and ("Iteration" in str(type(temp.parentCtx)) or \
                    "Selection" in str(type(temp.parentCtx)) and temp.parentCtx.getChild(0).getText() == "switch") ):
                return True
            temp = temp.parentCtx
        return False

    def __nrOfCompoundsUntilIterationOrSwitch(self, ctx):
        temp = ctx
        count = 0
        while( temp.parentCtx != None and not("Iteration" in str(type(temp)) or
                ("Selection" in str(type(temp)) and temp.getChild(0).getText() == "switch"))  ):
            if( "Compounds" in str(type(temp)) ):
                count += 1
            temp = temp.parentCtx
        return count

    # Exit a parse tree produced by subCParser#jump.
    def exitJump(self, ctx):
        cc = ctx.getChildCount()
        instr = []
        if( cc > 0 ):
            if( ctx.getChild(0).getText() == "return" ):
                ty = "void"
                if( cc == 2 ):
                    expr = ctx.getChild(1)
                    if( "Terminal" in str(type(expr)) ):
                        ty = self.__getType(expr)
                    else:
                        ty = self.__type[-1]
                rtype = self.symboldict[self.__currentfunc][1]
                depth = (len(self.__parents)-1)
                if( rtype == "void" ):
                    for i in range(0, depth-1):
                        instr.append(("lda %d 0\ndec a 1\nldc i 1\nsto i\n"%i))
                    if( depth > 0 ):
                        instr.append(("lda %d 0\ndec a 1\nldc i 2\nsto i\n"%(depth-1)))
                    instr.append("retp\n")
                else:
                    typ = self.__getTypeP(ty)
                    typr = self.__getTypeP(self.symboldict[self.__currentfunc][1])
                    self.__generateLoadCode(expr, instr, typ, typr, 1, False)
                    instr.append("str %s %d 0\n"%(typr,depth))
                    for i in range(0, depth-1):
                        instr.append(("lda %d 0\ndec a 1\nldc i 1\nsto i\n"%i))
                    if( depth > 0 ):
                        instr.append(("lda %d 0\ndec a 1\nldc i 2\nsto i\n"%(depth-1)))
                        instr.append("retp\n")
                    else:
                        instr.append("retf\n")
                self.__exitInitiator(ctx)
            elif( ctx.getChild(0).getText() in ["continue","break"] ):
                if( ctx.getChild(0).getText() == "break" and len(self.__exitcases) > 0 ):
                    if( not self.__inCompoundsFollowedByIterationContext(ctx) ):
                        instr.append("ujp %s\n" % self.__exitcases[-1])
                    else:
                        depth = self.__nrOfCompoundsUntilIterationOrSwitch(ctx)
                        for i in range(0, depth):
                            instr.append(("lda %d 0\ndec a 1\nldc i 1\nsto i\n"%i))
                        instr.append("retp\n")
                elif( ctx.getChild(0).getText() == "continue" and len(self.__begincases) > 0 ):
                    if( not self.__inCompoundsFollowedByIterationContext(ctx) ):
                        instr.append("ujp %s\n" % self.__begincases[-1])
                    else:
                        instr.append("retp\n")

            #elif goto part if we decide to implement...
        ntnodes = ctx.getChildCount() - self.__countTerminalNodes(ctx)
        if( ntnodes > 0 ):
            self.__instrs = self.__instrs[:-ntnodes]
            self.__type = self.__type[:-ntnodes]
        self.__instrs.append(instr)
        self.__type.append("void")
        pass


    def __globalVariablesInit(self, ctx):
        #rearrange first nodes in order: first includes, then decls, functiondefs at last...
        incls = []
        decls = []
        fdefs = []
        terms = []
        for i in range(0, len(ctx.children)):
            child = ctx.children[i]
            if( "Include" in str(type(child)) ):
                incls.append(child)
            elif( "Decl" in str(type(child)) ):
                decls.append(child)
            elif( "Functiondef" in str(type(child)) ):
                fdefs.append(child)
            elif( "Terminal" in str(type(child)) ):
                terms.append(child)
        ctx.children = incls + decls + fdefs + terms
        return (not decls)

    # Enter a parse tree produced by subCParser#program.
    def enterProgram(self, ctx):
        self.__scopesyms = self.symboldict
        #open file or something like that?
        File = sys.argv[1].rsplit('.', 1)[0]
        self.__f = open(File+".p","w")
        self.__f.write("; This file was generated by the subC compiler.\n\n")
        noGlobDecls = self.__globalVariablesInit(ctx) #now global decls will be executed first...
        if( noGlobDecls ):
            self.__f.write("mst 0\nldc i 6\ncup 1 main\nhlt\n")
        pass

    # Exit a parse tree produced by subCParser#program.
    def exitProgram(self, ctx):
        if( self.__stdioref > 0 ):
            if( self.__stdioref in [1,3] ):
                #generate code for printf
                self.__f.write("printf:\n")
                exitcase = ((self.__l+str(self.__nrl)))
                self.__f.write("lod i 0 5\nldc i 1\nequ i\nfjp %s\n" % (self.__l+str(self.__nrl+1)))
                self.__f.write("inc a 1\ndpl a\ndec a 1\nind c\nldc c 0\nneq c\nfjp %s\n" % exitcase)
                self.__f.write("dpl a\ndec a 1\nind c\nujp %s\n" % (self.__l+str(self.__nrl+2)))
                self.__f.write("%s:\ndpl c\nldc c 0\nneq c\nfjp %s\n" % ((self.__l+str(self.__nrl+1)), exitcase))
                self.__nrl += 3
                self.__f.write("%s:\ndpl c\nldc c '%%'\nneq c\nfjp %s\n"
                        % ((self.__l+str(self.__nrl-1)), ((self.__l+str(self.__nrl)))))
                self.__f.write("out c\nujp printf\n%s:\nldc c '%%'\nneq c\n" % ((self.__l+str(self.__nrl))))
                self.__nrl += 1
                self.__f.write("fjp %s\n%s:\n" % (((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))
                self.__nrl += 1
                self.__f.write("lod i 0 5\nldc i 1\nequ i\nfjp %s\ndpl a\nind c\n%s:\n"
                        % (((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))
                self.__nrl += 1
                self.__f.write("dpl c\nldc c 'd'\nequ c\nfjp %s\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind i\nout i\n"
                        "lod i 0 6\ninc i 1\nstr i 0 6\nldc c 'd'\nequ c\nfjp %s\n"
                        "lod i 0 5\nldc i 1\nequ i\nfjp printf\ninc a 1\nujp printf\n%s:\n"
                            % (((self.__l+str(self.__nrl))),
                                ((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))
                self.__nrl += 1
                self.__f.write("dpl c\nldc c 'i'\nequ c\nfjp %s\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind i\nout i\n"
                        "lod i 0 6\ninc i 1\nstr i 0 6\nldc c 'i'\nequ c\nfjp %s\n"
                        "lod i 0 5\nldc i 1\nequ i\nfjp printf\ninc a 1\nujp printf\n%s:\n"
                            % (((self.__l+str(self.__nrl))),
                                ((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))

                self.__nrl += 1
                self.__f.write("dpl c\nldc c 'f'\nequ c\nfjp %s\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind r\nout r\n"
                        "lod i 0 6\ninc i 1\nstr i 0 6\nldc c 'f'\nequ c\nfjp %s\n"
                        "lod i 0 5\nldc i 1\nequ i\nfjp printf\ninc a 1\nujp printf\n%s:\n"
                            % (((self.__l+str(self.__nrl))),
                                ((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))
                self.__nrl += 1
                self.__f.write("dpl c\nldc c 'c'\nequ c\nfjp %s\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind c\nout c\n"
                        "lod i 0 6\ninc i 1\nstr i 0 6\nldc c 'c'\nequ c\nfjp %s\n"
                        "lod i 0 5\nldc i 1\nequ i\nfjp printf\ninc a 1\nujp printf\n%s:\n"
                            % (((self.__l+str(self.__nrl))),
                                ((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))
                self.__nrl += 1
                self.__f.write("dpl c\nldc c 's'\nequ c\nfjp %s\n"
                        "ldc i 0\nstr i 0 0\nlod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\n"
                        "%s:\ndpl a\nind a\nlod i 0 0\ndpl i\ninc i 1\nstr i 0 0\nixa 1\nind c\ndpl c\nldc c 0\nneq c\nfjp %s\n"
                        "out c\nujp %s\n%s:\nout c\nldc a 0\nequ a\nfjp %s\n%s:\n"
                        "ldc c 0\nequ c\nlod i 0 6\ninc i 1\nstr i 0 6\nfjp %s\n%s:\n"
                        "lod i 0 5\nldc i 1\nequ i\nfjp %s\ninc a 1\n%s:\nujp printf\n%s:\nout c\nujp printf\n"
                            % ((self.__l+str(self.__nrl)), (self.__l+str(self.__nrl+1)),
                                (self.__l+str(self.__nrl+2)), (self.__l+str(self.__nrl+1)),
                                (self.__l+str(self.__nrl+2)), (self.__l+str(self.__nrl+3)),
                                (self.__l+str(self.__nrl+3)), (self.__l+str(self.__nrl+4)),
                                (self.__l+str(self.__nrl+4)), (self.__l+str(self.__nrl+5)),
                                (self.__l+str(self.__nrl+5)), (self.__l+str(self.__nrl))))
                self.__nrl += 7
                self.__f.write("%s:\nretp\n" % exitcase)
            if( self.__stdioref in [2,3] ):
                #generate code for scanf
                self.__f.write("scanf:\n")
                exitcase = ((self.__l+str(self.__nrl)))
                self.__f.write("lod i 0 5\nldc i 1\nequ i\nfjp %s\n" % (self.__l+str(self.__nrl+1)))
                self.__f.write("inc a 1\ndpl a\ndec a 1\nind c\nldc c 0\nneq c\nfjp %s\n" % exitcase)
                self.__f.write("dpl a\ndec a 1\nind c\nujp %s\n" % (self.__l+str(self.__nrl+2)))
                self.__f.write("%s:\ndpl c\nldc c 0\nneq c\nfjp %s\n" % ((self.__l+str(self.__nrl+1)), exitcase))
                self.__nrl += 3
                self.__f.write("%s:\ndpl c\nldc c '%%'\nneq c\nfjp %s\n"
                        % ((self.__l+str(self.__nrl-1)), ((self.__l+str(self.__nrl)))))
                self.__f.write("out c\nujp scanf\n%s:\nldc c '%%'\nneq c\n" % ((self.__l+str(self.__nrl))))
                self.__nrl += 1
                self.__f.write("fjp %s\n%s:\n" % (((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))
                self.__nrl += 1
                self.__f.write("lod i 0 5\nldc i 1\nequ i\nfjp %s\ndpl a\nind c\n%s:\n"
                        % (((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))
                self.__nrl += 1
                self.__f.write("dpl c\nldc c 'd'\nequ c\nfjp %s\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind a\nin i\nsto i\n"
                        "lod i 0 6\ninc i 1\nstr i 0 6\nldc c 'd'\nequ c\nfjp %s\n"
                        "lod i 0 5\nldc i 1\nequ i\nfjp scanf\ninc a 1\nujp scanf\n%s:\n"
                            % (((self.__l+str(self.__nrl))),
                                ((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))
                self.__nrl += 1
                self.__f.write("dpl c\nldc c 'i'\nequ c\nfjp %s\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind a\nin i\nsto i\n"
                        "lod i 0 6\ninc i 1\nstr i 0 6\nldc c 'i'\nequ c\nfjp %s\n"
                        "lod i 0 5\nldc i 1\nequ i\nfjp scanf\ninc a 1\nujp scanf\n%s:\n"
                            % (((self.__l+str(self.__nrl))),
                                ((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))

                self.__nrl += 1
                self.__f.write("dpl c\nldc c 'f'\nequ c\nfjp %s\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind a\nin r\nsto r\n"
                        "lod i 0 6\ninc i 1\nstr i 0 6\nldc c 'f'\nequ c\nfjp %s\n"
                        "lod i 0 5\nldc i 1\nequ i\nfjp scanf\ninc a 1\nujp scanf\n%s:\n"
                            % (((self.__l+str(self.__nrl))),
                                ((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))
                self.__nrl += 1
                self.__f.write("dpl c\nldc c 'c'\nequ c\nfjp %s\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind a\nin c\nsto c\n"
                        "lod i 0 6\ninc i 1\nstr i 0 6\nldc c 'c'\nequ c\nfjp %s\n"
                        "lod i 0 5\nldc i 1\nequ i\nfjp scanf\ninc a 1\nujp scanf\n%s:\n"
                            % (((self.__l+str(self.__nrl))),
                                ((self.__l+str(self.__nrl))), ((self.__l+str(self.__nrl)))))
                self.__nrl += 1
                #what do we do here? allocate dynamic memory & assign it to the given pointer? -> probably yeah...
                #if a reference to another array goes lost, that's the user's problem...
                self.__f.write("dpl c\nldc c 's'\nequ c\nfjp %s\n"
                        "ldc i 1\nstr i 0 0\nlod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind a\n"
                        "%s:\nlod i 0 0\ndec i 1\nstr i 0 0\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind a\nldc i 1\nnew\n"
                        "dpl a\nind a\nin c\ndpl c\nldc c 27\nneq c\nfjp %s\ndpl c\nldc c 32\nles c\nfjp %s\n"
                        "conv c b\nldc b f\nand\nconv b c\ninc c 32\n%s:\nsto c\nujp %s\n%s:\n"
                        "conv c b\nldc b f\nand\nconv b c\nsto c\nind a\nconv a i\n"
                        "lod i 0 0\nsub i\nconv i a\nldc i 0\nstr i 0 3\n%s:\n"
                        "dpl a\nlod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind a\nind a\nconv a i\n"
                        "lod i 0 3\nsub i\nconv i a\nind c\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind a\nind a\nconv a i\n"
                        "lod i 0 3\nsub i\nconv i a\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind a\nind a\nconv a i\n"
                        "lod i 0 0\nsub i\nconv i a\nind c\nsto c\nsto c\n"
                        "lod i 0 0\ninc i 1\nstr i 0 0\nlod i 0 3\ndec i 1\nstr i 0 3\ndec a 1\ndpl a\n"
                        "lod i 0 6\nlda 0 0\nconv a i\nadd i\nldc i 6\nadd i\nconv i a\nind a\nind a\nconv a i\n"
                        "lod i 0 3\nsub i\nconv i a\nleq a\nfjp %s\nconv a b\nldc b f\nand\nconv b c\n"
                        "%s:\nout c\nconv c b\nldc b f\nand\nconv b c\nout c\nujp scanf\n"
                            % ((self.__l+str(self.__nrl)), (self.__l+str(self.__nrl+1)),
                                    (self.__l+str(self.__nrl+2)), (self.__l+str(self.__nrl+4)),
                                    (self.__l+str(self.__nrl+4)), (self.__l+str(self.__nrl+1)),
                                    (self.__l+str(self.__nrl+2)), (self.__l+str(self.__nrl+3)),
                                    (self.__l+str(self.__nrl+3)), (self.__l+str(self.__nrl))))
                self.__nrl += 5
                self.__f.write("%s:\nldc a 0\nstr a 0 3\nretp\n" % exitcase)
        self.__f.close()
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

        self.__f.write(("%s:\n" % self.__currentfunc))
        self.__parents.append(self.__scopesyms)
        self.__scopesyms = self.__scopesyms[self.__currentfunc][3]
        self.__funcscope = True
        self.__offaddrs.append(self.__offaddr)
        self.__offaddr = 0
        pass

    # Exit a parse tree produced by subCParser#functiondef.
    def exitFunctiondef(self, ctx):
        #if we get here it means we didn't jump back with a return statement...
        #if the return type differs from void, we got a problem...
        self.__f.write("retp\n")
        self.__currentfunc = u""
        self.__funcscope = False
        self.__scopesyms = self.__parents.pop()
        pass


    # Enter a parse tree produced by subCParser#identifier.
    def enterIdentifier(self, ctx):
        pass

    # Exit a parse tree produced by subCParser#identifier.
    def exitIdentifier(self, ctx):
        pass


