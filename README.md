## Run CLI

1. Git clone:
```
$ git clone git@github.com:kewtree1408/sitemapper.git
```

2. Install requirements:
```
$ pip install -r req.txt
```

3. Getting the sitemap:
```
$ cd sitemapper
$ ./sitemapper/cli.py --url=https://www.python.org --proto-format=file
$ ./sitemapper/cli.py --url=https://www.python.org --proto-format=xml
```

## Tests:
$ tox


### Warning
This CLI will **not return all pages** for the **large** site with deep links (for ex: google.com). You will not go deeper than 50 iterations.
