<div align="center">
  <img width="30%" src="https://svgshare.com/i/CE1.svg"></img>
</div>
<h1 align="center">Instagram Story Scraper</h1>
<p align="center">
    <a href="https://github.com/SeleniumHQ/selenium">
      <img src="https://img.shields.io/badge/built%20with-Selenium-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
  </p>
<p>An <b>OPENSOURCE</b> non-api Instagram story scraper that uses your user login information to download stories from a given set of users.</p>
<p>
  <p>A tool that <b>scrapes</b> Instagram stories implemented in Python 3 using the Selenium module.<p>
</p>
<p>
  Made to save stories for offline usage such as back ups or archiving usages.
</p>


## Quick Start 🚀

- **You need to have Python 3.6 or above installed**

  - `python3 --version`

On Windows you might have to use `python` without the version (`3`) suffix.

- **If your version is below 3.6, we recommend you install the latest Python 3.7**

  - [Python on Raspberry Raspbian / Debian / Ubuntu](https://github.com/instabot-py/instabot.py/wiki/Installing-Python-3.7-on-Raspberry-Pi)
  - [Python on Windows](https://github.com/instabot-py/instabot.py/wiki/Installing-Python-on-Windows)
  - [Python on Mac](https://github.com/instabot-py/instabot.py/wiki/Installing-Python-3.7-on-macOS)

- **Install REQUIREMENTS from requirements.txt**

  - `python3 -m pip install -r requirements.txt`

- **Start** 🏁

    - `scrape_stories.py`
    - or `python3 -m scrape_stories.py`

## **Examples** 🍽️
### For one account
  - `scrape_stories.py username password 0 "pewdiepie"`
### For multiple accounts
  - `scrape_stories.py username password 1 ("pewdiepie", "jacksepticeye", "jaiden_animations")")`

## Video Tutorials 🎥
List of how-to videos
* Coming soon (If someone requests it)

## To-Do List
  - Make it schedulable (ex: daily downloader)
  - Find a way to use only requests similar to [instabot.py](https://github.com/instabot-py/instabot.py)
  - Make it more reliable and consistent
  - Add post functionality
