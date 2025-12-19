# Добавьте путь к вашему коду
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# Расширения
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
]

# Настройки автодокументации
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Настройки для Google стиля документации
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True

# Язык
language = 'ru'  # или 'en'

# Тема
html_theme = 'sphinx_rtd_theme'  # или 'alabaster', 'nature'