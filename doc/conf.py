#-----------------------------------------------------------------------------
#
# Sphinx configuration for StateTip project
#
#-----------------------------------------------------------------------------

project = u'StateTip'
#copyright = u'...'

release = '0.0.0'
version = '0.0'

#-----------------------------------------------------------------------------

# minimal Sphinx version
#needs_sphinx = '1.0'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo']

master_doc = 'index'
source_suffix = '.rst'
exclude_trees = ['html', 'man']

#-----------------------------------------------------------------------------
# configuration specific to Python code
#-----------------------------------------------------------------------------

# ignored prefixes for module index sorting
#modindex_common_prefix = []

#-----------------------------------------------------------------------------
# HTML output
#-----------------------------------------------------------------------------

import sphinx
def ver(v):
    return [int(i) for i in v.split('.')]

if ver(sphinx.__version__) >= ver('1.3'):
    html_theme = 'classic'
else:
    html_theme = 'default'

pygments_style = 'sphinx'

#html_static_path = ['static']

#-----------------------------------------------------------------------------
# TROFF/man output
#-----------------------------------------------------------------------------

man_pages = [
    ('manpages/statetip', 'statetip', u'StateTip Client',
     [], 1),
    ('manpages/statetipd', 'statetipd', u'StateTip Daemon',
     [], 1),
]

#man_show_urls = False

#-----------------------------------------------------------------------------
# vim:ft=python