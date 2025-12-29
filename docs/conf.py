# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'celbridge-docs'
#copyright = '2025, Celbridge.org'
copyright = (
    "2025-present - Celbridge community (CC BY 4.0)"
)
author = 'Celbridge team'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx_new_tab_link",
    "sphinx_copybutton",
    "myst_parser",
]

#     "notfound.extension",


myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
    "substitution"
]


myst_heading_anchors = 3

# open extenal links in NEW TAB
new_tab_link_show_external_link_icon = True

templates_path = ['_templates']
exclude_patterns = []

# You can specify multiple suffix as a list of string: ['.rst', '.md']
source_suffix = ".rst"
source_encoding = "utf-8-sig"

# The master toctree document
master_doc = "index"


from sphinx.highlighting import lexers
pygments_style = "sphinx"

html_theme_options = {
    # if we have a html_logo below, this shows /only/ the logo with no title text
    "logo_only": True,
    # Collapse navigation (False makes it tree-like)
    "collapse_navigation": False,
    # Remove version and language picker beneath the title
    "version_selector": False,
    "language_selector": False,
    # Set Flyout menu to attached
    "flyout_display": "attached",
}

html_logo = "images/icon2.svg"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (e.g. https://...)
html_css_files = [
    "css/custom.css",
]


html_js_files = [
    "js/custom.js",
    ('https://plausible.godot.foundation/js/script.file-downloads.outbound-links.js',
     {'defer': 'defer', 'data-domain': 'godotengine.org'}),
]

