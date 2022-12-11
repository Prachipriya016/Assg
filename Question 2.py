#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from html_to_etree import parse_html_bytes
from extract_social_media import find_links_tree
web = input("Enter Website adress")
res = requests.get('https://ful.io')
tree = parse_html_bytes(res.content, res.headers.get('content-type'))

set(find_links_tree(tree))

# In[ ]:



