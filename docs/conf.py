# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '公路桥涵养护规范<br /><br />JTG 5120－2021'
copyright = '' 

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

language ='zh'

templates_path = ['_templates']
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]
html_style = 'css/custom.css'
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_theme = "sphinxawesome_theme"

# html_theme = 'sphinx_book_theme'

html_title = "公路桥涵养护规范  JTG 5120－2021"
# html_logo = "_static/logo.png"
html_favicon = "_static/logo.png"


extensions = ['recommonmark']
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst','.md']