
#! /usr/bin/env python3

import os
import requests

feedbacks_dir = '/data/feedback'
url = 'http://<corpweb-external-IP>/feedback/' #Replace <corpweb-external-IP> with your external ip

files = os.listdir(feedbacks_dir)

for file in files:
  file_obj = open(os.path.join(feedbacks_dir, file), 'r')

  lines = [ line.replace('\n', '') for line in file_obj ]

  feedback_dict = { "title": lines[0], "name": lines[1], "date": lines[2], "feedback": lines[3] }

  res = requests.post(url, data=feedback_dict)

  if not res.status_code == 201:
    print('Something went wrong')

  file_obj.close()
