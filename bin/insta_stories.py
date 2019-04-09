from selenium import webdriver
from bs4 import BeautifulSoup
import selenium
import time
import wget
import urllib.request
import sys, os
import subprocess
import requests
from os.path import basename
import shutil
from pathlib import Path

#driver = webdriver.Firefox()

def login(myusername, mypassword, mode, accounts):
    driver = webdriver.Firefox()
    # Login with arguments
    print("Logging in as " + '"' + myusername + '".')
    time.sleep(2)
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)
    driver.find_element_by_name('username').send_keys(myusername)
    driver.find_element_by_name('password').send_keys(mypassword)
    time.sleep(2.25)
    # Click Login
    try:
        driver.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]/button/div").click()
    except Exception as e:
        #print(e)
        print("Not able to use the default login button path...")
        print("Using alternative path...")
        print("")
        driver.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[5]/button").click()
    time.sleep(2)
    # Main loop of whole program
    try:
        if mode != 0:
            for username in accounts:
                scrapeStories(username)
            killMe()
        else:
            scrapeStories(accounts)
            killMe()
    except Exception as e:
        print(e)
        killMe()

def scrapeStories(username):
    #put links in arrays
    print("Scraping stories from " + '"' + username + '".' )
    ImageList = []
    VideoList = []
    getSRCS(username, ImageList, VideoList)
    # Download images into folders made with username of account
    downloadInto(ImageList, username)
    downloadInto(VideoList, username)
    # Put downloading system into a function
    # Make an array of users to download
    print("Downloaded " + str(len(ImageList)) + " images from " + '"' + username + '".')
    print("Downloaded " + str(len(VideoList)) + " videos from " + '"' + username + '".')

def getSRCS(username, ImageList, VideoList):
    # Get every path of image and video for specific user by pressing button then adding
    # While the stories are from the given user, keep clicking and logging
    story_page = "https://www.instagram.com/stories" + "/" + username + "/"
    driver.get(story_page)
    while driver.current_url == story_page:
        #Get all resources after clicking
        Resources = driver.execute_script("return window.performance.getEntriesByType('resource');")
        time.sleep(2)
        Resources = driver.execute_script("return window.performance.getEntriesByType('resource');")
        #print(Resources)
        for resource in Resources:
            if 'jpg' in resource['name'] and resource['decodedBodySize'] > 9900:
                if resource['name'] not in ImageList:
                    ImageList.append(resource['name'])
            if 'mp4' in resource['name'] and resource['initiatorType'] != 'imageset':
                if resource['name'] not in ImageList:
                    VideoList.append(resource['name'])
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/span/section/div/div/section/div[2]/button[2]/div").click()

def downloadInto(array, username):
    #Make folders for files
    cwd = os.getcwd()
    newpath = cwd + "\\" + username
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    # Download files into folder
    try:
        for i in range(len(array)):
            f_name = array[i].split('/')[10].split('?')[0]
            f_path_file = "./" + username + "/" + f_name
            my_file = Path(f_path_file)
            if my_file.is_file():
                print("File exsists...")
                continue
            else:
                # print(f_name)
                with requests.get(array[i], stream=True) as r:
                    r.raise_for_status()
                    with open(f_path_file, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk: # filter out keep-alive new chunks
                                f.write(chunk)
    except Exception as e:
        print(e)



def killMe():
    driver.close()
