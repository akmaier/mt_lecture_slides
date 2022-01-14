																			   #
# Makefile
# Stephan Seitz, 2020-05-20 11:01
#

all: just s00 s01 s02 s03 s04 s05 s05_2 s06 s07 s07_2 s08 s09 s10 s11 
.PHONY: all

just:
	if [ ! -f ./just ]; then curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to .;fi
	
s00: just
	./just s00

s01: just
	./just s01

s02: just
	./just s02

s03: just
	./just s03

s04: just
	./just s04

s05: just
	./just s05
s05_2: just
	./just s05_2

s06: just
	./just s06

s07: just
	./just s07
s07_2: just
	./just s07_2

s08: just
	./just s08

s09: just
	./just s09

s10: just
	./just s10

s11: just
	./just s11


