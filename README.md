**Metabolon Project - RSS feed date check**

**Python 3.9**
**Author Carlos Mestre**

**Script uses series of arguments, first URL(s), then number of days to check for activity.**
ex:<br />
py .\rss_feed_inactivity_checker.py 'https://podcastfeeds.nbcnews.com/dateline-nbc' 'https://mcsorleys.barstoolsports.com/feed/call-her-daddy' 3<br />

Expected result:<br />
Checking URL #1<br />
{'status': 'Success', 'message': 'Company active within the last 3 days.'}<br />
Checking URL #2<br />
{'status': 'Success', 'message': 'Company active within the last 3 days.'}<br />

**Error if number of days less than 1**
ex:<br />
py .\rss_feed_inactivity_checker.py 'https://podcastfeeds.nbcnews.com/dateline-nbc' 0<br />

Expected result:<br />
Error:<br /> Please enter required attributes of URL(s) and Days

**Error if at least 2 arguments (url, days) is not given:**
ex:<br /> 
py .\rss_feed_inactivity_checker.py 'https://podcastfeeds.nbcnews.com/dateline-nbc'<br />

Expected result:
Error:<br /> Please enter required attributes of URL(s) and Days

**Assumptions:**
1. URL first, days second.<br />
2. URL inserted as a string with single quotes surrounding<br />
3. Days as a number<br />

**Possible improvements:**
Custom date parser to handle multiple types of input dates. Although this shouldnt be necessary considering pubDate has a standard. Still should cover all bases.<br />

**Notes:**
If you see the name Andy around, its my nickname and what most people call me. So it may be seen in paths or GitHub.<br />
