<p align="center">
  <img src="rebel-documentation.png" alt="Rebel Documentation"/>
</p>

[![Documentation Status](https://readthedocs.org/projects/rebel-documentation/badge/?version=latest)](https://docs.rebeltoolbox.com/en/latest/?badge=latest)

This repository contains the source documents for the [Rebel Toolbox](https://rebeltoolbox.com) and [Rebel Engine](https://github.com/RebelToolbox/RebelEngine) user documentation: https://docs.rebeltoolbox.com.

The documentation uses the [reStructuredText](https://docutils.sourceforge.io/rst.html) (reST) file format.
The Rebel Documentation website is generated using [Sphinx](https://www.sphinx-doc.org/),
which uses [Docutils](https://docutils.sourceforge.io/) to convert the reST files to html.

## Contributing changes

Updates to the documentation can be made here, directly on Github.
Contributions are submitted via [Pull Requests](https://docs.github.com/en/pull-requests).
To learn more about making Pull Requests, please refer to the [Github documentation](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).
If you plan on making significant contributions to Rebel Documentation,
you will want to learn how to use Git.
For good tutorials on using Git, try the [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials).

The Rebel Engine API documentation files are included under the `classes` folder.
They are automatically generated from Rebel Engine's [XML class references](https://github.com/RebelToolbox/RebelEngine/tree/main/doc/classes).
These are maintained in [Rebel Engine](https://github.com/RebelToolbox/RebelEngine) under the `doc` folder.
Please make updates and Pull Requests to the API documenation there.
See the [Contributing to the Class Reference](https://docs.rebeltoolbox.com/en/latest/contributing/updating_the_class_reference.html) documentation for more information.

To edit an existing page, simply locate and edit its `.rst` file.
The file can be edited directly here on Github or you can edit it in your favorite text editor.
For an introduction to the `.rst` file format, refer to the Sphinx [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).
For more information on how Sphinx extends reStructuredText, refer to the [Using Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html).
For more information on reStructuredText, refer to the Docutils' [reStructuredText documentation](https://docutils.sourceforge.io/rst.html).

To add a new page, create a `.rst` file with a meaningful name in the section you want to add the documentation e.g. `tutorials/3d/light_baking.rst`.
The documentation is divided into sections defined by the folder structure.
Add the new page to the section's table of contents file e.g. `tutorials/3d/index.rst`.
Under the `.. toctree::` directive, include the filename without the extension.

To add an image to a page, place the image in the `img` folder in the folder that contains the page.
Use a meaningful name, and reference the image in the page with:
```rst
.. image:: img/light_baking_result.png
```

To add a downloadable file to a page, place the file in the `files` folder in the folder that contains the page.
Use a meaningful name, and reference the file in the page with:
```rst
:download:`Light Baking Project <files/light-backing-project.zip>`
```

## Building the documentation with Sphinx

To test significant changes before creating a Pull Request, you can build a local copy of the Rebel Documentation website.
To do this, you will need a local copy of the Rebel Documentation.

Building the documentation requires Python.
For more information on installing Python, refer to the [Python documentation](https://www.python.org/downloads/). 

It is recommended that you build the documentation inside a virtual Python environment.
Keep your Python virtual environments separate from your local copy of the Rebel Documentation.
Create a virtual environment called `env` in your separate virtual environments folder,
and activate it.

On Linux or Mac run:
```sh
virtualenv env
source env/bin/activate
```
On Windows run:
```sh
virtualenv env
.\env\Scripts\activate
```
For more information on installing and using `virtualenv`, refer to the [virtualenv documentation](https://virtualenv.pypa.io/en/latest/index.html).

Install the required software.
From a command prompt inside the folder containing your local copy of the Rebel Documentation, run:
```sh
pip install -r requirements.txt
```

Build the html documentation.

On Linux or Mac run:
```sh
make html
```
On Windows run:
```sh
.\make.bat html
```

You can view your changes by opening `_build/html/index.html` in your favorite browser.

The compilation can be slow and might take a long time.
It might even fail with a `MemoryError` or an `EOFError` error.
The Rebel Engine API in the `classes` folder contains a lot of files.
To fix or speed up the build, remove the `classes` folder and run `make html` again.
**Note:** If you have created your local copy of the Rebel Documentation using `git clone`,
don't use `git add .`, because it will delete the Rebel Engine API documentation.


## License

With the exception of the `classes` folder, all the content in this repository is licensed under the Creative Commons Attribution 4.0 International Public License ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)). Attribution should be made to the Rebel Documentation Contributors and/or the specific author.

The files in the `classes` folder are derived from [Rebel Engine](https://github.com/RebelToolbox/RebelEngine) and are distributed under the MIT license.
