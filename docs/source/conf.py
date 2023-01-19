# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from errno import ENOENT

import sphinx.util.osutil

sphinx.util.osutil.ENOENT = ENOENT

sys.path.insert(0, os.path.abspath('../../source'))


# -- Project information -----------------------------------------------------

project = 'dialogflow-fulfillment'
copyright = '2020, Gabriel Farias Caccáos'
author = 'Gabriel Farias Caccáos'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxcontrib.mermaid',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []


# -- Other settings ----------------------------------------------------------

add_module_names = False

autodoc_typehints = 'description'
autodoc_default_options = {
    'show-inheritance': True,
    'members': None,
    'inherited-members': True,
    'undoc-members': True,
}

master_doc = 'index'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

nitpicky = True
nitpick_ignore = [
    ('py:class', 'any'),
    ('py:class', 'callable'),
    ('py:class', 'optional'),
]
