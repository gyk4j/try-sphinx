# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Try Sphinx'
copyright = '2024, gyk4j'
author = 'gyk4j'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.jquery',
    'sphinx_rtd_theme',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
#    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
#    'analytics_anonymize_ip': False,
    'display_version': True,
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': 'blob',
    'style_nav_header_background': '#2980B9',
    'flyout_display': 'attached',
    'version_selector': True,
    'language_selector': True,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'github_url': 'https://github.com/gyk4j/try-sphinx/edit/main/'
}

# For classic theme
#html_theme_options = {
#    "rightsidebar" : False,
#    "stickysidebar" : False,
#    "collapsiblesidebar" : False,
#    "externalrefs" : False,
#    "footerbgcolor" : "#000000",
#    "footertextcolor" : "#000000",
#    "sidebarbgcolor" : "#000000",
#    "sidebarbtncolor" : "#000000",
#    "sidebartextcolor" : "#000000",
#    "sidebarlinkcolor" : "#000000",
#    "relbarbgcolor" : "#000000",
#    "relbartextcolor" : "#000000",
#    "relbarlinkcolor" : "#000000",
#    "bgcolor" : "#000000",
#    "textcolor" : "#000000",
#    "linkcolor" : "#000000",
#    "visitedlinkcolor" : "#000000",
#    "headbgcolor" : "#000000",
#    "headtextcolor" : "#000000",
#    "headlinkcolor" : "#000000",
#    "codebgcolor" : "#000000",
#    "codetextcolor" : "#000000",
#    "bodyfont" : "#000000",
#    "headfont" : "#000000",
#}

html_static_path = [
    '_static',
    '_images',
    '_downloads',
]

html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.svg"

latex_engine = 'pdflatex'
latex_elements = {
    "papersize": "a4paper",
#    "sphinxsetup": "iconpackage=fontawesome5",
}
latex_show_urls = 'footnote'
