import sys, re
assign_patt = re.compile(r'.*[^=]=[^=].*')
blank_patt = re.compile(r'^\s+$')
code_file = sys.argv[1]
with open(code_file) as code:
    for line in code:
        if blank_patt.match(line) or line.startswith('#'):
            continue
        raw_input()
        print '>>>'+line,
        if assign_patt.match(line):
            try:
                exec(line)
            except Exception as error:
                print error
        else:
            try:
                result = eval(line)
            except Exception as error:
                print error
                result = None
            if not result is None:
                raw_input()
                print repr(result),
