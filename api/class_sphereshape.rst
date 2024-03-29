:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the SphereShape.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_SphereShape:

SphereShape
===========

**Inherits:** :ref:`Shape<class_Shape>` **<** :ref:`Resource<class_Resource>` **<** :ref:`Reference<class_Reference>` **<** :ref:`Object<class_Object>`

Sphere shape for 3D collisions.

Description
-----------

Sphere shape for 3D collisions, which can be set into a :ref:`PhysicsBody<class_PhysicsBody>` or :ref:`Area<class_Area>`. This shape is useful for modeling sphere-like 3D objects.

Properties
----------

+---------------------------+--------------------------------------------------+---------+
| :ref:`float<class_float>` | :ref:`radius<class_SphereShape_property_radius>` | ``1.0`` |
+---------------------------+--------------------------------------------------+---------+

Property Descriptions
---------------------

.. _class_SphereShape_property_radius:

- :ref:`float<class_float>` **radius**

+-----------+-------------------+
| *Default* | ``1.0``           |
+-----------+-------------------+
| *Setter*  | set_radius(value) |
+-----------+-------------------+
| *Getter*  | get_radius()      |
+-----------+-------------------+

The sphere's radius. The shape's diameter is double the radius.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
