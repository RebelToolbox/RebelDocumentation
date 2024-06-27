.. _doc_about_intro:

Introduction
============

::

    func _ready():
        $Label.text = "Hello world!"

Welcome to the official documentation of Rebel Engine, the free and open source
community-driven 2D and 3D game engine! Behind this mouthful, you will find a
powerful yet user-friendly tool that you can use to develop any kind of game,
for any platform and with no usage restriction whatsoever.

This page gives a broad presentation of the engine and of the contents
of this documentation, so that you know where to start if you are a beginner or
where to look if you need info on a specific feature.

About Rebel Engine
------------------

A game engine is a complex tool, and it is therefore difficult to present Rebel Engine
in a few words. Here's a quick synopsis, which you are free to reuse
if you need a quick writeup about Rebel Engine.

    Rebel Engine is a feature-packed, cross-platform game engine to create 2D
    and 3D games from a unified interface. It provides a comprehensive set of
    common tools, so users can focus on making games without having to
    reinvent the wheel. Games can be exported in one click to a number of
    platforms, including the major desktop platforms (Linux, macOS, Windows)
    as well as mobile (Android, iOS) and web-based (HTML5) platforms.

    Rebel Engine is completely free and open source under the permissive MIT
    license. No strings attached, no royalties, nothing. Users' games are
    theirs, down to the last line of engine code. Rebel Engine's development is fully
    independent and community-driven, empowering users to help shape their
    engine to match their expectations. It is supported by the `Software
    Freedom Conservancy <https://sfconservancy.org>`_ not-for-profit.

For a more in-depth view of the engine, you are encouraged to read this
documentation further, especially the :ref:`Step by step
<toc-learn-step_by_step>` tutorial.

About the documentation
-----------------------

This documentation is continuously written, corrected, edited, and revamped by
members of the Rebel Toolbox community. It is edited via text files in the
`reStructuredText <http://www.sphinx-doc.org/en/stable/rest.html>`_ markup
language and then compiled into a static website/offline document using the
open source `Sphinx <http://www.sphinx-doc.org>`_ and `ReadTheDocs
<https://readthedocs.org/>`_ tools.

.. note:: You can contribute to Rebel Engine's documentation by opening issue tickets
          or sending patches via pull requests on its GitHub
          `source repository <https://github.com/RebelToolbox/RebelDocumentation>`_.

All the contents are under the permissive Creative Commons Attribution 4.0 International
(`CC-BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_) license, with
attribution to "Rebel Toolbox Community".

Organization of the documentation
---------------------------------

This documentation is organized in five sections with an impressively
unbalanced distribution of contents – but the way it is split up should be
relatively intuitive:

- The :ref:`sec-general` section contains this introduction as well as
  information about the engine, its history, its licensing, authors, etc. It
  also contains the :doc:`faq`.
- The :ref:`sec-learn` section is the primary reason for this
  documentation, as it contains all the necessary information on using the
  engine to make games. It starts with the :ref:`Step by step
  <toc-learn-step_by_step>` tutorial which should be the entry point for all
  new users.
- The :ref:`sec-tutorials` section can be read as needed,
  in any order. It contains feature-specific tutorials and documentation.
- The :ref:`sec-devel` section is intended for advanced users and contributors
  to the engine development, with information on compiling the engine,
  developing C++ modules or editor plugins.
- The :ref:`sec-contributing` section gives information related to contributing to
  engine development, how to report bugs,
  help with the documentation, etc.
- Finally, the :ref:`sec-api` is the documentation of the Rebel Engine API,
  which is also available directly within the engine's script editor. It is
  generated automatically from a file in the main source repository, therefore
  the generated files of the documentation are not meant to be modified. See
  :doc:`/contributing/updating_the_api_documentation` for details.

Have fun reading and making games with Rebel Engine!
