/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

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
/* Line 1529 of yacc.c.  */
#line 188 "pmachine.tab.h"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

