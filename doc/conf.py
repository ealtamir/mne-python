# -*- coding: utf-8 -*-
#
# MNE documentation build configuration file, created by
# sphinx-quickstart on Fri Jun 11 10:45:48 2010.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import date
from distutils.version import LooseVersion
import os
import os.path as op
import sys
import warnings

import sphinx_gallery
from sphinx_gallery.sorting import FileNameSortKey, ExplicitOrder
from numpydoc import docscrape
import mne
from mne.utils import linkcode_resolve  # noqa, analysis:ignore

if LooseVersion(sphinx_gallery.__version__) < LooseVersion('0.2'):
    raise ImportError('Must have at least version 0.2 of sphinx-gallery, got '
                      '%s' % (sphinx_gallery.__version__,))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
curdir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(curdir, '..', 'mne')))
sys.path.append(os.path.abspath(os.path.join(curdir, 'sphinxext')))

if not os.path.isdir('_images'):
    os.mkdir('_images')

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.5'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.linkcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx_gallery.gen_gallery',
    'sphinx_fontawesome',
    'numpydoc',
    'gen_commands',
    'sphinx_bootstrap_theme',
]

linkcheck_ignore = [
    'https://doi.org/10.1088/0031-9155/57/7/1937',  # 403 Client Error: Forbidden for url: http://iopscience.iop.org/article/10.1088/0031-9155/57/7/1937/meta
    'https://sccn.ucsd.edu/wiki/.*',  # HTTPSConnectionPool(host='sccn.ucsd.edu', port=443): Max retries exceeded with url: /wiki/Firfilt_FAQ (Caused by SSLError(SSLError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847)'),))
    'https://docs.python.org/dev/howto/logging.html',  # ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
    'https://docs.python.org/3/library/.*',  # ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
    'https://hal.archives-ouvertes.fr/hal-01848442/',  # Sometimes: 503 Server Error: Service Unavailable for url: https://hal.archives-ouvertes.fr/hal-01848442/
]
linkcheck_anchors = False  # saves a bit of time

autosummary_generate = True
autodoc_default_options = {'inherited-members': None}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'MNE'
td = date.today()
copyright = u'2012-%s, MNE Developers. Last updated on %s' % (td.year,
                                                              td.isoformat())

nitpicky = True
suppress_warnings = ['image.nonlocal_uri']  # we intentionally link outside

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = mne.__version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "autolink"

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['mne.']

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'navbar_title': ' ',  # we replace this with an image
    'source_link_position': "nav",  # default
    'bootswatch_theme': "flatly",  # yeti paper lumen
    'navbar_sidebarrel': False,  # Render the next/prev links in navbar?
    'navbar_pagenav': False,
    'navbar_class': "navbar",
    'bootstrap_version': "3",  # default
    'navbar_links': [
        ("Install", "getting_started"),
        ("Documentation", "documentation"),
        ("API", "python_reference"),
        ("Glossary", "glossary"),
        ("Examples", "auto_examples/index"),
        ("Contribute", "contributing"),
    ],
    }

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/mne_logo_small.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', '_images']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
html_copy_source = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# variables to pass to HTML templating engine
build_dev_html = bool(int(os.environ.get('BUILD_DEV_HTML', False)))

html_context = {'use_google_analytics': True, 'use_twitter': True,
                'use_media_buttons': True, 'build_dev_html': build_dev_html}

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'mne-doc'


# -- Options for LaTeX output ---------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
#    ('index', 'MNE.tex', u'MNE Manual',
#     u'MNE Contributors', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/logo.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_toplevel_sectioning = 'part'

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True

trim_doctests_flags = True

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://www.numpy.org/devdocs', None),
    'scipy': ('https://scipy.github.io/devdocs', None),
    'matplotlib': ('https://matplotlib.org', None),
    'sklearn': ('https://scikit-learn.org/stable', None),
    'joblib': ('https://joblib.readthedocs.io/en/latest', None),
    'mayavi': ('http://docs.enthought.com/mayavi/mayavi', None),
    'nibabel': ('https://nipy.org/nibabel', None),
    'nilearn': ('http://nilearn.github.io', None),
    'surfer': ('https://pysurfer.github.io/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
    'statsmodels': ('http://www.statsmodels.org/stable/', None),
    'dipy': ('http://nipy.org/dipy', None),
}

##############################################################################
# sphinx-gallery

examples_dirs = ['../examples', '../tutorials']
gallery_dirs = ['auto_examples', 'auto_tutorials']

try:
    mlab = mne.utils._import_mlab()
    # Do not pop up any mayavi windows while running the
    # examples. These are very annoying since they steal the focus.
    mlab.options.offscreen = True
    scrapers = ('matplotlib', 'mayavi')
except Exception:
    scrapers = ('matplotlib',)
else:
    # Let's do the same thing we do in tests: reraise traits exceptions
    from traits.api import push_exception_handler
    push_exception_handler(reraise_exceptions=True)


class Resetter(object):
    """Simple class to make the str(obj) static for Sphinx build env hash."""

    def __repr__(self):
        return '<%s>' % (self.__class__.__name__,)

    def __call__(self, gallery_conf, fname):
        reset_warnings(gallery_conf, fname)


def reset_warnings(gallery_conf, fname):
    """Ensure we are future compatible and ignore silly warnings."""
    # In principle, our examples should produce no warnings.
    # Here we cause warnings to become errors, with a few exceptions.
    # This list should be considered alongside
    # setup.cfg -> [tool:pytest] -> filterwarnings

    # remove tweaks from other module imports or example runs
    warnings.resetwarnings()
    # restrict
    warnings.filterwarnings('error')
    # allow these, but show them
    warnings.filterwarnings('always', '.*cannot make axes width small.*')
    warnings.filterwarnings('always', '.*Axes that are not compatible.*')
    warnings.filterwarnings('always', '.*FastICA did not converge.*')
    warnings.filterwarnings(  # xhemi morph (should probably update sample)
        'always', '.*does not exist, creating it and saving it.*')
    warnings.filterwarnings('default', module='sphinx')  # internal warnings
    warnings.filterwarnings(
        'always', '.*converting a masked element to nan.*')  # matplotlib?
    # allow these warnings, but don't show them
    warnings.filterwarnings(
        'ignore', '.*OpenSSL\\.rand is deprecated.*')
    warnings.filterwarnings('ignore', '.*is currently using agg.*')
    warnings.filterwarnings(  # SciPy-related warning (maybe 1.2.0 will fix it)
        'ignore', '.*the matrix subclass is not the recommended.*')
    warnings.filterwarnings(  # some joblib warning
        'ignore', '.*semaphore_tracker: process died unexpectedly.*')
    warnings.filterwarnings(  # needed until SciPy 1.2.0 is released
        'ignore', '.*will be interpreted as an array index.*', module='scipy')
    for key in ('HasTraits', r'numpy\.testing', 'importlib', r'np\.loads',
                'Using or importing the ABCs from',  # internal modules on 3.7
                r"it will be an error for 'np\.bool_'",  # ndimage
                "'U' mode is deprecated",  # sphinx io
                r"joblib is deprecated in 0\.21",  # nilearn
                ):
        warnings.filterwarnings(  # deal with other modules having bad imports
            'ignore', message=".*%s.*" % key, category=DeprecationWarning)
    warnings.filterwarnings(  # deal with bootstrap-theme bug
        'ignore', message=".*modify script_files in the theme.*",
        category=Warning)
    warnings.filterwarnings(  # deal with other modules having bad imports
        'ignore', message=".*ufunc size changed.*", category=RuntimeWarning)
    warnings.filterwarnings(  # realtime
        'ignore', message=".*unclosed file.*", category=ResourceWarning)
    warnings.filterwarnings('ignore', message='Exception ignored in.*')
    # allow this ImportWarning, but don't show it
    warnings.filterwarnings(
        'ignore', message="can't resolve package from", category=ImportWarning)


reset_warnings(None, None)
sphinx_gallery_conf = {
    'doc_module': ('mne',),
    'reference_url': dict(mne=None),
    'examples_dirs': examples_dirs,
    'subsection_order': ExplicitOrder(['../examples/io/',
                                       '../examples/simulation/',
                                       '../examples/preprocessing/',
                                       '../examples/visualization/',
                                       '../examples/time_frequency/',
                                       '../examples/stats/',
                                       '../examples/decoding/',
                                       '../examples/connectivity/',
                                       '../examples/forward/',
                                       '../examples/inverse/',
                                       '../examples/realtime/',
                                       '../examples/datasets/',
                                       '../tutorials/intro/',
                                       '../tutorials/raw/',
                                       '../tutorials/preprocessing/',
                                       '../tutorials/epochs/',
                                       '../tutorials/evoked/',
                                       '../tutorials/time-freq/',
                                       '../tutorials/source-modeling/',
                                       '../tutorials/stats-sensor-space/',
                                       '../tutorials/stats-source-space/',
                                       '../tutorials/machine-learning/',
                                       '../tutorials/simulation/',
                                       '../tutorials/sample-datasets/',
                                       '../tutorials/discussions/',
                                       '../tutorials/misc/']),
    'gallery_dirs': gallery_dirs,
    'default_thumb_file': os.path.join('_static', 'mne_helmet.png'),
    'backreferences_dir': 'generated',
    'plot_gallery': 'True',  # Avoid annoying Unicode/bool default warning
    'download_section_examples': False,
    'thumbnail_size': (160, 112),
    'min_reported_time': 1.,
    'abort_on_example_error': False,
    'reset_modules': ('matplotlib', Resetter()),  # called w/each script
    'image_scrapers': scrapers,
    'show_memory': True,
    'line_numbers': False,  # XXX currently (0.3.dev0) messes with style
    'within_subsection_order': FileNameSortKey,
    'junit': op.join('..', 'test-results', 'sphinx-gallery', 'junit.xml'),
}

##############################################################################
# numpydoc

# XXX This hack defines what extra methods numpydoc will document
docscrape.ClassDoc.extra_public_methods = mne.utils._doc_special_members
numpydoc_class_members_toctree = False
numpydoc_attributes_as_param_list = False
numpydoc_xref_param_type = True
numpydoc_xref_aliases = {
    'Popen': 'python:subprocess.Popen',
    # Matplotlib
    'colormap': ':doc:`colormap <matplotlib:tutorials/colors/colormaps>`',
    'color': ':doc:`color <matplotlib:api/colors_api>`',
    'collection': ':doc:`collections <matplotlib:api/collections_api>`',
    'Axes': 'matplotlib.axes.Axes',
    'Figure': 'matplotlib.figure.Figure',
    'Axes3D': 'mpl_toolkits.mplot3d.axes3d.Axes3D',
    # Mayavi
    'mayavi.mlab.Figure': 'mayavi.core.api.Scene',
    'mlab.Figure': 'mayavi.core.api.Scene',
    # sklearn
    'LeaveOneOut': 'sklearn.model_selection.LeaveOneOut',
    # joblib
    'joblib.Parallel': 'joblib.Parallel',
    # nibabel
    'Nifti1Image': 'nibabel.nifti1.Nifti1Image',
    'Nifti2Image': 'nibabel.nifti2.Nifti2Image',
    # MNE
    'Label': 'mne.Label', 'Forward': 'mne.Forward', 'Evoked': 'mne.Evoked',
    'Info': 'mne.Info', 'SourceSpaces': 'mne.SourceSpaces',
    'Epochs': 'mne.Epochs', 'Layout': 'mne.channels.Layout',
    'EvokedArray': 'mne.EvokedArray', 'BiHemiLabel': 'mne.BiHemiLabel',
    'AverageTFR': 'mne.time_frequency.AverageTFR',
    'EpochsTFR': 'mne.time_frequency.EpochsTFR',
    'Raw': 'mne.io.Raw', 'ICA': 'mne.preprocessing.ICA',
    'Covariance': 'mne.Covariance', 'Annotations': 'mne.Annotations',
    'Montage': 'mne.channels.Montage',
    'DigMontage': 'mne.channels.DigMontage',
    'VectorSourceEstimate': 'mne.VectorSourceEstimate',
    'VolSourceEstimate': 'mne.VolSourceEstimate',
    'VolVectorSourceEstimate': 'mne.VolVectorSourceEstimate',
    'MixedSourceEstimate': 'mne.MixedSourceEstimate',
    'SourceEstimate': 'mne.SourceEstimate', 'Projection': 'mne.Projection',
    'ConductorModel': 'mne.bem.ConductorModel',
    'Dipole': 'mne.Dipole', 'DipoleFixed': 'mne.DipoleFixed',
    'InverseOperator': 'mne.minimum_norm.InverseOperator',
    'CrossSpectralDensity': 'mne.time_frequency.CrossSpectralDensity',
    'RtEpochs': 'mne.realtime.RtEpochs',
    'SourceMorph': 'mne.SourceMorph',
    'Xdawn': 'mne.preprocessing.Xdawn',
    'Report': 'mne.Report', 'Forward': 'mne.Forward',
    'TimeDelayingRidge': 'mne.decoding.TimeDelayingRidge',
    'Vectorizer': 'mne.decoding.Vectorizer',
    'UnsupervisedSpatialFilter': 'mne.decoding.UnsupervisedSpatialFilter',
    'TemporalFilter': 'mne.decoding.TemporalFilter',
    'Scaler': 'mne.decoding.Scaler', 'SPoC': 'mne.decoding.SPoC',
    'PSDEstimator': 'mne.decoding.PSDEstimator',
    'LinearModel': 'mne.decoding.LinearModel',
    'FilterEstimator': 'mne.decoding.FilterEstimator',
    'EMS': 'mne.decoding.EMS', 'CSP': 'mne.decoding.CSP',
    'Beamformer': 'mne.beamformer.Beamformer',
}
numpydoc_xref_ignore = {
    # words
    'instance', 'instances', 'of', 'default', 'shape', 'or',
    'with', 'length', 'pair', 'matplotlib', 'optional', 'kwargs', 'in',
    'dtype', 'object', 'self.verbose',
    # shapes
    'n_vertices', 'n_faces', 'n_channels', 'm', 'n', 'n_events', 'n_colors',
    'n_times', 'obj', 'n_chan', 'n_epochs', 'n_picks', 'n_ch_groups',
    'n_dipoles', 'n_ica_components', 'n_pos', 'n_node_names', 'n_tapers',
    'n_signals', 'n_step', 'n_freqs', 'wsize', 'Tx', 'M', 'N', 'p', 'q',
    'n_observations', 'n_regressors', 'n_cols', 'n_frequencies', 'n_tests',
    'n_samples', 'n_permutations', 'nchan', 'n_points', 'n_features',
    'n_parts', 'n_features_new', 'n_components', 'n_labels', 'n_events_in',
    'n_splits', 'n_scores', 'n_outputs', 'n_trials', 'n_estimators', 'n_tasks',
    'nd_features', 'n_classes', 'n_targets', 'n_slices', 'n_hpi', 'n_fids',
    'n_elp', 'n_pts', 'n_tris', 'n_nodes', 'n_nonzero', 'n_events_out',
    # Undocumented (on purpose)
    'RawKIT', 'RawEximia', 'RawEGI', 'RawEEGLAB', 'RawEDF', 'RawCTF', 'RawBTi',
    'RawBrainVision',
    # sklearn subclasses
    'mapping', 'to', 'any',
    # unlinkable
    'mayavi.mlab.pipeline.surface',
}
