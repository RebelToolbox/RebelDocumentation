# Sphinx build configuration file for Rebel Documentation.
#
# Contents
# 1. Project information
# 2. General configuration
# 3. Options for internationalization
# 4. Options for HTML output
# 5. Options for HTML help output
# 6. Options for the linkcheck builder
# 7. Options for Docutils
#   7.1 restructuredText Directives
# 8. Extensions
#   8.1 Sphinx tabs extension
#   8.2 Sphinx not found page extension
#   8.3 Sphinx opengraph extension

import sphinx_rtd_theme
import sys
import os


# 1. Project information
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Rebel Documentation"
author = "Rebel Documentation Contributors"
copyright = "2023, Rebel Documentation Contributors"
version = os.getenv("READTHEDOCS_VERSION", "1.0")
release = version


# 2. General configuration
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# https://www.sphinx-doc.org/en/master/usage/extensions/
sys.path.append("_extensions")
extensions = [
    "gdscript",
    "sphinx_rtd_theme",
    "sphinx_tabs.tabs",
    "notfound.extension",
    "sphinxext.opengraph",
]

exclude_patterns = [
    "_build",
    "env",
]

templates_path = [
    "_templates",
]

smartquotes = False

from gdscript import GDScriptLexer
from sphinx.highlighting import lexers

lexers["gdscript"] = GDScriptLexer()
highlight_language = "gdscript"


# 3. Options for internationalization
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

# TODO Rebel internationalisation needs to configured.
# https://www.sphinx-doc.org/en/master/usage/advanced/intl.html
# https://readthedocs-lst.readthedocs.io/en/latest/i18n.html
# https://readthedocs-lst.readthedocs.io/en/latest/localization.html

language = os.getenv("READTHEDOCS_LANGUAGE", "en")

supported_languages = {
    "en": "Rebel Toolbox (%s) documentation in English",
}
if language not in supported_languages.keys():
    print("Unknown language: " + language)
    print("Supported languages: " + ", ".join(supported_languages.keys()))
    print(
        "The configured language is either wrong,"
        + " or it should be added to supported_languages in conf.py."
        + " Falling back to 'en'."
    )
    language = "en"


# 4. Options for HTML output
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    "collapse_navigation": False,
    "logo_only": True,
}

html_theme_path = [
    sphinx_rtd_theme.get_html_theme_path(),
]

html_title = supported_languages[language] % version

html_context = {
    # https://readthedocs-lst.readthedocs.io/en/latest/vcs.html
    # Manually set Read the Docs variables for local builds.
    "github_user": "RebelToolbox",  # GitHub username.
    "github_repo": "RebelDocumentation",  # Github repo name.
    "github_version": "main",  # Version.
    "conf_py_path": "/",  # Path in the checkout to the docs root.
    "display_github": True,
    # Define variables used in _templates/layout.html.
    "inject_language_links": True,
    "docs_supported_languages": list(supported_languages.keys()),
    "docs_basepath": "https://docs.rebeltoolbox.com/",
    "docs_suffix": ".html",
    "default_lang": "en",
    "canonical_version": "stable",
    "title_prefix": "",
}

html_logo = "img/rebel-logo.png"

html_css_files = [
    "css/custom.css",
]

html_js_files = [
    "js/custom.js",
]

html_static_path = [
    "_static",
]


# 5. Options for HTML help output
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-help-output

htmlhelp_basename = "RebelDocumentation"


# 6. Options for the linkcheck builder
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

linkcheck_anchors = False
linkcheck_timeout = 10


# 7. Options for Docutils
# https://www.docutils.org/docs/user/config.html

# 7.1 restructuredText Directives
# https://www.docutils.org/docs/ref/rst/directives.html

# To avoid potential security holes in the csv-table, include and
# raw directives file_insertion and raw are disabled.
file_insertion_enabled = False
raw_enabled = False

# 8. Extensions

# 8.1 Sphinx tabs extension
# https://sphinx-tabs.readthedocs.io
# Required by Read the Docs

sphinx_tabs_nowarn = True


# 8.2 Sphinx not found extension
# https://sphinx-notfound-page.readthedocs.io

notfound_context = {
    "title": "Page not found",
    "body": """
        <h1>Page not found</h1>
        <p>
            Sorry, we couldn't find that page. It may have been renamed or
            removed in the version of the documentation you're currently
            browsing.
        </p>
        <p>
            If you're currently browsing the <em>stable</em> version of the
            documentation, try browsing the
            <a href="/en/latest/"><em>latest</em> version of the
            documentation</a>.
        </p>
        <p>
            Alternatively, use the <a href="#"
            onclick="$('#rtd-search-form [name=\\'q\\']').focus()">Search
            docs</a> box on the left or <a href="/">go to the homepage</a>.
        </p>
    """,
}

# 8.3 Sphinx opengraph extension
# https://github.com/wpilibsuite/sphinxext-opengraph

ogp_site_name = "Rebel Toolbox Documentation"
