# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
# Custom article design
from pathlib import Path

_article_static = Path(__file__).resolve().parent / "_static"
_article_static.mkdir(parents=True, exist_ok=True)

_article_css = """
/* Article area */
div.body,
.rst-content,
.bd-article {
    color: #334155;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 17px;
    line-height: 1.85;
    overflow-wrap: break-word;
}

div.body,
.wy-nav-content {
    background: #ffffff;
}

/* Main title */
:is(div.body, .rst-content, .bd-article) h1 {
    margin: 0 0 28px;
    padding: 0 0 22px;
    border-bottom: 3px solid #167d8d;
    color: #143544;
    font-family: Arial, Helvetica, sans-serif;
    font-size: clamp(29px, 4vw, 42px);
    font-weight: 700;
    line-height: 1.25;
    letter-spacing: -0.5px;
}

/* Section headings */
:is(div.body, .rst-content, .bd-article) h2 {
    margin: 40px 0 20px;
    padding: 14px 18px;
    border-left: 4px solid #167d8d;
    border-radius: 0 8px 8px 0;
    background: #edf7f8;
    color: #143544;
    font-family: Arial, Helvetica, sans-serif;
    font-size: clamp(23px, 3vw, 28px);
    font-weight: 700;
    line-height: 1.4;
}

/* Subheadings and FAQ questions */
:is(div.body, .rst-content, .bd-article) h3 {
    margin: 28px 0 12px;
    color: #175568;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 21px;
    font-weight: 700;
    line-height: 1.5;
}

:is(div.body, .rst-content, .bd-article) h4 {
    margin: 24px 0 12px;
    color: #175568;
    font-size: 19px;
    line-height: 1.5;
}

/* Paragraphs */
:is(div.body, .rst-content, .bd-article) p {
    margin: 0 0 20px;
    font-size: inherit;
    line-height: 1.85;
}

/* Opening paragraph */
:is(div.body, .rst-content, .bd-article) h1 + p {
    color: #405b6b;
    font-size: 1.08em;
}

/* Lists */
:is(div.body, .rst-content, .bd-article) ul,
:is(div.body, .rst-content, .bd-article) ol {
    margin: 18px 0 26px;
    padding-left: 26px;
}

:is(div.body, .rst-content, .bd-article) li {
    margin-bottom: 10px;
    line-height: 1.8;
}

:is(div.body, .rst-content, .bd-article) li > p {
    margin-bottom: 8px;
}

:is(div.body, .rst-content, .bd-article) li::marker {
    color: #167d8d;
}

/* Links */
:is(div.body, .rst-content, .bd-article) a {
    color: #126c7b;
    text-underline-offset: 3px;
}

:is(div.body, .rst-content, .bd-article) a:hover {
    color: #104453;
}

:is(div.body, .rst-content, .bd-article) a:focus-visible {
    outline: 3px solid #167d8d;
    outline-offset: 4px;
}

/* Heading anchor */
:is(div.body, .rst-content, .bd-article) a.headerlink {
    font-size: 0.7em;
    text-decoration: none;
}

/* Images */
:is(div.body, .rst-content, .bd-article) img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
}

/* Code blocks */
:is(div.body, .rst-content, .bd-article) pre {
    max-width: 100%;
    padding: 18px;
    overflow-x: auto;
    border: 1px solid #dce7eb;
    border-radius: 8px;
    background: #f5f8fa;
    line-height: 1.6;
}

/* Notes */
:is(div.body, .rst-content, .bd-article) .admonition {
    margin: 24px 0;
    padding: 18px 20px;
    border: 1px solid #dce7eb;
    border-left: 4px solid #167d8d;
    border-radius: 8px;
    background: #f3fafb;
}

/* Comfortable heading navigation */
:is(div.body, .rst-content, .bd-article) section {
    scroll-margin-top: 28px;
}

/* Mobile */
@media (max-width: 767px) {
    div.body,
    .rst-content,
    .bd-article {
        font-size: 16px;
    }

    .wy-nav-content {
        padding: 24px 18px;
    }

    :is(div.body, .rst-content, .bd-article) h1 {
        margin-bottom: 22px;
        padding-bottom: 18px;
    }

    :is(div.body, .rst-content, .bd-article) h2 {
        margin-top: 30px;
        padding: 12px 14px;
    }

    :is(div.body, .rst-content, .bd-article) h3 {
        font-size: 20px;
    }

    :is(div.body, .rst-content, .bd-article) p {
        line-height: 1.75;
    }
}
"""

(_article_static / "custom.css").write_text(
    _article_css,
    encoding="utf-8",
)

# Preserve existing static files and stylesheets
html_static_path = list(globals().get("html_static_path", []))
if "_static" not in html_static_path:
    html_static_path.append("_static")

html_css_files = list(globals().get("html_css_files", []))
if not any(
    (entry[0] if isinstance(entry, (tuple, list)) else entry)
    == "custom.css"
    for entry in html_css_files
):
    html_css_files.append("custom.css")
