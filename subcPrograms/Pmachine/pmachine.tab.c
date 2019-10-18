/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton implementation for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "2.3"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Using locations.  */
#define YYLSP_NEEDED 0



/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     add_instr = 258,
     sub_instr = 259,
     mul_instr = 260,
     div_instr = 261,
     neg_instr = 262,
     and_instr = 263,
     or_instr = 264,
     not_instr = 265,
     equ_instr = 266,
     geq_instr = 267,
     leq_instr = 268,
     les_instr = 269,
     grt_instr = 270,
     neq_instr = 271,
     ldo_instr = 272,
     ldc_instr = 273,
     ind_instr = 274,
     sro_instr = 275,
     sto_instr = 276,
     ujp_instr = 277,
     fjp_instr = 278,
     ixj_instr = 279,
     ixa_instr = 280,
     inc_instr = 281,
     dec_instr = 282,
     chk_instr = 283,
     dpl_instr = 284,
     ldd_instr = 285,
     sli_instr = 286,
     new_instr = 287,
     lod_instr = 288,
     lda_instr = 289,
     str_instr = 290,
     mst_instr = 291,
     cup_instr = 292,
     ssp_instr = 293,
     sep_instr = 294,
     ent_instr = 295,
     retf_instr = 296,
     retp_instr = 297,
     movs_instr = 298,
     movd_instr = 299,
     smp_instr = 300,
     cupi_instr = 301,
     mstf_instr = 302,
     hlt_instr = 303,
     inp_instr = 304,
     out_instr = 305,
     conv_instr = 306,
     BLANK = 307,
     endline = 308,
     boolean_specifier = 309,
     real_specifier = 310,
     integer_specifier = 311,
     character_specifier = 312,
     address_specifier = 313,
     boolvalue = 314,
     integervalue = 315,
     charactervalue = 316,
     realvalue = 317,
     addressvalue = 318,
     appliedlabel = 319,
     defininglabel = 320
   };
#endif
/* Tokens.  */
#define add_instr 258
#define sub_instr 259
#define mul_instr 260
#define div_instr 261
#define neg_instr 262
#define and_instr 263
#define or_instr 264
#define not_instr 265
#define equ_instr 266
#define geq_instr 267
#define leq_instr 268
#define les_instr 269
#define grt_instr 270
#define neq_instr 271
#define ldo_instr 272
#define ldc_instr 273
#define ind_instr 274
#define sro_instr 275
#define sto_instr 276
#define ujp_instr 277
#define fjp_instr 278
#define ixj_instr 279
#define ixa_instr 280
#define inc_instr 281
#define dec_instr 282
#define chk_instr 283
#define dpl_instr 284
#define ldd_instr 285
#define sli_instr 286
#define new_instr 287
#define lod_instr 288
#define lda_instr 289
#define str_instr 290
#define mst_instr 291
#define cup_instr 292
#define ssp_instr 293
#define sep_instr 294
#define ent_instr 295
#define retf_instr 296
#define retp_instr 297
#define movs_instr 298
#define movd_instr 299
#define smp_instr 300
#define cupi_instr 301
#define mstf_instr 302
#define hlt_instr 303
#define inp_instr 304
#define out_instr 305
#define conv_instr 306
#define BLANK 307
#define endline 308
#define boolean_specifier 309
#define real_specifier 310
#define integer_specifier 311
#define character_specifier 312
#define address_specifier 313
#define boolvalue 314
#define integervalue 315
#define charactervalue 316
#define realvalue 317
#define addressvalue 318
#define appliedlabel 319
#define defininglabel 320




/* Copy the first part of user declarations.  */
#line 1 "pmachine.y"

#include <string>
using namespace std;

#include "stackelement.h"
#include "stackmachine.h"
#include "pmachine.h"

#include "add.h"
#include "sub.h"
#include "mul.h"
#include "div.h"
#include "neg.h"
#include "and.h"
#include "or.h"
#include "not.h"
#include "equ.h"
#include "geq.h"
#include "leq.h"
#include "les.h"
#include "grt.h"
#include "neq.h"
#include "ldo.h"
#include "ldc.h"
#include "ind.h"
#include "sro.h"
#include "sto.h"
#include "ujp.h"
#include "fjp.h"
#include "ixj.h"
#include "ixa.h"
#include "inc.h"
#include "dec.h"
#include "chk.h"
#include "dpl.h"
#include "ldd.h"
#include "sli.h"
#include "new.h"
#include "lod.h"
#include "lda.h"
#include "str.h"
#include "mst.h"
#include "cup.h"
#include "ssp.h"
#include "sep.h"
#include "ent.h"
#include "retf.h"
#include "retp.h"
#include "movs.h"
#include "movd.h"
#include "smp.h"
#include "cupi.h"
#include "mstf.h"
#include "hlt.h"
#include "in.h"
#include "out.h"
#include "conv.h"

//#define YACCOUTPUT


extern StackMachine Pmachine;
extern int linecount;
extern int yylex();

// prototypes
void yyerror(string msg);




/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* Enabling the token table.  */
#ifndef YYTOKEN_TABLE
# define YYTOKEN_TABLE 0
#endif

#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 71 "pmachine.y"
{
	int integernumbervalue;
	double realnumbervalue;
	bool booleanvalue;
	string *textvalue;
	char charvalue;
	enum Stacktypes {r, i, b, c, a} type;
}
/* Line 193 of yacc.c.  */
#line 306 "pmachine.tab.c"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif



/* Copy the second part of user declarations.  */


/* Line 216 of yacc.c.  */
#line 319 "pmachine.tab.c"

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#elif (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
typedef signed char yytype_int8;
#else
typedef short int yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(msgid) dgettext ("bison-runtime", msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(msgid) msgid
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(e) ((void) (e))
#else
# define YYUSE(e) /* empty */
#endif

/* Identity function, used to suppress warnings about constant conditions.  */
#ifndef lint
# define YYID(n) (n)
#else
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static int
YYID (int i)
#else
static int
YYID (i)
    int i;
#endif
{
  return i;
}
#endif

#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#     ifndef _STDLIB_H
#      define _STDLIB_H 1
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's `empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (YYID (0))
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined _STDLIB_H \
       && ! ((defined YYMALLOC || defined malloc) \
	     && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef _STDLIB_H
#    define _STDLIB_H 1
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
	 || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss;
  YYSTYPE yyvs;
  };

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

/* Copy COUNT objects from FROM to TO.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(To, From, Count) \
      __builtin_memcpy (To, From, (Count) * sizeof (*(From)))
#  else
#   define YYCOPY(To, From, Count)		\
      do					\
	{					\
	  YYSIZE_T yyi;				\
	  for (yyi = 0; yyi < (Count); yyi++)	\
	    (To)[yyi] = (From)[yyi];		\
	}					\
      while (YYID (0))
#  endif
# endif

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack)					\
    do									\
      {									\
	YYSIZE_T yynewbytes;						\
	YYCOPY (&yyptr->Stack, Stack, yysize);				\
	Stack = &yyptr->Stack;						\
	yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
	yyptr += yynewbytes / sizeof (*yyptr);				\
      }									\
    while (YYID (0))

#endif

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  191
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   350

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  66
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  58
/* YYNRULES -- Number of rules.  */
#define YYNRULES  172
/* YYNRULES -- Number of states.  */
#define YYNSTATES  300

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   320

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint16 yyprhs[] =
{
       0,     0,     3,     4,     6,     9,    11,    15,    18,    20,
      22,    24,    26,    28,    30,    32,    34,    36,    38,    40,
      42,    44,    46,    48,    50,    52,    54,    56,    58,    60,
      62,    64,    66,    68,    70,    72,    74,    76,    78,    80,
      82,    84,    86,    88,    90,    92,    94,    96,    98,   100,
     102,   104,   106,   108,   110,   112,   114,   116,   118,   120,
     122,   124,   126,   128,   130,   132,   135,   137,   141,   144,
     148,   151,   155,   158,   162,   165,   169,   172,   174,   176,
     178,   182,   185,   189,   192,   196,   199,   203,   206,   210,
     213,   217,   220,   226,   229,   235,   241,   247,   253,   259,
     265,   268,   272,   275,   281,   284,   288,   291,   295,   298,
     302,   305,   309,   312,   316,   319,   325,   328,   334,   337,
     343,   346,   350,   353,   357,   360,   364,   367,   369,   377,
     380,   386,   389,   397,   400,   404,   407,   413,   416,   420,
     423,   427,   430,   436,   439,   441,   443,   447,   450,   454,
     457,   461,   464,   470,   473,   479,   482,   484,   488,   492,
     496,   500,   504,   507,   513,   517,   521,   525,   529,   533,
     536,   542,   545
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int8 yyrhs[] =
{
      67,     0,    -1,    -1,    69,    -1,    68,    53,    -1,    53,
      -1,    69,    70,    68,    -1,    70,    68,    -1,    68,    -1,
      74,    -1,    75,    -1,    76,    -1,    77,    -1,    78,    -1,
      79,    -1,    80,    -1,    81,    -1,    82,    -1,    83,    -1,
      84,    -1,    85,    -1,    86,    -1,    87,    -1,    88,    -1,
      89,    -1,    90,    -1,    91,    -1,    92,    -1,    93,    -1,
      94,    -1,    95,    -1,    96,    -1,    97,    -1,    98,    -1,
      99,    -1,   100,    -1,   101,    -1,   102,    -1,   103,    -1,
     104,    -1,   105,    -1,   106,    -1,   107,    -1,   108,    -1,
     109,    -1,   110,    -1,   111,    -1,   112,    -1,   113,    -1,
     114,    -1,   115,    -1,   116,    -1,   117,    -1,   118,    -1,
     119,    -1,   120,    -1,   121,    -1,   122,    -1,   123,    -1,
      55,    -1,    56,    -1,    71,    -1,    54,    -1,    57,    -1,
      58,    -1,    52,    73,    -1,    52,    -1,     3,    73,    71,
      -1,     3,     1,    -1,     4,    73,    71,    -1,     4,     1,
      -1,     5,    73,    71,    -1,     5,     1,    -1,     6,    73,
      71,    -1,     6,     1,    -1,     7,    73,    71,    -1,     7,
       1,    -1,     8,    -1,     9,    -1,    10,    -1,    11,    73,
      72,    -1,    11,     1,    -1,    12,    73,    72,    -1,    12,
       1,    -1,    13,    73,    72,    -1,    13,     1,    -1,    14,
      73,    72,    -1,    14,     1,    -1,    15,    73,    72,    -1,
      15,     1,    -1,    16,    73,    72,    -1,    16,     1,    -1,
      17,    73,    72,    73,    60,    -1,    17,     1,    -1,    18,
      73,    55,    73,    62,    -1,    18,    73,    56,    73,    60,
      -1,    18,    73,    54,    73,    59,    -1,    18,    73,    57,
      73,    60,    -1,    18,    73,    57,    73,    61,    -1,    18,
      73,    58,    73,    60,    -1,    18,     1,    -1,    19,    73,
      72,    -1,    19,     1,    -1,    20,    73,    72,    73,    60,
      -1,    20,     1,    -1,    21,    73,    72,    -1,    21,     1,
      -1,    22,    73,    64,    -1,    22,     1,    -1,    23,    73,
      64,    -1,    23,     1,    -1,    24,    73,    64,    -1,    24,
       1,    -1,    25,    73,    60,    -1,    25,     1,    -1,    26,
      73,    72,    73,    60,    -1,    26,     1,    -1,    27,    73,
      72,    73,    60,    -1,    27,     1,    -1,    28,    73,    60,
      73,    60,    -1,    28,     1,    -1,    29,    73,    72,    -1,
      29,     1,    -1,    30,    73,    60,    -1,    30,     1,    -1,
      31,    73,    72,    -1,    31,     1,    -1,    32,    -1,    33,
      73,    72,    73,    60,    73,    60,    -1,    33,     1,    -1,
      34,    73,    60,    73,    60,    -1,    34,     1,    -1,    35,
      73,    72,    73,    60,    73,    60,    -1,    35,     1,    -1,
      36,    73,    60,    -1,    36,     1,    -1,    37,    73,    60,
      73,    64,    -1,    37,     1,    -1,    38,    73,    60,    -1,
      38,     1,    -1,    39,    73,    60,    -1,    39,     1,    -1,
      40,    73,    60,    73,    60,    -1,    40,     1,    -1,    41,
      -1,    42,    -1,    43,    73,    60,    -1,    43,     1,    -1,
      44,    73,    60,    -1,    44,     1,    -1,    45,    73,    60,
      -1,    45,     1,    -1,    46,    73,    60,    73,    60,    -1,
      46,     1,    -1,    47,    73,    60,    73,    60,    -1,    47,
       1,    -1,    48,    -1,    49,    73,    56,    -1,    49,    73,
      55,    -1,    49,    73,    54,    -1,    49,    73,    57,    -1,
      49,    73,    58,    -1,    49,     1,    -1,    50,    73,    55,
      73,    56,    -1,    50,    73,    55,    -1,    50,    73,    56,
      -1,    50,    73,    57,    -1,    50,    73,    58,    -1,    50,
      73,    54,    -1,    50,     1,    -1,    51,    73,    72,    73,
      72,    -1,    51,     1,    -1,    65,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   156,   156,   157,   159,   160,   162,   163,   164,   166,
     172,   178,   184,   190,   196,   202,   208,   214,   220,   226,
     232,   238,   244,   250,   256,   262,   268,   274,   280,   286,
     292,   298,   304,   310,   316,   322,   328,   334,   340,   346,
     352,   358,   364,   370,   376,   382,   388,   394,   400,   406,
     412,   418,   424,   430,   436,   442,   448,   454,   460,   467,
     471,   476,   477,   481,   485,   490,   491,   493,   505,   510,
     522,   527,   539,   545,   557,   562,   574,   579,   584,   589,
     594,   615,   620,   641,   646,   667,   672,   693,   698,   719,
     724,   745,   750,   771,   776,   780,   784,   788,   792,   796,
     800,   805,   827,   832,   853,   858,   879,   884,   888,   893,
     897,   902,   906,   911,   915,   920,   941,   946,   967,   972,
     976,   981,  1002,  1007,  1011,  1016,  1037,  1042,  1047,  1068,
    1074,  1078,  1083,  1104,  1109,  1113,  1118,  1122,  1127,  1131,
    1136,  1140,  1145,  1149,  1154,  1159,  1164,  1168,  1173,  1177,
    1182,  1186,  1191,  1195,  1200,  1204,  1209,  1214,  1218,  1222,
    1226,  1230,  1234,  1239,  1243,  1247,  1251,  1255,  1259,  1263,
    1268,  1309,  1313
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "add_instr", "sub_instr", "mul_instr",
  "div_instr", "neg_instr", "and_instr", "or_instr", "not_instr",
  "equ_instr", "geq_instr", "leq_instr", "les_instr", "grt_instr",
  "neq_instr", "ldo_instr", "ldc_instr", "ind_instr", "sro_instr",
  "sto_instr", "ujp_instr", "fjp_instr", "ixj_instr", "ixa_instr",
  "inc_instr", "dec_instr", "chk_instr", "dpl_instr", "ldd_instr",
  "sli_instr", "new_instr", "lod_instr", "lda_instr", "str_instr",
  "mst_instr", "cup_instr", "ssp_instr", "sep_instr", "ent_instr",
  "retf_instr", "retp_instr", "movs_instr", "movd_instr", "smp_instr",
  "cupi_instr", "mstf_instr", "hlt_instr", "inp_instr", "out_instr",
  "conv_instr", "BLANK", "endline", "boolean_specifier", "real_specifier",
  "integer_specifier", "character_specifier", "address_specifier",
  "boolvalue", "integervalue", "charactervalue", "realvalue",
  "addressvalue", "appliedlabel", "defininglabel", "$accept", "Grammar",
  "EndlineRepeater", "InstructionSequence", "Instruction", "numeric",
  "arbitrary", "space", "add_instruction", "sub_instruction",
  "mul_instruction", "div_instruction", "neg_instruction",
  "and_instruction", "or_instruction", "not_instruction",
  "equ_instruction", "geq_instruction", "leq_instruction",
  "les_instruction", "grt_instruction", "neq_instruction",
  "ldo_instruction", "ldc_instruction", "ind_instruction",
  "sro_instruction", "sto_instruction", "ujp_instruction",
  "fjp_instruction", "ixj_instruction", "ixa_instruction",
  "inc_instruction", "dec_instruction", "chk_instruction",
  "dpl_instruction", "ldd_instruction", "sli_instruction",
  "new_instruction", "lod_instruction", "lda_instruction",
  "str_instruction", "mst_instruction", "cup_instruction",
  "ssp_instruction", "sep_instruction", "ent_instruction",
  "retf_instruction", "retp_instruction", "movs_instruction",
  "movd_instruction", "smp_instruction", "cupi_instruction",
  "mstf_instruction", "hlt_instruction", "inp_instruction",
  "out_instruction", "conv_instruction", "label_introduction", 0
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[YYLEX-NUM] -- Internal token number corresponding to
   token YYLEX-NUM.  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
     315,   316,   317,   318,   319,   320
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    66,    67,    67,    68,    68,    69,    69,    69,    70,
      70,    70,    70,    70,    70,    70,    70,    70,    70,    70,
      70,    70,    70,    70,    70,    70,    70,    70,    70,    70,
      70,    70,    70,    70,    70,    70,    70,    70,    70,    70,
      70,    70,    70,    70,    70,    70,    70,    70,    70,    70,
      70,    70,    70,    70,    70,    70,    70,    70,    70,    71,
      71,    72,    72,    72,    72,    73,    73,    74,    74,    75,
      75,    76,    76,    77,    77,    78,    78,    79,    80,    81,
      82,    82,    83,    83,    84,    84,    85,    85,    86,    86,
      87,    87,    88,    88,    89,    89,    89,    89,    89,    89,
      89,    90,    90,    91,    91,    92,    92,    93,    93,    94,
      94,    95,    95,    96,    96,    97,    97,    98,    98,    99,
      99,   100,   100,   101,   101,   102,   102,   103,   104,   104,
     105,   105,   106,   106,   107,   107,   108,   108,   109,   109,
     110,   110,   111,   111,   112,   113,   114,   114,   115,   115,
     116,   116,   117,   117,   118,   118,   119,   120,   120,   120,
     120,   120,   120,   121,   121,   121,   121,   121,   121,   121,
     122,   122,   123
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     0,     1,     2,     1,     3,     2,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     2,     1,     3,     2,     3,
       2,     3,     2,     3,     2,     3,     2,     1,     1,     1,
       3,     2,     3,     2,     3,     2,     3,     2,     3,     2,
       3,     2,     5,     2,     5,     5,     5,     5,     5,     5,
       2,     3,     2,     5,     2,     3,     2,     3,     2,     3,
       2,     3,     2,     3,     2,     5,     2,     5,     2,     5,
       2,     3,     2,     3,     2,     3,     2,     1,     7,     2,
       5,     2,     7,     2,     3,     2,     5,     2,     3,     2,
       3,     2,     5,     2,     1,     1,     3,     2,     3,     2,
       3,     2,     5,     2,     5,     2,     1,     3,     3,     3,
       3,     3,     2,     5,     3,     3,     3,     3,     3,     2,
       5,     2,     1
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       2,     0,     0,     0,     0,     0,    77,    78,    79,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,     0,     0,   144,
     145,     0,     0,     0,     0,     0,   156,     0,     0,     0,
       5,   172,     0,     8,     3,     0,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    18,    19,    20,    21,    22,
      23,    24,    25,    26,    27,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    51,    52,
      53,    54,    55,    56,    57,    58,    68,    66,     0,    70,
       0,    72,     0,    74,     0,    76,     0,    81,     0,    83,
       0,    85,     0,    87,     0,    89,     0,    91,     0,    93,
       0,   100,     0,   102,     0,   104,     0,   106,     0,   108,
       0,   110,     0,   112,     0,   114,     0,   116,     0,   118,
       0,   120,     0,   122,     0,   124,     0,   126,     0,   129,
       0,   131,     0,   133,     0,   135,     0,   137,     0,   139,
       0,   141,     0,   143,     0,   147,     0,   149,     0,   151,
       0,   153,     0,   155,     0,   162,     0,   169,     0,   171,
       0,     1,     4,     0,     7,    65,    59,    60,    67,    69,
      71,    73,    75,    62,    63,    64,    61,    80,    82,    84,
      86,    88,    90,     0,     0,     0,     0,     0,     0,   101,
       0,   105,   107,   109,   111,   113,     0,     0,     0,   121,
     123,   125,     0,     0,     0,   134,     0,   138,   140,     0,
     146,   148,   150,     0,     0,   159,   158,   157,   160,   161,
     168,   164,   165,   166,   167,     0,     6,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    92,    96,    94,    95,
      97,    98,    99,   103,   115,   117,   119,     0,   130,     0,
     136,   142,   152,   154,   163,   170,     0,     0,   128,   132
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,    52,    53,    54,    55,   206,   207,   108,    56,    57,
      58,    59,    60,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    87,
      88,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      98,    99,   100,   101,   102,   103,   104,   105
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -73
static const yytype_int16 yypact[] =
{
     140,     5,    27,    37,    43,    48,   -73,   -73,   -73,    50,
      52,    54,    58,    59,    60,    62,    64,    67,    68,    69,
      70,    71,    72,    73,    74,    76,    79,    80,    82,    83,
     -73,    84,    86,    89,   191,   193,   194,   195,   196,   -73,
     -73,   198,   199,   200,   203,   205,   -73,   206,   207,   208,
     -73,   -73,    91,   -48,   285,   -16,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,    15,    38,   -73,
      38,   -73,    38,   -73,    38,   -73,    38,   -73,   165,   -73,
     165,   -73,   165,   -73,   165,   -73,   165,   -73,   165,   -73,
     165,   -73,   216,   -73,   165,   -73,   165,   -73,   165,   -73,
      34,   -73,    35,   -73,    39,   -73,    41,   -73,   165,   -73,
     165,   -73,    47,   -73,   165,   -73,    49,   -73,   165,   -73,
     165,   -73,    53,   -73,   165,   -73,    55,   -73,    57,   -73,
      77,   -73,   138,   -73,   142,   -73,   150,   -73,   157,   -73,
     167,   -73,   168,   -73,   169,   -73,   221,   -73,   226,   -73,
     165,   -73,   -73,   -16,   -48,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,    15,    15,    15,    15,    15,    15,   -73,
      15,   -73,   -73,   -73,   -73,   -73,    15,    15,    15,   -73,
     -73,   -73,    15,    15,    15,   -73,    15,   -73,   -73,    15,
     -73,   -73,   -73,    15,    15,   -73,   -73,   -73,   -73,   -73,
     -73,    15,   -73,   -73,   -73,    15,   -48,   173,    81,    46,
     175,    36,   176,   178,   179,   180,   184,   202,   204,   277,
      63,   278,   279,   280,   210,   165,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,    15,   -73,    15,
     -73,   -73,   -73,   -73,   -73,   -73,   281,   282,   -73,   -73
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
     -73,   -73,   -51,   -73,    75,   153,   -72,    -2,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -1
static const yytype_uint16 yytable[] =
{
     110,   112,   114,   116,   194,   192,   106,   118,   120,   122,
     124,   126,   128,   130,   132,   134,   136,   138,   140,   142,
     144,   146,   148,   150,   152,   154,   156,   158,   109,   160,
     162,   164,   166,   168,   170,   172,   174,    50,   111,   176,
     178,   180,   182,   184,   113,   186,   188,   190,   208,   115,
     209,   117,   210,   119,   211,   121,   212,   107,   213,   123,
     125,   127,   219,   129,   220,   131,   221,   107,   133,   135,
     137,   139,   141,   143,   145,   147,   226,   149,   227,   107,
     151,   153,   229,   155,   157,   159,   231,   161,   232,   107,
     163,   191,   234,   196,   197,   107,   280,   281,   222,   223,
     107,   225,   107,   224,   107,   195,   107,   228,   278,   230,
     107,   107,   107,   233,   107,   235,   107,   236,   255,   107,
     107,   107,   107,   107,   107,   107,   107,   290,   107,   193,
       0,   107,   107,     0,   107,   107,   107,   237,   107,     0,
     277,   107,   256,     1,     2,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      18,    19,    20,    21,    22,    23,    24,    25,    26,    27,
      28,    29,    30,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,    41,    42,    43,    44,    45,    46,    47,
      48,    49,   165,    50,   167,   169,   171,   173,   238,   175,
     177,   179,   239,   295,   181,    51,   183,   185,   187,   189,
     240,   257,   258,   259,   260,   261,   262,   241,   263,   203,
     196,   197,   204,   205,   264,   265,   266,   242,   243,   244,
     267,   268,   269,   276,   270,   279,   282,   271,   283,   284,
     285,   272,   273,   107,   286,   107,   107,   107,   107,   274,
     107,   107,   107,   275,     0,   107,     0,   107,   107,   107,
     107,   198,   287,   199,   288,   200,   294,   201,     0,   202,
     214,   215,   216,   217,   218,   245,   246,   247,   248,   249,
     250,   251,   252,   253,   254,   296,     0,   297,     1,     2,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    18,    19,    20,    21,    22,
      23,    24,    25,    26,    27,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,    41,    42,
      43,    44,    45,    46,    47,    48,    49,   289,   291,   292,
     293,   298,   299,     0,     0,     0,     0,     0,     0,     0,
      51
};

static const yytype_int16 yycheck[] =
{
       2,     3,     4,     5,    55,    53,     1,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,    28,    29,     1,    31,
      32,    33,    34,    35,    36,    37,    38,    53,     1,    41,
      42,    43,    44,    45,     1,    47,    48,    49,   120,     1,
     122,     1,   124,     1,   126,     1,   128,    52,   130,     1,
       1,     1,   134,     1,   136,     1,   138,    52,     1,     1,
       1,     1,     1,     1,     1,     1,   148,     1,   150,    52,
       1,     1,   154,     1,     1,     1,   158,     1,   160,    52,
       1,     0,   164,    55,    56,    52,    60,    61,    64,    64,
      52,    60,    52,    64,    52,   107,    52,    60,    62,    60,
      52,    52,    52,    60,    52,    60,    52,    60,   190,    52,
      52,    52,    52,    52,    52,    52,    52,    64,    52,    54,
      -1,    52,    52,    -1,    52,    52,    52,    60,    52,    -1,
      59,    52,   193,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,     1,    53,     1,     1,     1,     1,    60,     1,
       1,     1,    60,   275,     1,    65,     1,     1,     1,     1,
      60,   213,   214,   215,   216,   217,   218,    60,   220,    54,
      55,    56,    57,    58,   226,   227,   228,    60,    60,    60,
     232,   233,   234,    60,   236,    60,    60,   239,    60,    60,
      60,   243,   244,    52,    60,    52,    52,    52,    52,   251,
      52,    52,    52,   255,    -1,    52,    -1,    52,    52,    52,
      52,   108,    60,   110,    60,   112,    56,   114,    -1,   116,
      54,    55,    56,    57,    58,    54,    55,    56,    57,    58,
      54,    55,    56,    57,    58,   287,    -1,   289,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    60,    60,    60,
      60,    60,    60,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      65
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,    41,
      42,    43,    44,    45,    46,    47,    48,    49,    50,    51,
      53,    65,    67,    68,    69,    70,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    87,
      88,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      98,    99,   100,   101,   102,   103,   104,   105,   106,   107,
     108,   109,   110,   111,   112,   113,   114,   115,   116,   117,
     118,   119,   120,   121,   122,   123,     1,    52,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     0,    53,    70,    68,    73,    55,    56,    71,    71,
      71,    71,    71,    54,    57,    58,    71,    72,    72,    72,
      72,    72,    72,    72,    54,    55,    56,    57,    58,    72,
      72,    72,    64,    64,    64,    60,    72,    72,    60,    72,
      60,    72,    72,    60,    72,    60,    60,    60,    60,    60,
      60,    60,    60,    60,    60,    54,    55,    56,    57,    58,
      54,    55,    56,    57,    58,    72,    68,    73,    73,    73,
      73,    73,    73,    73,    73,    73,    73,    73,    73,    73,
      73,    73,    73,    73,    73,    73,    60,    59,    62,    60,
      60,    61,    60,    60,    60,    60,    60,    60,    60,    60,
      64,    60,    60,    60,    56,    72,    73,    73,    60,    60
};

#define yyerrok		(yyerrstatus = 0)
#define yyclearin	(yychar = YYEMPTY)
#define YYEMPTY		(-2)
#define YYEOF		0

#define YYACCEPT	goto yyacceptlab
#define YYABORT		goto yyabortlab
#define YYERROR		goto yyerrorlab


/* Like YYERROR except do call yyerror.  This remains here temporarily
   to ease the transition to the new meaning of YYERROR, for GCC.
   Once GCC version 2 has supplanted version 1, this can go.  */

#define YYFAIL		goto yyerrlab

#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)					\
do								\
  if (yychar == YYEMPTY && yylen == 1)				\
    {								\
      yychar = (Token);						\
      yylval = (Value);						\
      yytoken = YYTRANSLATE (yychar);				\
      YYPOPSTACK (1);						\
      goto yybackup;						\
    }								\
  else								\
    {								\
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;							\
    }								\
while (YYID (0))


#define YYTERROR	1
#define YYERRCODE	256


/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#define YYRHSLOC(Rhs, K) ((Rhs)[K])
#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)				\
    do									\
      if (YYID (N))                                                    \
	{								\
	  (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;	\
	  (Current).first_column = YYRHSLOC (Rhs, 1).first_column;	\
	  (Current).last_line    = YYRHSLOC (Rhs, N).last_line;		\
	  (Current).last_column  = YYRHSLOC (Rhs, N).last_column;	\
	}								\
      else								\
	{								\
	  (Current).first_line   = (Current).last_line   =		\
	    YYRHSLOC (Rhs, 0).last_line;				\
	  (Current).first_column = (Current).last_column =		\
	    YYRHSLOC (Rhs, 0).last_column;				\
	}								\
    while (YYID (0))
#endif


/* YY_LOCATION_PRINT -- Print the location on the stream.
   This macro was not mandated originally: define only if we know
   we won't break user code: when these are the locations we know.  */

#ifndef YY_LOCATION_PRINT
# if defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL
#  define YY_LOCATION_PRINT(File, Loc)			\
     fprintf (File, "%d.%d-%d.%d",			\
	      (Loc).first_line, (Loc).first_column,	\
	      (Loc).last_line,  (Loc).last_column)
# else
#  define YY_LOCATION_PRINT(File, Loc) ((void) 0)
# endif
#endif


/* YYLEX -- calling `yylex' with the right arguments.  */

#ifdef YYLEX_PARAM
# define YYLEX yylex (YYLEX_PARAM)
#else
# define YYLEX yylex ()
#endif

/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)			\
do {						\
  if (yydebug)					\
    YYFPRINTF Args;				\
} while (YYID (0))

# define YY_SYMBOL_PRINT(Title, Type, Value, Location)			  \
do {									  \
  if (yydebug)								  \
    {									  \
      YYFPRINTF (stderr, "%s ", Title);					  \
      yy_symbol_print (stderr,						  \
		  Type, Value); \
      YYFPRINTF (stderr, "\n");						  \
    }									  \
} while (YYID (0))


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_value_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# else
  YYUSE (yyoutput);
# endif
  switch (yytype)
    {
      default:
	break;
    }
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (yytype < YYNTOKENS)
    YYFPRINTF (yyoutput, "token %s (", yytname[yytype]);
  else
    YYFPRINTF (yyoutput, "nterm %s (", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_stack_print (yytype_int16 *bottom, yytype_int16 *top)
#else
static void
yy_stack_print (bottom, top)
    yytype_int16 *bottom;
    yytype_int16 *top;
#endif
{
  YYFPRINTF (stderr, "Stack now");
  for (; bottom <= top; ++bottom)
    YYFPRINTF (stderr, " %d", *bottom);
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)				\
do {								\
  if (yydebug)							\
    yy_stack_print ((Bottom), (Top));				\
} while (YYID (0))


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_reduce_print (YYSTYPE *yyvsp, int yyrule)
#else
static void
yy_reduce_print (yyvsp, yyrule)
    YYSTYPE *yyvsp;
    int yyrule;
#endif
{
  int yynrhs = yyr2[yyrule];
  int yyi;
  unsigned long int yylno = yyrline[yyrule];
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
	     yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      fprintf (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr, yyrhs[yyprhs[yyrule] + yyi],
		       &(yyvsp[(yyi + 1) - (yynrhs)])
		       		       );
      fprintf (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)		\
do {					\
  if (yydebug)				\
    yy_reduce_print (yyvsp, Rule); \
} while (YYID (0))

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef	YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif



#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static YYSIZE_T
yystrlen (const char *yystr)
#else
static YYSIZE_T
yystrlen (yystr)
    const char *yystr;
#endif
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static char *
yystpcpy (char *yydest, const char *yysrc)
#else
static char *
yystpcpy (yydest, yysrc)
    char *yydest;
    const char *yysrc;
#endif
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
	switch (*++yyp)
	  {
	  case '\'':
	  case ',':
	    goto do_not_strip_quotes;

	  case '\\':
	    if (*++yyp != '\\')
	      goto do_not_strip_quotes;
	    /* Fall through.  */
	  default:
	    if (yyres)
	      yyres[yyn] = *yyp;
	    yyn++;
	    break;

	  case '"':
	    if (yyres)
	      yyres[yyn] = '\0';
	    return yyn;
	  }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into YYRESULT an error message about the unexpected token
   YYCHAR while in state YYSTATE.  Return the number of bytes copied,
   including the terminating null byte.  If YYRESULT is null, do not
   copy anything; just return the number of bytes that would be
   copied.  As a special case, return 0 if an ordinary "syntax error"
   message will do.  Return YYSIZE_MAXIMUM if overflow occurs during
   size calculation.  */
static YYSIZE_T
yysyntax_error (char *yyresult, int yystate, int yychar)
{
  int yyn = yypact[yystate];

  if (! (YYPACT_NINF < yyn && yyn <= YYLAST))
    return 0;
  else
    {
      int yytype = YYTRANSLATE (yychar);
      YYSIZE_T yysize0 = yytnamerr (0, yytname[yytype]);
      YYSIZE_T yysize = yysize0;
      YYSIZE_T yysize1;
      int yysize_overflow = 0;
      enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
      char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
      int yyx;

# if 0
      /* This is so xgettext sees the translatable formats that are
	 constructed on the fly.  */
      YY_("syntax error, unexpected %s");
      YY_("syntax error, unexpected %s, expecting %s");
      YY_("syntax error, unexpected %s, expecting %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s");
# endif
      char *yyfmt;
      char const *yyf;
      static char const yyunexpected[] = "syntax error, unexpected %s";
      static char const yyexpecting[] = ", expecting %s";
      static char const yyor[] = " or %s";
      char yyformat[sizeof yyunexpected
		    + sizeof yyexpecting - 1
		    + ((YYERROR_VERBOSE_ARGS_MAXIMUM - 2)
		       * (sizeof yyor - 1))];
      char const *yyprefix = yyexpecting;

      /* Start YYX at -YYN if negative to avoid negative indexes in
	 YYCHECK.  */
      int yyxbegin = yyn < 0 ? -yyn : 0;

      /* Stay within bounds of both yycheck and yytname.  */
      int yychecklim = YYLAST - yyn + 1;
      int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
      int yycount = 1;

      yyarg[0] = yytname[yytype];
      yyfmt = yystpcpy (yyformat, yyunexpected);

      for (yyx = yyxbegin; yyx < yyxend; ++yyx)
	if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR)
	  {
	    if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
	      {
		yycount = 1;
		yysize = yysize0;
		yyformat[sizeof yyunexpected - 1] = '\0';
		break;
	      }
	    yyarg[yycount++] = yytname[yyx];
	    yysize1 = yysize + yytnamerr (0, yytname[yyx]);
	    yysize_overflow |= (yysize1 < yysize);
	    yysize = yysize1;
	    yyfmt = yystpcpy (yyfmt, yyprefix);
	    yyprefix = yyor;
	  }

      yyf = YY_(yyformat);
      yysize1 = yysize + yystrlen (yyf);
      yysize_overflow |= (yysize1 < yysize);
      yysize = yysize1;

      if (yysize_overflow)
	return YYSIZE_MAXIMUM;

      if (yyresult)
	{
	  /* Avoid sprintf, as that infringes on the user's name space.
	     Don't have undefined behavior even if the translation
	     produced a string with the wrong number of "%s"s.  */
	  char *yyp = yyresult;
	  int yyi = 0;
	  while ((*yyp = *yyf) != '\0')
	    {
	      if (*yyp == '%' && yyf[1] == 's' && yyi < yycount)
		{
		  yyp += yytnamerr (yyp, yyarg[yyi++]);
		  yyf += 2;
		}
	      else
		{
		  yyp++;
		  yyf++;
		}
	    }
	}
      return yysize;
    }
}
#endif /* YYERROR_VERBOSE */


/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
#else
static void
yydestruct (yymsg, yytype, yyvaluep)
    const char *yymsg;
    int yytype;
    YYSTYPE *yyvaluep;
#endif
{
  YYUSE (yyvaluep);

  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  switch (yytype)
    {

      default:
	break;
    }
}


/* Prevent warnings from -Wmissing-prototypes.  */

#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int yyparse (void *YYPARSE_PARAM);
#else
int yyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int yyparse (void);
#else
int yyparse ();
#endif
#endif /* ! YYPARSE_PARAM */



/* The look-ahead symbol.  */
int yychar;

/* The semantic value of the look-ahead symbol.  */
YYSTYPE yylval;

/* Number of syntax errors so far.  */
int yynerrs;



/*----------.
| yyparse.  |
`----------*/

#ifdef YYPARSE_PARAM
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void *YYPARSE_PARAM)
#else
int
yyparse (YYPARSE_PARAM)
    void *YYPARSE_PARAM;
#endif
#else /* ! YYPARSE_PARAM */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void)
#else
int
yyparse ()

#endif
#endif
{
  
  int yystate;
  int yyn;
  int yyresult;
  /* Number of tokens to shift before error messages enabled.  */
  int yyerrstatus;
  /* Look-ahead token as an internal (translated) token number.  */
  int yytoken = 0;
#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

  /* Three stacks and their tools:
     `yyss': related to states,
     `yyvs': related to semantic values,
     `yyls': related to locations.

     Refer to the stacks thru separate pointers, to allow yyoverflow
     to reallocate them elsewhere.  */

  /* The state stack.  */
  yytype_int16 yyssa[YYINITDEPTH];
  yytype_int16 *yyss = yyssa;
  yytype_int16 *yyssp;

  /* The semantic value stack.  */
  YYSTYPE yyvsa[YYINITDEPTH];
  YYSTYPE *yyvs = yyvsa;
  YYSTYPE *yyvsp;



#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  YYSIZE_T yystacksize = YYINITDEPTH;

  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;


  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY;		/* Cause a token to be read.  */

  /* Initialize stack pointers.
     Waste one element of value and location stack
     so that they stay on the same level as the state stack.
     The wasted elements are never initialized.  */

  yyssp = yyss;
  yyvsp = yyvs;

  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
	/* Give user a chance to reallocate the stack.  Use copies of
	   these so that the &'s don't force the real ones into
	   memory.  */
	YYSTYPE *yyvs1 = yyvs;
	yytype_int16 *yyss1 = yyss;


	/* Each stack pointer address is followed by the size of the
	   data in use in that stack, in bytes.  This used to be a
	   conditional around just the two extra args, but that might
	   be undefined if yyoverflow is a macro.  */
	yyoverflow (YY_("memory exhausted"),
		    &yyss1, yysize * sizeof (*yyssp),
		    &yyvs1, yysize * sizeof (*yyvsp),

		    &yystacksize);

	yyss = yyss1;
	yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
	goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
	yystacksize = YYMAXDEPTH;

      {
	yytype_int16 *yyss1 = yyss;
	union yyalloc *yyptr =
	  (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
	if (! yyptr)
	  goto yyexhaustedlab;
	YYSTACK_RELOCATE (yyss);
	YYSTACK_RELOCATE (yyvs);

#  undef YYSTACK_RELOCATE
	if (yyss1 != yyssa)
	  YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;


      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
		  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
	YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     look-ahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to look-ahead token.  */
  yyn = yypact[yystate];
  if (yyn == YYPACT_NINF)
    goto yydefault;

  /* Not known => get a look-ahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid look-ahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = YYLEX;
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yyn == 0 || yyn == YYTABLE_NINF)
	goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  if (yyn == YYFINAL)
    YYACCEPT;

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the look-ahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token unless it is eof.  */
  if (yychar != YYEOF)
    yychar = YYEMPTY;

  yystate = yyn;
  *++yyvsp = yylval;

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     `$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 9:
#line 167 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "add_instruction completed" << endl;	
						#endif
					;}
    break;

  case 10:
#line 173 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "sub_instruction completed" << endl;	
						#endif
					;}
    break;

  case 11:
#line 179 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "mul_instruction completed" << endl;	
						#endif
					;}
    break;

  case 12:
#line 185 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "div_instruction completed" << endl;	
						#endif
					;}
    break;

  case 13:
#line 191 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "neg_instruction completed" << endl;	
						#endif
					;}
    break;

  case 14:
#line 197 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "and_instruction completed" << endl;	
						#endif
					;}
    break;

  case 15:
#line 203 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "or_instruction completed" << endl;	
						#endif
					;}
    break;

  case 16:
#line 209 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "not_instruction completed" << endl;	
						#endif
					;}
    break;

  case 17:
#line 215 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "equ_instruction completed" << endl;	
						#endif
					;}
    break;

  case 18:
#line 221 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "geq_instruction completed" << endl;	
						#endif
					;}
    break;

  case 19:
#line 227 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "leq_instruction completed" << endl;	
						#endif
					;}
    break;

  case 20:
#line 233 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "les_instruction completed" << endl;	
						#endif
					;}
    break;

  case 21:
#line 239 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "grt_instruction completed" << endl;	
						#endif
					;}
    break;

  case 22:
#line 245 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "neq_instruction completed" << endl;	
						#endif
					;}
    break;

  case 23:
#line 251 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "ldo_instruction completed" << endl;	
						#endif
					;}
    break;

  case 24:
#line 257 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "ldc_instruction completed" << endl;	
						#endif
					;}
    break;

  case 25:
#line 263 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "ind_instruction completed" << endl;	
						#endif
					;}
    break;

  case 26:
#line 269 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "sro_instruction completed" << endl;	
						#endif
					;}
    break;

  case 27:
#line 275 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "sto_instruction completed" << endl;	
						#endif
					;}
    break;

  case 28:
#line 281 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "ujp_instruction completed" << endl;	
						#endif
					;}
    break;

  case 29:
#line 287 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "fjp_instruction completed" << endl;	
						#endif
					;}
    break;

  case 30:
#line 293 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "ixj_instruction completed" << endl;	
						#endif
					;}
    break;

  case 31:
#line 299 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "ixa_instruction completed" << endl;	
						#endif
					;}
    break;

  case 32:
#line 305 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "inc_instruction completed" << endl;	
						#endif
					;}
    break;

  case 33:
#line 311 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "dec_instruction completed" << endl;	
						#endif
					;}
    break;

  case 34:
#line 317 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "chk_instruction completed" << endl;	
						#endif
					;}
    break;

  case 35:
#line 323 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "dpl_instruction completed" << endl;	
						#endif
					;}
    break;

  case 36:
#line 329 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "ldd_instruction completed" << endl;	
						#endif
					;}
    break;

  case 37:
#line 335 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "sli_instruction completed" << endl;	
						#endif
					;}
    break;

  case 38:
#line 341 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "new_instruction completed" << endl;	
						#endif
					;}
    break;

  case 39:
#line 347 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "lod_instruction completed" << endl;	
						#endif
					;}
    break;

  case 40:
#line 353 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "lda_instruction completed" << endl;	
						#endif
					;}
    break;

  case 41:
#line 359 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "str_instruction completed" << endl;	
						#endif
					;}
    break;

  case 42:
#line 365 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "mst_instruction completed" << endl;	
						#endif
					;}
    break;

  case 43:
#line 371 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "cup_instruction completed" << endl;	
						#endif
					;}
    break;

  case 44:
#line 377 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "ssp_instruction completed" << endl;	
						#endif
					;}
    break;

  case 45:
#line 383 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "sep_instruction completed" << endl;	
						#endif
					;}
    break;

  case 46:
#line 389 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "ent_instruction completed" << endl;	
						#endif
					;}
    break;

  case 47:
#line 395 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "retf_instruction completed" << endl;	
						#endif
					;}
    break;

  case 48:
#line 401 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "retp_instruction completed" << endl;	
						#endif
					;}
    break;

  case 49:
#line 407 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "movs_instruction completed" << endl;	
						#endif
					;}
    break;

  case 50:
#line 413 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "movd_instruction completed" << endl;	
						#endif
					;}
    break;

  case 51:
#line 419 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "smp_instruction completed" << endl;	
						#endif
					;}
    break;

  case 52:
#line 425 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "cupi_instruction completed" << endl;	
						#endif
					;}
    break;

  case 53:
#line 431 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "mstf_instruction completed" << endl;	
						#endif
					;}
    break;

  case 54:
#line 437 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "hlt_instruction completed" << endl;	
						#endif
					;}
    break;

  case 55:
#line 443 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "inp_instruction completed" << endl;	
						#endif
					;}
    break;

  case 56:
#line 449 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "out_instruction completed" << endl;	
						#endif
					;}
    break;

  case 57:
#line 455 "pmachine.y"
    {
						#ifdef YACCOUPUT
							cout << "conv_instruction completed" << endl;
						#endif
					;}
    break;

  case 58:
#line 461 "pmachine.y"
    {
						#ifdef YACCOUTPUT
							cout << "label_introduction completed" << endl;	
						#endif
					;}
    break;

  case 59:
#line 468 "pmachine.y"
    {
						(yyval.type) = YYSTYPE::r;
					;}
    break;

  case 60:
#line 472 "pmachine.y"
    {
						(yyval.type) = YYSTYPE::i;
					;}
    break;

  case 62:
#line 478 "pmachine.y"
    {
								(yyval.type) = YYSTYPE::b;
							;}
    break;

  case 63:
#line 482 "pmachine.y"
    {
								(yyval.type) = YYSTYPE::c;
							;}
    break;

  case 64:
#line 486 "pmachine.y"
    {
								(yyval.type) = YYSTYPE::a;
							;}
    break;

  case 67:
#line 494 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Add(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Add(real));
								break;
						}
					;}
    break;

  case 68:
#line 506 "pmachine.y"
    {
						yyerror("instruction add: add [i|r]");
					;}
    break;

  case 69:
#line 511 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Sub(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Sub(real));
								break;
						}
					;}
    break;

  case 70:
#line 523 "pmachine.y"
    {
						yyerror("instruction sub: sub [i|r]");
					;}
    break;

  case 71:
#line 528 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Mul(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Mul(real));
								break;
						}
					;}
    break;

  case 72:
#line 540 "pmachine.y"
    {
						yyerror("instruction mul: mul [i|r]");
					;}
    break;

  case 73:
#line 546 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Div(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Div(real));
								break;
						}
					;}
    break;

  case 74:
#line 558 "pmachine.y"
    {
						yyerror("instruction div: div [i|r]");
					;}
    break;

  case 75:
#line 563 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Neg(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Neg(real));
								break;
						}
					;}
    break;

  case 76:
#line 575 "pmachine.y"
    {
						yyerror("instruction neg: neg [i|r]");
					;}
    break;

  case 77:
#line 580 "pmachine.y"
    {
						Pmachine.addInstruction(new And());
					;}
    break;

  case 78:
#line 585 "pmachine.y"
    {
						Pmachine.addInstruction(new Or());
					;}
    break;

  case 79:
#line 590 "pmachine.y"
    {
						Pmachine.addInstruction(new Not());
					;}
    break;

  case 80:
#line 595 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Equ(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Equ(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Equ(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Equ(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Equ(boolean));
								break;
						}
					;}
    break;

  case 81:
#line 616 "pmachine.y"
    {
						yyerror("instruction equ: equ [i|r|a|b|c]");
					;}
    break;

  case 82:
#line 621 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Geq(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Geq(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Geq(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Geq(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Geq(boolean));
								break;
						}
					;}
    break;

  case 83:
#line 642 "pmachine.y"
    {
						yyerror("instruction geq: geq [i|r|a|b|c]");
					;}
    break;

  case 84:
#line 647 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Leq(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Leq(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Leq(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Leq(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Leq(boolean));
								break;
						}
					;}
    break;

  case 85:
#line 668 "pmachine.y"
    {
						yyerror("instruction leq: leq [i|r|a|b|c]");
					;}
    break;

  case 86:
#line 673 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Les(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Les(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Les(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Les(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Les(boolean));
								break;
						}
					;}
    break;

  case 87:
#line 694 "pmachine.y"
    {
						yyerror("instruction les: les [i|r|a|b|c]");
					;}
    break;

  case 88:
#line 699 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Grt(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Grt(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Grt(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Grt(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Grt(boolean));
								break;
						}
					;}
    break;

  case 89:
#line 720 "pmachine.y"
    {
						yyerror("instruction grt: grt [i|r|a|b|c]");
					;}
    break;

  case 90:
#line 725 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Neq(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Neq(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Neq(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Neq(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Neq(boolean));
								break;
						}
					;}
    break;

  case 91:
#line 746 "pmachine.y"
    {
						yyerror("instruction neq: neq [i|r|a|b|c]");
					;}
    break;

  case 92:
#line 751 "pmachine.y"
    {
						switch((yyvsp[(3) - (5)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Ldo(integer, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Ldo(real, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Ldo(character, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Ldo(address, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Ldo(boolean, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
						}
					;}
    break;

  case 93:
#line 772 "pmachine.y"
    {
						yyerror("instruction ldo: ldo [i|r|a|b|c]");
					;}
    break;

  case 94:
#line 777 "pmachine.y"
    {
						Pmachine.addInstruction(new Ldc(real, new StackReal((yyvsp[(5) - (5)].realnumbervalue))));
					;}
    break;

  case 95:
#line 781 "pmachine.y"
    {
						Pmachine.addInstruction(new Ldc(integer, new StackInteger((yyvsp[(5) - (5)].integernumbervalue))));
					;}
    break;

  case 96:
#line 785 "pmachine.y"
    {
						Pmachine.addInstruction(new Ldc(boolean, new StackBoolean((yyvsp[(5) - (5)].booleanvalue))));
					;}
    break;

  case 97:
#line 789 "pmachine.y"
    {
						Pmachine.addInstruction(new Ldc(character, new StackCharacter(static_cast<char>((yyvsp[(5) - (5)].integernumbervalue)))));
					;}
    break;

  case 98:
#line 793 "pmachine.y"
    {
						Pmachine.addInstruction(new Ldc(character, new StackCharacter(static_cast<char>((yyvsp[(5) - (5)].charvalue)))));
					;}
    break;

  case 99:
#line 797 "pmachine.y"
    {
						Pmachine.addInstruction(new Ldc(address, new StackAddress((yyvsp[(5) - (5)].integernumbervalue))));
					;}
    break;

  case 100:
#line 801 "pmachine.y"
    {
						yyerror("instruction ldc: ldc [i|r|a|b|c] [value]");
					;}
    break;

  case 101:
#line 806 "pmachine.y"
    {
						
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Ind(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Ind(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Ind(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Ind(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Ind(boolean));
								break;
						}
					;}
    break;

  case 102:
#line 828 "pmachine.y"
    {
						yyerror("instruction ind: ind [i|r|a|b|c]");
					;}
    break;

  case 103:
#line 833 "pmachine.y"
    {
						switch((yyvsp[(3) - (5)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Sro(integer, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Sro(real, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Sro(character, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Sro(address, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Sro(boolean, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
						}
					;}
    break;

  case 104:
#line 854 "pmachine.y"
    {
						yyerror("instruction sro: sro [i|r|a|b|c] [integer]");
					;}
    break;

  case 105:
#line 859 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Sto(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Sto(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Sto(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Sto(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Sto(boolean));
								break;
						}
					;}
    break;

  case 106:
#line 880 "pmachine.y"
    {
						yyerror("instruction sto: sto [i|r|a|b|c]");
					;}
    break;

  case 107:
#line 885 "pmachine.y"
    {
						Pmachine.addInstruction(new Ujp(*(yyvsp[(3) - (3)].textvalue)));
					;}
    break;

  case 108:
#line 889 "pmachine.y"
    {	
						yyerror("instruction ujp: ujp [label]");
					;}
    break;

  case 109:
#line 894 "pmachine.y"
    {
						Pmachine.addInstruction(new Fjp(*(yyvsp[(3) - (3)].textvalue)));
					;}
    break;

  case 110:
#line 898 "pmachine.y"
    {
						yyerror("instruction fjp: fjp [label]");
					;}
    break;

  case 111:
#line 903 "pmachine.y"
    {
						Pmachine.addInstruction(new Ixj(*(yyvsp[(3) - (3)].textvalue)));
					;}
    break;

  case 112:
#line 907 "pmachine.y"
    {
						yyerror("instruction ixj: ixj [label]");
					;}
    break;

  case 113:
#line 912 "pmachine.y"
    {
						Pmachine.addInstruction(new Ixa((yyvsp[(3) - (3)].integernumbervalue)));
					;}
    break;

  case 114:
#line 916 "pmachine.y"
    {
						yyerror("instruction ixa: ixa [integer]");
					;}
    break;

  case 115:
#line 921 "pmachine.y"
    {
						switch((yyvsp[(3) - (5)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Inc(integer, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Inc(real, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Inc(character, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Inc(address, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Inc(boolean, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
						}
					;}
    break;

  case 116:
#line 942 "pmachine.y"
    {
						yyerror("instruction inc: inc [i|r|a|b|c] [integervalue]");
					;}
    break;

  case 117:
#line 947 "pmachine.y"
    {
						switch((yyvsp[(3) - (5)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Dec(integer, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Dec(real, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Dec(character, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Dec(address, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Dec(boolean, (yyvsp[(5) - (5)].integernumbervalue)));
								break;
						}
					;}
    break;

  case 118:
#line 968 "pmachine.y"
    {
						yyerror("instruction dec: dec [i|r|a|b|c] [integervalue]");
					;}
    break;

  case 119:
#line 973 "pmachine.y"
    {
						Pmachine.addInstruction(new Chk((yyvsp[(3) - (5)].integernumbervalue), (yyvsp[(5) - (5)].integernumbervalue)));
					;}
    break;

  case 120:
#line 977 "pmachine.y"
    {
						yyerror("instruction chk: chk [integervalue] [integervalue]");
					;}
    break;

  case 121:
#line 982 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Dpl(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Dpl(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Dpl(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Dpl(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Dpl(boolean));
								break;
						}
					;}
    break;

  case 122:
#line 1003 "pmachine.y"
    {
						yyerror("instruction dpl: dpl [i|r|a|b|c]");
					;}
    break;

  case 123:
#line 1008 "pmachine.y"
    {
						Pmachine.addInstruction(new Ldd((yyvsp[(3) - (3)].integernumbervalue)));
					;}
    break;

  case 124:
#line 1012 "pmachine.y"
    {
						yyerror("instruction ldd: ldd [integervalue]");
					;}
    break;

  case 125:
#line 1017 "pmachine.y"
    {
						switch((yyvsp[(3) - (3)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Sli(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Sli(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Sli(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Sli(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Sli(boolean));
								break;
						}
					;}
    break;

  case 126:
#line 1038 "pmachine.y"
    {
						yyerror("instruction sli: sli [i|r|a|b|c]");
					;}
    break;

  case 127:
#line 1043 "pmachine.y"
    {
						Pmachine.addInstruction(new New());
					;}
    break;

  case 128:
#line 1048 "pmachine.y"
    {
						switch((yyvsp[(3) - (7)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Lod(integer, (yyvsp[(5) - (7)].integernumbervalue), (yyvsp[(7) - (7)].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Lod(real, (yyvsp[(5) - (7)].integernumbervalue), (yyvsp[(7) - (7)].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Lod(character, (yyvsp[(5) - (7)].integernumbervalue), (yyvsp[(7) - (7)].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Lod(address, (yyvsp[(5) - (7)].integernumbervalue), (yyvsp[(7) - (7)].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Lod(boolean, (yyvsp[(5) - (7)].integernumbervalue), (yyvsp[(7) - (7)].integernumbervalue)));
								break;
						}
					;}
    break;

  case 129:
#line 1069 "pmachine.y"
    {
						yyerror("instruction lod: lod [i|r|a|b|c] [integervalue] [integervalue]");
					;}
    break;

  case 130:
#line 1075 "pmachine.y"
    {
						Pmachine.addInstruction(new Lda((yyvsp[(3) - (5)].integernumbervalue), (yyvsp[(5) - (5)].integernumbervalue)));
					;}
    break;

  case 131:
#line 1079 "pmachine.y"
    {
						yyerror("instruction lda: lda [integervalue] [integervalue]");
					;}
    break;

  case 132:
#line 1084 "pmachine.y"
    {
						switch((yyvsp[(3) - (7)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Str(integer, (yyvsp[(5) - (7)].integernumbervalue), (yyvsp[(7) - (7)].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Str(real, (yyvsp[(5) - (7)].integernumbervalue), (yyvsp[(7) - (7)].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Str(character, (yyvsp[(5) - (7)].integernumbervalue), (yyvsp[(7) - (7)].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Str(address, (yyvsp[(5) - (7)].integernumbervalue), (yyvsp[(7) - (7)].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Str(boolean, (yyvsp[(5) - (7)].integernumbervalue), (yyvsp[(7) - (7)].integernumbervalue)));
								break;
						}
					;}
    break;

  case 133:
#line 1105 "pmachine.y"
    {
						yyerror("instruction str: str [i|r|a|b|c] [intergervalue] [integervalue]");
					;}
    break;

  case 134:
#line 1110 "pmachine.y"
    {
						Pmachine.addInstruction(new Mst((yyvsp[(3) - (3)].integernumbervalue)));
					;}
    break;

  case 135:
#line 1114 "pmachine.y"
    {
						yyerror("instruction mst: mst [integer]");
					;}
    break;

  case 136:
#line 1119 "pmachine.y"
    {
						Pmachine.addInstruction(new Cup((yyvsp[(3) - (5)].integernumbervalue), *(yyvsp[(5) - (5)].textvalue)));
					;}
    break;

  case 137:
#line 1123 "pmachine.y"
    {
						yyerror("instruction cup: cup [integervalue] [integervalue]");
					;}
    break;

  case 138:
#line 1128 "pmachine.y"
    {
						Pmachine.addInstruction(new Ssp((yyvsp[(3) - (3)].integernumbervalue)));
					;}
    break;

  case 139:
#line 1132 "pmachine.y"
    {
						yyerror("instruction ssp: ssp [integervalue]");
					;}
    break;

  case 140:
#line 1137 "pmachine.y"
    {
						Pmachine.addInstruction(new Sep((yyvsp[(3) - (3)].integernumbervalue)));
					;}
    break;

  case 141:
#line 1141 "pmachine.y"
    {
						yyerror("instruction sep: sep [integervalue]");
					;}
    break;

  case 142:
#line 1146 "pmachine.y"
    {
						Pmachine.addInstruction(new Ent((yyvsp[(3) - (5)].integernumbervalue), (yyvsp[(5) - (5)].integernumbervalue)));
					;}
    break;

  case 143:
#line 1150 "pmachine.y"
    {
						yyerror("instruction ent: ent [integervalue] [integervalue]");
					;}
    break;

  case 144:
#line 1155 "pmachine.y"
    {
						Pmachine.addInstruction(new Retf());
					;}
    break;

  case 145:
#line 1160 "pmachine.y"
    {
						Pmachine.addInstruction(new Retp());
					;}
    break;

  case 146:
#line 1165 "pmachine.y"
    {
						Pmachine.addInstruction(new Movs((yyvsp[(3) - (3)].integernumbervalue)));
					;}
    break;

  case 147:
#line 1169 "pmachine.y"
    {
						yyerror("instruction movs: movs [integervalue]");
					;}
    break;

  case 148:
#line 1174 "pmachine.y"
    {
						Pmachine.addInstruction(new Movd((yyvsp[(3) - (3)].integernumbervalue)));
					;}
    break;

  case 149:
#line 1178 "pmachine.y"
    {
						yyerror("instruction movd: movd [integervalue]");
					;}
    break;

  case 150:
#line 1183 "pmachine.y"
    {
						Pmachine.addInstruction(new Smp((yyvsp[(3) - (3)].integernumbervalue)));
					;}
    break;

  case 151:
#line 1187 "pmachine.y"
    {
						yyerror("instruction smp: smp [integervalue]");
					;}
    break;

  case 152:
#line 1192 "pmachine.y"
    {
						Pmachine.addInstruction(new Cupi((yyvsp[(3) - (5)].integernumbervalue), (yyvsp[(5) - (5)].integernumbervalue)));
					;}
    break;

  case 153:
#line 1196 "pmachine.y"
    {
						yyerror("instruction cupi: cupi [integervalue] [integervalue]");
					;}
    break;

  case 154:
#line 1201 "pmachine.y"
    {
						Pmachine.addInstruction(new Mstf((yyvsp[(3) - (5)].integernumbervalue), (yyvsp[(5) - (5)].integernumbervalue)));
					;}
    break;

  case 155:
#line 1205 "pmachine.y"
    {
						yyerror("instruction mstf: mstf [integervalue] [integervalue]");
					;}
    break;

  case 156:
#line 1210 "pmachine.y"
    {
						Pmachine.addInstruction(new Hlt());
					;}
    break;

  case 157:
#line 1215 "pmachine.y"
    {
						Pmachine.addInstruction(new In(integer));
					;}
    break;

  case 158:
#line 1219 "pmachine.y"
    {
						Pmachine.addInstruction(new In(real));
					;}
    break;

  case 159:
#line 1223 "pmachine.y"
    {
						Pmachine.addInstruction(new In(boolean));
					;}
    break;

  case 160:
#line 1227 "pmachine.y"
    {
						Pmachine.addInstruction(new In(character));
					;}
    break;

  case 161:
#line 1231 "pmachine.y"
    {
						yyerror("instruction in: input of address at runtime is forbidden");
					;}
    break;

  case 162:
#line 1235 "pmachine.y"
    {
						yyerror("instruction in: in [i|r|b|c]");
					;}
    break;

  case 163:
#line 1240 "pmachine.y"
    {
						Pmachine.addInstruction(new Out(real, true));
					;}
    break;

  case 164:
#line 1244 "pmachine.y"
    {
						Pmachine.addInstruction(new Out(real, false));
					;}
    break;

  case 165:
#line 1248 "pmachine.y"
    {
						Pmachine.addInstruction(new Out(integer));
					;}
    break;

  case 166:
#line 1252 "pmachine.y"
    {
						Pmachine.addInstruction(new Out(character));				
					;}
    break;

  case 167:
#line 1256 "pmachine.y"
    {
						Pmachine.addInstruction(new Out(address));
					;}
    break;

  case 168:
#line 1260 "pmachine.y"
    {
						Pmachine.addInstruction(new Out(boolean));
					;}
    break;

  case 169:
#line 1264 "pmachine.y"
    {
						yyerror("instruction out: out r i\ninstruction out: out [r|i|a|b|c]");
					;}
    break;

  case 170:
#line 1269 "pmachine.y"
    {
						StackElementType type;
						switch((yyvsp[(5) - (5)].type))
						{
							case YYSTYPE::i:
								type = integer;
								break;
							case YYSTYPE::r:
								type = real;
								break;
							case YYSTYPE::c:
								type = character;
								break;
							case YYSTYPE::a:
								type = address;
								break;
							case YYSTYPE::b:
								type = boolean;
								break;
						}
												
						switch((yyvsp[(3) - (5)].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Conv(integer, type));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Conv(real, type));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Conv(character, type));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Conv(address, type));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Conv(boolean, type));
								break;
						}
					;}
    break;

  case 171:
#line 1310 "pmachine.y"
    {
							yyerror("instruction conv: conv [r|i|a|b|c] [r|i|a|b|c]");
						;}
    break;

  case 172:
#line 1314 "pmachine.y"
    {
						Pmachine.addLabel(*(yyvsp[(1) - (1)].textvalue));
					;}
    break;


/* Line 1267 of yacc.c.  */
#line 3407 "pmachine.tab.c"
      default: break;
    }
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;


  /* Now `shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*------------------------------------.
| yyerrlab -- here on detecting error |
`------------------------------------*/
yyerrlab:
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
      {
	YYSIZE_T yysize = yysyntax_error (0, yystate, yychar);
	if (yymsg_alloc < yysize && yymsg_alloc < YYSTACK_ALLOC_MAXIMUM)
	  {
	    YYSIZE_T yyalloc = 2 * yysize;
	    if (! (yysize <= yyalloc && yyalloc <= YYSTACK_ALLOC_MAXIMUM))
	      yyalloc = YYSTACK_ALLOC_MAXIMUM;
	    if (yymsg != yymsgbuf)
	      YYSTACK_FREE (yymsg);
	    yymsg = (char *) YYSTACK_ALLOC (yyalloc);
	    if (yymsg)
	      yymsg_alloc = yyalloc;
	    else
	      {
		yymsg = yymsgbuf;
		yymsg_alloc = sizeof yymsgbuf;
	      }
	  }

	if (0 < yysize && yysize <= yymsg_alloc)
	  {
	    (void) yysyntax_error (yymsg, yystate, yychar);
	    yyerror (yymsg);
	  }
	else
	  {
	    yyerror (YY_("syntax error"));
	    if (yysize != 0)
	      goto yyexhaustedlab;
	  }
      }
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse look-ahead token after an
	 error, discard it.  */

      if (yychar <= YYEOF)
	{
	  /* Return failure if at end of input.  */
	  if (yychar == YYEOF)
	    YYABORT;
	}
      else
	{
	  yydestruct ("Error: discarding",
		      yytoken, &yylval);
	  yychar = YYEMPTY;
	}
    }

  /* Else will try to reuse look-ahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule which action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;	/* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (yyn != YYPACT_NINF)
	{
	  yyn += YYTERROR;
	  if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
	    {
	      yyn = yytable[yyn];
	      if (0 < yyn)
		break;
	    }
	}

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
	YYABORT;


      yydestruct ("Error: popping",
		  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  if (yyn == YYFINAL)
    YYACCEPT;

  *++yyvsp = yylval;


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#ifndef yyoverflow
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEOF && yychar != YYEMPTY)
     yydestruct ("Cleanup: discarding lookahead",
		 yytoken, &yylval);
  /* Do not reclaim the symbols of the rule which action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
		  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  /* Make sure YYID is used.  */
  return YYID (yyresult);
}


#line 1319 "pmachine.y"


/////////////////////////////////////////////////////////////////////////////
// programs section

void yyerror(string msg)
{
	cerr << "--> line " << linecount << ": " << msg << endl;
	exit(0);
}


