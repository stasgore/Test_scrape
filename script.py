import sys
import requests
import bs4 as BeautifulSoup


# print()
# ## shows the version of python we are using
# print(f"You are using Python version: {sys.version}")
# print()
# ## prints out the location where python is located on this mashine
# print(f"Your python interpreter is installed here: {sys.executable}")


# def greet(who_to_greet):
#     greeting = "Hello, {}!".format(who_to_greet)
#     return greeting


# print(greet("Stas"))
# r = requests.get("https://coreyms.com")
# print(r.status_code)
name = input("Your name?")
print("Hello,", name)
