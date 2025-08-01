Compiling for iOS
=================

.. highlight:: shell

.. seealso::

    This page describes how to compile iOS export template binaries from source.
    If you're looking to export your project to iOS instead, read :doc:`/tutorials/export/exporting_for_ios`.

Requirements
------------

-  SCons 3.0+ (you can install it via `Homebrew <https://brew.sh/>`_ or
   `MacPorts <https://www.macports.org/>`_, you should be able
   to run ``scons`` in a terminal when installed).
-  Xcode 10.0 (or later) with the iOS (10.0) SDK and the command line tools.

.. seealso:: To get the Rebel Engine source code for compiling, see
             :doc:`getting_source`.

             For a general overview of SCons usage for Rebel Engine, see
             :doc:`introduction_to_the_buildsystem`.

Compiling
---------

Open a Terminal, go to the root dir of the engine source code and type:

::

    $ scons p=iphone target=debug

for a debug build, or:

::

    $ scons p=iphone target=release

for a release build (check ``platforms/iphone/detect.py`` for the compiler
flags used for each configuration).

Alternatively, you can run

::

    $ scons p=iphone arch=x86_64 target=debug

for a Simulator executable.

For recent devices, Apple requires 64-bit versions of application binaries when you are uploading to the Apple Store.
The best way to provide these is to create a bundle in which there are both 32-bit and 64-bit binaries, so every device will be able to run the game.

It can be done in three steps: first compile the 32-bit version, then compile the 64-bit version and then use ``lipo`` to bundle them into one "universal" binary.
All those steps can be performed with following commands:

::

    $ scons p=iphone tools=no target=release arch=arm
    $ scons p=iphone tools=no target=release arch=arm64
    $ lipo -create bin/librebel.iphone.opt.arm.a bin/librebel.iphone.opt.arm64.a -output bin/librebel.iphone.release.fat.a
    $ lipo -create bin/librebel_camera_module.iphone.opt.arm.a bin/librebel_camera_module.iphone.opt.arm64.a -output bin/librebel_camera_module.iphone.release.fat.a
    $ lipo -create bin/librebel_arkit_module.iphone.opt.arm.a bin/librebel_arkit_module.iphone.opt.arm64.a -output bin/librebel_arkit_module.iphone.release.fat.a

If you also want to provide a simulator build (reduces the chance of any linker errors with dependencies), you'll need to build and lipo the ``x86_64`` architecture as well.

::

    $ scons p=iphone tools=no target=release arch=arm
    $ scons p=iphone tools=no target=release arch=arm64
    $ scons p=iphone tools=no target=release arch=x86_64
    $ lipo -create bin/librebel.iphone.opt.arm.a bin/librebel.iphone.opt.arm64.a bin/librebel.iphone.opt.x86_64.a -output bin/librebel.iphone.release.fat.a
    $ lipo -create bin/librebel_camera_module.iphone.opt.arm.a bin/librebel_camera_module.iphone.opt.arm64.a bin/librebel_camera_module.iphone.opt.x86_64.a -output bin/librebel_camera_module.iphone.release.fat.a
    $ lipo -create bin/librebel_arkit_module.iphone.opt.arm.a bin/librebel_arkit_module.iphone.opt.arm64.a bin/librebel_arkit_module.iphone.opt.x86_64.a -output bin/librebel_arkit_module.iphone.release.fat.a

Run
---

To run on a device or simulator, follow these instructions:
:doc:`/tutorials/export/exporting_for_ios`.

Replace or add your executable to the Xcode project, and change the
"executable name" property on Info.plist accordingly if you use an
alternative build.
