# Just file: https://github.com/casey/just
#


default := '-f'

s00 args=default:
    cd 00_motivation && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} $(find *.tex)

s01 args=default:
    cd 01_system-theory && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} 01_system-theory.tex

s02 args=default:
    cd 02_image_processing && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} $(find *.tex)

s03 args=default:
    cd 03_endoscopy && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} $(find *.tex)

s04 args=default:
    cd 04_microscopy && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} $(find *.tex)

s05 args=default:
    cd 05_mr && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} 05_mr.tex

s05_2 args=default:
    cd 05_mr && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} 05_mr2.tex

s06 args=default:
    cd 06_x-ray  && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} 06_x-ray.tex

s07 args=default:
    cd 07_ct && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} 07_ct.tex
s07_2 args=default:
    cd 07_ct && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} 07_spectral_ct.tex

s08 args=default:
   cd 08_phase-contrast_x-ray &&latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} 08_phase-contrast_x-ray.tex

s09 args=default:
    cd 09_emission_tomography && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} 09_emission_tomography.tex

s10 args=default:
    cd 10_ultrasound && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} 10_ultrasound.tex

s11 args=default:
    cd 11_oct && latexmk -silent -pdf -shell-escape -file-line-error -interaction=nonstopmode {{args}} 11_oct.tex

render_java_code:
	cd exercise-slides && python3 format.py

build: s00 s01 s02 s03 s04 s05 s05_2 s06 s07 s07_2 s08 s09 s10 s11
all:
     make -j8
