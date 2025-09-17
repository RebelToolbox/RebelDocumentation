List of features
================

This page aims to list all features currently supported by Rebel Engine.

.. note::

    This page lists features supported by Rebel Engine.

Features
--------

Platforms
^^^^^^^^^

**Can run both the editor and exported projects:**

- Windows 7 and later (64-bit and 32-bit).
- macOS 10.12 and later (64-bit, x86 and ARM).
- Linux (64-bit and 32-bit, x86 and ARM).

   - Binaries are statically linked and can run on any distribution if compiled
     on an old enough base distribution.
   - Official binaries are compiled on Ubuntu 14.04.

- HTML5 via WebAssembly (Firefox, Chrome, Edge, Opera).

**Runs exported projects:**

- Android 4.4 and later.
- iOS 10.0 and later.
- :doc:`Consoles </tutorials/platforms/consoles>`.
- :doc:`Headless Linux and macOS servers </tutorials/export/exporting_for_dedicated_servers>`.

Rebel Engine aims to be as platform-independent as possible and can be ported to new
platforms with relative ease.

Editor
^^^^^^

**Features:**

- Scene tree editor.
- Built-in script editor.
- Support for :doc:`external script editors </tutorials/editor/external_editor>` such as
  Visual Studio Code or Vim.
- GDScript :doc:`debugger </tutorials/scripting/debug/debugger_panel>`.

   - No support for debugging in threads yet.
- Performance monitoring tools.
- Live script reloading.
- Live scene editing.

   - Changes will reflect in the editor and will be kept after closing the running project.

- Remote inspector.

   - Changes won't reflect in the editor and won't be kept after closing the running project.

- Live camera replication.

   - Move the in-editor camera and see the result in the running project.

- Use the editor in dozens of languages contributed by the community.

**Plugins:**

Editor plugins are used to extend editor functionality.
:doc:`Create your own plugins </tutorials/plugins/editor/making_plugins>` using GDScript to add new features or speed up your workflow.

2D graphics
^^^^^^^^^^^

**Two renderers available:**

- OpenGL ES 3.0 renderer (uses OpenGL 3.3 on desktop platforms).

   - High-end visuals. Recommended on desktop platforms.

- OpenGL ES 2.0 renderer (uses OpenGL 2.1 on desktop platforms).

   - Recommended on mobile and Web platforms.

**Features:**

- Sprite, polygon and line rendering.

   - High-level tools to draw lines and polygons such as Polygon2D and Line2D.

- AnimatedSprite as a helper for creating animated sprites.
- Parallax layers.

   - Pseudo-3D support including preview in the editor.

- 2D lighting with normal maps.

   - Hard or soft shadows.

- Font rendering using bitmaps (BitmapFont) or rasterization using FreeType (DynamicFont).

   - Bitmap fonts can be exported using tools like BMFont.
   - DynamicFont supports monochrome fonts as well as colored fonts (e.g. for emoji).
     Supported formats are TTF, OTF and WOFF1.
   - DynamicFont supports optional font outlines with adjustable width and color.
   - Support for font oversampling to keep fonts sharp at higher resolutions.

- GPU-based particles with support for custom particle shaders.
- CPU-based particles.

2D tools
^^^^^^^^

- 2D camera with built-in smoothing and drag margins.
- Path2D node to represent a path in 2D space.

   - Can be drawn in the editor or generated procedurally.
   - PathFollow2D node to make nodes follow a Path2D.

- 2D geometry helper class.
- Line2D node to draw textured 2D lines.

2D physics
^^^^^^^^^^

**Physics bodies:**

- Static bodies.
- Rigid bodies.
- Kinematic bodies.
- Joints.
- Areas to detect bodies entering or leaving it.

**Collision detection:**

- Built-in shapes: line, box, circle, capsule.
- Collision polygons (can be drawn manually or generated from a sprite in the editor).

3D graphics
^^^^^^^^^^^

**Two renderers available:**

- OpenGL ES 3.0 renderer (uses OpenGL 3.3 on desktop platforms).

   - High-end visuals. Recommended on desktop platforms.
   - Optional HDR rendering with sRGB (enabled by default).
   - Uses an optional depth prepass (enabled by default) to reduce the cost of
     overdraw, which speeds up complex scene rendering.

- OpenGL ES 2.0 renderer (uses OpenGL 2.1 on desktop platforms).

   - Recommended on mobile and Web platforms.
   - LDR rendering for greater compatibility.
   - Not all features are available. Features available only when using
     the OpenGL ES 3.0 renderer are marked *GLES3* below.

**Camera:**

- Perspective, orthographic and frustum-offset cameras.

**Physically-based rendering (built-in material features):**

- Follows the Disney PBR model.
- Supports Lambert, Lambert Wrap (half-Lambert), Oren-Nayar and Toon diffuse shading modes.
- Supports Schlick-GGX, Blinn, Phong, Toon and Disabled specular shading modes.
- Uses a roughness-metallic workflow with support for ORM textures.
- Uses horizon specular occlusion (Filament model) to improve material appearance
- Normal mapping.
- Detail mapping for the albedo and normal maps.
- Distance fade which can use alpha blending or dithering to avoid going through
  the transparent pipeline.
- Dithering can be determined on a per-pixel or per-object basis.
- *GLES3:* Parallax/relief mapping with automatic level of detail based on distance.
- *GLES3:* Sub-surface scattering and transmittance.
- *GLES3:* Refraction with support for material roughness (resulting in blurry refraction).
  On GLES2, refraction is still functional but lacks support for material roughness.
- *GLES3:* Proximity fade (soft particles).

**Real-time lighting:**

- Directional lights (sun/moon). Up to 4 per scene.
- Omnidirectional lights.
- Spot lights with adjustable cone angle and attenuation.
- Specular energy can be adjusted on a per-light basis.
- *GLES3:* Lighting is done with a single-pass forward approach.
  By default, up to 32 omni light and 32 spot lights can be displayed per mesh resource.
  If needed, this limit can be increased at the cost of increased shader compilation times and lower performance.
  GLES2 uses a multi-pass forward approach to lighting, which doesn't have a
  limit on the number of lights but is slower with many lights.

**Shadow mapping:**

- *DirectionalLight:* Orthogonal (fastest), PSSM 2-split and 4-split.
  Supports blending between splits.
- *OmniLight:* Dual paraboloid (fast) or cubemap (slower but more accurate).
  Supports colored projector textures in the form of panoramas.
- *SpotLight:* Single texture.

**Global illumination with indirect lighting:**

- Baked lightmaps (fast, but can't be updated at run-time).

   - Supports baking indirect light only or baking both direct and indirect lighting.
     The bake mode can be adjusted on a per-light basis to allow for hybrid light
     baking setups.
   - Supports lighting dynamic objects using an automatic octree-based system.
     No manual probe placement is required.
   - Lightmaps are baked on the CPU.

- *GLES3:* GI probes (slower, semi-real-time). Supports reflections.

**Reflections:**

- Fast baked reflections or slow real-time reflections using ReflectionProbe.
  Parallax box correction can optionally be enabled.
- Reflection techniques can be mixed together for greater accuracy or scalability.
- *GLES3:* Voxel-based reflections (when using GI probes).
- *GLES3:* Screen-space reflections.

**Sky:**

- Panorama sky (using an HDRI).
- Procedural sky.

**Fog:**

- Depth fog with an adjustable attenuation curve.
- Height fog (floor or ceiling) with adjustable attenuation.
- Support for automatic depth fog color depending on the camera direction
  (to match the sun color).
- Optional transmittance to make lights more visible in the fog.

**Particles:**

- *GLES3:* GPU-based particles with support for custom particle shaders.
- CPU-based particles.

**Post-processing:**

- Tonemapping (Linear, Reinhard, Filmic, ACES).
- *GLES3:* Automatic exposure adjustments based on viewport brightness.
- *GLES3:* Near and far depth of field.
- *GLES3:* Screen-space ambient occlusion.
- *GLES3:* Optional debanding to avoid color banding (effective when HDR rendering is enabled).
- Glow/bloom with optional bicubic upscaling and several blend modes available:
  Screen, Soft Light, Add, Replace.
- Color correction using an one-dimensional ramp.
- Brightness, contrast and saturation adjustments.

**Texture filtering:**

- Nearest, bilinear, trilinear or anisotropic filtering.

**Texture compression:**

- Lossless or lossy WebP (does not save VRAM; only reduces storage size).
- S3TC (only supported on desktop platforms).
- ETC1 (recommended when using the GLES2 renderer).
- *GLES3:* BPTC for high-quality compression (not supported on macOS).
- *GLES3:* ETC2 (not supported on macOS).

**Anti-aliasing:**

- Multi-sample antialiasing (MSAA).
- Fast approximate antialiasing (FXAA).

**Performance:**

- Occlusion culling with :doc:`rooms and portals </tutorials/3d/portals/index>`.
  Supports gameplay notifications with primary and secondary visibility to
  disable AI/physics processing for nodes that don't need it.
- Real-time occluder spheres. Not as effective as rooms and portals
  (and doesn't support gameplay notifications), but easier to set up.

.. note::

    Most of the effects listed above can be adjusted for better performance or
    to further improve quality. This can be helpful when using Rebel Engine for
    offline rendering.

3D tools
^^^^^^^^

- Built-in meshes: cube, cylinder/cone, (hemi)sphere, prism, plane, quad.
- Tools for :doc:`procedural geometry generation </tutorials/3d/procedural_geometry/index>`.
- :doc:`Constructive solid geometry </tutorials/3d/csg_tools>` (intended for prototyping).
- Path3D node to represent a path in 3D space.

   - Can be drawn in the editor or generated procedurally.
   - PathFollow3D node to make nodes follow a Path3D.

- 3D geometry helper class.
- Support for exporting the current scene as a glTF 2.0 file from the editor.

3D physics
^^^^^^^^^^

**Physics bodies:**

- Static bodies.
- Rigid bodies.
- Kinematic bodies.
- Vehicle bodies (intended for arcade physics, not simulation).
- Joints.
- Soft bodies.
- Ragdolls.
- Areas to detect bodies entering or leaving it.

**Collision detection:**

- Built-in shapes: cuboid, sphere, capsule, cylinder.
- Generate triangle collision shapes for any mesh from the editor.
- Generate one or several convex collision shapes for any mesh from the editor.

Shaders
^^^^^^^

- *2D:* Custom vertex, fragment, and light shaders.
- *3D:* Custom vertex, fragment, light, and sky shaders.
- Text-based shaders using a :doc:`shader language inspired by GLSL </tutorials/shaders/shader_reference/shading_language>`.
- Visual shader editor.

   - Support for visual shader plugins.

Scripting
^^^^^^^^^

**General:**

- Object-oriented design pattern with scripts extending nodes.
- Signals and groups for communicating between scripts.
- Support for :doc:`cross-language scripting </tutorials/scripting/cross_language_scripting>`.
- Many 2D and 3D linear algebra data types such as vectors and transforms.

:ref:`GDScript: <toc-learn-scripting-gdscript>`

- :doc:`High-level interpreted language </tutorials/scripting/gdscript/gdscript_basics>` with
  :doc:`optional static typing </tutorials/scripting/gdscript/static_typing>`.
- Syntax inspired by Python.
- Syntax highlighting is provided on GitHub.
- :doc:`Use threads </tutorials/performance/threads/using_multiple_threads>` to perform asynchronous actions
  or make use of multiple processor cores.

:ref:`C#: <toc-learn-scripting-C#>`

- Packaged in a separate binary to keep file sizes and dependencies down.
- Uses Mono 6.x.

   - Full support for the C# 7.0 syntax and features.

- Supports all platforms.
- Using an external editor is recommended to benefit from IDE functionality.

:ref:`VisualScript: <toc-learn-scripting-visual_script>`

- :doc:`Graph-based visual scripting language </tutorials/scripting/visual_script/what_is_visual_scripting>`.
- Works best when used for specific purposes (such as level-specific logic)
  rather than as a language to create entire projects.

While Rebel Engine will keep VisualScript supported, we recommend
:ref:`trying out GDScript <toc-learn-scripting-gdscript>` instead.

**GDNative (C, C++, Rust, D, ...):**

- When you need it, link to native libraries for higher performance and third-party integrations.

   - For scripting game logic, GDScript or C# are recommended if their
     performance is suitable.

- Official bindings for C and C++.

   - Use any build system and language features you wish.

Audio
^^^^^

**Features:**

- Mono, stereo, 5.1 and 7.1 output.
- Non-positional and positional playback in 2D and 3D.

   - Optional Doppler effect in 2D and 3D.

- Support for re-routable :doc:`audio buses </tutorials/audio/audio_buses>` and effects
  with dozens of effects included.
- Listener2D and Listener3D nodes to listen from a position different than the camera.
- Audio input to record microphones with real-time access using the AudioEffectCapture class.
- MIDI input.

   - No support for MIDI output yet.

**APIs used:**

- *Windows:* WASAPI.
- *macOS:* CoreAudio.
- *Linux:* PulseAudio or ALSA.

Import
^^^^^^

- Support for :doc:`custom import plugins </tutorials/plugins/editor/import_plugins>`.

**Formats:**

- *Images:* See :doc:`/tutorials/assets_pipeline/importing_images`.
- *Audio:*

   - WAV with optional IMA-ADPCM compression.
   - Ogg Vorbis.
   - MP3.

- *3D scenes:*

   - glTF 2.0 *(recommended)*.
   - FBX (experimental, static meshes only).
   - Collada (.dae).
   - Wavefront OBJ (static scenes only, can be loaded directly as a mesh).

- 3D meshes use `Mikktspace <http://www.mikktspace.com/>`__ to generate tangents
  on import, which ensures consistency with other 3D applications such as Blender.

Input
^^^^^

- Input mapping system using hardcoded input events or remappable input actions.

   - Axis values can be mapped to two different actions with a configurable deadzone.
   - Use the same code to support both keyboards and gamepads.

- Keyboard input.

   - Keys can be mapped in "physical" mode to be independent of the keyboard layout.

- Mouse input.

   - The mouse cursor can be visible, hidden, captured or confined within the window.
   - When captured, raw input will be used on Windows and Linux to
     sidestep the OS' mouse acceleration settings.

- Gamepad input (up to 8 simultaneous controllers).
- Pen/tablet input with pressure support.
- Gamepad, keyboard and mouse input support are also available on Android.

Navigation
^^^^^^^^^^

- A* algorithm in 2D and 3D.
- Navigation meshes.
- Generate navigation meshes from the editor.

Networking
^^^^^^^^^^

- Low-level TCP networking using StreamPeer and TCP_Server.
- Low-level UDP networking using PacketPeer and UDPServer.
- Low-level HTTP requests using HTTPClient.
- High-level HTTP requests using HTTPRequest.

   - Supports HTTPS out of the box using bundled certificates.

- High-level multiplayer API using UDP and ENet.

   - Automatic replication using remote procedure calls (RPCs).
   - Supports unreliable, reliable and ordered transfers.

- WebSocket client and server, available on all platforms.
- WebRTC client and server, available on all platforms.
- Support for UPnP to sidestep the requirement to forward ports when hosting
  a server behind a NAT.

Internationalization
^^^^^^^^^^^^^^^^^^^^

- Full support for Unicode including emoji.
- Store localization strings using :doc:`CSV </tutorials/i18n/internationalizing_games>`
  or :doc:`gettext </tutorials/i18n/localization_using_gettext>`.
- Use localized strings in your project automatically in GUI elements or by
  using the ``tr()`` function.

Windowing and OS integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Move, resize, minimize, and maximize the window spawned by the project.
- Change the window title and icon.
- Request attention (will cause the title bar to blink on most platforms).
- Fullscreen mode.

   - Doesn't use exclusive fullscreen, so the screen resolution can't be changed this way.
     Use a Viewport with a different resolution instead.

- Borderless window (fullscreen or non-fullscreen).
- Ability to keep the window always on top.
- Transparent window with per-pixel transparency.
- Global menu integration on macOS.
- Execute commands in a blocking or non-blocking manner.
- Open file paths and URLs using default or custom protocol handlers (if registered on the system).
- Parse custom command line arguments.
- :doc:`Headless/server binaries </tutorials/export/exporting_for_dedicated_servers>` can be
  downloaded for Linux and :doc:`compiled for macOS </development/compiling/compiling_for_osx>`.
  Any binary can be used without a window using the ``--no-window``
  :doc:`command line argument </tutorials/editor/command_line_tutorial>`.

Mobile
^^^^^^

- In-app purchases on Android and iOS.
- Support for advertisements using third-party modules.
- Support for subview embedding on Android.

XR support (AR and VR)
^^^^^^^^^^^^^^^^^^^^^^

- Support for ARKit on iOS out of the box.
- Support for the OpenXR APIs.

   - Includes support for popular headsets like the Meta Quest and the Valve Index.

- Support for the OpenVR APIs.

GUI system
^^^^^^^^^^

Rebel Engine's GUI is built using the same Control nodes used to make games in Rebel Engine.
The editor UI can easily be extended in many ways using add-ons.

**Nodes:**

- Buttons.
- Checkboxes, check buttons, radio buttons.
- Text entry using LineEdit (single line) and TextEdit (multiple lines).
- Dropdown menus using PopupMenu and OptionButton.
- Scrollbars.
- Labels.
- RichTextLabel for :doc:`text formatted using BBCode </tutorials/ui/bbcode_in_richtextlabel>`.
- Trees (can also be used to represent tables).
- Color picker with RGB and HSV modes.
- Containers (horizontal, vertical, grid, flow, center, margin, aspect ratio, draggable splitter, ...).
- Controls can be rotated and scaled.

**Sizing:**

- Anchors to keep GUI elements in a specific corner, edge or centered.
- Containers to place GUI elements automatically following certain rules.

   - :ref:`Stack <class_BoxContainer>` layouts.
   - :ref:`Grid <class_GridContainer>` layouts.
   - :ref:`Margin <class_MarginContainer>` and :ref:`centered <class_CenterContainer>`
     layouts.
   - :ref:`Draggable splitter <class_SplitContainer>` layouts.

- Scale to multiple resolutions using the ``2d`` or ``viewport`` stretch modes.
- Support any aspect ratio using anchors and the ``expand`` stretch aspect.

**Theming:**

- Built-in theme editor.

   - Generate a theme based on the current editor theme settings.

- Procedural vector-based theming using :ref:`class_StyleBoxFlat`.

   - Supports rounded/beveled corners, drop shadows, per-border widths and antialiasing.

- Texture-based theming using :ref:`class_StyleBoxTexture`.

Rebel Engine's small distribution size can make it a suitable alternative to frameworks
like Electron or Qt.

Animation
^^^^^^^^^

- Direct kinematics and inverse kinematics.
- :ref:`Tween <class_Tween>` node to easily perform procedural animations by code.
- Support for animating any property with customizable interpolation.
- Support for calling methods in animation tracks.
- Support for playing sounds in animation tracks.
- Support for Bézier curves in animation.

File formats
^^^^^^^^^^^^

- Scenes and resources can be saved in :doc:`text-based </development/file_formats/tscn>` or binary formats.

   - Text-based formats are human-readable and more friendly to version control.
   - Binary formats are faster to save/load for large scenes/resources.

- Read and write text or binary files using :ref:`class_File`.

   - Can optionally be compressed or encrypted.

- Read and write :ref:`class_JSON` files.
- Read and write INI-style configuration files using :ref:`class_ConfigFile`.

   - Can (de)serialize any Rebel Engine datatype, including Vector2/3, Color, ...

- Read XML files using :ref:`class_XMLParser`.
- Pack game data into a PCK file (custom format optimized for fast seeking),
  into a ZIP archive, or directly into the executable for single-file distribution.
- :doc:`Export additional PCK files</tutorials/export/exporting_pcks>` that can be read
  by the engine to support mods and DLCs.

Miscellaneous
^^^^^^^^^^^^^

- :doc:`Low-level access to servers </tutorials/performance/using_servers>` which allows bypassing
  the scene tree's overhead when needed.
- :doc:`Command line interface </tutorials/editor/command_line_tutorial>` for automation.

   - Export and deploy projects using continuous integration platforms.
   - `Shell completion scripts <https://github.com/RebelToolbox/RebelEngine/tree/main/tools/dist/shell>`__
     are available for Bash, zsh and fish.

- Support for :doc:`C++ modules </development/engine/custom_modules_in_cpp>` statically linked
  into the engine binary.
- Engine and editor written in C++03.

   - Can be :doc:`compiled </development/compiling/introduction_to_the_buildsystem>` using GCC,
     Clang and MSVC. MinGW is also supported.
   - Friendly towards packagers. In most cases, system libraries can be used
     instead of the ones provided by Rebel Engine. The build system doesn't download anything.
     Builds can be fully reproducible.

- Licensed under the permissive MIT license.

   - Open development process with :doc:`contributions welcome </contributing/ways_to_contribute>`.
