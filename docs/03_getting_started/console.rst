
.. _doc_console:


Using the console
=================

Celbridge comes with a  **Console** panel offering a CLI (Command Line Interface). The prompt in this terminal comprises 3 greater-than signs **>>>**.



.. image:: /03_getting_started/images/console.png
    :width: 75%
    :alt: Screenshot showing Console panel with some Python REPL commands


.. sidebar:: The IPython REPL

    The console panel is rendered using `Xterm.js <https://xtermjs.org/>`_ hosted in a WebView2. The Xterm.js terminal is connected to a terminal emulator session via `ConPTY <https://devblogs.microsoft.com/commandline/windows-command-line-introducing-the-windows-pseudo-console-conpty/>`_ which is hosting a Python process. The REPL environment is implemented using `IPython <https://ipython.org/>`_ (the same tech used in `Jupyter Notebooks <https://jupyter.org/>`_). The IPython REPL is a full replacement for the built-in Python REPL that adds a lot of useful functionality. We support all the standard IPython magic commands, such as %run, !, %ls, etc.



The terminal is where you'll see messages from Celbridge, such as the status of loading new extensions or a different version of Python if you change the project settings and re-load the project.


(I)Python REPL
--------------

This terminal offers a full Python `REPL <https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop>`_, with which you can interact. Some examples of using the Python REPL terminal include:

1. Run a Python script file named `hello.py`, one that contains a Python `print()` statement to ouput the string **Hello world from Python**:

    .. code:: 

        >>> run hello.py
        Hello world from Python

2. some basic Python commands, including setting and then using variables:

    .. code:: Python

        >>> print(3 + 3)
        6

        >>> num_pizzas = 3

        >>> print(num_pizzas * 10)
        30


CLI commands
------------

It also offers a range of commands for running CLI programs, available using the bang "`!`" (`exclamation mark <https://en.wikipedia.org/wiki/Exclamation_mark>`_) character. Examples including:

1. Directory list (in this example I'm working from an **X:** drive in a Celbridge project named **celbridge_sample**):

    .. code:: 

        >>> !dir
        Volume in drive X is Shared Folders

        Directory of X:\Downloads\celbridge_sample

        12/03/2025  10:56 PM               hello.py
        12/03/2025  07:59 AM               celbridge_sample.celbridge
        12/03/2025  08:08 AM               README.md

2. Running `make` commands. For eaxmpe, if you're building code solution or websites using the MAKE tool. In this example I'm runnig the **make html** command to generate HTML files from RST files in a `Sphinx <https://www.formosa1544.com/2019/09/19/use-sphinx-for-python-documentation/>`_  project (only the first few lines of output are shown ...):

    .. code:: 

        >>> !make
        Running Sphinx v8.2.3
        loading translations [en]... done
        loading pickled environment... done
        building [mo]: targets for 0 po files that are out of date
        writing output... 
        ... and so on ...

.. note::
   **TIP** Use <CTRL>+L to clear the console

Learn more about REPLs and this console at:

- `REPL (Read-Evaluate-Print-Loop) <https://en.wikipedia.org/wiki/Replit>`_
- `CLI (Command Line Interface (terminal)) <https://en.wikipedia.org/wiki/Command-line_interface>`_
- `MAKE <https://en.wikipedia.org/wiki/Make_(software)>`_

The IPython documentation pages provide 
a `full list of the magic commands <https://ipython.readthedocs.io/en/stable/interactive/magics.html>`_



