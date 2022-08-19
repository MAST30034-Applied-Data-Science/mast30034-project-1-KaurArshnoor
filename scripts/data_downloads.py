# from urllib import request

# remote_url = 'https://www.calendarpedia.com/2019-calendar-excel-templates.html'

# local_file = '../data/raw/2019_holidays.csv'

# request.urlretrieve(remote_url, local_file)

# import requests
# # Define the remote file to retrieve
# remote_url = 'https://www.calendarpedia.com/2019-calendar-excel-templates.html'
# # Define the local filename to save data
# local_file = '../data/raw/2019_holidays.csv'
# # Make http request for remote file data
# data = requests.get(remote_url)
# # Save file data to local copy
# with open(local_file, 'wb')as file:
#     file.write(data.content)

import requests, urllib, csv, json, sys, codecs
    
try: 
  ResultBytes = urllib.request.urlopen("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/New%20York%20City%2CUSA/2018-10-01/2019-04-01?unitGroup=metric&include=days&key=87T4ZF4YVXS6GTTXX2EVXTREQ&contentType=csv")
  # Parse the results as CSV
  CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
  # Parse the results as JSON
  jsonData = json.loads(ResultBytes.decode('utf-8'))
except urllib.error.HTTPError  as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code, ErrorInfo)
  sys.exit()
except  urllib.error.URLError as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code,ErrorInfo)
  sys.exit()