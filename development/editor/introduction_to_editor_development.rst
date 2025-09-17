Introduction to editor development
==================================

On this page, you will learn:

- The **design decisions** behind the Rebel Editor.
- How to work efficiently on the Rebel Editor's C++ code.

This guide is aimed at current or future engine contributors.
To create editor plugins in GDScript, see :doc:`/tutorials/plugins/editor/making_plugins` instead.

.. seealso::

    If you are new to Rebel, we recommended you to read
    :doc:`/getting_started/introduction/design_philosophy` before continuing. Since the Rebel Editor
    is a Rebel project written in C++, much of the engine's philosophy applies
    to the editor.

Technical choices
-----------------

The Rebel Editor is drawn using Rebel's renderer and
:ref:`UI system <toc-gui-basics>`. It does *not* rely on a toolkit
such as GTK or Qt. This is similar in spirit to software like Blender.
While using toolkits makes it easier to achieve a "native" appearance, they are
also quite heavy and their licensing is not compatible with Rebel Engine's.

The editor is fully written in C++. It can't contain any GDScript or C# code.

Directory structure
-------------------

The editor's code is fully self-contained in the
`editor/ <https://github.com/RebelToolbox/RebelEngine/tree/main/editor>`__ folder
of the Rebel Engine source repository.

Some editor functionality is also implemented via
:doc:`modules </development/engine/custom_modules_in_cpp>`. Some of these are only enabled in
editor builds to decrease the binary size of export templates. See the
`modules/ <https://github.com/RebelToolbox/RebelEngine/tree/main/modules>`__ folder
in the Rebel Engine source repository.

Some important files in the editor are:

- `editor/editor_node.h <https://github.com/RebelToolbox/RebelEngine/blob/main/editor/editor_node.h>`__:
  Main editor initialization file. Effectively the "main scene" of the editor.
- `editor/project_manager.h <https://github.com/RebelToolbox/RebelEngine/blob/main/editor/project_manager.h>`__:
  Main project manager initialization file. Effectively the "main scene" of the project manager.
- `editor/plugins/canvas_item_editor_plugin.h <https://github.com/RebelToolbox/RebelEngine/blob/main/editor/plugins/canvas_item_editor_plugin.h>`__:
  The 2D editor viewport and related functionality (toolbar at the top, editing modes, overlaid helpers/panels, …).
- `editor/plugins/spatial_editor_plugin.h <https://github.com/RebelToolbox/RebelEngine/blob/main/editor/plugins/spatial_editor_plugin.h>`__:
  The 3D editor viewport and related functionality (toolbar at the top, editing modes, overlaid panels, …).
- `editor/spatial_editor_gizmos.h <https://github.com/RebelToolbox/RebelEngine/blob/main/editor/spatial_editor_gizmos.h>`__:
  Where the 3D editor gizmos are defined and drawn.
  This file doesn't have a 2D counterpart as 2D gizmos are drawn by the nodes themselves.

Editor dependencies in ``scene/`` files
---------------------------------------

When working on an editor feature, you may have to modify files in
Rebel Engine's GUI nodes, which you can find in the ``scene/`` folder.

One rule to keep in mind is that you must **not** introduce new dependencies to
``editor/`` includes in other folders such as ``scene/``. This applies even if
you use ``#ifdef TOOLS_ENABLED``.

To make the codebase easier to follow and more self-contained, the allowed
dependency order is:

- ``editor/`` -> ``scene/`` -> ``servers/`` -> ``core/``

This means that files in ``editor/`` can depend on includes from ``scene/``,
``servers/``, and ``core/``. But, for example, while ``scene/`` can depend on includes
from ``servers/`` and ``core/``, it cannot depend on includes from ``editor/``.

Currently, there are some dependencies to ``editor/`` includes in ``scene/``
files, see `Github issue <https://github.com/godotengine/godot/issues/29730>`__.

Development tips
----------------

To iterate quickly on the editor, we recommend to set up a test project and
:doc:`open it from the command line </tutorials/editor/command_line_tutorial>` after compiling
the editor. This way, you don't have to go through the project manager every
time you start Rebel Editor.
