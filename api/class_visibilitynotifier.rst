:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the VisibilityNotifier.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_VisibilityNotifier:

VisibilityNotifier
==================

**Inherits:** :ref:`CullInstance<class_CullInstance>` **<** :ref:`Spatial<class_Spatial>` **<** :ref:`Node<class_Node>` **<** :ref:`Object<class_Object>`

**Inherited By:** :ref:`VisibilityEnabler<class_VisibilityEnabler>`

Detects approximately when the node is visible on screen.

Description
-----------

The VisibilityNotifier detects when it is visible on the screen. It also notifies when its bounding rectangle enters or exits the screen or a :ref:`Camera<class_Camera>`'s view.

If you want nodes to be disabled automatically when they exit the screen, use :ref:`VisibilityEnabler<class_VisibilityEnabler>` instead.

**Note:** VisibilityNotifier uses an approximate heuristic for performance reasons. It doesn't take walls and other occlusion into account (unless you are using :ref:`Portal<class_Portal>`\ s). The heuristic is an implementation detail and may change in future versions. If you need precise visibility checking, use another method such as adding an :ref:`Area<class_Area>` node as a child of a :ref:`Camera<class_Camera>` node and/or :ref:`Vector3.dot<class_Vector3_method_dot>`.

Properties
----------

+-------------------------+-----------------------------------------------------+---------------------------------+
| :ref:`AABB<class_AABB>` | :ref:`aabb<class_VisibilityNotifier_property_aabb>` | ``AABB( -1, -1, -1, 2, 2, 2 )`` |
+-------------------------+-----------------------------------------------------+---------------------------------+

Methods
-------

+-------------------------+---------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>` | :ref:`is_on_screen<class_VisibilityNotifier_method_is_on_screen>` **(** **)** |const| |
+-------------------------+---------------------------------------------------------------------------------------+

Signals
-------

.. _class_VisibilityNotifier_signal_camera_entered:

- **camera_entered** **(** :ref:`Camera<class_Camera>` camera **)**

Emitted when the VisibilityNotifier enters a :ref:`Camera<class_Camera>`'s view.

----

.. _class_VisibilityNotifier_signal_camera_exited:

- **camera_exited** **(** :ref:`Camera<class_Camera>` camera **)**

Emitted when the VisibilityNotifier exits a :ref:`Camera<class_Camera>`'s view.

----

.. _class_VisibilityNotifier_signal_screen_entered:

- **screen_entered** **(** **)**

Emitted when the VisibilityNotifier enters the screen.

----

.. _class_VisibilityNotifier_signal_screen_exited:

- **screen_exited** **(** **)**

Emitted when the VisibilityNotifier exits the screen.

Property Descriptions
---------------------

.. _class_VisibilityNotifier_property_aabb:

- :ref:`AABB<class_AABB>` **aabb**

+-----------+---------------------------------+
| *Default* | ``AABB( -1, -1, -1, 2, 2, 2 )`` |
+-----------+---------------------------------+
| *Setter*  | set_aabb(value)                 |
+-----------+---------------------------------+
| *Getter*  | get_aabb()                      |
+-----------+---------------------------------+

The VisibilityNotifier's bounding box.

Method Descriptions
-------------------

.. _class_VisibilityNotifier_method_is_on_screen:

- :ref:`bool<class_bool>` **is_on_screen** **(** **)** |const|

If ``true``, the bounding box is on the screen.

**Note:** It takes one frame for the node's visibility to be assessed once added to the scene tree, so this method will return ``false`` right after it is instantiated, even if it will be on screen in the draw pass.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
