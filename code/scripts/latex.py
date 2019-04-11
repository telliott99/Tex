import os, subprocess, shutil

d1 = '/Users/telliott_admin/Dropbox/Tex'
d2 = '/Users/telliott_admin/Desktop/tex'
def part1():
    shutil.copytree(d1,d2)

def part2():
    os.chdir(d2)
    for f in os.listdir(d2):
        if not f.endswith('.tex'):
            continue
        cmd = 'pdflatex ' + f 
        subprocess.call(cmd, shell=True)

#part1
#part2
# mv *.pdf ~/Desktop/pdf