# celbridge-docs
User documentation for the OOS Celbridge project:
- 

The docs can be found published via Github pages at:
- https://celbridge-org.github.io/celbridge-docs/

## This repo is a Celbridge project - you can build the docs in Celbridge :-)
These docs are to be generated using the Spinx Python static HTML site generator, in a Celbridge project:

1. clone repo locally

3. open project in the **Celbridge** application

4. at the console 'cd' into the `/docs` folder:
    ```
    >>> %cd docs
    ```

5. use MAKE to clean any previous generated docxs with a **clean** build
     ```
    >>> !make clean
    ```

6. use MAKE to build a new set of docs in direcotry `_build`
    ```
    >>> !make html
    ```

7. run a webserver, to serve up the contents of `/docs/_build/html`

![screenshot of docs project open in Celbrdige with Console make commands](make_html.png)




## Acknowledgements
I got the Sphinx Github Actions to work thanks to this resource from Shengyu Zhang:
- https://sphinx.silverrainz.me/pages/index.html
  
