import ply.lex as lex

# List of token names
tokens = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
          'CAR', 'TRUE', 'FALSE', 'GR', 'GREQ', 'LT', 'LTEQ', 'EQ', 'NEQ',
          'NOT', 'AND', 'OR', 'CDR', 'IF', 'CONS', 'SEMI']

# regular expressions rules
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CAR = r'car'
t_TRUE = r'True'
t_FALSE = r'False'
t_GR = r'>'
t_GREQ = r'>='
t_LT = r'<'
t_LTEQ = r'<='
t_EQ = r'='
t_NEQ = r'<>'
t_NOT = r'not'
t_AND = r'and'
t_OR = r'or'
t_CDR = r'cdr'
t_IF = r'if'
t_CONS = r'cons'
t_SEMI = r';'

#regular expression rules with some action
def t_NUMBER(t):
    r'[-+]?[0-9]+(\.([0-9]+)?)?'
    t.value = float(t.value)
    return t

#A rule to track line number
def t_newline(t):
    r'\n+'
    t.lexer.lineon += len(t.value)

#Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

#Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#build lexer
lexer = lex.lex()

