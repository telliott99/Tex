import sys
fn = sys.argv[1]
math_header = '.. math::'

def load_data(fn):
    FH = open(fn)
    data = FH.read()
    FH.close()
    return data.strip().split('\n')

def format_new_header(fn):
    s = '.'.join(fn.split('.')[:-1])
    line1 = '.. _' + s + ':'
    sp = '#'*len(s)
    title = sp + '\n' + s.capitalize() + '\n' + sp
    return line1 + '\n\n' + title

def still_in_header(s):
    s = s.strip()
    if s == '':
        return True
    for c in ['\\','%']:
        if s.strip().startswith(c):
            return True
    return False

def remove_header(L):
    while still_in_header(L[0]):
        L.pop(0)

#==================================

def reformat_eqn(line):
    line = line[2:].strip()
    line = '    ' + line
    return line.replace('\]','')

def reformat_inline(s):
    n = s.count('$')
    t = ':math:`'
    if n % 2:
        print 'error line: ', str(i+1), n
        sys.exit()
    while True:
        i = s.find('$')
        if i == -1:
            break
        j = s.find('$',i+1)
        s = s[:i] + t + s[i+1:j] + '`' + s[j+1:]
    return s

def reformat_section(s):
    s = s.replace('\subsection*{', '')[:-1]
    s = s.capitalize()
    i = len(s)
    return '='*i + '\n' + s + '\n' + '='*i  

def reformat_graphics(s):
    i = s.find('center')

    i = s.find('{',i+1)
    j = s.find('}',i+1)
    fn = s[i+1:j]
    sys.stderr.write(fn + '\n')
    s = '.. image:: /figs/'  + fn + '\n'
    s += '   :scale: 50 %'
    return s

def reformat_italics(s):
    t = '\emph'
    i = s.find(t)
    j = s.find('}', i+6)
    s = s[:i] + '*' + s[i+6:j] + '*' + s[j+1:]
    return s

def replace_range(s,t,i,j):
    return s[:i] + t + s[j+1:]

def remove_vspace(s):
    i = s.find('vspace')
    if i == -1:
        return s
    j = s.find('}', i+1)
    i -= 1 # to get '\'
    return replace_range(s,'',i,j)

#==================================

if __name__ == "__main__":    
    L = load_data(fn)
    remove_header(L)
    doing_math = False
      
    s = format_new_header(fn)
    pL = [s]

    for i,s in enumerate(L):
        s = remove_vspace(s)
        s = s.replace('\\noindent','')
        s = s.replace('\Large','')
        s = s.replace('\large','')
        s = s.strip()
        if s == '':
            continue
            
        # handle equations
        if s.startswith('\['):
            if not doing_math:
                doing_math = True
                pL.append(math_header)
            pL.append(reformat_eqn(s))
            continue
        else:
            doing_math = False
            
        # handle inline math
        if '$' in s:
            pL.append(reformat_inline(s))
            continue
        
        if 'subsection' in s:
            pL.append(reformat_section(s))
            continue
        
        if 'includegraphics' in s:
            pL.append(reformat_graphics(s))
            continue
        
        if '\\begin{center}' in s:
            continue
            
        if  '\\end{center}' in s:
            continue
                
        if '\\end{document}' in s:
            continue
        
        if '\\begin{verbatim}' in s:
            continue
            
        if '\\end{verbatim}' in s:
            continue

        if '\emph{' in s:
            pL.append(reformat_italics(s))
            continue
        
        if '\\' in s:
            msg = 'control seq:  line ' + str(i+1) + '\n'
            msg += s
            sys.stderr.write(msg + '\n\n')
         
        pL.append(s)

    print '\n\n'.join(pL)

