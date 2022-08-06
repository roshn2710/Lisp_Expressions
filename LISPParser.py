import ply.yacc as parser
from LISPLexer import tokens
#not building the tree directly evaluating the expressions

def p_start_expr(p):
    '''Start : Expr SEMI
            | BoolExpr SEMI
            | ListExpr SEMI'''
    p[0] = p[1]

def p_lisp_number(p):
    'Expr : NUMBER'
    p[0] = p[1]

def p_lisp_plus(p):
    'Expr : LPAREN PLUS Expr Expr RPAREN'
    p[0] = p[3] + p[4]

def p_lisp_minus(p):
    'Expr : LPAREN MINUS Expr Expr RPAREN'
    p[0] = p[3] - p[4]

def p_lisp_times(p):
    'Expr : LPAREN TIMES Expr Expr RPAREN'
    p[0] = p[3] * p[4]

def p_lisp_divide(p):
    'Expr : LPAREN DIVIDE Expr Expr RPAREN'
    numerator = p[3]
    denom = p[4]
    if denom == 0:
        raise Exception("DIVIDE BY ZERO!")
    p[0] = numerator / denom

def p_lisp_car(p):
    'Expr : LPAREN CAR ListExpr RPAREN'
    if len(p[3]) == 0:
        raise Exception("Cannot CAR on an empty list!")
    p[0] = p[3][0]

def p_lisp_exprif(p):
    'Expr : LPAREN IF BoolExpr Expr Expr RPAREN'
    if p[3]:
        p[0] = p[4]
    else:
        p[0] = p[5]

def p_lisp_booltrue(p):
    'BoolExpr : TRUE'
    p[0] = True

def p_lisp_boolfalse(p):
    'BoolExpr : FALSE'
    p[0] = False

def p_lisp_boolgreater(p):
    'BoolExpr : LPAREN GR Expr Expr RPAREN'
    p[0] = p[3] > p[4]

def p_lisp_boolgreaterEqual(p):
    'BoolExpr : LPAREN GREQ Expr Expr RPAREN'
    p[0] = p[3] >= p[4]

def p_lisp_boolless(p):
    'BoolExpr : LPAREN LT Expr Expr RPAREN'
    p[0] = p[3] < p[4]

def p_lisp_boollessthenequal(p):
    'BoolExpr : LPAREN LTEQ Expr Expr RPAREN'
    p[0] = p[3] <= p[4]

def p_lisp_boolequal(p):
    'BoolExpr : LPAREN EQ Expr Expr RPAREN'
    p[0] = p[3] == p[4]

def p_lisp_boolnotequal(p):
    'BoolExpr : LPAREN NEQ Expr Expr RPAREN'
    p[0] = p[3] != p[4]

def p_lisp_boolnegate(p):
    'BoolExpr : LPAREN NOT BoolExpr RPAREN'
    p[0] = not p[3]

def p_lisp_booland(p):
    'BoolExpr : LPAREN AND BoolExpr BoolExpr RPAREN'
    p[0] = p[3]  and p[4]

def p_lisp_boolor(p):
    'BoolExpr : LPAREN OR BoolExpr BoolExpr RPAREN'
    p[0] = p[3] or p[4]

def p_lisp_array(p):
    'ExprArray : ExprArray Expr'
    p[1].append(p[2])
    p[0] = p[1]

def p_lisp_array_expr(p):
    'ExprArray : Expr'
    p[0] = [p[1]]

def p_lisp_list(p):
    'ListExpr : LPAREN ExprArray RPAREN'
    p[0] = p[2]

def p_lisp_list_empty(p):
    'ListExpr : LPAREN RPAREN'
    p[0] =[]

def p_lisp_list_cdr(p):
    'ListExpr : LPAREN CDR ListExpr RPAREN'
    if len(p[3]) == 0:
        raise Exception("Cannot CDR on an empty list!")
    p[3].pop(0)
    p[0] = p[3]

def p_lisp_list_cons(p):
    'ListExpr : LPAREN CONS Expr ListExpr RPAREN'
    p[4].insert(0, p[3])
    p[0] = p[4]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    raise Exception("Syntax error in input!")

parser = parser.yacc()






