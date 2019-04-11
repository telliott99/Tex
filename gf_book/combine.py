# python combine.py > full.tex
# python /Users/telliott_admin/Dropbox/Tex/gf_book/combine.py > full.tex

# debug:
# python /Users/telliott_admin/Dropbox/Tex/gf_book/combine.py

# need typeset 2x to get toc filled out!
import sys

path = '/Users/telliott_admin/Dropbox/Tex/gf_book/'

def load(fn):
    FH = open(path + fn, 'r')
    data = FH.read()
    FH.close()
    return data

fn = 'master.txt'
cL = load(fn).strip().split('\n')
   
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

for fn in cL:
    print "\\chapter{%s}" % fn
    text = get_text(fn)
    print text

print foot

