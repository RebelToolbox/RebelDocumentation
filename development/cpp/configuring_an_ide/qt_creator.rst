Qt Creator
==========

`Qt Creator <https://doc.qt.io/qtcreator/index.html>`_ is a free, open source IDE for all desktop platforms.

Importing the project
---------------------

- From the Qt Creator's main screen select **New Project > Import Project > Import Existing Project**.

.. figure:: img/qtcreator-new-project.png
   :figclass: figure-w480
   :align: center

- Under **Location** select the Rebel Engine root folder.

.. figure:: img/qtcreator-set-project-path.png
   :figclass: figure-w480
   :align: center

- Next, you can choose which folders and files will be visible to the project.
  While C/C++ files are added automatically, other extensions can be potentially useful:
  ``*.glsl`` for shader files, ``*.py`` for buildsystem files,
  ``*.java`` for Android platform development, ``*.mm`` for macOS platform development.

.. figure:: img/qtcreator-apply-import-filter.png
   :figclass: figure-w480
   :align: center

.. note:: You can change this configuration later by right-clicking on your project
          and selecting the **Edit Files...** option.

          .. figure:: img/qtcreator-edit-files-menu.png
            :figclass: figure-w480
            :align: center


- Finish the import.
- Open the ``project_name.includes`` file and add a line containing ``.`` to it
  to correctly enable the code completion.

.. figure:: img/qtcreator-project-name-includes.png
   :figclass: figure-w480
   :align: center

- From the left-side menu select **Projects** and open the **Build** tab.
- Delete the predefined ``make`` build step.

.. figure:: img/qtcreator-projects-build.png
   :figclass: figure-w480
   :align: center

- Click **Add Build Step > Custom Process Step** to add a new build step 
  with the following settings:

  +-----------+-------------------------------------------------------------------------------------------------+
  | Command   | **scons**                                                                                       |
  +-----------+-------------------------------------------------------------------------------------------------+
  | Arguments | See :doc:`/development/compiling/introduction_to_the_buildsystem` for a full list of arguments. |
  +-----------+-------------------------------------------------------------------------------------------------+

.. figure:: img/qtcreator-set-scons-command.png
   :figclass: figure-w480
   :align: center

.. note:: If the build fails with ``Could not start process "scons"``, it can mean that ``scons`` 
          is not in your ``PATH`` environment variable. In this case, you'll have to specify the
          full path to the SCons binary.

Debugging the project
---------------------

- From the left-side menu select **Projects** and open the **Run** tab.
- Under **Executable** specify the path to your executable located in 
  the ``RebelEngine/bin`` folder. The name depends on your build configuration,
  e.g. ``rebel.x11.tools.64`` for 64-bit X11 platform with ``tools`` enabled.
  You can use ``%{buildDir}`` to reference the project root, e.g: ``%{buildDir}/bin/rebel.x11.opt.tools.64``.
- If you want to run a specific project, specify its root folder under **Working directory**.
- If you want to run the editor, add ``-e`` to the **Command line arguments** field.

.. figure:: img/qtcreator-run-command.png
   :figclass: figure-w480
   :align: center

To learn more about command line arguments, refer to the
:doc:`command line tutorial </tutorials/editor/command_line_tutorial>`.

Code style configuration
------------------------

Developers must follow the project's :doc:`code style </contributing/code_style_guidelines>`
and the IDE should help them follow it. By default, Qt Creator uses spaces
for indentation which doesn't match the Rebel Engine code style guidelines. You can
change this behavior by changing the **Code Style** in **Tools > Options > C++**.

.. figure:: img/qtcreator-options-cpp.png
   :figclass: figure-w480
   :align: center

Click on **Edit** to change the current settings, then click on
**Copy Built-in Code Style** button to set a new code style. Set a name for it
(e.g. Rebel) and change the Tab policy to be **Tabs Only**.

.. figure:: img/qtcreator-edit-codestyle.png
   :figclass: figure-w480
   :align: center
