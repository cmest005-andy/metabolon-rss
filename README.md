Metabolon Project - RSS feed date check

Python 3.9
Author Carlos Mestre
---------------------
Script uses series of arguments, first URL(s), then number of days to check for activity.
ex: 
py .\rss_feed_inactivity_checker.py 'https://podcastfeeds.nbcnews.com/dateline-nbc' 'https://mcsorleys.barstoolsports.com/feed/call-her-daddy' 3

Expected result:
Checking URL #1
{'status': 'Success', 'message': 'Company active within the last 3 days.'}
Checking URL #2
{'status': 'Success', 'message': 'Company active within the last 3 days.'}
---------------------
Error if number of days less than 1
ex: 
py .\rss_feed_inactivity_checker.py 'https://podcastfeeds.nbcnews.com/dateline-nbc' 0

Expected result: 
Error: Please enter required attributes of URL(s) and Days
---------------------
Error if at least 2 arguments (url, days) is not given:
ex: 
py .\rss_feed_inactivity_checker.py 'https://podcastfeeds.nbcnews.com/dateline-nbc'

Expected result:
Error: Please enter required attributes of URL(s) and Days
---------------------
Assumptions:
URL first, days second.
URL inserted as a string with single quotes surrounding
Days as a number
---------------------
Possible improvements:
Custom date parser to handle multiple types of input dates. Although this shouldnt be necessary considering pubDate has a standard. Still should cover all bases.
---------------------
Notes:
If you see the name Andy around, its my nickname and what most people call me. So it may be seen in paths or GitHub.
