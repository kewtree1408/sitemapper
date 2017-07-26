## Run CLI

1. Git clone and install requirements:
```
git clone git@github.com:kewtree1408/sitemapper.git
cd sitemapper
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install -r req.txt
```
Note: Run on Linux/MacOS only.

2. Getting the sitemap:
```
$ ./cli.py --url=https://www.python.org --proto-format=file
$ ./cli.py --url=https://www.python.org --proto-format=xml
```

## Tests
$ tox --


### Warning
This CLI will **not return all pages** for the **large** site with deep links (for ex: google.com). You will not go deeper than 50 iterations.
