Python Versions and Packages
============================

The project settings file configures the project for a specific version of Python. This file is named `yourprojectname.celbridge` , and is visible in the explorer panel. 

**Python version**

The `Python` section of the project settings file declares the Python version for the project. For example, this declares Python version **3.13.6** for a project:

.. code:: 

    [python]
    version = "3.13.6"

.. note::
   Every project **must** have a `[python]` section, and a Python language `version` specified.

   When you create a new Celbridge project an up-to-date version of Python will autopmatically be declared in the project settings file created with the project.
   
**Python Packages**

Additionally, you can specific Pythn (PyPi) packages to be automatically loaded through the project settings file. 

For example, let's add the data analysis library `Pandas`_  to our Celbridge project. 

1. Open the `.celbridge` project settings file:
    - double-click it in the explorer panel.

2. Under the `packages` key in the `[python]` section, type `"pandas"`:
    - ensure you wrap double-quotes around the package name.


.. image:: /images/project_settings.png
   :alt: Screenshot showing Python version and extensions in .celbridge configuration file


3. Reload the project:
    - navigate to the hambuger menu in the top left and click `Reload project`. 

4. The console window will show Pandas being installed. 

You can specify multiple packages by declaring a comma-separate list of them in the `packages` key. For example, here we specify both the `"pandas"` and `"numpy"` packages:

.. code:: 

    [python]
    version = "3.13.6"
    packages = ["pandas", "numpy"]

For a list of Python packages visit `Pypi`_ 


.. _Pypi: https://pypi.org/
.. _Pandas: https://pandas.pydata.org/

