import os, subprocess, shutil

home = '/Users/telliott_admin'
dst = 'Desktop'
src = 'Dropbox'
ext = 'pdf'

src = '/'.join([home,src,'Tex'])
dst = '/'.join([home,dst,'Tex'])
sL = ['png','scripts','todo']

def get_fnL(src):
    L = list()
    for d in os.listdir(src):
        if d.startswith('.'):
            continue
        rL = [1 for t in sL if t == d]
        if sum(rL):
            continue
        p = '/'.join((src,d))
        if os.path.isfile(p):
            continue
        for fn in os.listdir(p):
            if fn.endswith('.' + ext):
                L.append((d, fn))
    return L

if not os.path.exists(dst):
    os.mkdir(dst)

L = get_fnL(src)
counter = 0

for d,fn in L:
    p = dst + '/' + d
    if not os.path.isdir(p):
        os.mkdir(p)
    shutil.copyfile(src + '/' + d + '/' + fn,
                    dst + '/' + d + '/' + fn )
    for f in os.listdir(src):
        if f.endswith('pdf'):
            shutil.copy(src+'/'+f, dst+'/'+f)
            counter += 1

print 'copied %d files' % counter
        
