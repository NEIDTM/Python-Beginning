import requests
import urllib
import webbrowser

task = input("Your request: ")

webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome"))

webbrowser.get(using="chrome").open_new_tab("google.co.uk\search?q=" + task)
