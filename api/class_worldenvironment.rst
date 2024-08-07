:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the WorldEnvironment.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_WorldEnvironment:

WorldEnvironment
================

**Inherits:** :ref:`Node<class_Node>` **<** :ref:`Object<class_Object>`

Default environment properties for the entire scene (post-processing effects, lighting and background settings).

Description
-----------

The ``WorldEnvironment`` node is used to configure the default :ref:`Environment<class_Environment>` for the scene.

The parameters defined in the ``WorldEnvironment`` can be overridden by an :ref:`Environment<class_Environment>` node set on the current :ref:`Camera<class_Camera>`. Additionally, only one ``WorldEnvironment`` may be instanced in a given scene at a time.

The ``WorldEnvironment`` allows the user to specify default lighting parameters (e.g. ambient lighting), various post-processing effects (e.g. SSAO, DOF, Tonemapping), and how to draw the background (e.g. solid color, skybox). Usually, these are added in order to improve the realism/color balance of the scene.

Tutorials
---------

- :doc:`Environment and post-processing </tutorials/3d/environment_and_post_processing>`

Properties
----------

+---------------------------------------+-----------------------------------------------------------------+
| :ref:`Environment<class_Environment>` | :ref:`environment<class_WorldEnvironment_property_environment>` |
+---------------------------------------+-----------------------------------------------------------------+

Property Descriptions
---------------------

.. _class_WorldEnvironment_property_environment:

- :ref:`Environment<class_Environment>` **environment**

+----------+------------------------+
| *Setter* | set_environment(value) |
+----------+------------------------+
| *Getter* | get_environment()      |
+----------+------------------------+

The :ref:`Environment<class_Environment>` resource used by this ``WorldEnvironment``, defining the default properties.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
