:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the FuncRef.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_FuncRef:

FuncRef
=======

**Inherits:** :ref:`Reference<class_Reference>` **<** :ref:`Object<class_Object>`

Reference to a function in an object.

Description
-----------

In GDScript, functions are not *first-class objects*. This means it is impossible to store them directly as variables, return them from another function, or pass them as arguments.

However, by creating a ``FuncRef`` using the :ref:`@GDScript.funcref<class_@GDScript_method_funcref>` function, a reference to a function in a given object can be created, passed around and called.

Properties
----------

+-----------------------------+--------------------------------------------------+--------+
| :ref:`String<class_String>` | :ref:`function<class_FuncRef_property_function>` | ``""`` |
+-----------------------------+--------------------------------------------------+--------+

Methods
-------

+-------------------------------+---------------------------------------------------------------------------------------------------------+
| :ref:`Variant<class_Variant>` | :ref:`call_func<class_FuncRef_method_call_func>` **(** ... **)** |vararg|                               |
+-------------------------------+---------------------------------------------------------------------------------------------------------+
| :ref:`Variant<class_Variant>` | :ref:`call_funcv<class_FuncRef_method_call_funcv>` **(** :ref:`Array<class_Array>` arg_array **)**      |
+-------------------------------+---------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`       | :ref:`is_valid<class_FuncRef_method_is_valid>` **(** **)** |const|                                      |
+-------------------------------+---------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_instance<class_FuncRef_method_set_instance>` **(** :ref:`Object<class_Object>` instance **)** |
+-------------------------------+---------------------------------------------------------------------------------------------------------+

Property Descriptions
---------------------

.. _class_FuncRef_property_function:

- :ref:`String<class_String>` **function**

+-----------+---------------------+
| *Default* | ``""``              |
+-----------+---------------------+
| *Setter*  | set_function(value) |
+-----------+---------------------+
| *Getter*  | get_function()      |
+-----------+---------------------+

The name of the referenced function.

Method Descriptions
-------------------

.. _class_FuncRef_method_call_func:

- :ref:`Variant<class_Variant>` **call_func** **(** ... **)** |vararg|

Calls the referenced function previously set in :ref:`function<class_FuncRef_property_function>` or :ref:`@GDScript.funcref<class_@GDScript_method_funcref>`.

----

.. _class_FuncRef_method_call_funcv:

- :ref:`Variant<class_Variant>` **call_funcv** **(** :ref:`Array<class_Array>` arg_array **)**

Calls the referenced function previously set in :ref:`function<class_FuncRef_property_function>` or :ref:`@GDScript.funcref<class_@GDScript_method_funcref>`. Contrarily to :ref:`call_func<class_FuncRef_method_call_func>`, this method does not support a variable number of arguments but expects all parameters to be passed via a single :ref:`Array<class_Array>`.

----

.. _class_FuncRef_method_is_valid:

- :ref:`bool<class_bool>` **is_valid** **(** **)** |const|

Returns whether the object still exists and has the function assigned.

----

.. _class_FuncRef_method_set_instance:

- void **set_instance** **(** :ref:`Object<class_Object>` instance **)**

The object containing the referenced function. This object must be of a type actually inheriting from :ref:`Object<class_Object>`, not a built-in type such as :ref:`int<class_int>`, :ref:`Vector2<class_Vector2>` or :ref:`Dictionary<class_Dictionary>`.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
