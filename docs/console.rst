Using the console 
=================

Celbridge comes with a CLI (Command Line Interface) **Terminal** panel. The prompt in this terminal comprising 3 greater-than signs **>>>**.

The console panel is rendered using `Xterm`_.js hosted in a WebView2

The terminal is where you'll see messages from Celbridge, such as the status of loading new extensions or a different version of Python if you change the project settings and re-load the project.

.. image:: /images/console.png
   :alt: Screenshot showing Console panel with some Python REPL commands


**Python REPL**

This terminal offers a full Python REPL, with which you can interact. Some examples of using the Python REPL terminal include:

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


**CLI commands**

It also offers a range of commands for running CLI programs. Examples including:

1. Directory list (in this example I'm working from an **X:** drive in a Celbridge project named **celbridge_sample**):

    .. code:: 

        >>> !dir
        Volume in drive X is Shared Folders

        Directory of X:\Downloads\celbridge_sample

        12/03/2025  10:56 PM               hello.py
        12/03/2025  07:59 AM               celbridge_sample.celbridge
        12/03/2025  08:08 AM               README.md

2. Running `make` commands. For eaxmpe, if you're building code solution or websites using the MAKE tool. In this example I'm runnig the **make html** command to generate HTML files from RST files in a `Sphinx`_  project (only the first few lines of output are shown ...):

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

- REPL (Read-Evaluate-Print-Loop) `repl`_ 
- CLI (Command Line Interface (terminal)) `cli`_ 
- MAKE `make`_ 


.. _repl: https://en.wikipedia.org/wiki/Replit
.. _cli: https://en.wikipedia.org/wiki/Command-line_interface
.. _make: https://en.wikipedia.org/wiki/Make_(software)
.. _Xterm: https://xtermjs.org/



.. _Sphinx: https://www.formosa1544.com/2019/09/19/use-sphinx-for-python-documentation/

