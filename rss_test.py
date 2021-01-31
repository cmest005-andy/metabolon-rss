import rss_feed_inactivity_checker
import unittest


class Test_TestRSS(unittest.TestCase):
    def test_feed_return(self):
        self.assertEqual(rss_feed_inactivity_checker.RSS_Reader.getXMLfromRSSfeed(self,'https://podcastfeeds.nbcnews.com/HL4TzgYC',3),"{'status': 'Success', 'message': 'Company active within the last 3 days.'}")

if __name__ == '__main__':
    unittest.main()