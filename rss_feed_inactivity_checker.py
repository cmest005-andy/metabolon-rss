"""
rss_feed_inactivity_checker.py
Script which parses the XML from a RSS feed and identifies if the company has had activity for the last given n number of days

Carlos Mestre 2021-1-31
"""

import requests
from bs4 import BeautifulSoup
from datetime import timedelta
import datetime
import json
import sys


class RSS_Reader(object):
    """
    Class which contains the functionality to parse RSS feeds for activity use
    """

    def getXMLfromRSSfeed(self, url, days):
        """
        Retrieves XML data for url passed in console arguments with the help of a private method.

        Args:
            url (str): the url string passed in the first argument which directs the requests library to the website address
            days (int): the number of days passed by the second argument which tests the feed for activity 
        """
        results = ''
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, features='xml')
            
            info = soup.findAll('item')
            datetime_list = []

            for i in info:
                dt = datetime.datetime.strptime(i.find('pubDate').text, "%a, %d %b %Y %H:%M:%S %z") 
                datetime_list.append(dt)
            
            results = self._processDateList(datetime_list,days)

        except Exception as e:
            print(e)
        
        ###unit test sample ###
        #return "{'status': 'Success', 'message': 'Company active within the last 3 days.'}"
        return results

    def _processDateList(self, datetime_list, days):
        """
        Processes list of dates to test for activity within the set amount.

        Args:
            datetime_list (list): list passed which contains all datetimes from RSS feed parsed above
            days (int): the number of days passed by the second argument which tests the feed for activity 
        """
        for dt in datetime_list:
            testdate = dt - datetime.timedelta(days=days)

            if dt > testdate:
                test_result = {'status':'Success','message':'Company active within the last '+str(days)+' days.'}
                return test_result

        test_result = {'status':'Failed','message':'Alert: company inactive greater than '+str(days)+' days.'}
        return test_result

def main():
    arg_list = sys.argv[1:]

    #Test for arguments
    if int(len(arg_list)) == 0 or int(len(arg_list)) == 1:
        print('Error: Please enter required attributes of URL(s) and Days')
        sys.exit(0)

    #Test for invalid input for number of days
    if int(arg_list[len(arg_list)-1]) < 1:
        print('Error: Please enter a value for days greater than 0')
        sys.exit(0)

    count = 1
    while count < len(arg_list):
        rss_reader = RSS_Reader()
        print("Checking URL #"+str(count))
        result = rss_reader.getXMLfromRSSfeed(arg_list[0],int(arg_list[len(arg_list)-1]))
        count +=1
        print(result)

if __name__ == "__main__":
    main()
