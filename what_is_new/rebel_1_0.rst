What's new in Rebel 1.0
=======================

Rebel Engine and Rebel Editor were forked from Godot Engine in 2023; so that they can be developed with different priorities. The Rebel development philosophy is:

- Focus on the needs of the game developer before the engine developer
- Fix bugs before writing new code
- Write maintainable code that follows C++ Core Guidelines
- Reduce existing technical debt

Rebel was forked from Godot Engine 3.4.5. This version was chosen as the basis for Rebel, because it was a stable and reliable version used to develop many published games. Rebel 1.0 remains fully compatible with Godot Engine 3.4.5. Godot projects created with Godot Engine 3.4.5 can be imported and edited in Rebel Editor.

Rebel Engine and Rebel Editor 1.0 include the following updates:

Bug Fixes
---------

- `Ensure that all architecture specific folders are included in third-party libraries <https://github.com/RebelToolbox/RebelEngine/pull/5>`_
- `Replace sprintf with snprintf where needed <https://github.com/RebelToolbox/RebelEngine/pull/5>`_
- `Ensure that core files are not ignored <https://github.com/RebelToolbox/RebelEngine/pull/5>`_
- `Replace deprecated has_trivial* with std::is_trivally* <https://github.com/RebelToolbox/RebelEngine/pull/7>`_
- `Fix store to null pointer error in Image.fill() <https://github.com/RebelToolbox/RebelEngine/pull/11>`_
- `Fix read from unknown address in Image::get_pixel <https://github.com/RebelToolbox/RebelEngine/pull/12>`_
- `Fix segmentation fault when converting RGBE images to SRGB <https://github.com/RebelToolbox/RebelEngine/pull/13>`_
- `Fix methods with array parameters with mismatched bounds <https://github.com/RebelToolbox/RebelEngine/pull/8>`_
- `Fix floating-point comparison is always false warning <https://github.com/RebelToolbox/RebelEngine/pull/10>`_
- `Fix missing stdint.h in old version of V-HACD library <https://github.com/RebelToolbox/RebelEngine/pull/18>`_
- `Fix requirement for -mstackrealign comment in Android x86 <https://github.com/RebelToolbox/RebelEngine/pull/20>`_
- `Fix Windows builds <https://github.com/RebelToolbox/RebelEngine/pull/23>`_
- `Fix unwanted line-breaks and spaces in empty Dictionary default value documentation <https://github.com/RebelToolbox/RebelEngine/pull/25>`_
- `Fix the API XML documentation generation tool not removing indents on multi-line entries <https://github.com/RebelToolbox/RebelEngine/pull/25>`_
- `Fix the XML to RST documentation creation tool not removing indents properly <https://github.com/RebelToolbox/RebelEngine/pull/25>`_
- `Fix the Python shebang of the documentation status tool <https://github.com/RebelToolbox/RebelEngine/pull/25>`_
- `Fix Windows IMMNotificationClient having non-virtual destructor warning <https://github.com/RebelToolbox/RebelEngine/pull/30>`_
- `Fix Rebel Engine API documentation not displaying images <https://github.com/RebelToolbox/RebelEngine/pull/31>`_
- `Add missing newline character in RST file header <https://github.com/RebelToolbox/RebelEngine/pull/34>`_
- `Fix web export builds <https://github.com/RebelToolbox/RebelEngine/pull/38>`_
- `Fix Android JNI name mismatch <https://github.com/RebelToolbox/RebelEngine/pull/42>`_
- `Fix Android Rebel rebranding <https://github.com/RebelToolbox/RebelEngine/pull/43>`_
- `Ensure Android Java and Kotlin compile to the same version <https://github.com/RebelToolbox/RebelEngine/pull/46>`_
- `Replace distutils.dir_util.copy_tree with shutil.copytree <https://github.com/RebelToolbox/RebelEngine/pull/47>`_
- `Remove 32 bit builds from iOS <https://github.com/RebelToolbox/RebelEngine/pull/50>`_
- `Update create release to support updated Android builds <https://github.com/RebelToolbox/RebelEngine/pull/59>`_
- `Fix create release workflow not copying Android libraries <https://github.com/RebelToolbox/RebelEngine/pull/76>`_
- `Fix Windows header include order <https://github.com/RebelToolbox/RebelEngine/pull/77>`_
- `Fix create release workflow not renaming android library <https://github.com/RebelToolbox/RebelEngine/pull/87>`_
- `When a KinematicBody is stuck, set the unsafe proportion to the minimum instead of zero <https://github.com/RebelToolbox/RebelEngine/pull/97>`_
- `Don't use unsafe strcpy <https://github.com/RebelToolbox/RebelEngine/pull/95>`_
- `Refactor List operator[] to prevent compiler warnings <https://github.com/RebelToolbox/RebelEngine/pull/94>`_
- `Include cstdint in FBXCommon.h <https://github.com/RebelToolbox/RebelEngine/pull/105>`_
- `Remove 32-bit Linux builds from Rebel export templates <https://github.com/RebelToolbox/RebelEngine/pull/106>`_
- `Fix function used to detect a Rebel source root folder <https://github.com/RebelToolbox/RebelEngine/pull/113>`_
- `Remove workflow dependency on external software sources <https://github.com/RebelToolbox/RebelEngine/pull/115>`_
- `Fix control reaches end of non-void function warnings <https://github.com/RebelToolbox/RebelEngine/pull/117>`_
- `Fix patch file created from black diff on Windows <https://github.com/RebelToolbox/RebelEngine/pull/128>`_
- `Fix Visual Studio project creation <https://github.com/RebelToolbox/RebelEngine/pull/131>`_
- `Fix mono tools dependency <https://github.com/RebelToolbox/RebelEngine/pull/142>`_
- `Fix the create iOS template job <https://github.com/RebelToolbox/RebelEngine/pull/148>`_
- `Add a default copy constructor to CharProxy <https://github.com/RebelToolbox/RebelEngine/pull/154>`_
- `Make tile data size a constant <https://github.com/RebelToolbox/RebelEngine/pull/157>`_
- `Fix control reaches end of non-void function <https://github.com/RebelToolbox/RebelEngine/pull/156>`_
- `Fix greater than or equal comparisons to zero on unsigned variables <https://github.com/RebelToolbox/RebelEngine/pull/155>`_
- `Fix may be used uninitialized warning in CSG module <https://github.com/RebelToolbox/RebelEngine/pull/159>`_
- `Separate UDP packet reading and converting to integer <https://github.com/RebelToolbox/RebelEngine/pull/160>`_
- `Fix may be used uninitialized warning in Audio Server <https://github.com/RebelToolbox/RebelEngine/pull/161>`_
- `Fix may be used uninitialized in Physics Space <https://github.com/RebelToolbox/RebelEngine/pull/164>`_
- `Use an older version of Ubuntu for creating Linux builds <https://github.com/RebelToolbox/RebelEngine/pull/165>`_
- `Assign a default value of zero to MipMaps Size GL names <https://github.com/RebelToolbox/RebelEngine/pull/168>`_
- `Ensure that GLES Canvas batch pointer is never a nullptr <https://github.com/RebelToolbox/RebelEngine/pull/167>`_
- `Crash instead of returning an invalid index value <https://github.com/RebelToolbox/RebelEngine/pull/166>`_
- `Select the project when trying to add an existing project <https://github.com/RebelToolbox/RebelEngine/pull/170>`_
- `Fix Projects Manager's Projects List Item's refresh() method <https://github.com/RebelToolbox/RebelEngine/pull/179>`_
- `Fix Projects Manager's Projects List view not updating when renaming a project <https://github.com/RebelToolbox/RebelEngine/pull/181>`_
- `Fix Projects List add_project() method <https://github.com/RebelToolbox/RebelEngine/pull/182>`_
- `Fix memory leaks in ConfigFile <https://github.com/RebelToolbox/RebelEngine/pull/187>`_

Enhancements
------------

- `Apply Rebel Branding <https://github.com/RebelToolbox/RebelEngine/pull/14>`_
- `Apply Rebel Branding to Android platform <https://github.com/RebelToolbox/RebelEngine/pull/16>`_
- `Apply Rebel coding style <https://github.com/RebelToolbox/RebelEngine/pull/19>`_
- `Apply standard Black Python code style <https://github.com/RebelToolbox/RebelEngine/pull/21>`_
- `Use SPDX standard headers for all code files <https://github.com/RebelToolbox/RebelEngine/pull/22>`_
- `Use Rebel Engine splash screen <https://github.com/RebelToolbox/RebelEngine/pull/24>`_
- `Replace tabs with spaces in all documentation files <https://github.com/RebelToolbox/RebelEngine/pull/25>`_
- `Add SPDX standard headers to all documentation and translation files <https://github.com/RebelToolbox/RebelEngine/pull/25>`_
- `Use docs instead of doc when referencing multiple documentation files <https://github.com/RebelToolbox/RebelEngine/pull/25>`_
- `Rename the --doctool option to --generate-docs <https://github.com/RebelToolbox/RebelEngine/pull/25>`_
- `Remove various unused documentation creation tools <https://github.com/RebelToolbox/RebelEngine/pull/25>`_
- `Documentation and translations folder restructuring <https://github.com/RebelToolbox/RebelEngine/pull/26>`_
- `Update translations <https://github.com/RebelToolbox/RebelEngine/pull/27>`_
- `Update README.md files for translations <https://github.com/RebelToolbox/RebelEngine/pull/28>`_
- `Add API documentation spelling checks <https://github.com/RebelToolbox/RebelEngine/pull/29>`_
- `Update GitHub Actions <https://github.com/RebelToolbox/RebelEngine/pull/32>`_
- `Always use MinGW when cross-compiling for Windows on POSIX platforms <https://github.com/RebelToolbox/RebelEngine/pull/33>`_
- `Automate the update of translation files <https://github.com/RebelToolbox/RebelEngine/pull/36>`_
- `Make the Android default build arm64v8 <https://github.com/RebelToolbox/RebelEngine/pull/39>`_
- `Copy, don't move, built Android library into Java libraries folder <https://github.com/RebelToolbox/RebelEngine/pull/40>`_
- `Create Release builds workflow <https://github.com/RebelToolbox/RebelEngine/pull/41>`_
- `Apply Rebel Branding to Android classes and filenames <https://github.com/RebelToolbox/RebelEngine/pull/48>`_
- `Test Android builds on all platforms <https://github.com/RebelToolbox/RebelEngine/pull/56>`_
- `Change Android ndk_platform option to android_ndk_api <https://github.com/RebelToolbox/RebelEngine/pull/57>`_
- `Fix spelling mistake in NavigationMesh.xml <https://github.com/RebelToolbox/RebelEngine/pull/61>`_
- `Apply Rebel Branding to the X11, Windows, macOS, UWP and Server platforms <https://github.com/RebelToolbox/RebelEngine/pull/62>`_
- `Apply Rebel Branding to the iPhone and JavaScript platforms <https://github.com/RebelToolbox/RebelEngine/pull/64>`_
- `Remove creation of unused AndroidManifest.xml file <https://github.com/RebelToolbox/RebelEngine/pull/69>`_
- `Standardise the Android project folder structure <https://github.com/RebelToolbox/RebelEngine/pull/73>`_
- `Create automatic release documentation <https://github.com/RebelToolbox/RebelEngine/pull/79>`_
- `Rename platforms to better reflect their current names <https://github.com/RebelToolbox/RebelEngine/pull/80>`_
- `Automate updates from Weblate <https://github.com/RebelToolbox/RebelEngine/pull/83>`_
- `Update libsquish <https://github.com/RebelToolbox/RebelEngine/pull/85>`_
- `Add labels to automated pull requests <https://github.com/RebelToolbox/RebelEngine/pull/88>`_
- `Fix broken and updated links in the Rebel Engine API documentation <https://github.com/RebelToolbox/RebelEngine/pull/89>`_
- `Use the correct internal link format in Rebel Engine API <https://github.com/RebelToolbox/RebelEngine/pull/90>`_
- `Update broken and permanently redirected links <https://github.com/RebelToolbox/RebelEngine/pull/92>`_
- `Enable Bullet DEBUG on debug builds <https://github.com/RebelToolbox/RebelEngine/pull/96>`_
- `Include the root directory in Android CMakeLists.txt <https://github.com/RebelToolbox/RebelEngine/pull/99>`_
- `Apply Rebel branding to Rebel servers <https://github.com/RebelToolbox/RebelEngine/pull/100>`_
- `Clean up error_macros.h <https://github.com/RebelToolbox/RebelEngine/pull/98>`_
- `Update namespace formatting <https://github.com/RebelToolbox/RebelEngine/pull/102>`_
- `Apply Rebel branding to core code <https://github.com/RebelToolbox/RebelEngine/pull/110>`_
- `Remove clang-format off from Windows audio driver <https://github.com/RebelToolbox/RebelEngine/pull/111>`_
- `Remove dependence on VERSION_STATUS environmental variable <https://github.com/RebelToolbox/RebelEngine/pull/114>`_
- `Update .gitignore <https://github.com/RebelToolbox/RebelEngine/pull/116>`_
- `Improve Projects Manager <https://github.com/RebelToolbox/RebelEngine/pull/122>`_
- `Replace deprecated ANDROID_SDK_ROOT with ANDROID_HOME <https://github.com/RebelToolbox/RebelEngine/pull/132>`_
- `Rename platform folder to platforms <https://github.com/RebelToolbox/RebelEngine/pull/134>`_
- `Update .gitignore to exclude CSharp comiiled files https://github.com/RebelToolbox/RebelEngine/pull/ compiled files <https://github.com/RebelToolbox/RebelEngine/pull/141>`_
- `Upgrade ENet library to v1.3.18 <https://github.com/RebelToolbox/RebelEngine/pull/145>`_
- `Apply Rebel branding to iOS Xcode files <https://github.com/RebelToolbox/RebelEngine/pull/146>`_
- `Apply Rebel branding to OIDN changes <https://github.com/RebelToolbox/RebelEngine/pull/150>`_
- `Apply Rebel branding to modules <https://github.com/RebelToolbox/RebelEngine/pull/149>`_
- `Ignore temporary build files <https://github.com/RebelToolbox/RebelEngine/pull/163>`_
- `Treat warnings as errors in Linux build tests <https://github.com/RebelToolbox/RebelEngine/pull/169>`_
- `Fix spelling of _on_browse_button_pressed method <https://github.com/RebelToolbox/RebelEngine/pull/171>`_
- `Refactor ProjectSettings <https://github.com/RebelToolbox/RebelEngine/pull/172>`_
- `Upgrade web platform node.js modules <https://github.com/RebelToolbox/RebelEngine/pull/173>`_
- `Automate web platform tool updates <https://github.com/RebelToolbox/RebelEngine/pull/174>`_
- `Allow ScrollContainer's ensure_control_visible() method to accept a const Control parameter <https://github.com/RebelToolbox/RebelEngine/pull/180>`_
- `Simplify ProjectsList <https://github.com/RebelToolbox/RebelEngine/pull/183>`_
- `Don't create a Config File section heading, if the section name is blank <https://github.com/RebelToolbox/RebelEngine/pull/194>`_
