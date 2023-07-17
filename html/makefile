all: out.pdf original.pdf

out.pdf: boom.css sample.html
	prince -s boom.css sample.html -o out.pdf

original.pdf: boom.og.css original.html
	prince -s boom.og.css original.html -o original.pdf