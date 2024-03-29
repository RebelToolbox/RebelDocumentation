:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the Performance.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_Performance:

Performance
===========

**Inherits:** :ref:`Object<class_Object>`

Exposes performance-related data.

Description
-----------

This class provides access to a number of different monitors related to performance, such as memory usage, draw calls, and FPS. These are the same as the values displayed in the **Monitor** tab in the editor's **Debugger** panel. By using the :ref:`get_monitor<class_Performance_method_get_monitor>` method of this class, you can access this data from your code.

**Note:** A few of these monitors are only available in debug mode and will always return 0 when used in a release build.

**Note:** Many of these monitors are not updated in real-time, so there may be a short delay between changes.

Methods
-------

+---------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>` | :ref:`get_monitor<class_Performance_method_get_monitor>` **(** :ref:`Monitor<enum_Performance_Monitor>` monitor **)** |const| |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------------+

Enumerations
------------

.. _enum_Performance_Monitor:

.. _class_Performance_constant_TIME_FPS:

.. _class_Performance_constant_TIME_PROCESS:

.. _class_Performance_constant_TIME_PHYSICS_PROCESS:

.. _class_Performance_constant_MEMORY_STATIC:

.. _class_Performance_constant_MEMORY_DYNAMIC:

.. _class_Performance_constant_MEMORY_STATIC_MAX:

.. _class_Performance_constant_MEMORY_DYNAMIC_MAX:

.. _class_Performance_constant_MEMORY_MESSAGE_BUFFER_MAX:

.. _class_Performance_constant_OBJECT_COUNT:

.. _class_Performance_constant_OBJECT_RESOURCE_COUNT:

.. _class_Performance_constant_OBJECT_NODE_COUNT:

.. _class_Performance_constant_OBJECT_ORPHAN_NODE_COUNT:

.. _class_Performance_constant_RENDER_OBJECTS_IN_FRAME:

.. _class_Performance_constant_RENDER_VERTICES_IN_FRAME:

.. _class_Performance_constant_RENDER_MATERIAL_CHANGES_IN_FRAME:

.. _class_Performance_constant_RENDER_SHADER_CHANGES_IN_FRAME:

.. _class_Performance_constant_RENDER_SURFACE_CHANGES_IN_FRAME:

.. _class_Performance_constant_RENDER_DRAW_CALLS_IN_FRAME:

.. _class_Performance_constant_RENDER_2D_ITEMS_IN_FRAME:

.. _class_Performance_constant_RENDER_2D_DRAW_CALLS_IN_FRAME:

.. _class_Performance_constant_RENDER_VIDEO_MEM_USED:

.. _class_Performance_constant_RENDER_TEXTURE_MEM_USED:

.. _class_Performance_constant_RENDER_VERTEX_MEM_USED:

.. _class_Performance_constant_RENDER_USAGE_VIDEO_MEM_TOTAL:

.. _class_Performance_constant_PHYSICS_2D_ACTIVE_OBJECTS:

.. _class_Performance_constant_PHYSICS_2D_COLLISION_PAIRS:

.. _class_Performance_constant_PHYSICS_2D_ISLAND_COUNT:

.. _class_Performance_constant_PHYSICS_3D_ACTIVE_OBJECTS:

.. _class_Performance_constant_PHYSICS_3D_COLLISION_PAIRS:

.. _class_Performance_constant_PHYSICS_3D_ISLAND_COUNT:

.. _class_Performance_constant_AUDIO_OUTPUT_LATENCY:

.. _class_Performance_constant_MONITOR_MAX:

enum **Monitor**:

- **TIME_FPS** = **0** --- Number of frames per second.

- **TIME_PROCESS** = **1** --- Time it took to complete one frame, in seconds.

- **TIME_PHYSICS_PROCESS** = **2** --- Time it took to complete one physics frame, in seconds.

- **MEMORY_STATIC** = **3** --- Static memory currently used, in bytes. Not available in release builds.

- **MEMORY_DYNAMIC** = **4** --- Dynamic memory currently used, in bytes. Not available in release builds.

- **MEMORY_STATIC_MAX** = **5** --- Available static memory. Not available in release builds.

- **MEMORY_DYNAMIC_MAX** = **6** --- Available dynamic memory. Not available in release builds.

- **MEMORY_MESSAGE_BUFFER_MAX** = **7** --- Largest amount of memory the message queue buffer has used, in bytes. The message queue is used for deferred functions calls and notifications.

- **OBJECT_COUNT** = **8** --- Number of objects currently instanced (including nodes).

- **OBJECT_RESOURCE_COUNT** = **9** --- Number of resources currently used.

- **OBJECT_NODE_COUNT** = **10** --- Number of nodes currently instanced in the scene tree. This also includes the root node.

- **OBJECT_ORPHAN_NODE_COUNT** = **11** --- Number of orphan nodes, i.e. nodes which are not parented to a node of the scene tree.

- **RENDER_OBJECTS_IN_FRAME** = **12** --- 3D objects drawn per frame.

- **RENDER_VERTICES_IN_FRAME** = **13** --- Vertices drawn per frame. 3D only.

- **RENDER_MATERIAL_CHANGES_IN_FRAME** = **14** --- Material changes per frame. 3D only.

- **RENDER_SHADER_CHANGES_IN_FRAME** = **15** --- Shader changes per frame. 3D only.

- **RENDER_SURFACE_CHANGES_IN_FRAME** = **16** --- Render surface changes per frame. 3D only.

- **RENDER_DRAW_CALLS_IN_FRAME** = **17** --- Draw calls per frame. 3D only.

- **RENDER_2D_ITEMS_IN_FRAME** = **18** --- Items or joined items drawn per frame.

- **RENDER_2D_DRAW_CALLS_IN_FRAME** = **19** --- Draw calls per frame.

- **RENDER_VIDEO_MEM_USED** = **20** --- The amount of video memory used, i.e. texture and vertex memory combined.

- **RENDER_TEXTURE_MEM_USED** = **21** --- The amount of texture memory used.

- **RENDER_VERTEX_MEM_USED** = **22** --- The amount of vertex memory used.

- **RENDER_USAGE_VIDEO_MEM_TOTAL** = **23** --- Unimplemented in the GLES2 and GLES3 rendering backends, always returns 0.

- **PHYSICS_2D_ACTIVE_OBJECTS** = **24** --- Number of active :ref:`RigidBody2D<class_RigidBody2D>` nodes in the game.

- **PHYSICS_2D_COLLISION_PAIRS** = **25** --- Number of collision pairs in the 2D physics engine.

- **PHYSICS_2D_ISLAND_COUNT** = **26** --- Number of islands in the 2D physics engine.

- **PHYSICS_3D_ACTIVE_OBJECTS** = **27** --- Number of active :ref:`RigidBody<class_RigidBody>` and :ref:`VehicleBody<class_VehicleBody>` nodes in the game.

- **PHYSICS_3D_COLLISION_PAIRS** = **28** --- Number of collision pairs in the 3D physics engine.

- **PHYSICS_3D_ISLAND_COUNT** = **29** --- Number of islands in the 3D physics engine.

- **AUDIO_OUTPUT_LATENCY** = **30** --- Output latency of the :ref:`AudioServer<class_AudioServer>`.

- **MONITOR_MAX** = **31** --- Represents the size of the :ref:`Monitor<enum_Performance_Monitor>` enum.

Method Descriptions
-------------------

.. _class_Performance_method_get_monitor:

- :ref:`float<class_float>` **get_monitor** **(** :ref:`Monitor<enum_Performance_Monitor>` monitor **)** |const|

Returns the value of one of the available monitors. You should provide one of the :ref:`Monitor<enum_Performance_Monitor>` constants as the argument, like this:

::

    print(Performance.get_monitor(Performance.TIME_FPS)) # Prints the FPS to the console

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
