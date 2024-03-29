:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the VisualShaderNodeUniform.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_VisualShaderNodeUniform:

VisualShaderNodeUniform
=======================

**Inherits:** :ref:`VisualShaderNode<class_VisualShaderNode>` **<** :ref:`Resource<class_Resource>` **<** :ref:`Reference<class_Reference>` **<** :ref:`Object<class_Object>`

**Inherited By:** :ref:`VisualShaderNodeBooleanUniform<class_VisualShaderNodeBooleanUniform>`, :ref:`VisualShaderNodeColorUniform<class_VisualShaderNodeColorUniform>`, :ref:`VisualShaderNodeScalarUniform<class_VisualShaderNodeScalarUniform>`, :ref:`VisualShaderNodeTextureUniform<class_VisualShaderNodeTextureUniform>`, :ref:`VisualShaderNodeTransformUniform<class_VisualShaderNodeTransformUniform>`, :ref:`VisualShaderNodeVec3Uniform<class_VisualShaderNodeVec3Uniform>`

A base type for the uniforms within the visual shader graph.

Description
-----------

A uniform represents a variable in the shader which is set externally, i.e. from the :ref:`ShaderMaterial<class_ShaderMaterial>`. Uniforms are exposed as properties in the :ref:`ShaderMaterial<class_ShaderMaterial>` and can be assigned from the inspector or from a script.

Properties
----------

+-----------------------------+--------------------------------------------------------------------------+--------+
| :ref:`String<class_String>` | :ref:`uniform_name<class_VisualShaderNodeUniform_property_uniform_name>` | ``""`` |
+-----------------------------+--------------------------------------------------------------------------+--------+

Property Descriptions
---------------------

.. _class_VisualShaderNodeUniform_property_uniform_name:

- :ref:`String<class_String>` **uniform_name**

+-----------+-------------------------+
| *Default* | ``""``                  |
+-----------+-------------------------+
| *Setter*  | set_uniform_name(value) |
+-----------+-------------------------+
| *Getter*  | get_uniform_name()      |
+-----------+-------------------------+

Name of the uniform, by which it can be accessed through the :ref:`ShaderMaterial<class_ShaderMaterial>` properties.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
