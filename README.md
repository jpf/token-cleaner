Token cleaner
-------------

Turn an authentication token into a similar looking, but obviously fake token.

This is useful for documentation or sample configuration files, where you want to have a similar "look" but don't want to put a real token.

Takes a real token like: 
"b45HoPmm4HG"
and makes a "fake" token like:
"a01BcDef2GH"


Usage:

    $ python clean.py b45HoPmm4HG
    a01BcDef2GH

