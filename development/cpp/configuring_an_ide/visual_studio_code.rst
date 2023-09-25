.. _doc_configuring_an_ide_vscode:

Visual Studio Code
==================

`Visual Studio Code <https://code.visualstudio.com>`_ is a free cross-platform code editor
by `Microsoft <https://microsoft.com>`_ (not to be confused with :ref:`doc_configuring_an_ide_vs`).

Importing the project
---------------------

- Make sure the C/C++ extension is installed. You can find instructions in
  the `official documentation <https://code.visualstudio.com/docs/languages/cpp>`_.
  Alternatively, `clangd <https://open-vsx.org/extension/llvm-vs-code-extensions/vscode-clangd>`_
  can be used instead.
- When using the clangd extension, run ``scons compiledb=yes``.
- From the Visual Studio Code's main screen open the Godot root folder with
  **File > Open Folder...**.
- Press :kbd:`Ctrl + Shift + P` to open the command prompt window and enter *Configure Task*.

.. figure:: img/vscode_configure_task.png
   :align: center

- Select the **Create tasks.json file from template** option.

.. figure:: img/vscode_create_tasksjson.png
   :align: center

- Then select **Others**.

.. figure:: img/vscode_create_tasksjson_others.png
   :align: center

- Within the ``tasks.json`` file find the ``"tasks"`` array and add a new section to it:

.. tabs::
  .. code-tab:: js Linux/X11

    {
      "label": "build",
      "group": "build",
      "type": "shell",
      "command": "scons",
      "args": [
        "-j $(nproc)"
      ],
      "problemMatcher": "$msCompile"
    }

  .. code-tab:: js Windows

    {
      "label": "build",
      "group": "build",
      "type": "shell",
      "command": "scons",
      "args": [
        // Use this when your default shell is Command Prompt (cmd.exe).
        "-j %NUMBER_OF_PROCESSORS%",
        // Use this when your default shell is PowerShell.
        "-j $env:NUMBER_OF_PROCESSORS"
      ],
      "problemMatcher": "$msCompile"
    }

.. figure:: img/vscode_3_tasks.json.png
   :figclass: figure-w480
   :align: center

   An example of a filled out ``tasks.json``.

Arguments can be different based on your own setup and needs. See
:ref:`doc_introduction_to_the_buildsystem` for a full list of arguments.

Debugging the project
---------------------

To run and debug the project you need to create a new configuration in the ``launch.json`` file.

- Press :kbd:`Ctrl + Shift + D` to open the Run panel.
- If ``launch.json`` file is missing you will be prompted to create a new one.

.. figure:: img/vscode_1_create_launch.json.png
   :align: center

- Select **C++ (GDB/LLDB)**. There may be another platform specific option here. If selected,
  adjust the configuration example provided accordingly.
- Within the ``launch.json`` file find the ``"configurations"`` array and add a new section to it:

.. tabs::
  .. code-tab:: js X11

    {
      "name": "Launch Project",
      "type": "lldb",
      "request": "launch",
      // Change to godot.x11.tools.64.llvm for llvm-based builds.
      "program": "${workspaceFolder}/bin/godot.x11.tools.64",
      // Change the arguments below for the project you want to test with.
      // To run the project instead of editing it, remove the "--editor" argument.
      "args": [ "--editor", "--path", "path-to-your-godot-project-folder" ],
      "stopAtEntry": false,
      "cwd": "${workspaceFolder}",
      "environment": [],
      "externalConsole": false,
      "preLaunchTask": "build"
    }
  .. code-tab:: js X11_gdb

    {
      "name": "Launch Project",
      "type": "cppdbg",
      "request": "launch",
      // Change to godot.x11.tools.64.llvm for llvm-based builds.
      "program": "${workspaceFolder}/bin/godot.x11.tools.64",
      // Change the arguments below for the project you want to test with.
      // To run the project instead of editing it, remove the "--editor" argument.
      "args": [ "--editor", "--path", "path-to-your-godot-project-folder" ],
      "stopAtEntry": false,
      "cwd": "${workspaceFolder}",
      "environment": [],
      "externalConsole": false,
      "setupCommands":
      [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        }
      ],
      "preLaunchTask": "build"
    }

  .. code-tab:: js Windows

    {
      "name": "Launch Project",
      "type": "cppvsdbg",
      "request": "launch",
      "program": "${workspaceFolder}/bin/godot.windows.tools.64.exe",
      // Change the arguments below for the project you want to test with.
      // To run the project instead of editing it, remove the "--editor" argument.
      "args": [ "--editor", "--path", "path-to-your-godot-project-folder" ],
      "stopAtEntry": false,
      "cwd": "${workspaceFolder}",
      "environment": [],
      "console": "internalConsole",
      "visualizerFile": "${workspaceFolder}/platform/windows/godot.natvis",
      "preLaunchTask": "build"
    }

.. figure:: img/vscode_2_launch.json.png
   :figclass: figure-w480
   :align: center

   An example of a filled out ``launch.json``.


.. note::

    Due to sporadic performance issues, it is recommended to use LLDB over GDB on Unix-based systems.
    Make sure that the `CodeLLDB extension <https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb>`_
    is installed.

    If you encounter issues with lldb, you may consider using gdb (see the X11_gdb configuration).

    Do note that lldb may work better with llvm-based builds. See :ref:`doc_compiling_for_x11` for further information.

The name under ``program`` depends on your build configuration,
e.g. ``godot.x11.tools.64`` for 64-bit X11 platform with ``tools`` enabled.

If you run into any issues, ask for help in one of
`Godot's community channels <https://godotengine.org/community>`__.
