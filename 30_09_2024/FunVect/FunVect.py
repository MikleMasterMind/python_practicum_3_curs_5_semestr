def superposition(funmod, funseq):
    funres = [lambda x, j=i: funmod(funseq[j](x)) for i in range(len(funseq))]
    return funres


import sys
exec(sys.stdin.read())