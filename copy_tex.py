# copy a directory and its whole tree
# into same structure on Desktop
# with a filter
import os, shutil

def f(p):
    return p.endswith('tex')
    
sep = '/'

u = '/Users/telliott_admin'
d = '/Dropbox/Tex'
src = u + d
dst = u + '/Desktop/Tex'

to_process = os.listdir(src)
to_process = [src + '/' + p for p in to_process]

to_write = list()

while to_process:
    p = to_process.pop(0)
    fn = p.split('/')[-1]
    if fn.startswith('.'):
        continue
    if os.path.isfile(p):
        if f(p):
            to_write.append(p)
    else:
        # directory contents
        L = os.listdir(p)
        L = [p + '/' + e for e in L]
        to_process.extend(L)

print len(to_write)
if not os.path.exists(dst):
    os.mkdir(dst)

for p in to_write:
    L = p.split(sep)
    fn = L.pop()
    # sub 'Desktop' for 'Dropbox'
    # rather than generalize, use what we know
    L = L[5:]
    dst_p = dst
    while L:
        dst_p += sep + L.pop(0)
        if not os.path.exists(dst_p):
            os.mkdir(dst_p)
            print dst_p
    shutil.copy(p, dst_p + sep + fn)
