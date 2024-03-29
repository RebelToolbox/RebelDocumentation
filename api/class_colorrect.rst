:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the ColorRect.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_ColorRect:

ColorRect
=========

**Inherits:** :ref:`Control<class_Control>` **<** :ref:`CanvasItem<class_CanvasItem>` **<** :ref:`Node<class_Node>` **<** :ref:`Object<class_Object>`

Colored rectangle.

Description
-----------

Displays a rectangle filled with a solid :ref:`color<class_ColorRect_property_color>`. If you need to display the border alone, consider using :ref:`ReferenceRect<class_ReferenceRect>` instead.

Properties
----------

+---------------------------+----------------------------------------------+-------------------------+
| :ref:`Color<class_Color>` | :ref:`color<class_ColorRect_property_color>` | ``Color( 1, 1, 1, 1 )`` |
+---------------------------+----------------------------------------------+-------------------------+

Property Descriptions
---------------------

.. _class_ColorRect_property_color:

- :ref:`Color<class_Color>` **color**

+-----------+-------------------------+
| *Default* | ``Color( 1, 1, 1, 1 )`` |
+-----------+-------------------------+
| *Setter*  | set_frame_color(value)  |
+-----------+-------------------------+
| *Getter*  | get_frame_color()       |
+-----------+-------------------------+

The fill color.

::

    $ColorRect.color = Color(1, 0, 0, 1) # Set ColorRect's color to red.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
