.. meta::
    :keywords: FAQ

Frequently asked questions
==========================

What can I do with Rebel Toolbox? How much does it cost? What are the license terms?
------------------------------------------------------------------------------------

Rebel Engine is `Free and Open-Source Software <https://en.wikipedia.org/wiki/Free_and_open-source_software>`_ available under the `OSI-approved <https://opensource.org/licenses/MIT>`_ MIT license. This means it is free as in "free speech" as well as in "free beer."

In short:

* You are free to download and use Rebel Engine for any purpose: personal, non-profit, commercial, or otherwise.
* You are free to modify, distribute, redistribute, and remix Rebel Engine to your heart's content, for any reason, both non-commercially and commercially.

All the contents of this accompanying documentation are published under
the permissive Creative Commons Attribution 3.0 (`CC-BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_) license, with attribution to "Rebel Toolbox Contributors"

Logos and icons are generally under the same Creative Commons license. Note
that some third-party libraries included with Rebel Engine's source code may have
different licenses.

For full details, look at the `COPYRIGHT.txt <https://github.com/RebelToolbox/RebelEngine/blob/main/COPYRIGHT.txt>`_ and the `LICENSE <https://github.com/RebelToolbox/RebelEngine/blob/main/LICENSE>`_ files in the Rebel Engine repository.

Also, see `the license page on the Rebel Toolbox website <https://rebeltoolbox.com/license>`_.

Which platforms are supported by Rebel Engine?
----------------------------------------------

**For the editor:**

* Windows
* macOS
* X11 (Linux, \*BSD)

**For exporting your games:**

* Windows (and UWP)
* macOS
* X11 (Linux, \*BSD)
* Android
* iOS
* Web

Both 32- and 64-bit binaries are supported where it makes sense, with 64
being the default.

Some users also report building and using Rebel Engine successfully on ARM-based
systems with Linux, like the Raspberry Pi.

Additionally, there is some unofficial third-party work being done on building
for some consoles. However, none of this is included in the default build
scripts or export templates at this time.

For more on this, see the sections on :ref:`exporting <toc-learn-workflow-export>`
and :ref:`compiling Rebel Engine yourself <toc-devel-compiling>`.

Which programming languages are supported in Rebel Engine?
----------------------------------------------------------

The officially supported languages for Rebel Engine are GDScript, Visual Scripting,
C#, and C++. See the subcategories for each language in the
:ref:`scripting <toc-learn-scripting>` section.

If you are just starting out with either Rebel Engine or game development in general,
GDScript is the recommended language to learn and use since it is native to Rebel Engine.
While scripting languages tend to be less performant than lower-level languages in
the long run, for prototyping, developing Minimum Viable Products (MVPs), and
focusing on Time-To-Market (TTM), GDScript will provide a fast, friendly, and capable
way of developing your games.

Note that C# support is still relatively new, and as such, you may encounter some
issues along the way. Our friendly and hard-working development community is always
ready to tackle new problems as they arise, but since this is an open-source project,
we recommend that you first do some due diligence yourself. Searching through
discussions on `open issues <https://github.com/RebelToolbox/RebelEngine/issues>`_ is a
great way to start your troubleshooting.

What is GDScript and why should I use it?
-----------------------------------------

GDScript is Rebel Engine's integrated scripting language. It was built from the ground
up to maximize Rebel Engine's potential in the least amount of code, affording both novice
and expert developers alike to capitalize on Rebel Engine's strengths as fast as possible.
If you've ever written anything in a language like Python before then you'll feel
right at home. For examples, history, and a complete overview of the power GDScript
offers you, check out the :doc:`GDScript scripting guide </tutorials/scripting/gdscript/gdscript_basics>`.

There are several reasons to use GDScript--especially when you are prototyping, in
alpha/beta stages of your project, or are not creating the next AAA title--but the
most salient reason is the overall **reduction of complexity**.

The intent of a tightly integrated, custom scripting language for
Rebel Engine is two-fold: first, it reduces the amount of time necessary to get up and running
with Rebel Engine, giving developers a rapid way of exposing themselves to the engine with a
focus on productivity; second, it reduces the overall burden of maintenance, attenuates
the dimensionality of issues, and allows the developers of the engine to focus on squashing
bugs and improving features related to the engine core--rather than spending a lot of time
trying to get a small set of incremental features working across a large set of languages.

Since Rebel Engine is an open-source project, it was imperative from the start to prioritize a
more integrated and seamless experience over attracting additional users by supporting
more familiar programming languages--especially when supporting those more familiar
languages would result in a worse experience. We understand if you would rather use
another language in Rebel Engine (see the list of supported options above). That being said, if
you haven't given GDScript a try, try it for **three days**. Just like Rebel Engine,
once you see how powerful it is and rapid your development becomes, we think GDScript
will grow on you.

More information about getting comfortable with GDScript or dynamically typed
languages can be found in the :doc:`/tutorials/scripting/gdscript/gdscript_advanced` tutorial.

What were the motivations behind creating GDScript?
---------------------------------------------------

In the early days, the engine used the `Lua <https://www.lua.org>`__
scripting language. Lua is fast, but creating bindings to an object
oriented system (by using fallbacks) was complex and slow and took an
enormous amount of code. After some experiments with
`Python <https://www.python.org>`__, it also proved difficult to embed.

The main reasons for a custom scripting language for Rebel Engine are:

1. Poor threading support in most script VMs, and Rebel Engine uses threads
   (Lua, Python, Squirrel, JavaScript, ActionScript, etc.).
2. Poor class-extending support in most script VMs, and adapting to
   the way Rebel Engine works is highly inefficient (Lua, Python, JavaScript).
3. Many existing languages have horrible interfaces for binding to C++, resulting in large amount of
   code, bugs, bottlenecks, and general inefficiency (Lua, Python,
   Squirrel, JavaScript, etc.) We wanted to focus on a great engine, not a great amount of integrations.
4. No native vector types (vector3, matrix4, etc.), resulting in highly
   reduced performance when using custom types (Lua, Python, Squirrel,
   JavaScript, ActionScript, etc.).
5. Garbage collector results in stalls or unnecessarily large memory
   usage (Lua, Python, JavaScript, ActionScript, etc.).
6. Difficulty to integrate with the code editor for providing code
   completion, live editing, etc. (all of them). This is well-supported
   by GDScript.

GDScript was designed to curtail the issues above, and more.

What type of 3D model formats does Rebel Engine support?
--------------------------------------------------------

Rebel Engine supports Collada via the `OpenCollada <https://github.com/KhronosGroup/OpenCOLLADA/wiki/OpenCOLLADA-Tools>`_ exporter (Maya, 3DSMax).
If you are using Blender, take a look at Godot's `Collada Exporter <https://github.com/godotengine/collada-exporter>`_.

glTF is supported.

FBX is supported via the Open Asset Import library. However, FBX is proprietary
so we recommend using other formats listed above, if suitable for your workflow.

Will [insert closed SDK such as FMOD, GameWorks, etc.] be supported in Rebel Engine?
------------------------------------------------------------------------------------

The aim of Rebel Toolbox is to create a free and open-source MIT-licensed software that
is modular and extendable. There are no plans for Rebel Toolbox to support any third-party,
closed-source/proprietary SDKs, as integrating with these would go against Rebel Toolbox's ethos.

That said, because Rebel Engine is open-source and modular, nothing prevents you or
anyone else interested in adding those libraries as a module and shipping your
game with them--as either open- or closed-source.

To see how support for your SDK of choice could still be provided, look at the
Plugins question below.

If you know of a third-party SDK that is not supported by Rebel Engine but that offers
free and open-source integration, consider starting the integration work yourself.
Rebel Engine is not owned by one person; it belongs to the community, and it grows along
with ambitious community contributors like you.

How do I install the Rebel Engine on my system (for desktop integration)?
-------------------------------------------------------------------------

Since you don't need to actually install Rebel Engine on your system to run it,
this means desktop integration is not performed automatically.
You can manually perform the steps that an installer would do for you:

Windows
^^^^^^^

- Move the Rebel Engine executable to a stable location (i.e. outside of your Downloads folder),
  so you don't accidentally move it and break the shortcut in the future.
- Right-click the Rebel Engine executable and choose **Create Shortcut**.
- Move the created shortcut to ``%LOCALAPPDATA%\Microsoft\Windows\Start Menu\Programs``.
  This is the user-wide location for shortcuts that will appear in the Start menu.
  You can also pin Rebel Engine in the task bar by right-clicking the executable and choosing
  **Pin to Task Bar**.

macOS
^^^^^

Drag the extracted Rebel Engine application to ``/Applications/RebelEngine.app``, then drag it
to the Dock if desired. Spotlight will be able to find Rebel Engine as long as it's in
``/Applications`` or ``~/Applications``.

Linux
^^^^^

- Move the Rebel Engine binary to a stable location (i.e. outside of your Downloads folder),
  so you don't accidentally move it and break the shortcut in the future.
- Rename and move the Rebel Engine binary to a location present in your ``PATH`` environment variable.
  This is typically ``/usr/local/bin/rebel`` or ``/usr/bin/rebel``.
  Doing this requires administrator privileges,
  but this also allows you to
  :doc:`run Rebel Engine from a terminal </tutorials/editor/command_line_tutorial>` by entering ``rebel``.

  - If you cannot move the Rebel Engine binary to a protected location, you can
    keep the binary somewhere in your home directory, and modify the ``Path=``
    line in the ``.desktop`` file linked below to contain the full *absolute* path
    to the Rebel Engine binary.

- Save `this .desktop file <https://github.com/RebelToolbox/RebelEngine/blob/main/misc/dist/linux/com.rebeltoolbox.rebelengine.desktop>`__
  to ``$HOME/.local/share/applications/``. If you have administrator privileges,
  you can also save the ``.desktop`` file to ``/usr/local/share/applications``
  to make the shortcut available for all users.

Is the Rebel Engine editor a portable application?
--------------------------------------------------

In its default configuration, Rebel Engine is *semi-portable*. Its executable can run
from any location (including non-writable locations) and never requires
administrator privileges.

However, configuration files will be written to the user-wide configuration or
data directory. This is usually a good approach, but this means configuration files
will not carry across machines if you copy the folder containing the Rebel Engine executable.
See :doc:`/tutorials/io/data_paths` for more information.

If *true* portable operation is desired (e.g. for use on an USB stick),
follow the steps in :ref:`tutorials/io/data_paths:self-contained mode`.

Why does Rebel Engine use Vulkan or OpenGL instead of Direct3D?
---------------------------------------------------------------

Rebel Toolbox aims for cross-platform compatibility and open standards first and
foremost. OpenGL and Vulkan are the technologies that are both open and
available (nearly) on all platforms. Thanks to this design decision, a project
developed with Rebel Engine on Windows will run out of the box on Linux, macOS, and
more.

Since Rebel Engine only has a few people working on its renderer, we would prefer
having fewer rendering backends to maintain. On top of that, using a single API
on all platforms allows for greater consistency with fewer platform-specific
issues.

In the long term, we may develop a Direct3D 12 renderer for Rebel Engine (mainly for
the Xbox's purposes), but Vulkan and OpenGL will remain the default rendering
backends on all platforms, including Windows.

Why does Rebel Toolbox aim to keep its core feature set small?
--------------------------------------------------------------

Rebel Toolbox intentionally does not include features that can be implemented by add-ons
unless they are used very often. One example of this would be advanced
artificial intelligence functionality.

There are several reasons for this:

- **Code maintenance and surface for bugs.** Every time we accept new code in
  the Rebel Engine repository, existing contributors often take the responsibility of
  maintaining it. Some contributors don't always stick around after getting
  their code merged, which can make it difficult for us to maintain the code in
  question. This can lead to poorly maintained features with bugs that are never
  fixed. On top of that, the "API surface" that needs to be tested and checked
  for regressions keeps increasing over time.

- **Ease of contribution.** By keeping the codebase small and tidy, it can remain
  fast and easy to compile from source. This makes it easier for new
  contributors to get started with Rebel Engine development, without requiring them to purchase
  high-end hardware.

- **Keeping the binary size small for the editor.** Not everyone has a fast Internet
  connection. Ensuring that everyone can download the Rebel Engine editor, extract it
  and run it in less than 5 minutes makes Rebel Engine more accessible to developers in
  all countries.

- **Keeping the binary size small for export templates.** This directly impacts the
  size of projects exported with Rebel Engine. On mobile and web platforms, keeping
  file sizes low is primordial to ensure fast installation and loading on
  underpowered devices. Again, there are many countries where high-speed
  Internet is not readily available. To add to this, strict data usage caps are
  often in effect in those countries.

For all the reasons above, we have to be selective of what we can accept as core
functionality in Rebel Engine. This is why we are aiming to move some core
functionality to officially supported add-ons in future versions of Rebel Engine. In
terms of binary size, this also has the advantage of making you pay only for what
you actually use in your project. (In the meantime, you can
:doc:`compile custom export templates with unused features disabled </development/compiling/optimizing_for_size>`
to optimize the distribution size of your project.)

How should assets be created to handle multiple resolutions and aspect ratios?
------------------------------------------------------------------------------

This question pops up often and it's probably thanks to the misunderstanding
created by Apple when they originally doubled the resolution of their devices.
It made people think that having the same assets in different resolutions was a
good idea, so many continued towards that path. That originally worked to a
point and only for Apple devices, but then several Android and Apple devices
with different resolutions and aspect ratios were created, with a very wide
range of sizes and DPIs.

The most common and proper way to achieve this is to, instead, use a single
base resolution for the game and only handle different screen aspect ratios.
This is mostly needed for 2D, as in 3D it's just a matter of Camera XFov or YFov.

1. Choose a single base resolution for your game. Even if there are
   devices that go up to 2K and devices that go down to 400p, regular
   hardware scaling in your device will take care of this at little or
   no performance cost. Most common choices are either near 1080p
   (1920x1080) or 720p (1280x720). Keep in mind the higher the
   resolution, the larger your assets, the more memory they will take
   and the longer the time it will take for loading.

2. Use the stretch options in Rebel Engine; 2D stretching while keeping aspect
   ratios works best. Check the :doc:`/tutorials/rendering/multiple_resolutions` tutorial
   on how to achieve this.

3. Determine a minimum resolution and then decide if you want your game
   to stretch vertically or horizontally for different aspect ratios, or
   if there is one aspect ratio and you want black bars to appear
   instead. This is also explained in :doc:`/tutorials/rendering/multiple_resolutions`.

4. For user interfaces, use the :doc:`anchoring </tutorials/ui/size_and_anchors>`
   to determine where controls should stay and move. If UIs are more
   complex, consider learning about Containers.

And that's it! Your game should work in multiple resolutions.

If there is a desire to make your game also work on ancient
devices with tiny screens (fewer than 300 pixels in width), you can use
the export option to shrink images, and set that build to be used for
certain screen sizes in the App Store or Google Play.

How can I extend Rebel Engine?
------------------------------

For extending Rebel Engine, like creating Rebel Editor plugins or adding support
for additional languages, take a look at :doc:`EditorPlugins </tutorials/plugins/editor/making_plugins>`
and tool scripts.

You can also take a look at the GDScript implementation and other the Rebel Engine modules.
This would be a good starting point to see how another third-party library
integrates with Rebel Engine.

When is the next release of Rebel Engine out?
---------------------------------------------

When it's ready! See :doc:`release_policy` for more
information.

I would like to contribute! How can I get started?
--------------------------------------------------

Awesome! As an open-source project, Rebel Engine thrives off of the innovation and
ambition of developers like you.

The first place to get started is in the `issues <https://github.com/RebelToolbox/RebelEngine/issues>`_.
Find an issue that resonates with you, then proceed to the `How to Contribute <https://github.com/RebelToolbox/RebelEngine/blob/main/CONTRIBUTING.md>`_
guide to learn how to fork, modify, and submit a Pull Request (PR) with your changes.

I have a great idea for Rebel Engine. How can I share it?
----------------------------------------------------------

It might be tempting to want to bring ideas to Rebel Engine, like ones that
result in massive core changes, some sort of mimicry of what another
game engine does, or alternative workflows that you'd like built into
the editor. These are great, and we are thankful to have such motivated
people want to contribute, but Rebel Engine's focus is and always will be the
core functionality.

Most developers in the Rebel Toolbox community will be more interested to learn
about things like:

-  Your experience using the software and the problems you have (we
   care about this much more than ideas on how to improve it).
-  The features you would like to see implemented because you need them
   for your project.
-  The concepts that were difficult to understand while learning the software.
-  The parts of your workflow you would like to see optimized.
-  Parts where you missed clear tutorials or where the documentation wasn't clear.

Please don't feel like your ideas for Rebel Toolbox are unwelcome. Instead,
try to reformulate them as a problem first, so developers and the community
have a functional foundation to ground your ideas on.

A good way to approach sharing your ideas and problems with the community
is as a set of user stories. Explain what you are trying to do, what behavior
you expect to happen, and then what behavior actually happened. Framing problems
and ideas this way will help the whole community stay focused on improving
developer experiences as a whole.

Bonus points for bringing screenshots, concrete numbers, test cases, or example
projects (if applicable).

Is it possible to use Rebel Engine to create non-game applications?
-------------------------------------------------------------------

Yes! Reble Engine features an extensive built-in UI system, and its small distribution
size can make it a suitable alternative to frameworks like Electron or Qt.

When creating a non-game application, make sure to enable
:ref:`low-processor mode <class_ProjectSettings_property_application/run/low_processor_mode>`
in the Project Settings to decrease CPU and GPU usage.

That said, we wouldn't recommend using Rebel Engine to create a *mobile* application
since low-processor mode isn't supported on mobile platforms yet.

Is it possible to use Rebel Engine as a library?
------------------------------------------------

Rebel Engine is meant to be used with its editor. We recommend you give it a try, as it
will most likely save you time in the long term. There are no plans to make
Rebel Engine usable as a library, as it would make the rest of the engine more
convoluted and difficult to use for casual users.

If you want to use a rendering library, look into using an established rendering
engine instead. Keep in mind rendering engines usually have smaller communities
compared to Rebel Toolbox. This will make it more difficult to find answers to your
questions.

What user interface toolkit does Rebel Engine use?
--------------------------------------------------

Rebel Engine does not use a standard :abbr:`GUI (Graphical User Interface)` toolkit
like GTK, Qt or wxWidgets. Instead, Rebel Engine uses its own user interface toolkit,
rendered using OpenGL ES or Vulkan. This toolkit is exposed in the form of
Control nodes, which are used to render the editor (which is written in C++).
These Control nodes can also be used in projects from any scripting language
supported by Rebel Engine.

This custom toolkit makes it possible to benefit from hardware acceleration and
have a consistent appearance across all platforms. On top of that, it doesn't
have to deal with the LGPL licensing caveats that come with GTK or Qt. Lastly,
this means Rebel Engine is "eating its own dog food" since the editor itself is one of
the most complex users of Rebel Engine's UI system.

This custom UI toolkit :ref:`can't be used as a library <about/faq:Is it possible to use Rebel Engine as a library?>`,
but you can still
:ref:`use Rebel Engine to create non-game applications by using the editor <about/faq:Is it possible to use Rebel Engine to create non-game applications?>`.

Why does Rebel Engine not use STL (Standard Template Library)?
--------------------------------------------------------------

Like many other libraries (Qt as an example), Rebel Engine does not make use of
STL. We believe STL is a great general purpose library, but we had special
requirements for Rebel Engine.

* STL templates create very large symbols, which results in huge debug binaries. We use few templates with very short names instead.
* Most of our containers cater to special needs, like Vector, which uses copy on write and we use to pass data around, or the RID system, which requires O(1) access time for performance. Likewise, our hash map implementations are designed to integrate seamlessly with internal engine types.
* Our containers have memory tracking built-in, which helps better track memory usage.
* For large arrays, we use pooled memory, which can be mapped to either a preallocated buffer or virtual memory.
* We use our custom String type, as the one provided by STL is too basic and lacks proper internationalization support.

Why does Rebel Engine not use exceptions?
-----------------------------------------

We believe games should not crash, no matter what. If an unexpected
situation happens, Rebel Engine will print an error (which can be traced even to
script), but then it will try to recover as gracefully as possible and keep
going.

Additionally, exceptions significantly increase binary size for the
executable.

Why does Rebel Engine not enforce RTTI?
---------------------------------------

Rebel Engine provides its own type-casting system, which can optionally use RTTI
internally. Disabling RTTI in Rebel Engine means considerably smaller binary sizes can
be achieved, at a little performance cost.

Why does Rebel Engine not force users to implement DoD (Data oriented Design)?
------------------------------------------------------------------------------

While Rebel Engine internally for a lot of the heavy performance tasks attempts
to use cache coherency as well as possible, we believe most users don't
really need to be forced to use DoD practices.

DoD is mostly a cache coherency optimization that can only gain you
significant performance improvements when dealing with dozens of
thousands of objects (which are processed every frame with little
modification). As in, if you are moving a few hundred sprites or enemies
per frame, DoD won't help you, and you should consider a different approach
to optimization.

The vast majority of games do not need this and Rebel Engine provides handy helpers
to do the job for most cases when you do.

If a game that really needs to process such large amount of objects is
needed, our recommendation is to use C++ and GDNative for the high
performance parts and GDScript (or C#) for the rest of the game.

How can I support Rebel Engine development or contribute?
---------------------------------------------------------

See :doc:`/contributing/ways_to_contribute`.
