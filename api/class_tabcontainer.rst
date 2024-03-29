:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the TabContainer.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_TabContainer:

TabContainer
============

**Inherits:** :ref:`Container<class_Container>` **<** :ref:`Control<class_Control>` **<** :ref:`CanvasItem<class_CanvasItem>` **<** :ref:`Node<class_Node>` **<** :ref:`Object<class_Object>`

Tabbed container.

Description
-----------

Arranges :ref:`Control<class_Control>` children into a tabbed view, creating a tab for each one. The active tab's corresponding :ref:`Control<class_Control>` has its ``visible`` property set to ``true``, and all other children's to ``false``.

Ignores non-:ref:`Control<class_Control>` children.

**Note:** The drawing of the clickable tabs themselves is handled by this node. Adding :ref:`Tabs<class_Tabs>` as children is not needed.

Properties
----------

+---------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| :ref:`bool<class_bool>`                     | :ref:`all_tabs_in_front<class_TabContainer_property_all_tabs_in_front>`                       | ``false`` |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| :ref:`int<class_int>`                       | :ref:`current_tab<class_TabContainer_property_current_tab>`                                   | ``0``     |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| :ref:`bool<class_bool>`                     | :ref:`drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>`       | ``false`` |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| :ref:`TabAlign<enum_TabContainer_TabAlign>` | :ref:`tab_align<class_TabContainer_property_tab_align>`                                       | ``1``     |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| :ref:`bool<class_bool>`                     | :ref:`tabs_visible<class_TabContainer_property_tabs_visible>`                                 | ``true``  |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+
| :ref:`bool<class_bool>`                     | :ref:`use_hidden_tabs_for_min_size<class_TabContainer_property_use_hidden_tabs_for_min_size>` | ``false`` |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+-----------+

Methods
-------

+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Control<class_Control>` | :ref:`get_current_tab_control<class_TabContainer_method_get_current_tab_control>` **(** **)** |const|                                           |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Popup<class_Popup>`     | :ref:`get_popup<class_TabContainer_method_get_popup>` **(** **)** |const|                                                                       |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`         | :ref:`get_previous_tab<class_TabContainer_method_get_previous_tab>` **(** **)** |const|                                                         |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Control<class_Control>` | :ref:`get_tab_control<class_TabContainer_method_get_tab_control>` **(** :ref:`int<class_int>` tab_idx **)** |const|                             |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`         | :ref:`get_tab_count<class_TabContainer_method_get_tab_count>` **(** **)** |const|                                                               |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`       | :ref:`get_tab_disabled<class_TabContainer_method_get_tab_disabled>` **(** :ref:`int<class_int>` tab_idx **)** |const|                           |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`       | :ref:`get_tab_hidden<class_TabContainer_method_get_tab_hidden>` **(** :ref:`int<class_int>` tab_idx **)** |const|                               |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_Texture>` | :ref:`get_tab_icon<class_TabContainer_method_get_tab_icon>` **(** :ref:`int<class_int>` tab_idx **)** |const|                                   |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`         | :ref:`get_tab_idx_at_point<class_TabContainer_method_get_tab_idx_at_point>` **(** :ref:`Vector2<class_Vector2>` point **)** |const|             |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_String>`   | :ref:`get_tab_title<class_TabContainer_method_get_tab_title>` **(** :ref:`int<class_int>` tab_idx **)** |const|                                 |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`         | :ref:`get_tabs_rearrange_group<class_TabContainer_method_get_tabs_rearrange_group>` **(** **)** |const|                                         |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_popup<class_TabContainer_method_set_popup>` **(** :ref:`Node<class_Node>` popup **)**                                                 |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_tab_disabled<class_TabContainer_method_set_tab_disabled>` **(** :ref:`int<class_int>` tab_idx, :ref:`bool<class_bool>` disabled **)** |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_tab_hidden<class_TabContainer_method_set_tab_hidden>` **(** :ref:`int<class_int>` tab_idx, :ref:`bool<class_bool>` hidden **)**       |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_tab_icon<class_TabContainer_method_set_tab_icon>` **(** :ref:`int<class_int>` tab_idx, :ref:`Texture<class_Texture>` icon **)**       |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_tab_title<class_TabContainer_method_set_tab_title>` **(** :ref:`int<class_int>` tab_idx, :ref:`String<class_String>` title **)**      |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_tabs_rearrange_group<class_TabContainer_method_set_tabs_rearrange_group>` **(** :ref:`int<class_int>` group_id **)**                  |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

Theme Properties
----------------

+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`Color<class_Color>`       | :ref:`font_color_bg<class_TabContainer_theme_color_font_color_bg>`             | ``Color( 0.69, 0.69, 0.69, 1 )`` |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`Color<class_Color>`       | :ref:`font_color_disabled<class_TabContainer_theme_color_font_color_disabled>` | ``Color( 0.9, 0.9, 0.9, 0.2 )``  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`Color<class_Color>`       | :ref:`font_color_fg<class_TabContainer_theme_color_font_color_fg>`             | ``Color( 0.94, 0.94, 0.94, 1 )`` |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`int<class_int>`           | :ref:`hseparation<class_TabContainer_theme_constant_hseparation>`              | ``4``                            |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`int<class_int>`           | :ref:`label_valign_bg<class_TabContainer_theme_constant_label_valign_bg>`      | ``2``                            |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`int<class_int>`           | :ref:`label_valign_fg<class_TabContainer_theme_constant_label_valign_fg>`      | ``0``                            |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`int<class_int>`           | :ref:`side_margin<class_TabContainer_theme_constant_side_margin>`              | ``8``                            |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`int<class_int>`           | :ref:`top_margin<class_TabContainer_theme_constant_top_margin>`                | ``24``                           |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`Font<class_Font>`         | :ref:`font<class_TabContainer_theme_font_font>`                                |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`decrement<class_TabContainer_theme_icon_decrement>`                      |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`decrement_highlight<class_TabContainer_theme_icon_decrement_highlight>`  |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`increment<class_TabContainer_theme_icon_increment>`                      |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`increment_highlight<class_TabContainer_theme_icon_increment_highlight>`  |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`menu<class_TabContainer_theme_icon_menu>`                                |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`menu_highlight<class_TabContainer_theme_icon_menu_highlight>`            |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`StyleBox<class_StyleBox>` | :ref:`panel<class_TabContainer_theme_style_panel>`                             |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`StyleBox<class_StyleBox>` | :ref:`tab_bg<class_TabContainer_theme_style_tab_bg>`                           |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`StyleBox<class_StyleBox>` | :ref:`tab_disabled<class_TabContainer_theme_style_tab_disabled>`               |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+
| :ref:`StyleBox<class_StyleBox>` | :ref:`tab_fg<class_TabContainer_theme_style_tab_fg>`                           |                                  |
+---------------------------------+--------------------------------------------------------------------------------+----------------------------------+

Signals
-------

.. _class_TabContainer_signal_pre_popup_pressed:

- **pre_popup_pressed** **(** **)**

Emitted when the ``TabContainer``'s :ref:`Popup<class_Popup>` button is clicked. See :ref:`set_popup<class_TabContainer_method_set_popup>` for details.

----

.. _class_TabContainer_signal_tab_changed:

- **tab_changed** **(** :ref:`int<class_int>` tab **)**

Emitted when switching to another tab.

----

.. _class_TabContainer_signal_tab_selected:

- **tab_selected** **(** :ref:`int<class_int>` tab **)**

Emitted when a tab is selected, even if it is the current tab.

Enumerations
------------

.. _enum_TabContainer_TabAlign:

.. _class_TabContainer_constant_ALIGN_LEFT:

.. _class_TabContainer_constant_ALIGN_CENTER:

.. _class_TabContainer_constant_ALIGN_RIGHT:

enum **TabAlign**:

- **ALIGN_LEFT** = **0** --- Align the tabs to the left.

- **ALIGN_CENTER** = **1** --- Align the tabs to the center.

- **ALIGN_RIGHT** = **2** --- Align the tabs to the right.

Property Descriptions
---------------------

.. _class_TabContainer_property_all_tabs_in_front:

- :ref:`bool<class_bool>` **all_tabs_in_front**

+-----------+------------------------------+
| *Default* | ``false``                    |
+-----------+------------------------------+
| *Setter*  | set_all_tabs_in_front(value) |
+-----------+------------------------------+
| *Getter*  | is_all_tabs_in_front()       |
+-----------+------------------------------+

If ``true``, all tabs are drawn in front of the panel. If ``false``, inactive tabs are drawn behind the panel.

----

.. _class_TabContainer_property_current_tab:

- :ref:`int<class_int>` **current_tab**

+-----------+------------------------+
| *Default* | ``0``                  |
+-----------+------------------------+
| *Setter*  | set_current_tab(value) |
+-----------+------------------------+
| *Getter*  | get_current_tab()      |
+-----------+------------------------+

The current tab index. When set, this index's :ref:`Control<class_Control>` node's ``visible`` property is set to ``true`` and all others are set to ``false``.

----

.. _class_TabContainer_property_drag_to_rearrange_enabled:

- :ref:`bool<class_bool>` **drag_to_rearrange_enabled**

+-----------+--------------------------------------+
| *Default* | ``false``                            |
+-----------+--------------------------------------+
| *Setter*  | set_drag_to_rearrange_enabled(value) |
+-----------+--------------------------------------+
| *Getter*  | get_drag_to_rearrange_enabled()      |
+-----------+--------------------------------------+

If ``true``, tabs can be rearranged with mouse drag.

----

.. _class_TabContainer_property_tab_align:

- :ref:`TabAlign<enum_TabContainer_TabAlign>` **tab_align**

+-----------+----------------------+
| *Default* | ``1``                |
+-----------+----------------------+
| *Setter*  | set_tab_align(value) |
+-----------+----------------------+
| *Getter*  | get_tab_align()      |
+-----------+----------------------+

The alignment of all tabs in the tab container. See the :ref:`TabAlign<enum_TabContainer_TabAlign>` constants for details.

----

.. _class_TabContainer_property_tabs_visible:

- :ref:`bool<class_bool>` **tabs_visible**

+-----------+-------------------------+
| *Default* | ``true``                |
+-----------+-------------------------+
| *Setter*  | set_tabs_visible(value) |
+-----------+-------------------------+
| *Getter*  | are_tabs_visible()      |
+-----------+-------------------------+

If ``true``, tabs are visible. If ``false``, tabs' content and titles are hidden.

----

.. _class_TabContainer_property_use_hidden_tabs_for_min_size:

- :ref:`bool<class_bool>` **use_hidden_tabs_for_min_size**

+-----------+-----------------------------------------+
| *Default* | ``false``                               |
+-----------+-----------------------------------------+
| *Setter*  | set_use_hidden_tabs_for_min_size(value) |
+-----------+-----------------------------------------+
| *Getter*  | get_use_hidden_tabs_for_min_size()      |
+-----------+-----------------------------------------+

If ``true``, children :ref:`Control<class_Control>` nodes that are hidden have their minimum size take into account in the total, instead of only the currently visible one.

Method Descriptions
-------------------

.. _class_TabContainer_method_get_current_tab_control:

- :ref:`Control<class_Control>` **get_current_tab_control** **(** **)** |const|

Returns the child :ref:`Control<class_Control>` node located at the active tab index.

----

.. _class_TabContainer_method_get_popup:

- :ref:`Popup<class_Popup>` **get_popup** **(** **)** |const|

Returns the :ref:`Popup<class_Popup>` node instance if one has been set already with :ref:`set_popup<class_TabContainer_method_set_popup>`.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their :ref:`CanvasItem.visible<class_CanvasItem_property_visible>` property.

----

.. _class_TabContainer_method_get_previous_tab:

- :ref:`int<class_int>` **get_previous_tab** **(** **)** |const|

Returns the previously active tab index.

----

.. _class_TabContainer_method_get_tab_control:

- :ref:`Control<class_Control>` **get_tab_control** **(** :ref:`int<class_int>` tab_idx **)** |const|

Returns the :ref:`Control<class_Control>` node from the tab at index ``tab_idx``.

----

.. _class_TabContainer_method_get_tab_count:

- :ref:`int<class_int>` **get_tab_count** **(** **)** |const|

Returns the number of tabs.

----

.. _class_TabContainer_method_get_tab_disabled:

- :ref:`bool<class_bool>` **get_tab_disabled** **(** :ref:`int<class_int>` tab_idx **)** |const|

Returns ``true`` if the tab at index ``tab_idx`` is disabled.

----

.. _class_TabContainer_method_get_tab_hidden:

- :ref:`bool<class_bool>` **get_tab_hidden** **(** :ref:`int<class_int>` tab_idx **)** |const|

Returns ``true`` if the tab at index ``tab_idx`` is hidden.

----

.. _class_TabContainer_method_get_tab_icon:

- :ref:`Texture<class_Texture>` **get_tab_icon** **(** :ref:`int<class_int>` tab_idx **)** |const|

Returns the :ref:`Texture<class_Texture>` for the tab at index ``tab_idx`` or ``null`` if the tab has no :ref:`Texture<class_Texture>`.

----

.. _class_TabContainer_method_get_tab_idx_at_point:

- :ref:`int<class_int>` **get_tab_idx_at_point** **(** :ref:`Vector2<class_Vector2>` point **)** |const|

Returns the index of the tab at local coordinates ``point``. Returns ``-1`` if the point is outside the control boundaries or if there's no tab at the queried position.

----

.. _class_TabContainer_method_get_tab_title:

- :ref:`String<class_String>` **get_tab_title** **(** :ref:`int<class_int>` tab_idx **)** |const|

Returns the title of the tab at index ``tab_idx``. Tab titles default to the name of the indexed child node, but this can be overridden with :ref:`set_tab_title<class_TabContainer_method_set_tab_title>`.

----

.. _class_TabContainer_method_get_tabs_rearrange_group:

- :ref:`int<class_int>` **get_tabs_rearrange_group** **(** **)** |const|

Returns the ``TabContainer`` rearrange group id.

----

.. _class_TabContainer_method_set_popup:

- void **set_popup** **(** :ref:`Node<class_Node>` popup **)**

If set on a :ref:`Popup<class_Popup>` node instance, a popup menu icon appears in the top-right corner of the ``TabContainer``. Clicking it will expand the :ref:`Popup<class_Popup>` node.

----

.. _class_TabContainer_method_set_tab_disabled:

- void **set_tab_disabled** **(** :ref:`int<class_int>` tab_idx, :ref:`bool<class_bool>` disabled **)**

If ``disabled`` is ``true``, disables the tab at index ``tab_idx``, making it non-interactable.

----

.. _class_TabContainer_method_set_tab_hidden:

- void **set_tab_hidden** **(** :ref:`int<class_int>` tab_idx, :ref:`bool<class_bool>` hidden **)**

If ``hidden`` is ``true``, hides the tab at index ``tab_idx``, making it disappear from the tab area.

----

.. _class_TabContainer_method_set_tab_icon:

- void **set_tab_icon** **(** :ref:`int<class_int>` tab_idx, :ref:`Texture<class_Texture>` icon **)**

Sets an icon for the tab at index ``tab_idx``.

----

.. _class_TabContainer_method_set_tab_title:

- void **set_tab_title** **(** :ref:`int<class_int>` tab_idx, :ref:`String<class_String>` title **)**

Sets a title for the tab at index ``tab_idx``. Tab titles default to the name of the indexed child node.

----

.. _class_TabContainer_method_set_tabs_rearrange_group:

- void **set_tabs_rearrange_group** **(** :ref:`int<class_int>` group_id **)**

Defines rearrange group id, choose for each ``TabContainer`` the same value to enable tab drag between ``TabContainer``. Enable drag with :ref:`drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>`.

Theme Property Descriptions
---------------------------

.. _class_TabContainer_theme_color_font_color_bg:

- :ref:`Color<class_Color>` **font_color_bg**

+-----------+----------------------------------+
| *Default* | ``Color( 0.69, 0.69, 0.69, 1 )`` |
+-----------+----------------------------------+

Font color of inactive tabs.

----

.. _class_TabContainer_theme_color_font_color_disabled:

- :ref:`Color<class_Color>` **font_color_disabled**

+-----------+---------------------------------+
| *Default* | ``Color( 0.9, 0.9, 0.9, 0.2 )`` |
+-----------+---------------------------------+

Font color of disabled tabs.

----

.. _class_TabContainer_theme_color_font_color_fg:

- :ref:`Color<class_Color>` **font_color_fg**

+-----------+----------------------------------+
| *Default* | ``Color( 0.94, 0.94, 0.94, 1 )`` |
+-----------+----------------------------------+

Font color of the currently selected tab.

----

.. _class_TabContainer_theme_constant_hseparation:

- :ref:`int<class_int>` **hseparation**

+-----------+-------+
| *Default* | ``4`` |
+-----------+-------+

Horizontal separation between tabs.

----

.. _class_TabContainer_theme_constant_label_valign_bg:

- :ref:`int<class_int>` **label_valign_bg**

+-----------+-------+
| *Default* | ``2`` |
+-----------+-------+

----

.. _class_TabContainer_theme_constant_label_valign_fg:

- :ref:`int<class_int>` **label_valign_fg**

+-----------+-------+
| *Default* | ``0`` |
+-----------+-------+

----

.. _class_TabContainer_theme_constant_side_margin:

- :ref:`int<class_int>` **side_margin**

+-----------+-------+
| *Default* | ``8`` |
+-----------+-------+

The space at the left and right edges of the tab bar.

----

.. _class_TabContainer_theme_constant_top_margin:

- :ref:`int<class_int>` **top_margin**

+-----------+--------+
| *Default* | ``24`` |
+-----------+--------+

----

.. _class_TabContainer_theme_font_font:

- :ref:`Font<class_Font>` **font**

The font used to draw tab names.

----

.. _class_TabContainer_theme_icon_decrement:

- :ref:`Texture<class_Texture>` **decrement**

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the first tab is visible), it appears semi-transparent.

----

.. _class_TabContainer_theme_icon_decrement_highlight:

- :ref:`Texture<class_Texture>` **decrement_highlight**

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

----

.. _class_TabContainer_theme_icon_increment:

- :ref:`Texture<class_Texture>` **increment**

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the last tab is visible) it appears semi-transparent.

----

.. _class_TabContainer_theme_icon_increment_highlight:

- :ref:`Texture<class_Texture>` **increment_highlight**

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

----

.. _class_TabContainer_theme_icon_menu:

- :ref:`Texture<class_Texture>` **menu**

The icon for the menu button (see :ref:`set_popup<class_TabContainer_method_set_popup>`).

----

.. _class_TabContainer_theme_icon_menu_highlight:

- :ref:`Texture<class_Texture>` **menu_highlight**

The icon for the menu button (see :ref:`set_popup<class_TabContainer_method_set_popup>`) when it's being hovered with the cursor.

----

.. _class_TabContainer_theme_style_panel:

- :ref:`StyleBox<class_StyleBox>` **panel**

The style for the background fill.

----

.. _class_TabContainer_theme_style_tab_bg:

- :ref:`StyleBox<class_StyleBox>` **tab_bg**

The style of inactive tabs.

----

.. _class_TabContainer_theme_style_tab_disabled:

- :ref:`StyleBox<class_StyleBox>` **tab_disabled**

The style of disabled tabs.

----

.. _class_TabContainer_theme_style_tab_fg:

- :ref:`StyleBox<class_StyleBox>` **tab_fg**

The style of the currently selected tab.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
