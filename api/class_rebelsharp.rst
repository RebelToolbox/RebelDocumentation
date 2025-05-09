:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the RebelSharp.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_RebelSharp:

RebelSharp
==========

**Inherits:** :ref:`Object<class_Object>`

Bridge between Rebel Engine and the Mono runtime (Mono-enabled builds only).

Description
-----------

This class is a bridge between Rebel Engine and the Mono runtime. It exposes several low-level operations and is only available in Mono-enabled Rebel builds.

See also :ref:`CSharpScript<class_CSharpScript>`.

Methods
-------

+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| void                    | :ref:`attach_thread<class_RebelSharp_method_attach_thread>` **(** **)**                                                                     |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| void                    | :ref:`detach_thread<class_RebelSharp_method_detach_thread>` **(** **)**                                                                     |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`   | :ref:`get_domain_id<class_RebelSharp_method_get_domain_id>` **(** **)**                                                                     |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`   | :ref:`get_scripts_domain_id<class_RebelSharp_method_get_scripts_domain_id>` **(** **)**                                                     |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>` | :ref:`is_domain_finalizing_for_unload<class_RebelSharp_method_is_domain_finalizing_for_unload>` **(** :ref:`int<class_int>` domain_id **)** |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>` | :ref:`is_runtime_initialized<class_RebelSharp_method_is_runtime_initialized>` **(** **)**                                                   |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>` | :ref:`is_runtime_shutting_down<class_RebelSharp_method_is_runtime_shutting_down>` **(** **)**                                               |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>` | :ref:`is_scripts_domain_loaded<class_RebelSharp_method_is_scripts_domain_loaded>` **(** **)**                                               |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

Method Descriptions
-------------------

.. _class_RebelSharp_method_attach_thread:

- void **attach_thread** **(** **)**

Attaches the current thread to the Mono runtime.

----

.. _class_RebelSharp_method_detach_thread:

- void **detach_thread** **(** **)**

Detaches the current thread from the Mono runtime.

----

.. _class_RebelSharp_method_get_domain_id:

- :ref:`int<class_int>` **get_domain_id** **(** **)**

Returns the current MonoDomain ID.

**Note:** The Mono runtime must be initialized for this method to work (use :ref:`is_runtime_initialized<class_RebelSharp_method_is_runtime_initialized>` to check). If the Mono runtime isn't initialized at the time this method is called, the engine will crash.

----

.. _class_RebelSharp_method_get_scripts_domain_id:

- :ref:`int<class_int>` **get_scripts_domain_id** **(** **)**

Returns the scripts MonoDomain's ID. This will be the same MonoDomain ID as :ref:`get_domain_id<class_RebelSharp_method_get_domain_id>`, unless the scripts domain isn't loaded.

**Note:** The Mono runtime must be initialized for this method to work (use :ref:`is_runtime_initialized<class_RebelSharp_method_is_runtime_initialized>` to check). If the Mono runtime isn't initialized at the time this method is called, the engine will crash.

----

.. _class_RebelSharp_method_is_domain_finalizing_for_unload:

- :ref:`bool<class_bool>` **is_domain_finalizing_for_unload** **(** :ref:`int<class_int>` domain_id **)**

Returns ``true`` if the domain is being finalized, ``false`` otherwise.

----

.. _class_RebelSharp_method_is_runtime_initialized:

- :ref:`bool<class_bool>` **is_runtime_initialized** **(** **)**

Returns ``true`` if the Mono runtime is initialized, ``false`` otherwise.

----

.. _class_RebelSharp_method_is_runtime_shutting_down:

- :ref:`bool<class_bool>` **is_runtime_shutting_down** **(** **)**

Returns ``true`` if the Mono runtime is shutting down, ``false`` otherwise.

----

.. _class_RebelSharp_method_is_scripts_domain_loaded:

- :ref:`bool<class_bool>` **is_scripts_domain_loaded** **(** **)**

Returns ``true`` if the scripts domain is loaded, ``false`` otherwise.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
