:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the VisualShaderNodeVectorSmoothStep.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_VisualShaderNodeVectorSmoothStep:

VisualShaderNodeVectorSmoothStep
================================

**Inherits:** :ref:`VisualShaderNode<class_VisualShaderNode>` **<** :ref:`Resource<class_Resource>` **<** :ref:`Reference<class_Reference>` **<** :ref:`Object<class_Object>`

Calculates a vector SmoothStep function within the visual shader graph.

Description
-----------

Translates to ``smoothstep(edge0, edge1, x)`` in the shader language, where ``x`` is a vector.

Returns ``0.0`` if ``x`` is smaller than ``edge0`` and ``1.0`` if ``x`` is larger than ``edge1``. Otherwise the return value is interpolated between ``0.0`` and ``1.0`` using Hermite polynomials.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
