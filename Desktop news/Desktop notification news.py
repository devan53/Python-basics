from topnews import topStories
from win10toast import ToastNotifier
import setuptools
import time
import requests


ICON = "/news.ico"

# fetch news items
newsitems = topStories()

# One-time initialization
toaster = ToastNotifier()

for news in newsitems:
    toaster.show_toast(news['title'], news['description'], icon_path = None, duration = 10)
    time.sleep(10)



                 
