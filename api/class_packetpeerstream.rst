:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the PacketPeerStream.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_PacketPeerStream:

PacketPeerStream
================

**Inherits:** :ref:`PacketPeer<class_PacketPeer>` **<** :ref:`Reference<class_Reference>` **<** :ref:`Object<class_Object>`

Wrapper to use a PacketPeer over a StreamPeer.

Description
-----------

PacketStreamPeer provides a wrapper for working using packets over a stream. This allows for using packet based code with StreamPeers. PacketPeerStream implements a custom protocol over the StreamPeer, so the user should not read or write to the wrapped StreamPeer directly.

Properties
----------

+-------------------------------------+---------------------------------------------------------------------------------------+-----------+
| :ref:`int<class_int>`               | :ref:`input_buffer_max_size<class_PacketPeerStream_property_input_buffer_max_size>`   | ``65532`` |
+-------------------------------------+---------------------------------------------------------------------------------------+-----------+
| :ref:`int<class_int>`               | :ref:`output_buffer_max_size<class_PacketPeerStream_property_output_buffer_max_size>` | ``65532`` |
+-------------------------------------+---------------------------------------------------------------------------------------+-----------+
| :ref:`StreamPeer<class_StreamPeer>` | :ref:`stream_peer<class_PacketPeerStream_property_stream_peer>`                       |           |
+-------------------------------------+---------------------------------------------------------------------------------------+-----------+

Property Descriptions
---------------------

.. _class_PacketPeerStream_property_input_buffer_max_size:

- :ref:`int<class_int>` **input_buffer_max_size**

+-----------+----------------------------------+
| *Default* | ``65532``                        |
+-----------+----------------------------------+
| *Setter*  | set_input_buffer_max_size(value) |
+-----------+----------------------------------+
| *Getter*  | get_input_buffer_max_size()      |
+-----------+----------------------------------+

----

.. _class_PacketPeerStream_property_output_buffer_max_size:

- :ref:`int<class_int>` **output_buffer_max_size**

+-----------+-----------------------------------+
| *Default* | ``65532``                         |
+-----------+-----------------------------------+
| *Setter*  | set_output_buffer_max_size(value) |
+-----------+-----------------------------------+
| *Getter*  | get_output_buffer_max_size()      |
+-----------+-----------------------------------+

----

.. _class_PacketPeerStream_property_stream_peer:

- :ref:`StreamPeer<class_StreamPeer>` **stream_peer**

+----------+------------------------+
| *Setter* | set_stream_peer(value) |
+----------+------------------------+
| *Getter* | get_stream_peer()      |
+----------+------------------------+

The wrapped :ref:`StreamPeer<class_StreamPeer>` object.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
