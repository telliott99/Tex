# python combine.py > full.tex
# python /Users/telliott_admin/Tex/calculus_book/scripts/combine.py > full.tex

# debug:
# python /Users/telliott_admin/Tex/calculus_book/scripts/combine.py

# typeset 2x to get toc filled out!
import sys

path = '/Users/telliott_admin/Tex/calculus_book/'

def load(fn):
    FH = open(path + fn, 'r')
    data = FH.read()
    FH.close()
    return data

def get_chapters():
    fn = 'master.txt'
    parts = load(fn).strip().split('\n\n')
    parts = [e for e in parts if not e.lstrip().startswith('-')]
    rL = list()
    for e in parts:
        name, sL = e.strip().split('\n',1)
        sL = sL.split('\n') 
        sL = [e for e in sL if not e.startswith('-')]
        sL = [e for e in sL if not e == '']
        sL = [e.strip() for e in sL]
        rL.append((name,sL))
    return rL
    
rL = get_chapters()
   
head = load('header.txt')
print head + '\n'

sep1 = "\\begin{document}\n\\maketitle\n\\Large"
foot = "\n\\end{document}"

def get_text(fn):
    data = load('files/' + fn + '.tex')
    sep = sep1
    data = data.split(sep,1)[1]
    sep = foot
    return data.split(sep)[0]

for name, sL in rL:
    print "\\part{%s}" % name
    for fn in sL:
        print "\\chapter{%s}" % fn
        text = get_text(fn)
        print text

print foot

