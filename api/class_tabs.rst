:github_url: hide

.. Generated automatically by RebelEngine/tools/scripts/rst_from_xml.py
.. DO NOT EDIT THIS FILE, but the Tabs.xml source instead.
.. The source is found in docs or modules/<name>/docs.

.. _class_Tabs:

Tabs
====

**Inherits:** :ref:`Control<class_Control>` **<** :ref:`CanvasItem<class_CanvasItem>` **<** :ref:`Node<class_Node>` **<** :ref:`Object<class_Object>`

Tabs control.

Description
-----------

Simple tabs control, similar to :ref:`TabContainer<class_TabContainer>` but is only in charge of drawing tabs, not interacting with children.

Properties
----------

+---------------------------------------------------------------------+---------------------------------------------------------------------------------+-----------+
| :ref:`int<class_int>`                                               | :ref:`current_tab<class_Tabs_property_current_tab>`                             | ``0``     |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------+-----------+
| :ref:`bool<class_bool>`                                             | :ref:`drag_to_rearrange_enabled<class_Tabs_property_drag_to_rearrange_enabled>` | ``false`` |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------+-----------+
| :ref:`bool<class_bool>`                                             | :ref:`scrolling_enabled<class_Tabs_property_scrolling_enabled>`                 | ``true``  |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------+-----------+
| :ref:`TabAlign<enum_Tabs_TabAlign>`                                 | :ref:`tab_align<class_Tabs_property_tab_align>`                                 | ``1``     |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------+-----------+
| :ref:`CloseButtonDisplayPolicy<enum_Tabs_CloseButtonDisplayPolicy>` | :ref:`tab_close_display_policy<class_Tabs_property_tab_close_display_policy>`   | ``0``     |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------+-----------+

Methods
-------

+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`add_tab<class_Tabs_method_add_tab>` **(** :ref:`String<class_String>` title="", :ref:`Texture<class_Texture>` icon=null **)**     |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`ensure_tab_visible<class_Tabs_method_ensure_tab_visible>` **(** :ref:`int<class_int>` idx **)**                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`       | :ref:`get_offset_buttons_visible<class_Tabs_method_get_offset_buttons_visible>` **(** **)** |const|                                     |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`         | :ref:`get_previous_tab<class_Tabs_method_get_previous_tab>` **(** **)** |const|                                                         |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`       | :ref:`get_select_with_rmb<class_Tabs_method_get_select_with_rmb>` **(** **)** |const|                                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`         | :ref:`get_tab_count<class_Tabs_method_get_tab_count>` **(** **)** |const|                                                               |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`       | :ref:`get_tab_disabled<class_Tabs_method_get_tab_disabled>` **(** :ref:`int<class_int>` tab_idx **)** |const|                           |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_Texture>` | :ref:`get_tab_icon<class_Tabs_method_get_tab_icon>` **(** :ref:`int<class_int>` tab_idx **)** |const|                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`         | :ref:`get_tab_offset<class_Tabs_method_get_tab_offset>` **(** **)** |const|                                                             |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_Rect2>`     | :ref:`get_tab_rect<class_Tabs_method_get_tab_rect>` **(** :ref:`int<class_int>` tab_idx **)** |const|                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_String>`   | :ref:`get_tab_title<class_Tabs_method_get_tab_title>` **(** :ref:`int<class_int>` tab_idx **)** |const|                                 |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`         | :ref:`get_tabs_rearrange_group<class_Tabs_method_get_tabs_rearrange_group>` **(** **)** |const|                                         |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`move_tab<class_Tabs_method_move_tab>` **(** :ref:`int<class_int>` from, :ref:`int<class_int>` to **)**                            |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`remove_tab<class_Tabs_method_remove_tab>` **(** :ref:`int<class_int>` tab_idx **)**                                               |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_select_with_rmb<class_Tabs_method_set_select_with_rmb>` **(** :ref:`bool<class_bool>` enabled **)**                           |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_tab_disabled<class_Tabs_method_set_tab_disabled>` **(** :ref:`int<class_int>` tab_idx, :ref:`bool<class_bool>` disabled **)** |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_tab_icon<class_Tabs_method_set_tab_icon>` **(** :ref:`int<class_int>` tab_idx, :ref:`Texture<class_Texture>` icon **)**       |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_tab_title<class_Tabs_method_set_tab_title>` **(** :ref:`int<class_int>` tab_idx, :ref:`String<class_String>` title **)**      |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| void                          | :ref:`set_tabs_rearrange_group<class_Tabs_method_set_tabs_rearrange_group>` **(** :ref:`int<class_int>` group_id **)**                  |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

Theme Properties
----------------

+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`Color<class_Color>`       | :ref:`font_color_bg<class_Tabs_theme_color_font_color_bg>`             | ``Color( 0.69, 0.69, 0.69, 1 )`` |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`Color<class_Color>`       | :ref:`font_color_disabled<class_Tabs_theme_color_font_color_disabled>` | ``Color( 0.9, 0.9, 0.9, 0.2 )``  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`Color<class_Color>`       | :ref:`font_color_fg<class_Tabs_theme_color_font_color_fg>`             | ``Color( 0.94, 0.94, 0.94, 1 )`` |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`int<class_int>`           | :ref:`hseparation<class_Tabs_theme_constant_hseparation>`              | ``4``                            |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`int<class_int>`           | :ref:`label_valign_bg<class_Tabs_theme_constant_label_valign_bg>`      | ``2``                            |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`int<class_int>`           | :ref:`label_valign_fg<class_Tabs_theme_constant_label_valign_fg>`      | ``0``                            |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`int<class_int>`           | :ref:`top_margin<class_Tabs_theme_constant_top_margin>`                | ``24``                           |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`Font<class_Font>`         | :ref:`font<class_Tabs_theme_font_font>`                                |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`close<class_Tabs_theme_icon_close>`                              |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`decrement<class_Tabs_theme_icon_decrement>`                      |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`decrement_highlight<class_Tabs_theme_icon_decrement_highlight>`  |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`increment<class_Tabs_theme_icon_increment>`                      |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`Texture<class_Texture>`   | :ref:`increment_highlight<class_Tabs_theme_icon_increment_highlight>`  |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`StyleBox<class_StyleBox>` | :ref:`button<class_Tabs_theme_style_button>`                           |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`StyleBox<class_StyleBox>` | :ref:`button_pressed<class_Tabs_theme_style_button_pressed>`           |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`StyleBox<class_StyleBox>` | :ref:`tab_bg<class_Tabs_theme_style_tab_bg>`                           |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`StyleBox<class_StyleBox>` | :ref:`tab_disabled<class_Tabs_theme_style_tab_disabled>`               |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+
| :ref:`StyleBox<class_StyleBox>` | :ref:`tab_fg<class_Tabs_theme_style_tab_fg>`                           |                                  |
+---------------------------------+------------------------------------------------------------------------+----------------------------------+

Signals
-------

.. _class_Tabs_signal_reposition_active_tab_request:

- **reposition_active_tab_request** **(** :ref:`int<class_int>` idx_to **)**

Emitted when the active tab is rearranged via mouse drag. See :ref:`drag_to_rearrange_enabled<class_Tabs_property_drag_to_rearrange_enabled>`.

----

.. _class_Tabs_signal_right_button_pressed:

- **right_button_pressed** **(** :ref:`int<class_int>` tab **)**

Emitted when a tab is right-clicked.

----

.. _class_Tabs_signal_tab_changed:

- **tab_changed** **(** :ref:`int<class_int>` tab **)**

Emitted when switching to another tab.

----

.. _class_Tabs_signal_tab_clicked:

- **tab_clicked** **(** :ref:`int<class_int>` tab **)**

Emitted when a tab is clicked, even if it is the current tab.

----

.. _class_Tabs_signal_tab_close:

- **tab_close** **(** :ref:`int<class_int>` tab **)**

Emitted when a tab is closed.

----

.. _class_Tabs_signal_tab_hover:

- **tab_hover** **(** :ref:`int<class_int>` tab **)**

Emitted when a tab is hovered by the mouse.

Enumerations
------------

.. _enum_Tabs_TabAlign:

.. _class_Tabs_constant_ALIGN_LEFT:

.. _class_Tabs_constant_ALIGN_CENTER:

.. _class_Tabs_constant_ALIGN_RIGHT:

.. _class_Tabs_constant_ALIGN_MAX:

enum **TabAlign**:

- **ALIGN_LEFT** = **0** --- Align the tabs to the left.

- **ALIGN_CENTER** = **1** --- Align the tabs to the center.

- **ALIGN_RIGHT** = **2** --- Align the tabs to the right.

- **ALIGN_MAX** = **3** --- Represents the size of the :ref:`TabAlign<enum_Tabs_TabAlign>` enum.

----

.. _enum_Tabs_CloseButtonDisplayPolicy:

.. _class_Tabs_constant_CLOSE_BUTTON_SHOW_NEVER:

.. _class_Tabs_constant_CLOSE_BUTTON_SHOW_ACTIVE_ONLY:

.. _class_Tabs_constant_CLOSE_BUTTON_SHOW_ALWAYS:

.. _class_Tabs_constant_CLOSE_BUTTON_MAX:

enum **CloseButtonDisplayPolicy**:

- **CLOSE_BUTTON_SHOW_NEVER** = **0** --- Never show the close buttons.

- **CLOSE_BUTTON_SHOW_ACTIVE_ONLY** = **1** --- Only show the close button on the currently active tab.

- **CLOSE_BUTTON_SHOW_ALWAYS** = **2** --- Show the close button on all tabs.

- **CLOSE_BUTTON_MAX** = **3** --- Represents the size of the :ref:`CloseButtonDisplayPolicy<enum_Tabs_CloseButtonDisplayPolicy>` enum.

Property Descriptions
---------------------

.. _class_Tabs_property_current_tab:

- :ref:`int<class_int>` **current_tab**

+-----------+------------------------+
| *Default* | ``0``                  |
+-----------+------------------------+
| *Setter*  | set_current_tab(value) |
+-----------+------------------------+
| *Getter*  | get_current_tab()      |
+-----------+------------------------+

Select tab at index ``tab_idx``.

----

.. _class_Tabs_property_drag_to_rearrange_enabled:

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

.. _class_Tabs_property_scrolling_enabled:

- :ref:`bool<class_bool>` **scrolling_enabled**

+-----------+------------------------------+
| *Default* | ``true``                     |
+-----------+------------------------------+
| *Setter*  | set_scrolling_enabled(value) |
+-----------+------------------------------+
| *Getter*  | get_scrolling_enabled()      |
+-----------+------------------------------+

if ``true``, the mouse's scroll wheel can be used to navigate the scroll view.

----

.. _class_Tabs_property_tab_align:

- :ref:`TabAlign<enum_Tabs_TabAlign>` **tab_align**

+-----------+----------------------+
| *Default* | ``1``                |
+-----------+----------------------+
| *Setter*  | set_tab_align(value) |
+-----------+----------------------+
| *Getter*  | get_tab_align()      |
+-----------+----------------------+

The alignment of all tabs. See :ref:`TabAlign<enum_Tabs_TabAlign>` for details.

----

.. _class_Tabs_property_tab_close_display_policy:

- :ref:`CloseButtonDisplayPolicy<enum_Tabs_CloseButtonDisplayPolicy>` **tab_close_display_policy**

+-----------+-------------------------------------+
| *Default* | ``0``                               |
+-----------+-------------------------------------+
| *Setter*  | set_tab_close_display_policy(value) |
+-----------+-------------------------------------+
| *Getter*  | get_tab_close_display_policy()      |
+-----------+-------------------------------------+

Sets when the close button will appear on the tabs. See :ref:`CloseButtonDisplayPolicy<enum_Tabs_CloseButtonDisplayPolicy>` for details.

Method Descriptions
-------------------

.. _class_Tabs_method_add_tab:

- void **add_tab** **(** :ref:`String<class_String>` title="", :ref:`Texture<class_Texture>` icon=null **)**

Adds a new tab.

----

.. _class_Tabs_method_ensure_tab_visible:

- void **ensure_tab_visible** **(** :ref:`int<class_int>` idx **)**

Moves the scroll view to make the tab visible.

----

.. _class_Tabs_method_get_offset_buttons_visible:

- :ref:`bool<class_bool>` **get_offset_buttons_visible** **(** **)** |const|

Returns ``true`` if the offset buttons (the ones that appear when there's not enough space for all tabs) are visible.

----

.. _class_Tabs_method_get_previous_tab:

- :ref:`int<class_int>` **get_previous_tab** **(** **)** |const|

Returns the previously active tab index.

----

.. _class_Tabs_method_get_select_with_rmb:

- :ref:`bool<class_bool>` **get_select_with_rmb** **(** **)** |const|

Returns ``true`` if select with right mouse button is enabled.

----

.. _class_Tabs_method_get_tab_count:

- :ref:`int<class_int>` **get_tab_count** **(** **)** |const|

Returns the number of tabs.

----

.. _class_Tabs_method_get_tab_disabled:

- :ref:`bool<class_bool>` **get_tab_disabled** **(** :ref:`int<class_int>` tab_idx **)** |const|

Returns ``true`` if the tab at index ``tab_idx`` is disabled.

----

.. _class_Tabs_method_get_tab_icon:

- :ref:`Texture<class_Texture>` **get_tab_icon** **(** :ref:`int<class_int>` tab_idx **)** |const|

Returns the :ref:`Texture<class_Texture>` for the tab at index ``tab_idx`` or ``null`` if the tab has no :ref:`Texture<class_Texture>`.

----

.. _class_Tabs_method_get_tab_offset:

- :ref:`int<class_int>` **get_tab_offset** **(** **)** |const|

Returns the number of hidden tabs offsetted to the left.

----

.. _class_Tabs_method_get_tab_rect:

- :ref:`Rect2<class_Rect2>` **get_tab_rect** **(** :ref:`int<class_int>` tab_idx **)** |const|

Returns tab :ref:`Rect2<class_Rect2>` with local position and size.

----

.. _class_Tabs_method_get_tab_title:

- :ref:`String<class_String>` **get_tab_title** **(** :ref:`int<class_int>` tab_idx **)** |const|

Returns the title of the tab at index ``tab_idx``.

----

.. _class_Tabs_method_get_tabs_rearrange_group:

- :ref:`int<class_int>` **get_tabs_rearrange_group** **(** **)** |const|

Returns the ``Tabs``' rearrange group ID.

----

.. _class_Tabs_method_move_tab:

- void **move_tab** **(** :ref:`int<class_int>` from, :ref:`int<class_int>` to **)**

Moves a tab from ``from`` to ``to``.

----

.. _class_Tabs_method_remove_tab:

- void **remove_tab** **(** :ref:`int<class_int>` tab_idx **)**

Removes the tab at index ``tab_idx``.

----

.. _class_Tabs_method_set_select_with_rmb:

- void **set_select_with_rmb** **(** :ref:`bool<class_bool>` enabled **)**

If ``true``, enables selecting a tab with the right mouse button.

----

.. _class_Tabs_method_set_tab_disabled:

- void **set_tab_disabled** **(** :ref:`int<class_int>` tab_idx, :ref:`bool<class_bool>` disabled **)**

If ``disabled`` is ``true``, disables the tab at index ``tab_idx``, making it non-interactable.

----

.. _class_Tabs_method_set_tab_icon:

- void **set_tab_icon** **(** :ref:`int<class_int>` tab_idx, :ref:`Texture<class_Texture>` icon **)**

Sets an ``icon`` for the tab at index ``tab_idx``.

----

.. _class_Tabs_method_set_tab_title:

- void **set_tab_title** **(** :ref:`int<class_int>` tab_idx, :ref:`String<class_String>` title **)**

Sets a ``title`` for the tab at index ``tab_idx``.

----

.. _class_Tabs_method_set_tabs_rearrange_group:

- void **set_tabs_rearrange_group** **(** :ref:`int<class_int>` group_id **)**

Defines the rearrange group ID. Choose for each ``Tabs`` the same value to dragging tabs between ``Tabs``. Enable drag with :ref:`drag_to_rearrange_enabled<class_Tabs_property_drag_to_rearrange_enabled>`.

Theme Property Descriptions
---------------------------

.. _class_Tabs_theme_color_font_color_bg:

- :ref:`Color<class_Color>` **font_color_bg**

+-----------+----------------------------------+
| *Default* | ``Color( 0.69, 0.69, 0.69, 1 )`` |
+-----------+----------------------------------+

Font color of inactive tabs.

----

.. _class_Tabs_theme_color_font_color_disabled:

- :ref:`Color<class_Color>` **font_color_disabled**

+-----------+---------------------------------+
| *Default* | ``Color( 0.9, 0.9, 0.9, 0.2 )`` |
+-----------+---------------------------------+

Font color of disabled tabs.

----

.. _class_Tabs_theme_color_font_color_fg:

- :ref:`Color<class_Color>` **font_color_fg**

+-----------+----------------------------------+
| *Default* | ``Color( 0.94, 0.94, 0.94, 1 )`` |
+-----------+----------------------------------+

Font color of the currently selected tab.

----

.. _class_Tabs_theme_constant_hseparation:

- :ref:`int<class_int>` **hseparation**

+-----------+-------+
| *Default* | ``4`` |
+-----------+-------+

The horizontal separation between the tabs.

----

.. _class_Tabs_theme_constant_label_valign_bg:

- :ref:`int<class_int>` **label_valign_bg**

+-----------+-------+
| *Default* | ``2`` |
+-----------+-------+

----

.. _class_Tabs_theme_constant_label_valign_fg:

- :ref:`int<class_int>` **label_valign_fg**

+-----------+-------+
| *Default* | ``0`` |
+-----------+-------+

----

.. _class_Tabs_theme_constant_top_margin:

- :ref:`int<class_int>` **top_margin**

+-----------+--------+
| *Default* | ``24`` |
+-----------+--------+

----

.. _class_Tabs_theme_font_font:

- :ref:`Font<class_Font>` **font**

The font used to draw tab names.

----

.. _class_Tabs_theme_icon_close:

- :ref:`Texture<class_Texture>` **close**

The icon for the close button (see :ref:`tab_close_display_policy<class_Tabs_property_tab_close_display_policy>`).

----

.. _class_Tabs_theme_icon_decrement:

- :ref:`Texture<class_Texture>` **decrement**

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the first tab is visible), it appears semi-transparent.

----

.. _class_Tabs_theme_icon_decrement_highlight:

- :ref:`Texture<class_Texture>` **decrement_highlight**

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

----

.. _class_Tabs_theme_icon_increment:

- :ref:`Texture<class_Texture>` **increment**

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the last tab is visible) it appears semi-transparent.

----

.. _class_Tabs_theme_icon_increment_highlight:

- :ref:`Texture<class_Texture>` **increment_highlight**

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

----

.. _class_Tabs_theme_style_button:

- :ref:`StyleBox<class_StyleBox>` **button**

Background of the close button when it's being hovered with the cursor.

----

.. _class_Tabs_theme_style_button_pressed:

- :ref:`StyleBox<class_StyleBox>` **button_pressed**

Background of the close button when it's being pressed.

----

.. _class_Tabs_theme_style_tab_bg:

- :ref:`StyleBox<class_StyleBox>` **tab_bg**

The style of an inactive tab.

----

.. _class_Tabs_theme_style_tab_disabled:

- :ref:`StyleBox<class_StyleBox>` **tab_disabled**

The style of a disabled tab

----

.. _class_Tabs_theme_style_tab_fg:

- :ref:`StyleBox<class_StyleBox>` **tab_fg**

The style of the currently selected tab.

.. |virtual| replace:: :abbr:`virtual (This method should typically be overridden by the user to have any effect.)`
.. |const| replace:: :abbr:`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`
.. |vararg| replace:: :abbr:`vararg (This method accepts any number of arguments after the ones described here.)`
