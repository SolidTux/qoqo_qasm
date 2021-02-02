#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# qoqo documentation build configuration file
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('../'))

# set __version__
try:
    with open('../qoqo_qasm/__version__.py') as f:
        lines = f.readlines()
    version = lines[-1].strip().split("'")[1].strip()
except Exception:
    version = '0.0.0'
versions = version.split(".")
main_version = "{}.{}".format(versions[0], versions[1])
# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              'sphinx.ext.autosummary',
              'nbsphinx', ]
# automatically use sphinx-autogen
autosummary_generate = True
autosummary_imported_members = True
# define mock imports for packages that are difficult to handle / install
alist = []
alist.extend(['hqsbase', 'calculatorqore'])
autodoc_mock_imports = alist

# 'both': class and __init__ docstring are concatenated and inserted
# 'class': only class docstring inserted
# 'init': only init docstring inserted
autoclass_content = 'both'
# This value is a list of autodoc directive flags that should be automatically applied to
# all autodoc directives. The supported flags are 'members', 'undoc-members',
# 'private-members', 'special-members', 'inherited-members', 'show-inheritance',
# 'ignore-module-all' and 'exclude-members'.
autodoc_default_flags = ['members', 'private-members', 'special-members']
# The default options for autodoc directives. They are applied to all autodoc directives
# automatically. It must be a dictionary which maps option names to the values.
autodoc_default_options = {
    'members': True,
    'special-members': True,
    'imported-members': False,
    'private-members': True,
    'inherited-members': False,
    #    'member-order': 'bysource',
    #    'special-members': '__init__',
    #    'undoc-members': False,
    #    'exclude-members': '__weakref__'
}
# This value controls the docstrings inheritance. If set to True the docstring for classes
# or methods, if not explicitly set, is inherited form parents.
autodoc_inherit_docstrings = True
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'qoqo_qasm'
copyright = '2019-2021, HQS Quantum Simulations GmbH'
author = 'The qoqo developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = main_version
# The full version, including alpha/beta/rc tags.
release = version

# The language for content is autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'English'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = "bizstyle"
html_theme = "sphinx_rtd_theme"
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#    '**': [
#        'about.html',
#        'navigation.html',
#        'relations.html',  # needs 'show_related': True theme option to display
#        'searchbox.html',
#        'donate.html',
#    ]
# }


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'qoqoqasmdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'qoqoqasm.tex', 'qoqo qasm Documentation',
     'Kirsten Bark, Jan Reiner, Nicolas Vogt, Sebastian Zanker', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'qoqo_qasm', 'qoqo qasm Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'qoqo_qasm', 'qoqo qasm Documentation',
     author, 'qoqo_qasm', 'One line description of project.',
     'Miscellaneous'),
]

# Turning off executing notebooks when adding them to Documentation
nbsphinx_execute = 'never'
