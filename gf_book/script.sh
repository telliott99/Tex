#! /bin/bash
arg=$1
path="/Users/telliott_admin/Dropbox/Tex/gf_book"

cd /Users/telliott_admin/Desktop

python $path/combine.py $arg > GF.tex
# once to generate .sty, twice for TOC, 3x for ref nums
pdflatex GF.tex >/dev/null
pdflatex GF.tex >/dev/null
pdflatex GF.tex >/dev/null

mv GF.pdf $path/Galois\ Fields.pdf
rm GF.*

osascript -e 'quit app "TeXShop"'

# cleanup random stuff
rm $path/files/*.aux $path/files/*.log 2>/dev/null
rm $path/files/*.out $path/files/*.gz 2>/dev/null
rm $path/files/*.pdf 2>/dev/null
rm stdclsdv.sty 2>/dev/null
# rm stdclsdv.sty 2>/dev/null

open -a Preview /Users/telliott_admin/Dropbox/Tex/gf_book/Galois\ Fields.pdf


