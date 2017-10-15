#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from twitter import Twitter, OAuth
import os
import CoreGraphics as cg

access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_SECRET_ACCESS_TOKEN"
api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET_API_KEY"

# TODO: create a log file if it does not exist
log_file_path = 'YOUR_LOG_PATH'
pdf_file_path = 'YOUR_PDF_PATH'
your_name = 'YOUR_NAME'
your_thesis_type = 'YOUR_THESIS_TYPE'

t = Twitter(auth = OAuth(access_token, access_token_secret, api_key, api_secret))

# read saved progress
file = open(log_file_path, 'r')
old_page = file.read()

# get current page number
number_of_pages = cg.CGPDFDocumentCreateWithProvider(cg.CGDataProviderCreateWithFilename(pdf_file_path)).getNumberOfPages()

# calc delta page
delta_page = number_of_pages - int(old_page)

# make text to post
text0 = your_name + 'さんの\n'
text1 = your_thesis_type + '論文の総ページ数は，' + str(number_of_pages) + 'ページです！\n'
text2 = '昨日からの進捗は' + str(delta_page) + 'ページです'
text = text0 + text1 + text2

# post tweet
statusUpdate = t.statuses.update(status=text)

# posted text and user data
# print(statusUpdate['user']['screen_name'])
# print(statusUpdate['user']['name'])
# print(statusUpdate['text'])

# save progress
file2 = open(log_file_path, 'w')
current_page = number_of_pages
file2.write(str(current_page))
