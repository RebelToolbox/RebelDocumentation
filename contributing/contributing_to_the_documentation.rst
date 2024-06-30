Contributing to the documentation
=================================

This guide explains how to contribute to Rebel Toolbox's documentation, be it by
writing or reviewing pages.

Getting started
---------------

To modify or create pages in the reference manual, you need to edit ``.rst``
files in the `Rebel Documentation repository on GitHub <https://github.com/RebelToolbox/RebelDocumentation>`__.
Modifying those pages in a pull request triggers a rebuild of the online documentation upon merging.

.. seealso:: For details on Git usage and the pull request workflow, please
             refer to the :doc:`pr_workflow` page.

.. warning:: The API documentation source files are in the `Rebel Engine
             repository <https://github.com/RebelToolbox/RebelEngine>`_. We generate
             the :ref:`Rebel API <toc-api>` section of this documentation
             from them. If you want to update the description of a class, its
             methods, or properties, read
             :doc:`updating_the_api_documentation`.

What is the Rebel Documentation
-------------------------------

The Rebel Documentation is intended as a comprehensive reference manual for Rebel Toolbox.
It is not meant to contain step-by-step tutorials, except for
two game creation tutorials in the Getting Started section.

We strive to write factual content in an accessible and well-written language. To
contribute, you should also read:

1. The :doc:`/contributing/docs_writing_guidelines`. There, you will find rules and
   recommendations to write in a way that everyone understands.
2. The content guidelines. They explain the principles we follow to write the
   documentation and the kind of content we accept.

Contributing changes
--------------------

**Pull Requests should use the** ``main`` **branch by default.** Only make Pull
Requests against other branches if your changes only apply to that specific version of the documentation.

Though less convenient to edit than a wiki, this Git repository is where we
write the documentation. Having direct access to the source files in a revision
control system is a plus to ensure our documentation quality.

Editing existing pages
~~~~~~~~~~~~~~~~~~~~~~

To edit an existing page, locate its ``.rst`` source file and open it in your
favorite text editor. You can then commit the changes, push them to your fork,
and make a pull request. **Note that the pages in** ``api/`` **should not be
edited here.** They are automatically generated from Rebel Engine's `XML class
reference <https://github.com/RebelToolbox/RebelEngine/tree/main/docs>`__.
See :doc:`updating_the_api_documentation` for details.

.. seealso:: To build the manual and test changes on your computer, see
             :doc:`building_the_documentation`.

Editing pages online
--------------------

You can edit the documentation online by clicking the **Edit on GitHub** link in
the top-right of every page.

Doing so takes you to the GitHub text editor. You need to have a GitHub account
and to log in to use it. Once logged in, you can propose change like so:

1. Click the **Edit on GitHub** button.

2. On the GitHub page you're taken to, click the pencil icon in the top-right
   corner near the **Raw**, **Blame**, and **Delete** buttons. It has the
   tooltip "Fork this project and edit the file".

3. Edit the text in the text editor.

4. At the bottom of the web page, summarize the changes you made and click the
   button **Propose file change**. Make sure to replace the placeholder "Update file.rst"
   by a short but clear one-line description, as this is the commit title.

5. On the following screens, click the **Create pull request** button until you
   see a message like *<YourUsername> wants to merge 1 commit into RebelToolbox:main
   from <YourUsername>:patch-1*.

Another contributor will review your changes and merge them into the docs if
they're good. They may also make changes or ask you to do so before merging.

Adding new pages
----------------

Before adding a new page, please ensure that it fits in the documentation:

1. Look for `existing issues
   <https://github.com/RebelToolbox/RebelEngine/issues>`_ or open a new one to see
   if the page is necessary.
2. Ensure there isn't a page that already covers the topic.
3. Read our :doc:`content_guidelines`.

To add a new page, create a ``.rst`` file with a meaningful name in the section you
want to add a file to, e.g. ``tutorials/3d/light_baking.rst``.

You should then add your page to the relevant "toctree" (table of contents,
e.g. ``tutorials/3d/index.rst``). Add your new filename to the list on a new
line, using a relative path and no extension, e.g. here ``light_baking``.

Titles
~~~~~~

Always begin pages with their title::

    Insert your title here
    ======================

Write your titles like plain sentences, without capitalizing each word:

-  **Good:** Understanding signals in Rebel Engine
-  **Bad:** Understanding Signals In Rebel Engine

Only propers nouns, projects, people, and node class names should have their
first letter capitalized.

Sphinx and reStructuredText syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check Sphinx’s `reST Primer <https://www.sphinx-doc.org/en/stable/rest.html>`__
and the `official reference <http://docutils.sourceforge.net/rst.html>`__ for
details on the syntax.

Sphinx uses specific reST comments to do specific operations, like defining the
table of contents (``.. toctree::``) or cross-referencing pages. Check the
`official Sphinx documentation
<https://www.sphinx-doc.org/en/stable/index.html>`__ for more details. To learn
how to use Sphinx directives like ``.. note::`` or ``.. seealso::``, check out
the `Sphinx directives documentation
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`__.

Adding images and attachments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add images, please put them in an ``img/`` folder next to the ``.rst`` file with
a meaningful name and include them in your page with:

.. code:: rst

   .. image:: img/image_name.png

Similarly, you can include attachments, like assets as support material for a
tutorial, by placing them into a ``files/`` folder next to the ``.rst`` file, and
using this inline markup:

.. code:: rst

   :download:`myfilename.zip <files/myfilename.zip>`
