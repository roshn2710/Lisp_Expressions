from LISPParser import parser
def eval(s):
    return parser.parse(s)
while True:
    try:
        s = input('lisp:  ')
        if s == "exit": exit()
        result = eval(s)
        print(result)
    except Exception as e:
        print(str(e))
