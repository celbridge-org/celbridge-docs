Setting up Sphinx with Celbridge
=================================

The documentation for Celbridge is generated from `.rst` (ReStructured Text `rst_guide`_) files using `sphinx_guide`_.

The steps below show how to setup a Sphinx project in Celbridge.


1. Create a new Celbridge project

    - ensure you wrap double-quotes around the package name.

2. Open the `.celbridge` project settings file, and for the **project** section, add to the **dependencies** the list of these 2 packages: `sphinx` and `sphinx_rtd_theme`:

    .. code::

        [project]
        requires-python = "3.12"
        dependencies = ["sphinx", "sphinx_rtd_theme"]

3. After a second or two Celbridge will detect you have changed the project settings file, and in the **Console** you'll be offered a button to `Reload project`.

    - Click this button to reload the project with the new settings.
    - The console window will show Sphyinx being installed.

5. Run the quickstart, by typing `!sphinx-quickstart` in the **Console**:
    - you'll need to enter some details such as:
        - separate source and build directories
            - I always say yes to this
        - project name 
            - e.g. sphinx demo
        - author name 
            - e.g. Matt Smith
        - project release
            - you can jut hit return, 
            - or give a version number like 1.0
        - project language 
            - default is English, so you can hit return, 
            - or enter 2-character language code)
    - you'll then see some files and folders created for your project

Here's the output I got when runnning this quickstart:
.. code:: 

    >>> !sphinx-quickstart
    Welcome to the Sphinx 8.2.3 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Selected root path: .

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: y

    The project name will occur in several places in the built documentation.
    > Project name: sphinx demo
    > Author name(s): Matt Smith
    > Project release []: 

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Project language [en]: 

    Creating file X:\Downloads\celbirdge-files\sphinx-demo2\source\conf.py.
    Creating file X:\Downloads\celbirdge-files\sphinx-demo2\source\index.rst.
    Creating file X:\Downloads\celbirdge-files\sphinx-demo2\Makefile.
    Creating file X:\Downloads\celbirdge-files\sphinx-demo2\make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file X:\Downloads\celbirdge-files\sphinx-demo2\source\index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
    make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

6. Note the new files and directories created:

    .. code:: 

        |____/build
        |____/source
        | |____/static
        | |____/templates
        | |____index.rst
        | |____conf.py
        |____make.bat
        |____Makefile

    - `build` is empty - this is where your generated HTML page go
    - `/source/index.rst` - this is your index page and also navigation page list
        - you'll add new pages to be linked in this file

7. Add a new `.rst` file saying hello world:
    - in `/source` create new file `hello.rst` containing the following:

    .. code:: 

        Hello world
        ===========

        I am some RST text in a new file

8. Add a reference to this file in `/source/index.rst`:
    - Add `hello`, indexed with 3 spaces, after a new blank line, at the end of this file:

    .. code:: 

        .. toctree::
        :maxdepth: 2
        :caption: Contents:

           hello

8. The Sphinx Read-The-Docs theme is great. To configure Sphinx to use this theme edit the last few lines of `/source/conf.py` file, by addingt the **"sphinx_rtd_theme"** into the list of extensions, and specifying that variable `html_theme` has the value **"sphinx_rtd_theme"**:

    .. code:: 

        extensions = [
            "sphinx_rtd_theme",
        ] 

        templates_path = ['_templates']
        exclude_patterns = []



        # -- Options for HTML output -------------------------------------------------
        # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

        #html_theme = 'alabaster'
        html_theme = "sphinx_rtd_theme"


8. Run the Sphinx website builder, by typing `!make html` in the **Console**:

9. Once you server the HTML files one the home page should see a link **Hello world**, linking to your simple Hello World generated HTML page:

.. image:: /images/hello_page.png
   :alt: Screenshot showing Hello World page now part of website and nav list


.. note::
   If links, not just page content, have changed, you should do a clean before the build, to clear out older files.

   To clean then build run these 2 commands in the **Console**:

    .. code:: 

        >>> !make clean
        >>> !make html

Acknowledgements

This `sphinx_guide`_ was useful in creating this documentation page.



.. _sphinx_guide: https://www.formosa1544.com/2019/09/19/use-sphinx-for-python-documentation/

.. _rst_guide: https://restructuredtext-guide.readthedocs.io/en/latest/ch_syntax.html


