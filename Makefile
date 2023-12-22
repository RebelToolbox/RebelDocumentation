# Makefile for Sphinx documentation

# You can set these variables from the command line.
# The first two can also be set from the environment.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# User-friendly check for sphinx-build.
ifneq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 0)
$(info The $(SPHINXBUILD) command was not found.)
$(info Make sure Sphinx is installed see:)
$(info https://www.sphinx-doc.org/en/master/usage/installation.html)
$(error )
endif

# Placed first, so that "make" without an argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target:
# Route all unknown targets to Sphinx using "make mode" option.
# $(O) is shorthand for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
