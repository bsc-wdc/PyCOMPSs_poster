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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Parallel programming with PyCOMPSs'
copyright = '2020 Barcelona Supercomputing Center (BSC)'
author = 'Rosa M Badia'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.imgmath',
              'sphinx.ext.ifconfig',
              # 'sphinx.ext.imgconverter',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.mathjax',
              'sphinxcontrib.contentui',
              'nbsphinx',
              # 'sphinxcontrib.rsvgconverter',
              'sphinxcontrib.bibtex',
              'sphinx_gallery.load_style',
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default' # 'sphinx'

# True to prefix each section label with the name of the document it is in,
# followed by a colon.
autosectionlabel_prefix_document = True

# Specific configuration
numfig = True
numfig_secnum_depth = 0
numfig_format = {'figure':'Figure %s',
                 'table':'Table %s',
                 'code-block':'Code %s',
                 'section':'Section %s'}
html_add_permalinks = ""  # Disabled permalinks
#html_logo = './_static/COMPSs_logo.png'
html_logo = './_static/logo_pycompss_scipy.png'
html_show_sourcelink = False
html_show_copyright = False
html_show_sphinx = True
nitpicky = True

# Disable notebooks Building
nbsphinx_execute = 'never'
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]
# Do not allow building if execution is enabled and a notebook fails
nbsphinx_allow_errors = True

# Notebook thumbnails
nbsphinx_thumbnails = {
    'Notebooks/wordcount': '_static/wordcount.png',
    'Notebooks/kmeans': '_static/kmeans.png',
    'Notebooks/dislib': '_static/dislib.png',
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# More themes: https://www.sphinx-doc.org/es/stable/theming.html

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {'show_related': True,
                     }

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}
