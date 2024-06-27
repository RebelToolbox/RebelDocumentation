.. _doc_data_paths:

File paths in Rebel projects
============================

This page explains how file paths work inside Rebel projects. You will learn how
to access paths in your projects using the ``res://`` and ``user://`` notations
and where Rebel stores user files on your hard-drive.

Path separators
---------------

To make supporting multiple platforms easier, Rebel Engine only accepts UNIX-style path
separators (``/``). These work on all platforms, **including Windows**.

Instead of writing paths like ``C:\Projects``, in Rebel Editor, you should write
``C:/Projects``.

Accessing files in the project folder
-------------------------------------

Rebel Editor considers that a project exists in any folder that contains a
``project.rebel`` text file, even if the file is empty. The folder that contains
this file is your project's root folder.

You can access any file relative to it by writing paths starting with
``res://``, which stands for resources. For example, you can access an image
file ``character.png`` located in the project's root folder in code with the
following path: ``res://character.png``.

Accessing persistent user data
------------------------------

To store persistent data files, like the player's save or settings, you want to
use ``user://`` instead of ``res://`` as your path's prefix. This is because
when the game is running, the project's file system will likely be read-only.

The ``user://`` prefix points to a different directory on the user's device.
Unlike ``res://``, the directory pointed at by ``user://`` is *guaranteed* to be
writable to, even in an exported project.

On desktop platforms, the actual directory paths for ``user://`` are:

+-------------------------------+------------------------------------------------------------------------------+
| Type                          | Location                                                                     |
+===============================+==============================================================================+
| User data                     | - Windows: ``%APPDATA%\Rebel\app_userdata\[project_name]``                   |
|                               | - macOS: ``~/Library/Application Support/Rebel/app_userdata/[project_name]`` |
|                               | - Linux: ``~/.local/share/rebel/app_userdata/[project_name]``                |
+-------------------------------+------------------------------------------------------------------------------+
| User data                     | - Windows: ``%APPDATA%\[project_name]``                                      |
| (when ``use_custom_user_dir`` | - macOS: ``~/Library/Application Support/[project_name]``                    |
| project setting is ``true``)  | - Linux: ``~/.local/share/[project_name]``                                   |
+-------------------------------+------------------------------------------------------------------------------+

``[project_name]`` is based on the application name defined in the Project Settings, but
you can override it on a per-platform basis using :doc:`feature tags </tutorials/export/feature_tags>`.

On mobile platforms, this path is unique to the project and is not accessible
by other applications for security reasons.

On HTML5 exports, ``user://`` will refer to a virtual filesystem stored on the
device via IndexedDB. (Interaction with the main filesystem can still be performed
through the :ref:`JavaScript <class_JavaScript>` singleton.)

Editor data paths
-----------------

The editor uses different paths for user data, user settings, and cache,
depending on the platform. By default, these paths are:

+-------------------------------+----------------------------------------------------------------+
| Type                          | Location                                                       |
+===============================+================================================================+
| User data                     | - Windows: ``%APPDATA%\Rebel\app_userdata\[project_name]``     |
|                               | - macOS: ``~/Library/Application Support/Rebel/[project_name]``|
|                               | - Linux: ``~/.local/share/rebel/[project_name]``               |
+-------------------------------+----------------------------------------------------------------+
| User data                     | - Windows: ``%APPDATA%\[project_name]``                        |
| (when ``use_custom_user_dir`` | - macOS: ``~/Library/Application Support/[project_name]``      |
| project setting is ``true``)  | - Linux: ``~/.local/share/[project_name]``                     |
+-------------------------------+----------------------------------------------------------------+
| User settings                 | - Windows: ``%APPDATA%\Rebel\``                                |
|                               | - macOS: ``~/Library/Application Support/Rebel/``              |
|                               | - Linux: ``~/.config/rebel/``                                  |
+-------------------------------+----------------------------------------------------------------+
| Cache                         | - Windows: ``%TEMP%\Rebel\``                                   |
|                               | - macOS: ``~/Library/Caches/Rebel/``                           |
|                               | - Linux: ``~/.cache/rebel/``                                   |
+-------------------------------+----------------------------------------------------------------+

- **User data** contains export templates and project-specific data.
- **User settings** contains editor settings, text editor themes, script
  templates, etc.
- **Cache** contains temporary data. It can safely be removed when Rebel Editor is
  closed.

Rebel Engine complies with the `XDG Base Directory Specification
<https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>`__
on all platforms. You can override environment variables following the
specification to change the editor and project data paths.

.. _doc_data_paths_self_contained_mode:

Self-contained mode
~~~~~~~~~~~~~~~~~~~

If you create a file called ``._sc_`` or ``_sc_`` in the same directory as the
editor binary, Rebel Engine will enable *self-contained mode*. This mode makes Rebel Engine
write all user data to a directory named ``editor_data/`` in the same directory
as the editor binary. You can use it to create a portable installation of the
editor.

.. note::

    Self-contained mode is not supported in exported projects yet.
    To read and write files relative to the executable path, use
    :ref:`OS.get_executable_path() <class_OS_method_get_executable_path>`.
    Note that writing files in the executable path only works if the executable
    is placed in a writable location (i.e. **not** Program Files or another
    directory that is read-only for regular users).
