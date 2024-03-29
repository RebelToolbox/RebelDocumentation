:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the VisualScriptVariableGet.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_VisualScriptVariableGet:

VisualScriptVariableGet
=======================

**Inherits:** :ref:`VisualScriptNode<class_VisualScriptNode>` **<** :ref:`Resource<class_Resource>` **<** :ref:`Reference<class_Reference>` **<** :ref:`Object<class_Object>`

Gets a variable's value.

Description
-----------

Returns a variable's value. "Var Name" must be supplied, with an optional type.

**Input Ports:**

none

**Output Ports:**

- Data (variant): ``value``

Properties
----------

+-----------------------------+------------------------------------------------------------------+--------+
| :ref:`String<class_String>` | :ref:`var_name<class_VisualScriptVariableGet_property_var_name>` | ``""`` |
+-----------------------------+------------------------------------------------------------------+--------+

Property Descriptions
---------------------

.. _class_VisualScriptVariableGet_property_var_name:

- :ref:`String<class_String>` **var_name**

+-----------+---------------------+
| *Default* | ``""``              |
+-----------+---------------------+
| *Setter*  | set_variable(value) |
+-----------+---------------------+
| *Getter*  | get_variable()      |
+-----------+---------------------+

The variable's name.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
