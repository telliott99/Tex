# python combine.py > full.tex

s='''
0 Introduction.tex,
1 Arithmetic.tex,
2 Conjugate.tex,
3 Differentiate.tex, 
4 CRE.tex,
5 Powers.tex, 
6 Exponential.tex,
7 Logarithm.tex, 
8 Roots.tex, 
9 Trig functions.tex,
10 Polar CRE.tex,
11 CRE Examples.tex, 
12 Integrate.tex, 
13 Integrate 2.tex, 
14 Cauchy 1.tex, 
15 Cauchy 2.tex, 
16 Partial Fractions.tex,
17 Residues.tex,
18 Kaplan.tex,
19 Quotients.tex,
20 Definitions.tex,
21 Series.tex,
22 Write series.tex,
23 Trig integrals.tex,
24 Real integrals.tex,
25 Conformal.tex,
26 End.tex'''


path = '/Users/telliott_admin/Dropbox/Tex/complex/book/'

def num(fn):
    # print fn
    return int(fn.split(' ')[0])

L = [False] * 28
for fn in s.strip().split(','):
    fn = fn.strip()
    i = num(fn)
    L[i] = fn

L = [e for e in L if e]
    
def load(fn):
    FH = open(path + fn, 'r')
    data = FH.read()
    FH.close()
    return data

def get_header(fn):
    data = load(fn)
    sep = 'Large\n'
    return data.split(sep)[0] + sep

head = get_header(L[0])
foot = "\n\\end{document}"

def get_text(fn):
    data = load(fn)
    sep = 'Large\n'
    data = data.split(sep)[1]
    sep = foot
    return data.split(sep)[0]

print head
for i,fn in enumerate(L):
    text = get_text(fn)
    n = str(num(fn))
    fn = ' '.join(fn.split(" ")[1:])
    fn = fn.split('.tex')[0]
    print "\\section{%s}" % fn
    print text
    if i != (len(L)-1):  print "\\newpage"
print foot

