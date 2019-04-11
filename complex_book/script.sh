#! /bin/bash
arg=$1
path="/Users/telliott_admin/Dropbox/Tex/complex_book"

cd /Users/telliott_admin/Desktop
python $path/combine.py $arg > CA.tex
pdflatex CA.tex >/dev/null
pdflatex CA.tex >/dev/null
pdflatex CA.tex >/dev/null

mv CA.pdf tmp
rm CA.*
sleep 1
mv tmp $path/Complex\ Analysis.pdf
osascript -e 'quit app "TeXShop"'

# cleanup random stuff
rm $path/files/*.aux $path/files/*.log 2>/dev/null
rm $path/files/*.out $path/files/*.gz 2>/dev/null
rm $path/files/*.pdf 2>/dev/null
rm stdclsdv.sty 2>/dev/null

open -a Preview /Users/telliott_admin/Dropbox/Tex/complex_book/Complex\ Analysis.pdf
