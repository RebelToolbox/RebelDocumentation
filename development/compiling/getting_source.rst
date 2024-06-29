Getting the source
==================

.. highlight:: shell

Downloading the Rebel Engine source code
----------------------------------------

Before :doc:`getting into the SCons build system </development/compiling/introduction_to_the_buildsystem>`
and compiling Rebel Engine, you need to actually download the Rebel Engine source code.

The source code is available on `GitHub <https://github.com/RebelToolbox/RebelEngine>`__
and while you can manually download it via the website, in general you want to
do it via the ``git`` version control system.

If you are compiling in order to make contributions or pull requests, you should
follow the instructions from the :doc:`Pull Request workflow </contributing/pr_workflow>`.

If you don't know much about ``git`` yet, there are a great number of
`tutorials <https://git-scm.com/book>`__ available on various websites.

In general, you need to install ``git`` and/or one of the various GUI clients.

Afterwards, to get the latest development version of the Rebel Engine source code
(the unstable ``main`` branch), you can use ``git clone``.

If you are using the ``git`` command line client, this is done by entering
the following in a terminal:

::

    git clone https://github.com/RebelToolbox/RebelEngine.git
    # You can add the --depth 1 argument to omit the commit history.
    # Faster, but not all Git operations (like blame) will work.

For any stable release, visit the `release page <https://github.com/RebelToolbox/RebelEngine/releases>`__
and click on the link for the release you want.
You can then download and extract the source from the download link on the page.

With ``git``, you can also clone a stable release by specifying its branch or tag
after the ``--branch`` (or just ``-b``) argument.

After downloading the Rebel Engine source code,
you can :doc:`continue to compiling Rebel Engine </development/compiling/introduction_to_the_buildsystem>`.
