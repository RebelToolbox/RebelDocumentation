:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the AudioEffectPanner.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_AudioEffectPanner:

AudioEffectPanner
=================

**Inherits:** :ref:`AudioEffect<class_AudioEffect>` **<** :ref:`Resource<class_Resource>` **<** :ref:`Reference<class_Reference>` **<** :ref:`Object<class_Object>`

Adds a panner audio effect to an Audio bus. Pans sound left or right.

Description
-----------

Determines how much of an audio signal is sent to the left and right buses.

Properties
----------

+---------------------------+--------------------------------------------------+---------+
| :ref:`float<class_float>` | :ref:`pan<class_AudioEffectPanner_property_pan>` | ``0.0`` |
+---------------------------+--------------------------------------------------+---------+

Property Descriptions
---------------------

.. _class_AudioEffectPanner_property_pan:

- :ref:`float<class_float>` **pan**

+-----------+----------------+
| *Default* | ``0.0``        |
+-----------+----------------+
| *Setter*  | set_pan(value) |
+-----------+----------------+
| *Getter*  | get_pan()      |
+-----------+----------------+

Pan position. Value can range from -1 (fully left) to 1 (fully right).

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
