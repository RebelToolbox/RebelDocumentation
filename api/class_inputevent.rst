:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the InputEvent.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_InputEvent:

InputEvent
==========

**Inherits:** :ref:`Resource<class_Resource>` **<** :ref:`Reference<class_Reference>` **<** :ref:`Object<class_Object>`

**Inherited By:** :ref:`InputEventAction<class_InputEventAction>`, :ref:`InputEventJoypadButton<class_InputEventJoypadButton>`, :ref:`InputEventJoypadMotion<class_InputEventJoypadMotion>`, :ref:`InputEventMIDI<class_InputEventMIDI>`, :ref:`InputEventScreenDrag<class_InputEventScreenDrag>`, :ref:`InputEventScreenTouch<class_InputEventScreenTouch>`, :ref:`InputEventWithModifiers<class_InputEventWithModifiers>`

Generic input event.

Description
-----------

Base class of all sort of input event. See :ref:`Node._input<class_Node_method__input>`.

Tutorials
---------

- :doc:`InputEvent </tutorials/inputs/inputevent>`

- :doc:`Viewport and canvas transforms </tutorials/2d/2d_transforms>`

Properties
----------

+-----------------------+-------------------------------------------------+-------+
| :ref:`int<class_int>` | :ref:`device<class_InputEvent_property_device>` | ``0`` |
+-----------------------+-------------------------------------------------+-------+

Methods
-------

+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`             | :ref:`accumulate<class_InputEvent_method_accumulate>` **(** :ref:`InputEvent<class_InputEvent>` with_event **)**                                                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_String>`         | :ref:`as_text<class_InputEvent_method_as_text>` **(** **)** |const|                                                                                                                                             |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`           | :ref:`get_action_strength<class_InputEvent_method_get_action_strength>` **(** :ref:`String<class_String>` action, :ref:`bool<class_bool>` exact_match=false **)** |const|                                       |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`             | :ref:`is_action<class_InputEvent_method_is_action>` **(** :ref:`String<class_String>` action, :ref:`bool<class_bool>` exact_match=false **)** |const|                                                           |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`             | :ref:`is_action_pressed<class_InputEvent_method_is_action_pressed>` **(** :ref:`String<class_String>` action, :ref:`bool<class_bool>` allow_echo=false, :ref:`bool<class_bool>` exact_match=false **)** |const| |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`             | :ref:`is_action_released<class_InputEvent_method_is_action_released>` **(** :ref:`String<class_String>` action, :ref:`bool<class_bool>` exact_match=false **)** |const|                                         |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`             | :ref:`is_action_type<class_InputEvent_method_is_action_type>` **(** **)** |const|                                                                                                                               |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`             | :ref:`is_echo<class_InputEvent_method_is_echo>` **(** **)** |const|                                                                                                                                             |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`             | :ref:`is_pressed<class_InputEvent_method_is_pressed>` **(** **)** |const|                                                                                                                                       |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`             | :ref:`shortcut_match<class_InputEvent_method_shortcut_match>` **(** :ref:`InputEvent<class_InputEvent>` event, :ref:`bool<class_bool>` exact_match=true **)** |const|                                           |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`InputEvent<class_InputEvent>` | :ref:`xformed_by<class_InputEvent_method_xformed_by>` **(** :ref:`Transform2D<class_Transform2D>` xform, :ref:`Vector2<class_Vector2>` local_ofs=Vector2( 0, 0 ) **)** |const|                                  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Property Descriptions
---------------------

.. _class_InputEvent_property_device:

- :ref:`int<class_int>` **device**

+-----------+-------------------+
| *Default* | ``0``             |
+-----------+-------------------+
| *Setter*  | set_device(value) |
+-----------+-------------------+
| *Getter*  | get_device()      |
+-----------+-------------------+

The event's device ID.

**Note:** This device ID will always be ``-1`` for emulated mouse input from a touchscreen. This can be used to distinguish emulated mouse input from physical mouse input.

Method Descriptions
-------------------

.. _class_InputEvent_method_accumulate:

- :ref:`bool<class_bool>` **accumulate** **(** :ref:`InputEvent<class_InputEvent>` with_event **)**

Returns ``true`` if the given input event and this input event can be added together (only for events of type :ref:`InputEventMouseMotion<class_InputEventMouseMotion>`).

The given input event's position, global position and speed will be copied. The resulting ``relative`` is a sum of both events. Both events' modifiers have to be identical.

----

.. _class_InputEvent_method_as_text:

- :ref:`String<class_String>` **as_text** **(** **)** |const|

Returns a :ref:`String<class_String>` representation of the event.

----

.. _class_InputEvent_method_get_action_strength:

- :ref:`float<class_float>` **get_action_strength** **(** :ref:`String<class_String>` action, :ref:`bool<class_bool>` exact_match=false **)** |const|

Returns a value between 0.0 and 1.0 depending on the given actions' state. Useful for getting the value of events of type :ref:`InputEventJoypadMotion<class_InputEventJoypadMotion>`.

If ``exact_match`` is ``false``, it ignores the input modifiers for :ref:`InputEventKey<class_InputEventKey>` and :ref:`InputEventMouseButton<class_InputEventMouseButton>` events, and the direction for :ref:`InputEventJoypadMotion<class_InputEventJoypadMotion>` events.

----

.. _class_InputEvent_method_is_action:

- :ref:`bool<class_bool>` **is_action** **(** :ref:`String<class_String>` action, :ref:`bool<class_bool>` exact_match=false **)** |const|

Returns ``true`` if this input event matches a pre-defined action of any type.

If ``exact_match`` is ``false``, it ignores the input modifiers for :ref:`InputEventKey<class_InputEventKey>` and :ref:`InputEventMouseButton<class_InputEventMouseButton>` events, and the direction for :ref:`InputEventJoypadMotion<class_InputEventJoypadMotion>` events.

----

.. _class_InputEvent_method_is_action_pressed:

- :ref:`bool<class_bool>` **is_action_pressed** **(** :ref:`String<class_String>` action, :ref:`bool<class_bool>` allow_echo=false, :ref:`bool<class_bool>` exact_match=false **)** |const|

Returns ``true`` if the given action is being pressed (and is not an echo event for :ref:`InputEventKey<class_InputEventKey>` events, unless ``allow_echo`` is ``true``). Not relevant for events of type :ref:`InputEventMouseMotion<class_InputEventMouseMotion>` or :ref:`InputEventScreenDrag<class_InputEventScreenDrag>`.

If ``exact_match`` is ``false``, it ignores the input modifiers for :ref:`InputEventKey<class_InputEventKey>` and :ref:`InputEventMouseButton<class_InputEventMouseButton>` events, and the direction for :ref:`InputEventJoypadMotion<class_InputEventJoypadMotion>` events.

**Note:** Due to keyboard ghosting, :ref:`is_action_pressed<class_InputEvent_method_is_action_pressed>` may return ``false`` even if one of the action's keys is pressed. See :ref:`Input examples <tutorials/inputs/input_examples:keyboard events>` in the documentation for more information.

----

.. _class_InputEvent_method_is_action_released:

- :ref:`bool<class_bool>` **is_action_released** **(** :ref:`String<class_String>` action, :ref:`bool<class_bool>` exact_match=false **)** |const|

Returns ``true`` if the given action is released (i.e. not pressed). Not relevant for events of type :ref:`InputEventMouseMotion<class_InputEventMouseMotion>` or :ref:`InputEventScreenDrag<class_InputEventScreenDrag>`.

If ``exact_match`` is ``false``, it ignores the input modifiers for :ref:`InputEventKey<class_InputEventKey>` and :ref:`InputEventMouseButton<class_InputEventMouseButton>` events, and the direction for :ref:`InputEventJoypadMotion<class_InputEventJoypadMotion>` events.

----

.. _class_InputEvent_method_is_action_type:

- :ref:`bool<class_bool>` **is_action_type** **(** **)** |const|

Returns ``true`` if this input event's type is one that can be assigned to an input action.

----

.. _class_InputEvent_method_is_echo:

- :ref:`bool<class_bool>` **is_echo** **(** **)** |const|

Returns ``true`` if this input event is an echo event (only for events of type :ref:`InputEventKey<class_InputEventKey>`).

----

.. _class_InputEvent_method_is_pressed:

- :ref:`bool<class_bool>` **is_pressed** **(** **)** |const|

Returns ``true`` if this input event is pressed. Not relevant for events of type :ref:`InputEventMouseMotion<class_InputEventMouseMotion>` or :ref:`InputEventScreenDrag<class_InputEventScreenDrag>`.

**Note:** Due to keyboard ghosting, :ref:`is_action_pressed<class_InputEvent_method_is_action_pressed>` may return ``false`` even if one of the action's keys is pressed. See :ref:`Input examples <tutorials/inputs/input_examples:keyboard events>` in the documentation for more information.

----

.. _class_InputEvent_method_shortcut_match:

- :ref:`bool<class_bool>` **shortcut_match** **(** :ref:`InputEvent<class_InputEvent>` event, :ref:`bool<class_bool>` exact_match=true **)** |const|

Returns ``true`` if the specified ``event`` matches this event. Only valid for action events i.e key (:ref:`InputEventKey<class_InputEventKey>`), button (:ref:`InputEventMouseButton<class_InputEventMouseButton>` or :ref:`InputEventJoypadButton<class_InputEventJoypadButton>`), axis :ref:`InputEventJoypadMotion<class_InputEventJoypadMotion>` or action (:ref:`InputEventAction<class_InputEventAction>`) events.

If ``exact_match`` is ``false``, it ignores the input modifiers for :ref:`InputEventKey<class_InputEventKey>` and :ref:`InputEventMouseButton<class_InputEventMouseButton>` events, and the direction for :ref:`InputEventJoypadMotion<class_InputEventJoypadMotion>` events.

----

.. _class_InputEvent_method_xformed_by:

- :ref:`InputEvent<class_InputEvent>` **xformed_by** **(** :ref:`Transform2D<class_Transform2D>` xform, :ref:`Vector2<class_Vector2>` local_ofs=Vector2( 0, 0 ) **)** |const|

Returns a copy of the given input event which has been offset by ``local_ofs`` and transformed by ``xform``. Relevant for events of type :ref:`InputEventMouseButton<class_InputEventMouseButton>`, :ref:`InputEventMouseMotion<class_InputEventMouseMotion>`, :ref:`InputEventScreenTouch<class_InputEventScreenTouch>`, :ref:`InputEventScreenDrag<class_InputEventScreenDrag>`, :ref:`InputEventMagnifyGesture<class_InputEventMagnifyGesture>` and :ref:`InputEventPanGesture<class_InputEventPanGesture>`.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
