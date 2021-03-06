### About

Original articles of the following blog http://vdmitriyev.github.io/blog/ in the markdown format configured to .

### Usage

* Install [pelican](https://github.com/getpelican/pelican) python package
```
pip install pelican
```
* Compile markdown files into html. Two options are available (a) ```localhost``` and (b) ```github account```, check ```pelicanconf.py``` file.
```
pelican content
```
or use pre-shipped ```bat``` script
```
run-pelican.bat
```

* Run simple HTTP server to check the results
```
# navigate to the folder with generated HTML files
python -m SimpleHTTPServer 8000
```
or use pre-shipped ```bat``` script
```
run-simple-http.bat
```

### Personal configurations

you need to create ```personal_configs.py``` file and fill following fields:
```
#!/usr/bin/env python
# -*- coding: utf-8 -*- #

#
# personal configurations
#

GOOGLE_ANALYTICS = u'UA-'

LINKS = (('Twitter', '#'),
          ('Wordpress', '#'),
          ('Tumblr', '#')
          )
```

More about configs and configs themselves you can find in pelican's [manual](http://docs.getpelican)com/en/3.5.0/settings.html)

### Theme

* Download [pure-single](https://github.com/PurePelicanTheme/pure-single)
* Install
```
pelican-themes --install PATH
```
### Author

* Viktor Dmitriyev
