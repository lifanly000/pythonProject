# -*- coding: utf-8 -*-

import requests

r =  requests.get("http://www.baidu.com")
print r.content.decode("utf-8")