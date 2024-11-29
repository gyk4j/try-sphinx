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

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_theme_options = {
    "rightsidebar" : False,
    "stickysidebar" : False,
    "collapsiblesidebar" : False,
    "externalrefs" : False,
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
}
html_static_path = ['_static']
