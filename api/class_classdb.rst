:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the ClassDB.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_ClassDB:

ClassDB
=======

**Inherits:** :ref:`Object<class_Object>`

Class information repository.

Description
-----------

Provides access to metadata stored for every available class.

Methods
-------

+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                       | :ref:`can_instance<class_ClassDB_method_can_instance>` **(** :ref:`String<class_String>` class **)** |const|                                                                                                                       |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                       | :ref:`class_exists<class_ClassDB_method_class_exists>` **(** :ref:`String<class_String>` class **)** |const|                                                                                                                       |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_String>`                   | :ref:`class_get_category<class_ClassDB_method_class_get_category>` **(** :ref:`String<class_String>` class **)** |const|                                                                                                           |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PoolStringArray<class_PoolStringArray>` | :ref:`class_get_enum_constants<class_ClassDB_method_class_get_enum_constants>` **(** :ref:`String<class_String>` class, :ref:`String<class_String>` enum, :ref:`bool<class_bool>` no_inheritance=false **)** |const|               |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PoolStringArray<class_PoolStringArray>` | :ref:`class_get_enum_list<class_ClassDB_method_class_get_enum_list>` **(** :ref:`String<class_String>` class, :ref:`bool<class_bool>` no_inheritance=false **)** |const|                                                           |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                         | :ref:`class_get_integer_constant<class_ClassDB_method_class_get_integer_constant>` **(** :ref:`String<class_String>` class, :ref:`String<class_String>` name **)** |const|                                                         |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_String>`                   | :ref:`class_get_integer_constant_enum<class_ClassDB_method_class_get_integer_constant_enum>` **(** :ref:`String<class_String>` class, :ref:`String<class_String>` name, :ref:`bool<class_bool>` no_inheritance=false **)** |const| |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PoolStringArray<class_PoolStringArray>` | :ref:`class_get_integer_constant_list<class_ClassDB_method_class_get_integer_constant_list>` **(** :ref:`String<class_String>` class, :ref:`bool<class_bool>` no_inheritance=false **)** |const|                                   |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_Array>`                     | :ref:`class_get_method_list<class_ClassDB_method_class_get_method_list>` **(** :ref:`String<class_String>` class, :ref:`bool<class_bool>` no_inheritance=false **)** |const|                                                       |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Variant<class_Variant>`                 | :ref:`class_get_property<class_ClassDB_method_class_get_property>` **(** :ref:`Object<class_Object>` object, :ref:`String<class_String>` property **)** |const|                                                                    |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_Array>`                     | :ref:`class_get_property_list<class_ClassDB_method_class_get_property_list>` **(** :ref:`String<class_String>` class, :ref:`bool<class_bool>` no_inheritance=false **)** |const|                                                   |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Dictionary<class_Dictionary>`           | :ref:`class_get_signal<class_ClassDB_method_class_get_signal>` **(** :ref:`String<class_String>` class, :ref:`String<class_String>` signal **)** |const|                                                                           |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_Array>`                     | :ref:`class_get_signal_list<class_ClassDB_method_class_get_signal_list>` **(** :ref:`String<class_String>` class, :ref:`bool<class_bool>` no_inheritance=false **)** |const|                                                       |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                       | :ref:`class_has_enum<class_ClassDB_method_class_has_enum>` **(** :ref:`String<class_String>` class, :ref:`String<class_String>` name, :ref:`bool<class_bool>` no_inheritance=false **)** |const|                                   |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                       | :ref:`class_has_integer_constant<class_ClassDB_method_class_has_integer_constant>` **(** :ref:`String<class_String>` class, :ref:`String<class_String>` name **)** |const|                                                         |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                       | :ref:`class_has_method<class_ClassDB_method_class_has_method>` **(** :ref:`String<class_String>` class, :ref:`String<class_String>` method, :ref:`bool<class_bool>` no_inheritance=false **)** |const|                             |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                       | :ref:`class_has_signal<class_ClassDB_method_class_has_signal>` **(** :ref:`String<class_String>` class, :ref:`String<class_String>` signal **)** |const|                                                                           |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Error<enum_@GlobalScope_Error>`         | :ref:`class_set_property<class_ClassDB_method_class_set_property>` **(** :ref:`Object<class_Object>` object, :ref:`String<class_String>` property, :ref:`Variant<class_Variant>` value **)** |const|                               |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PoolStringArray<class_PoolStringArray>` | :ref:`get_class_list<class_ClassDB_method_get_class_list>` **(** **)** |const|                                                                                                                                                     |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PoolStringArray<class_PoolStringArray>` | :ref:`get_inheriters_from_class<class_ClassDB_method_get_inheriters_from_class>` **(** :ref:`String<class_String>` class **)** |const|                                                                                             |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_String>`                   | :ref:`get_parent_class<class_ClassDB_method_get_parent_class>` **(** :ref:`String<class_String>` class **)** |const|                                                                                                               |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Variant<class_Variant>`                 | :ref:`instance<class_ClassDB_method_instance>` **(** :ref:`String<class_String>` class **)** |const|                                                                                                                               |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                       | :ref:`is_class_enabled<class_ClassDB_method_is_class_enabled>` **(** :ref:`String<class_String>` class **)** |const|                                                                                                               |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                       | :ref:`is_parent_class<class_ClassDB_method_is_parent_class>` **(** :ref:`String<class_String>` class, :ref:`String<class_String>` inherits **)** |const|                                                                           |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Method Descriptions
-------------------

.. _class_ClassDB_method_can_instance:

- :ref:`bool<class_bool>` **can_instance** **(** :ref:`String<class_String>` class **)** |const|

Returns ``true`` if you can instance objects from the specified ``class``, ``false`` in other case.

----

.. _class_ClassDB_method_class_exists:

- :ref:`bool<class_bool>` **class_exists** **(** :ref:`String<class_String>` class **)** |const|

Returns whether the specified ``class`` is available or not.

----

.. _class_ClassDB_method_class_get_category:

- :ref:`String<class_String>` **class_get_category** **(** :ref:`String<class_String>` class **)** |const|

Returns a category associated with the class for use in documentation and the Asset Library. Debug mode required.

----

.. _class_ClassDB_method_class_get_enum_constants:

- :ref:`PoolStringArray<class_PoolStringArray>` **class_get_enum_constants** **(** :ref:`String<class_String>` class, :ref:`String<class_String>` enum, :ref:`bool<class_bool>` no_inheritance=false **)** |const|

Returns an array with all the keys in ``enum`` of ``class`` or its ancestry.

----

.. _class_ClassDB_method_class_get_enum_list:

- :ref:`PoolStringArray<class_PoolStringArray>` **class_get_enum_list** **(** :ref:`String<class_String>` class, :ref:`bool<class_bool>` no_inheritance=false **)** |const|

Returns an array with all the enums of ``class`` or its ancestry.

----

.. _class_ClassDB_method_class_get_integer_constant:

- :ref:`int<class_int>` **class_get_integer_constant** **(** :ref:`String<class_String>` class, :ref:`String<class_String>` name **)** |const|

Returns the value of the integer constant ``name`` of ``class`` or its ancestry. Always returns 0 when the constant could not be found.

----

.. _class_ClassDB_method_class_get_integer_constant_enum:

- :ref:`String<class_String>` **class_get_integer_constant_enum** **(** :ref:`String<class_String>` class, :ref:`String<class_String>` name, :ref:`bool<class_bool>` no_inheritance=false **)** |const|

Returns which enum the integer constant ``name`` of ``class`` or its ancestry belongs to.

----

.. _class_ClassDB_method_class_get_integer_constant_list:

- :ref:`PoolStringArray<class_PoolStringArray>` **class_get_integer_constant_list** **(** :ref:`String<class_String>` class, :ref:`bool<class_bool>` no_inheritance=false **)** |const|

Returns an array with the names all the integer constants of ``class`` or its ancestry.

----

.. _class_ClassDB_method_class_get_method_list:

- :ref:`Array<class_Array>` **class_get_method_list** **(** :ref:`String<class_String>` class, :ref:`bool<class_bool>` no_inheritance=false **)** |const|

Returns an array with all the methods of ``class`` or its ancestry if ``no_inheritance`` is ``false``. Every element of the array is a :ref:`Dictionary<class_Dictionary>` with the following keys: ``args``, ``default_args``, ``flags``, ``id``, ``name``, ``return: (class_name, hint, hint_string, name, type, usage)``.

**Note:** In exported release builds the debug info is not available, so the returned dictionaries will contain only method names.

----

.. _class_ClassDB_method_class_get_property:

- :ref:`Variant<class_Variant>` **class_get_property** **(** :ref:`Object<class_Object>` object, :ref:`String<class_String>` property **)** |const|

Returns the value of ``property`` of ``class`` or its ancestry.

----

.. _class_ClassDB_method_class_get_property_list:

- :ref:`Array<class_Array>` **class_get_property_list** **(** :ref:`String<class_String>` class, :ref:`bool<class_bool>` no_inheritance=false **)** |const|

Returns an array with all the properties of ``class`` or its ancestry if ``no_inheritance`` is ``false``.

----

.. _class_ClassDB_method_class_get_signal:

- :ref:`Dictionary<class_Dictionary>` **class_get_signal** **(** :ref:`String<class_String>` class, :ref:`String<class_String>` signal **)** |const|

Returns the ``signal`` data of ``class`` or its ancestry. The returned value is a :ref:`Dictionary<class_Dictionary>` with the following keys: ``args``, ``default_args``, ``flags``, ``id``, ``name``, ``return: (class_name, hint, hint_string, name, type, usage)``.

----

.. _class_ClassDB_method_class_get_signal_list:

- :ref:`Array<class_Array>` **class_get_signal_list** **(** :ref:`String<class_String>` class, :ref:`bool<class_bool>` no_inheritance=false **)** |const|

Returns an array with all the signals of ``class`` or its ancestry if ``no_inheritance`` is ``false``. Every element of the array is a :ref:`Dictionary<class_Dictionary>` as described in :ref:`class_get_signal<class_ClassDB_method_class_get_signal>`.

----

.. _class_ClassDB_method_class_has_enum:

- :ref:`bool<class_bool>` **class_has_enum** **(** :ref:`String<class_String>` class, :ref:`String<class_String>` name, :ref:`bool<class_bool>` no_inheritance=false **)** |const|

Returns whether ``class`` or its ancestry has an enum called ``name`` or not.

----

.. _class_ClassDB_method_class_has_integer_constant:

- :ref:`bool<class_bool>` **class_has_integer_constant** **(** :ref:`String<class_String>` class, :ref:`String<class_String>` name **)** |const|

Returns whether ``class`` or its ancestry has an integer constant called ``name`` or not.

----

.. _class_ClassDB_method_class_has_method:

- :ref:`bool<class_bool>` **class_has_method** **(** :ref:`String<class_String>` class, :ref:`String<class_String>` method, :ref:`bool<class_bool>` no_inheritance=false **)** |const|

Returns whether ``class`` (or its ancestry if ``no_inheritance`` is ``false``) has a method called ``method`` or not.

----

.. _class_ClassDB_method_class_has_signal:

- :ref:`bool<class_bool>` **class_has_signal** **(** :ref:`String<class_String>` class, :ref:`String<class_String>` signal **)** |const|

Returns whether ``class`` or its ancestry has a signal called ``signal`` or not.

----

.. _class_ClassDB_method_class_set_property:

- :ref:`Error<enum_@GlobalScope_Error>` **class_set_property** **(** :ref:`Object<class_Object>` object, :ref:`String<class_String>` property, :ref:`Variant<class_Variant>` value **)** |const|

Sets ``property`` value of ``class`` to ``value``.

----

.. _class_ClassDB_method_get_class_list:

- :ref:`PoolStringArray<class_PoolStringArray>` **get_class_list** **(** **)** |const|

Returns the names of all the classes available.

----

.. _class_ClassDB_method_get_inheriters_from_class:

- :ref:`PoolStringArray<class_PoolStringArray>` **get_inheriters_from_class** **(** :ref:`String<class_String>` class **)** |const|

Returns the names of all the classes that directly or indirectly inherit from ``class``.

----

.. _class_ClassDB_method_get_parent_class:

- :ref:`String<class_String>` **get_parent_class** **(** :ref:`String<class_String>` class **)** |const|

Returns the parent class of ``class``.

----

.. _class_ClassDB_method_instance:

- :ref:`Variant<class_Variant>` **instance** **(** :ref:`String<class_String>` class **)** |const|

Creates an instance of ``class``.

----

.. _class_ClassDB_method_is_class_enabled:

- :ref:`bool<class_bool>` **is_class_enabled** **(** :ref:`String<class_String>` class **)** |const|

Returns whether this ``class`` is enabled or not.

----

.. _class_ClassDB_method_is_parent_class:

- :ref:`bool<class_bool>` **is_parent_class** **(** :ref:`String<class_String>` class, :ref:`String<class_String>` inherits **)** |const|

Returns whether ``inherits`` is an ancestor of ``class`` or not.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
