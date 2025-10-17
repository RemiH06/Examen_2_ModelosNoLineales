# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Examen2'
copyright = '2024, Tu Equipo'
author = 'Equipo de Predicción'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'myst_parser',  # ← IMPORTANTE
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The suffix(es) of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# HTML title
html_title = 'Predicción NVDA'
html_short_title = 'NVDA Prediction'

# Logo (optional - add your logo to _static/)
# html_logo = '_static/logo.png'

# Favicon (optional)
# html_favicon = '_static/favicon.ico'

# Language
language = 'es'