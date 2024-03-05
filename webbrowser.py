import requests
import urllib
import webbrowser

webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome"))

webbrowser.get(using="chrome").open_new_tab("github.com")
