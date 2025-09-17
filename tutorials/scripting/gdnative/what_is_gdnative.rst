What is GDNative?
=================

Introduction
------------

**GDNative** lets the engine interact with
native `shared libraries <https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries>`__
at run-time. You can use it to run native code without compiling it with the engine.

.. note:: GDNative is *not* a scripting language and has no relation to
          :doc:`GDScript </tutorials/scripting/gdscript/gdscript_basics>`.

Differences between GDNative and C++ modules
--------------------------------------------

You can use both GDNative and :doc:`C++ modules </development/engine/custom_modules_in_cpp>` to
run C or C++ code in a Rebel Project.

They also both allow you to integrate third-party libraries into Rebel Engine. The one
you should choose depends on your needs.

Advantages of GDNative
^^^^^^^^^^^^^^^^^^^^^^

Unlike modules, GDNative doesn't require compiling the engine's source code,
making it easier to distribute your work. It gives you access to most of the API
available to GDScript C#, allowing you to code game logic with full control
regarding performance. It's ideal if you need high-performance code you'd like
to distribute as an add-on.

Also:

- GDNative is not limited to C and C++. Thanks to :ref:`third-party bindings
  <tutorials/scripting/gdnative/what_is_gdnative:version compatibility>`, you can use it with many other
  languages.
- You can use the same compiled GDNative library in the editor and exported
  project. With C++ modules, you have to recompile all the export templates you
  plan to use if you require its functionality at run-time.
- GDNative only requires you to compile your library, not the whole engine.
  That's unlike C++ modules, which are statically compiled into the engine.
  Every time you change a module, you need to recompile the engine. Even with
  incremental builds, this process is slower than using GDNative.

Advantages of C++ modules
^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend :doc:`C++ modules </development/engine/custom_modules_in_cpp>` in cases where
GDNative isn't enough:

- C++ modules provide deeper integration into the engine. GDNative's access is
  limited to what the scripting API exposes.
- You can use C++ modules to provide additional features in a project without
  carrying native library files around. This extends to exported projects.
- C++ modules are supported on all platforms. In contrast, GDNative has only
  limited support on HTML5 (cannot be used together with multi-threading), and
  is not supported on Universal Windows Platform (UWP).
- C++ modules can be faster than GDNative, especially when the code requires a
  lot of communication through the scripting API.

Supported languages
-------------------

The Rebel developers officially support the following language bindings for
GDNative:

- C++ :doc:`(tutorial) </tutorials/scripting/gdnative/gdnative_cpp_example>`
- C :doc:`(tutorial) </tutorials/scripting/gdnative/gdnative_c_example>`

.. note::

    There are no plans to support additional languages with GDNative officially.
    That said, the community offers several bindings for other languages (see
    below).

Version compatibility
---------------------

:doc:`Unlike Rebel Engine </about/release_policy>`, GDNative has stricter version
compatibility requirements as it relies on low-level *ptrcalls* to function.

GDNative add-ons compiled for a given Rebel Engine version are only guaranteed to work
with the same minor release series.
