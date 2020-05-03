
import pandas as pd
import numpy as np
import requests


result = requests.get('https://imgs.xkcd.com/comics/python.png')

print(result.status_code)

print(result.text)

#print(result.headers)







