#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  urllib.request
import sys

def download(url, title):
    """download video from specific url"""
    urllib.request.urlretrieve(url, title)

if __name__ == "__main__":
    download("http://www.dygod.net/", "test.html")
