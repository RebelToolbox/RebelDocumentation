# Rebel Documentation

This repository contains the [Rebel Engine](https://github.com/RebelToolbox/RebelEngine) documentation.

The documentation uses the [reStructuredText](https://docutils.sourceforge.io/rst.html) (reST) format. The reST files are parsed with the [Sphinx](https://www.sphinx-doc.org/) documentation builder to build the HTML documentation on the Rebel Toolbox website: https://docs.rebeltoolbox.com.

## Style

The Rebel documentation uses the default ``sphinx_rtd_theme`` with additional [customizations](_static/). It will automatically switch between the light and dark theme depending on your browser/OS' theme preference.

## Contributing changes

Though arguably less convenient to edit than a wiki, using a Git repository provides authors with direct access to the documentation files in a revision control system. This enables everyone to discuss, add to and improve the documentation in an open collaborative way that helps ensure the on-going quality of the documentation.

Pull Requests should be made against the `main` branch by default. Only make Pull Requests against other branches if the changes only apply to that specific version of Rebel Engine.

### Editing existing pages

To edit an existing page, locate its `.rst` source file and open it in your favorite text editor. You can then commit the changes, push them to your fork and make a pull request.

Pages in the `classes/` folder should not be edited here. They are automatically generated from Rebel Engine's [XML class references](https://github.com/RebelToolbox/RebelEngine/tree/main/doc/classes). See [Contribute to the Class Reference](https://docs.rebeltoolbox.com/en/latest/community/contributing/updating_the_class_reference.html) for details.

### Adding new pages

To add a new page, create a `.rst` file with a meaningful name in the section you want to add a file to, e.g. `tutorials/3d/light_baking.rst`. Use your favorite text editor to create the content.

Add a reference name for Sphinx at the beginning of the file. Check other files for the syntax, which should be based on the file name with a `_doc_` prefix (e.g. `.. _doc_light_baking:`).

Add your page to the relevant table of contents file e.g. `tutorials/3d/index.rst`. By convention, the files used to define the various levels of table of contents are prefixed with an underscore. So, in the above example, the file should be referenced in `tutorials/3d/_3d_graphics.rst`. Add your new filename to the list on a new line, using a relative path and no extension, e.g. `light_baking`.

### Sphinx and reStructuredText syntax

Check Sphinx's [reST Primer](https://www.sphinx-doc.org/en/stable/rest.html) and the [official reference](http://docutils.sourceforge.net/rst.html) for details on the syntax.

Sphinx uses specific reST comments to do specific operations, like defining the table of contents (`:toctree:`) or cross-referencing pages. Check the [official Sphinx documentation](https://www.sphinx-doc.org/en/stable/index.html) for more details, or see how things are done in existing pages and adapt it to your needs.

### Adding images and attachments

To add images, please put them in an `img/` folder next to the .rst file with a meaningful name and include them in your page with:
```rst
.. image:: img/image_name.png
```

Similarly, you can include attachments (like assets as support material for a tutorial) by placing them into a `files/` folder next to the .rst file, and using this inline markup:
```rst
:download:`myfilename.zip <files/myfilename.zip>`
```

## Building with Sphinx

To build the HTML website (or any other format supported by Sphinx, like PDF, EPUB or LaTeX), you need to install [Sphinx](https://www.sphinx-doc.org/) >= 1.3 as well as (for the HTML) the [readthedocs.org theme](https://github.com/snide/sphinx_rtd_theme). You also need to install the Sphinx extensions defined in `requirements.txt`.

Those tools are best installed using [pip](https://pip.pypa.io), Python's module installer. The Python 3 version might be provided (on Linux distros) as `pip3` or `python3-pip`. You can then run:

```sh
pip install -r requirements.txt
```

You can then build the HTML documentation from the root folder of this repository with:

```sh
make html
```

or:

```sh
make SPHINXBUILD=~/.local/bin/sphinx-build html
```

Building the documentation requires at least 8 GB of RAM to be done without swapping. If you have at least 16 GB of RAM, you can speed up compilation by using:

```bash
make html SPHINXOPTS=-j2
```

The compilation might take some time as the `classes/` folder contains many files to parse.

In case of a `MemoryError` or `EOFError`, you can remove the `classes/` folder and run `make` again. This will drop the class references from the final HTML documentation but will keep the rest intact. Make sure to avoid using `git add .` in this case when working on a pull request, or the whole `classes/` folder will be removed when you make a commit.

You can then test the changes live by opening `_build/html/index.html` in your favorite browser.

### Building with Sphinx on Windows

On Windows, you need to:
* Download the Python installer [here](https://www.python.org/downloads/).
* Install Python. Don't forget to check the "Add Python to PATH" box.
* Use the above `pip` commands.

Building is still done at the root folder of this repository using the provided `make.bat`:
```sh
make.bat html
```

Alternatively, you can build with this command instead:
```sh
sphinx-build -b html ./ _build
```

Note that during the first build, various installation prompts may appear and ask to install LaTeX plugins.
Make sure you don't miss them, especially if they open behind other windows, else the build may appear to hang until you confirm these prompts.

You could also install a normal `make` toolchain (for example via MinGW) and build the docs using the normal `make html`.

### Building with Sphinx and virtualenv

If you want your Sphinx installation scoped to the project, you can install it using virtualenv.
Execute this from the root folder of this repository:

```sh
virtualenv --system-site-packages env/
. env/bin/activate
pip install -r requirements.txt
```

Then do `make html` like above.

## License

With the exception of the `classes/` folder, all the content in this repository is licensed under the Creative Commons Attribution 4.0 International Public License ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)). Attribution should be made to the Rebel Documentation Contributors and/or the specific author.

The files in the `classes/` folder are derived from [Rebel Engine](https://github.com/RebelToolbox/RebelEngine) and are distributed under the MIT license.

[![Documentation Status](https://readthedocs.org/projects/rebel-documentation/badge/?version=latest)](https://docs.rebeltoolbox.com/en/latest/?badge=latest)
