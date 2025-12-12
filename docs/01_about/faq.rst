:allow_comments: False

.. meta::
    :keywords: FAQ

.. _doc_faq:

Frequently asked questions
==========================

What can I do with Celbridge? How much does it cost? What are the license terms?
--------------------------------------------------------------------------------

Celbridge is `Free and open source Software <https://en.wikipedia.org/wiki/Free_and_open_source_software>`_
available under the `OSI-approved <https://opensource.org/licenses/MIT>`_ MIT license. This means it is
free as in "free speech" as well as in "free beer."

In short:

* You are free to download and use Celbridge for any purpose: personal, non-profit, commercial, or otherwise.
* You are free to modify, distribute, redistribute, and remix Celbridge to your heart's content, for any reason,
  both non-commercially and commercially.

All the contents of this accompanying documentation are published under the permissive Creative Commons
Attribution 4.0 International (`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`_) license, with attribution
to "the Celbridge community."

Logos and icons are generally under the same Creative Commons license.

For full details, look at the `LICENSE.txt <https://github.com/celbridge-org/celbridge/blob/main/LICENSE.txt>`_
in the Celbridge repository.

Which platforms are supported by Celbridge?
-------------------------------------------

* Windows

(MacOS and Linux versions coming soon we hope...)


Which standard file formats are supported by Celbridge?
-------------------------------------------------------

Your Celbridge projects can contain any file tyles.

However, Celbridge offers additional functionality for the following file types:


.. sidebar:: Additional editor features planned

    We are planning to integrate Monaco more tightly into Celbridge, particularly using `Language Server Protocol <https://coderivers.org/blog/python-language-server/>`_ to support code completion, syntax checking and type hinting, and also to expose the most common text editor features via a toolbar or other UI.

- **.py**
    The Celbridge editor supports Python code editing.

    The text editor in Celbridge is powered by the open source `Monaco Editor <https://microsoft.github.io/monaco-editor/>`_, which is the same text editor used in `Visual Studio Code <https://code.visualstudio.com/>`_. Monaco is a Javascript library that we run in a locally hosted web page displayed in a WebView2. All communication between Monaco Editor and the main Celbridge application is performed via the Web Message API.

    Out of the box, Monaco supports basic IntelliSense, Validation and Syntax Colorization for a wide range of text formats (e.g. `JSON <https://en.wikipedia.org/wiki/JSON>`_, Python, Markdown). It supports typical text editor features such as find and replace, cut, copy and paste and a wide range of coding-specific features, such as multi-cursors, that can be accessed via the Command Palette (accessed via the context menu or pressing F1).

- **.txt**
    - yes, the Celbridge editor can handle plain text files :-)

- **.md**
    - Celbridge offers a second, rendering panel, so you can see how your Markdown looks when parsed and rendered

    - **.rst** `ReStructured Text <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ rending coming soon!

- **.xlsx**
    - Celbridge opens a `SpreadJS <https://developer.mescius.com/spreadjs>`_ (thanks Mescius!) WYSIWYG editor, allowing you a natural visual editing experience when working with spreadsheet files
    - formulas, charts, pivot tables etc. are all supported
    - addionally, you can specify a Python script to be executed each time a cell has been updated

- **.celbridge**
    - these files are the project configuration files - they're text files that you can edit, for example to change the Python version or add packages the project requires


- **.webapp**
    - Celbridge includes a web viewer, so you can create a `.webapp` file, and then enter the URL of the web page to be rendered in the web viewer panel - this is a fully interactive web view just like in a browser


What were the motivations behind creating Celbridge?
----------------------------------------------------

Celbridge grew from a need for an easy-to-use workbench tool, to connect creators with data in spreadsheets with 3rd-party applications (such as the `Unreal <https://www.unrealengine.com/en-US>`_ game engine).  What started as an in-house tool for an Irish games company is now an active open-source software project, offering simplified workflows for many Python, spreadsheet and data pipeline tasks.

How can I extend Celbridge?
---------------------------

The development team are working on a powerful, flexible extension architecture.

Learn where we are in development at:
- `the Github repo issues <https://github.com/celbridge-org/celbridge/issues>`_
- the Celbridge community `Discourse forum <https://celbridge.discourse.group/>`_


I would like to contribute! How can I get started?
--------------------------------------------------

Awesome! As an open source project, Celbridge thrives off of the innovation and
the ambition of developers like you.

The best way to start contributing to Celbridge is by using it and reporting
any `issues <https://github.com/celbridge-org/celbridge/issues>`_ that you might experience.
A good bug report with clear reproduction steps helps your fellow contributors
fix bugs quickly and efficiently.

If you feel ready to submit your first PR, pick any issue that resonates with you from
one of the links above and try your hand at fixing it. You will need to learn how to
compile the engine from sources, or how to build the documentation. You also need to
get familiar with Git, a version control system that Celbridge developers use.

- if you're not sure how/whether to contribute, talk to us at the Celbridge community `Discourse forum <https://celbridge.discourse.group/>`_ :-)



Who is working on Celbridge?
----------------------------

See the named contributions/credits on the `Celbridge Github repo <https://github.com/celbridge-org/celbridge>`_.
