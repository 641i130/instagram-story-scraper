import insta_stories
import sys
# MODE
# Mode 0 is for download only one account
# Mode 1 is for downloading multiple accounts
# ACCOUNTS
# The accounts array is for the username(s) of the accounts scraping

try:
    username = sys.argv[1]
    password = sys.argv[2]
    mode = sys.argv[3]
    accounts = sys.argv[4]
    insta_stories.login(username, password, mode, accounts)
except:
    print("")
    print ('Usage: scrape_stories.py [username] [password] [mode] [accounts]')
    print('Example: scrape_stories.py username password 0 "pewdiepie"')
    print('or')
    print('Example: scrape_stories.py username password 1 ("pewdiepie", "jacksepticeye", "jaiden_animations")')

"""
 ___        ___        _    _        _
|_ _| ___  | . \ ___  | |  <_> ___ _| |_
 | | / . \ | | |/ . \ | |_ | |<_-<  | |
 |_| \___/ |___/\___/ |___||_|/__/  |_|
"""
# Speed up the whole process!!!
# Polish the "DownloadInto" function
# Add timeouts for controlled downloading and daily download if kept on always
# Add a function to download all the stories of the users followers


# works with only one need to fix array problem
