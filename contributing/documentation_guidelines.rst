.. _doc_documentation_guidelines:

Documentation guidelines
========================

This page describes the rules to follow if you want to contribute to Rebel
Toolbox by writing or reviewing documentation, or by translating existing
documentation. Also, have a look at README of the
`Rebel Documentation GitHub repository <https://github.com/RebelToolbox/RebelDocumentation>`_
and the `docs front page <https://docs.rebeltoolbox.com>`_
on what steps to follow.

How to contribute
-----------------

Creating or modifying documentation pages is mainly done via the
`Rebel Documentation GitHub repository <https://github.com/RebelToolbox/RebelDocumentation>`_.
The HTML (or PDF and EPUB) documentation is generated from the .rst files
(reStructuredText markup language) in that repository. Modifying those pages
in a pull request and getting it merged will trigger a rebuild of the online
documentation.

.. seealso:: For details on Git usage and the pull request workflow, please
             refer to the :ref:`doc_pr_workflow` page.

.. warning:: The API documentation's source files are in the `Rebel Engine repository
             <https://github.com/RebelToolbox/RebelEngine>`_. We generate the :ref:`Rebel API
             <toc-api>` section of this documentation from them. If you want to update the
             description of a class, its methods, or properties, read
             :ref:`doc_updating_the_api_documentation`.

.. warning:: If you want to edit the **Rebel Engine API**, please note that it
             should *not* be done in the Rebel Documentation repository. Instead, you
             should edit the XML files in the ``docs/`` folder of Rebel Engine's
             repository. These files are then later used to generate the
             in-editor documentation as well as the API reference of the
             online docs. Read more here: :ref:`doc_updating_the_api_documentation`.

The 'Edit on GitHub' link
-------------------------

If you're reading documentation on `docs.rebeltoolbox.com <https://docs.rebeltoolbox.com>`_,
you'll see an **Edit on GitHub** hyperlink at the top right of the page.
Once you've created a GitHub account, you can propose changes to a page you're
reading as follows:

1. Click the **Edit on GitHub** button.

2. On the GitHub page you're taken to, click the pencil icon in the top-right
   corner near the **Raw**, **Blame** and **History** buttons. It has the tooltip
   "Edit the file in a fork of this project".

3. Complete all the edits you want to make for that page.

4. Summarize the changes you made in the form at the bottom of the page and
   click the button labelled **Propose file change** when done.

5. On the following screens, click the **Create pull request** button until you
   see a message like *Username wants to merge 1 commit into
   RebelDocumentation:main from Username:patch-1*.

6. A reviewer will evaluate your changes and incorporate them into the docs if
   they're acceptable. You might also be asked to make
   modifications to your changes before they're included.

What makes good documentation?
------------------------------

Documentation should be well written in plain English, using well-formed
sentences and various levels of sections and subsections. It should be clear
and objective. Also, have a look at the :ref:`doc_docs_writing_guidelines`.

We differentiate tutorial pages from other documentation pages by these
definitions:

-  Tutorial: a page aiming at explaining how to use one or more concepts in
   the editor or scripts in order to achieve a specific goal with a learning
   purpose (e.g. "Making a simple 2d Pong game", "Applying forces to an
   object").
-  Documentation: a page describing precisely one and only one concept at a
   time, if possible exhaustively (e.g. the list of methods of the
   Sprite class, or an overview of the input management in Rebel Engine).

You are free to write the kind of documentation you wish, as long as you
respect the following rules (and the ones on the repo).

Titles
------

Always begin pages with their title and a Sphinx reference name:

::

    .. _doc_insert_your_title_here:

    Insert your title here
    ======================

The reference allows linking to this page using the ``:ref:`` format, e.g.
``:ref:`doc_insert_your_title_here``` would link to the above example page
(note the lack of leading underscore in the reference).

Also, avoid American CamelCase titles: title's first word should begin
with a capitalized letter, and every following word should not. Thus,
this is a good example:

-  Insert your title here

And this is a bad example:

-  Insert Your Title Here

Only project, people and node class names should have capitalized first
letter.
