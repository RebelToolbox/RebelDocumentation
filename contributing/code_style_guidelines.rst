.. _doc_code_style_guidelines:

Code style guidelines
=====================

.. highlight:: shell

When contributing to Rebel Engine's source code, you will be expected to follow the
style guidelines outlined below. Some of them are checked via the Continuous
Integration process and reviewers will ask you to fix potential issues, so
best setup your system as outlined below to ensure all your commits follow the
guidelines.

C++ and Objective-C
-------------------

There are no written guidelines, but the code style agreed upon by the
developers is enforced via the `clang-format <http://clang.llvm.org/docs/ClangFormat.html>`__
code beautifier, which takes care for you of all our conventions.
To name a few:

- Indentation and alignment are both tab based (respectively one and two tabs)
- One space around math and assignments operators as well as after commas
- Pointer and reference operators are affixed to the variable identifier, not
  to the type name
- See further down regarding header includes

The rules used by clang-format are outlined in the
`.clang-format <https://github.com/RebelToolbox/RebelEngine/blob/main/.clang-format>`__
file of the Rebel Engine repository.

As long as you ensure that your style matches the surrounding code and that you
not introducing trailing whitespace or space-based indentation, you should be
fine. If you plan to contribute regularly however, we strongly advise that you
setup clang-format locally to check and automatically fix all your commits.

.. warning:: Rebel's code style should *not* be applied to third-party code,
             i.e. that is included in Rebel Engine's source tree but was not written
             specifically for our project. Such code usually come from
             different upstream projects with their own style guides (or lack
             thereof), and don't want to introduce differences that would make
             syncing with upstream repositories harder.

             Third-party code is usually included in the ``thirdparty/`` folder
             and can thus easily be excluded from formatting scripts. For the
             rare cases where a third-party code snippet needs to be included
             directly within a Rebel Engine file, you can use
             ``/* clang-format off */`` and ``/* clang-format on */`` to tell
             clang-format to ignore a chunk of code.

.. seealso::

    These guidelines only cover code formatting. See :doc:`cpp_usage_guidelines`
    for a list of language features that are permitted in pull requests.

Using clang-format locally
~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all, you will need to install clang-format.

Installing clang-format
^^^^^^^^^^^^^^^^^^^^^^^

Here's how to install clang-format:

- Linux: It will usually be available out-of-the-box with the clang toolchain
  packaged by your distribution. If your distro version is not the required one,
  you can download a pre-compiled version from the
  `LLVM website <http://releases.llvm.org/download.html>`__, or if you are on
  a Debian derivative, use the `upstream repos <http://apt.llvm.org/>`__.
- macOS and Windows: You can download precompiled binaries from the
  `LLVM website <http://releases.llvm.org/download.html>`__. You may need to add
  the path to the binary's folder to your system's ``PATH`` environment
  variable to be able to call ``clang-format`` out of the box.

You then have different possibilities to apply clang-format to your changes:

Running clang-format
^^^^^^^^^^^^^^^^^^^^

You can apply clang-format manually one or more files with the following
command:

::

    clang-format -i <path/to/file(s)>

- ``-i`` means that the changes should be written directly to the file (by
  default clang-format would only output the fixed version to the terminal).
- The path can point to several files, either one after the other or using
  wildcards like in a typical Unix shell. Be careful when globbing so that
  you don't run clang-format on compiled objects (.o and .a files) that are
  in Rebel Engine's tree. So better use ``core/*.{cpp,h}`` than ``core/*``.

Pre-commit clang-format hook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For ease of use, we provide a pre-commit hook for Git that will run
clang-format automatically on all your commits to check them, and let you apply
its changes in the final commit.

This "hook" is a script which can be found in ``tools/hooks``, refer to that
folder's README.md for installation instructions.

If your clang-format is not in the ``PATH``, you may have to edit the
``pre-commit-clang-format`` to point to the correct binary for it to work.
The hook was tested on Linux and macOS, but should also work in the Git Shell
on Windows.

IDE plugin
^^^^^^^^^^

Most IDEs or code editors have beautifier plugins that can be configured to run
clang-format automatically, for example each time you save a file.

Here is a non-exhaustive list of beautifier plugins for some IDEs:

- Qt Creator: `Beautifier plugin <http://doc.qt.io/qtcreator/creator-beautifier.html>`__
- Visual Studio Code: `Clang-Format <https://marketplace.visualstudio.com/items?itemName=xaver.clang-format>`__
- Visual Studio: `ClangFormat <https://marketplace.visualstudio.com/items?itemName=LLVMExtensions.ClangFormat>`__
- vim: `vim-clang-format <https://github.com/rhysd/vim-clang-format>`__
- CLion: Starting from version ``2019.1``, no plugin is required. Instead, enable
  `ClangFormat <https://www.jetbrains.com/help/clion/clangformat-as-alternative-formatter.html#clion-support>`__

(Pull requests welcome to extend this list with tested plugins.)

.. _doc_code_style_guidelines_header_includes:

Header includes
~~~~~~~~~~~~~~~

When adding new C++ or Objective-C files or including new headers in existing
ones, the following rules should be followed:

- The first lines in the file should be Rebel Engine's copyright header and MIT
  license, copy-pasted from another file. Make sure to adjust the filename.
- In a ``.h`` header, include guards should be used with the form
  ``FILENAME_H``.

- In a ``.cpp`` file (e.g. ``filename.cpp``), the first include should be the
  one where the class is declared (e.g. ``#include "filename.h"``), followed by
  an empty line for separation.
- Then come headers from Rebel Engine's own code base, included in alphabetical order
  (enforced by ``clang-format``) with paths relative to the root folder. Those
  includes should be done with quotes, e.g. ``#include "core/object.h"``. The
  block of Rebel Engine header includes should then be followed by an empty line for
  separation.
- Finally, third-party headers (either from ``thirdparty`` or from the system's
  include paths) come next and should be included with the < and > symbols, e.g.
  ``#include <png.h>``. The block of third-party headers should also be followed
  by an empty line for separation.
- Rebel Engine and third-party headers should be included in the file that requires
  them, i.e. in the `.h` header if used in the declarative code or in the `.cpp`
  if used only in the imperative code.

Example:

.. code-block:: cpp

    /*************************************************************************/
    /*  my_new_file.h                                                        */
    /*************************************************************************/
    /*                       This file is part of:                           */
    /*                           REBEL ENGINE                                */
    /*************************************************************************/
    /* Copyright (c) 2022-Present Rebel Engine contributors                  */
    /* Copyright (c) 2014-2022 Godot Engine contributors                     */
    /* Copyright (c) 2007-2014 Juan Linietsky, Ariel Manzur                  */
    /*                                                                       */
    /* Permission is hereby granted, free of charge, to any person obtaining */
    /* a copy of this software and associated documentation files (the       */
    /* "Software"), to deal in the Software without restriction, including   */
    /* without limitation the rights to use, copy, modify, merge, publish,   */
    /* distribute, sublicense, and/or sell copies of the Software, and to    */
    /* permit persons to whom the Software is furnished to do so, subject to */
    /* the following conditions:                                             */
    /*                                                                       */
    /* The above copyright notice and this permission notice shall be        */
    /* included in all copies or substantial portions of the Software.       */
    /*                                                                       */
    /* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,       */
    /* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    */
    /* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.*/
    /* IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY  */
    /* CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,  */
    /* TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE     */
    /* SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                */
    /*************************************************************************/

    #ifndef MY_NEW_FILE_H
    #define MY_NEW_FILE_H

    #include "core/hash_map.h"
    #include "core/list.h"
    #include "scene/gui/control.h"

    #include <png.h>

    ...

    #endif // MY_NEW_FILE_H

.. code-block:: cpp

    /*************************************************************************/
    /*  my_new_file.cpp                                                      */
    /*************************************************************************/
    /*                       This file is part of:                           */
    /*                           REBEL ENGINE                                */
    /*************************************************************************/
    /* Copyright (c) 2022-Present Rebel Engine contributors                  */
    /* Copyright (c) 2014-2022 Godot Engine contributors                     */
    /* Copyright (c) 2007-2014 Juan Linietsky, Ariel Manzur                  */
    /*                                                                       */
    /* Permission is hereby granted, free of charge, to any person obtaining */
    /* a copy of this software and associated documentation files (the       */
    /* "Software"), to deal in the Software without restriction, including   */
    /* without limitation the rights to use, copy, modify, merge, publish,   */
    /* distribute, sublicense, and/or sell copies of the Software, and to    */
    /* permit persons to whom the Software is furnished to do so, subject to */
    /* the following conditions:                                             */
    /*                                                                       */
    /* The above copyright notice and this permission notice shall be        */
    /* included in all copies or substantial portions of the Software.       */
    /*                                                                       */
    /* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,       */
    /* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    */
    /* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.*/
    /* IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY  */
    /* CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,  */
    /* TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE     */
    /* SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                */
    /*************************************************************************/

    #include "my_new_file.h"

    #include "core/math/math_funcs.h"
    #include "scene/gui/line_edit.h"

    #include <zlib.h>
    #include <zstd.h>

Java
----

Rebel Engine's Java code (mostly in ``platform/android``) is also enforced via
``clang-format``, so see the instructions above to set it up. Keep in mind that
this style guide only applies to code written and maintained by Rebel Engine, not
third-party code such as the ``java/src/com/google`` subfolder.

Python
------

Rebel Engine's SCons buildsystem is written in Python, and various scripts included
in the source tree are also using Python.

For those, we follow the `Black style guide <https://github.com/psf/black#the-black-code-style>`__.
Blacken your Python changes using `Black <https://pypi.org/project/black/>`__.

Using black locally
~~~~~~~~~~~~~~~~~~~

First of all, you will need to install black. Black requires Python 3.6.0+
to run.

Installing black
^^^^^^^^^^^^^^^^

Here's how to install black:

::

    pip3 install black --user


You then have different possibilities to apply black to your changes:

Running black
^^^^^^^^^^^^^

You can apply ``black`` manually to one or more files with the following
command:

::

    black -l 120 <path/to/file(s)>

- ``-l 120`` means that the allowed number of characters per line is 120.
  This number was agreed upon by the developers.
- The path can point to several files, either one after the other or using
  wildcards like in a typical Unix shell.

Pre-commit black hook
^^^^^^^^^^^^^^^^^^^^^

For ease of use, we provide a pre-commit hook for Git that will run
black automatically on all your commits to check them, and let you apply
its changes in the final commit.

This "hook" is a script which can be found in ``tools/hooks``. Refer to that
folder's ``README.md`` for installation instructions.


Editor integration
^^^^^^^^^^^^^^^^^^

Many IDEs or code editors have beautifier plugins that can be configured to run
black automatically, for example each time you save a file. For details you can
check `Black editor integration <https://github.com/psf/black#editor-integration>`__.

Comment style guide
-------------------

This comment style guide applies to all programming languages used within
Rebel Engine's codebase.

- Begin comments with a space character to distinguish them from disabled code.
- Use sentence case for comments. Begin comments with an uppercase character and
  always end them with a period.
- Reference variable/function names and values using backticks.
- Wrap comments to ~100 characters.
- You can use ``TODO:``, ``FIXME:``, ``NOTE:``, or ``HACK:`` as adominitions
  when needed.

**Example:**

.. code-block:: cpp

    // Compute the first 10,000 decimals of Pi.
    // FIXME: Don't crash when computing the 1,337th decimal due to `increment`
    //        being negative.

Don't repeat what the code says in a comment. Explain the *why* rather than *how*.

**Bad:**

.. code-block:: cpp

    // Draw loading screen.
    draw_load_screen();

You can use Javadoc-style comments above function or macro definitions. It's
recommended to use Javadoc-style comments *only* for methods which are not
exposed to scripting. This is because exposed methods should be documented in
the :doc:`API Documentation </contributing/updating_the_api_documentation>`
instead.

**Example:**

.. code-block:: cpp

    /**
     * Returns the number of nodes in the universe.
     * This can potentially be a very large number, hence the 64-bit return type.
     */
    uint64_t Universe::get_node_count() {
        // ...
    }

For member variables, don't use Javadoc-style comments but use single-line comments instead:

.. code-block:: cpp

    class Universe {
        // The cached number of nodes in the universe.
        // This value may not always be up-to-date with the current number of nodes
        // in the universe.
        uint64_t node_count_cached = 0;
    };
