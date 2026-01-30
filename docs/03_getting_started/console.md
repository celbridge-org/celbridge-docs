(doc_console)=

# Using the console

Celbridge comes with a **Console** panel offering a CLI (Command Line Interface). The prompt in this terminal comprises 3 greater-than signs **>>>**.

```{image} /03_getting_started/images/console2.png
:alt: Screenshot showing Console panel with some Python REPL commands
:width: 50%
```

:::{sidebar} The IPython REPL
The console panel is rendered using [Xterm.js](https://xtermjs.org/) hosted in a WebView2. The Xterm.js terminal is connected to a terminal emulator session via [ConPTY](https://devblogs.microsoft.com/commandline/windows-command-line-introducing-the-windows-pseudo-console-conpty/) which is hosting a Python process. The REPL environment is implemented using [IPython](https://ipython.org/) (the same tech used in [Jupyter Notebooks](https://jupyter.org/)). The IPython REPL is a full replacement for the built-in Python REPL that adds a lot of useful functionality. We support all the standard IPython magic commands, such as %run, !, %ls, etc.
:::

The terminal is where you'll see messages from Celbridge, such as the status of loading new extensions or a different version of Python if you change the project settings and re-load the project.

## (I)Python REPL

This terminal offers a full Python [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop), with which you can interact. Some examples of using the Python REPL terminal include:

1. Run a Python script file named `hello.py`, one that contains a Python `print()` statement to ouput the string **Hello world from Python**:

   > ```
   > >>> run hello.py
   > Hello world from Python
   > ```

2. some basic Python commands, including setting and then using variables:

   > ```Python
   > >>> print(3 + 3)
   > 6
   >
   > >>> num_pizzas = 3
   >
   > >>> print(num_pizzas * 10)
   > 30
   > ```

## CLI commands

### CLI bang `!` commands

It also offers a range of commands for running CLI programs, available using the bang "`!`" ([exclamation mark](https://en.wikipedia.org/wiki/Exclamation_mark)) character. Examples including:

1. Directory list (in this example I'm working from an **X:** drive in a Celbridge project named **celbridge_sample**):

   > ```
   > >>> !dir
   > Volume in drive X is Shared Folders
   >
   > Directory of X:\Downloads\celbridge_sample
   >
   > 12/03/2025  10:56 PM               hello.py
   > 12/03/2025  07:59 AM               celbridge_sample.celbridge
   > 12/03/2025  08:08 AM               README.md
   > ```

2. Running `make` commands. For example, if you're building code solution or websites using the **MAKE** tool. In this example I'm running the `make html` command to generate HTML files from RST files in a [Sphinx](https://www.formosa1544.com/2019/09/19/use-sphinx-for-python-documentation/) project (only the first few lines of output are shown ...):

   > ```
   > >>> !make html
   > Running Sphinx v8.2.3
   > loading translations [en]... done
   > loading pickled environment... done
   > building [mo]: targets for 0 po files that are out of date
   > writing output...
   > ... and so on ...
   > ```

:::{note}
**TIP** Use \<CTRL>+L to clear the console
:::

### IPython built-in "magic" `%` commands

IPython offers a range of commands for running CLI programs, available using the percent "`%`" character. Automagic mode is switched on by default, so in almost all cases you can omit the percent "`%`" character, since IPython will saerch its list of magic commands to match against what you have typed.

Examples including:

1. Print Working Direcotry (`%pwd` or `pwd`):

   > ```
   > >>> %pwd
   > 'C:\Documents\github\celbridge-docs'
   >
   > >>> 
   > ```


1. Change Direcotry (`%cd` or `cd`):

   > ```
   > >>> %pwd
   > 'C:\Documents\github\celbridge-docs'
   >
   > >>> %cd ..
   > C:\Documents\github
   >
   > >>> %pwd
   > 'C:\Documents\github'
   >
   > >>>
   > ```

1. History of terminal commands (`%history` or `history`)

   > ```
   > >>> history
   > pwd
   > cd docs
   > !make clean
   > !make html
   > !python3 -m http.server 8000 --directory _build\html
   > history
   > ```

The IPython documentation pages provide
a [full list of the magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

### IPython `.ipy` files

If there are several commands you often type in the same sequence, or have commands with many arguments, you can type those commands into a text file with the `.ipy` extension, and then run the sequence of commands in that file at the terminal with:

   > ```
   > >>> run <filename>.ipy
   > ```

For example, when working with Sphinx I often wish to run `!make clean` immediately before running `!make html`. So I could create a file `make.ipy` containing these commands:

   > ```
   > !make clean
   > !make html
   > ```

And then I can run them by entering `run make.ipy` in the console.


Learn more about REPLs and this console at:

- [REPL (Read-Evaluate-Print-Loop)](https://en.wikipedia.org/wiki/Replit)
- [CLI (Command Line Interface (terminal))](https://en.wikipedia.org/wiki/Command-line_interface)
- [MAKE](<https://en.wikipedia.org/wiki/Make_(software)>)



