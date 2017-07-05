---
author: sricharanchiruvolu
comments: true
date: 2015-09-27 10:00:00+00:00
layout: post
slug: Crawling-the-web
title: Crawl the web with Python
disqus: y
tags:
- python
- webdev
- crawler
categories:
- webdev
---

One of the things that web developers had to do for their projects is to take the datapoints all over the web, from different resources around the world and pull them all together
and centralize them for easy access for end users. The way that you really go is to talk to those different websites and get exposure to some APIs where you can pull the data from.

Unfortunately, that's not always the case, what we had to resort to is do a bit of web crawling and scraping. We'll use some python code to get an exposure of crawling the web. (Google's original web crawler and scraper were written in Python. It's migrated to mostly C++ now.)

What exactly are we going to do is crawl around on some specific site. We'll write some code that's going to navigate around a website and find different links and then follow those links to different pages within that site and possibly
even other websites. Scraping is to look at the source code of the site and map them to extract specific information from it. It's defintely prone to failures and break over time. This is mostly crude and isn't the rudimentary way to do it, but it gets job done.

Let's do something interesting, we'll crawl and scrap the itunes site to get certain information about the apps (It's kinda boring to always open itunes for checking out the new apps, or if you're on a *nix machine). Once we get the information, we can do some analytics, create reports or just put it in our database.

This part of the tutorial will be very basic, we'll just start with an app page and then just take out the information we need; nothing complicated. Later iterations will have advanced parsing and scraping techniques.

Open the candy crush saga app website in your browser at [https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8](https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8). We'll start on this page, pull all the information we want, go another level deeper, say pull the information for "Customers also bought" apps, and so on. That should be enough to get started.

Let's start to get down into some code. Let's create a file called __itunes.py__.

Here's my structure of code for this case:

    #! /usr/bin/python

    class AppCrawler:
      def __init__(self, starting_url, depth):
	  self.starting_url = starting_url
	  self.depth = depth
	  self.apps = []
	
      def crawl(self):
	  # All the crawl logic goes here.
	  return

      def get_app_from_link(self, link):
	  # Get information from link
	  return

    # Do something with the data. We'll just be printing it.
    # We can do some analytics or whatever.
    class App:
      def __init__(self, name, developer, price, links):
	  self.name = name
	  self.developer = developer
	  self.price = price
	  self.links = links
	
      def __str__(self):
	  return ("Name" + self.name.encode('UTF-8') + "\r\nDeveloper: " + self.developer.encode('UTF-8') + "\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")
	
	
				    
    def main():
	# Execution starts here
	crawler = AppCrawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8', 0)
	crawler.crawl()
	for app in crawler.apps:
	    print app
		    
    if __name__ == "__main__": main()

The code is pretty much self-explainatory. It doesn't do much. Make sure that it executes with no errors.

Now, for writing the crawler code, we will use a _lxml_ and _requests_ modules. Both are present in *nix systems by default, if not you can install them via _pip_.

Import the following in your __itunes.py__ file:

    from lxml import html
    import requests

Let's issue a simple get request to the page and print the site, just to see everything is working. Here's how you do it.

    def crawl(self):
	# All the crawl logic goes here.
	self.get_app_from_link(self.starting_url)
	return
      
    def get_app_from_link(self, link):
	# Get information from link
	start_page = requests.get(link)
	print start_page.text
	return
	
Parsing that large chuck of data with native python might be a pain, so we use _lxml_ library for this cause. It creates a document tree out of that, which will be helpful. We generate this tree with the following command.

    tree = html.fromstring(start_page.text)
    
We can use this tree to execute xpath queries into that document and pull the data out. I'm not going into the xpath details here, but to get the app name from the site, app name is in the h1 tag of the html with the class itemprop="name" (You need to inspect element to find this out). The query below would generate a list with the h1 tag having itemprop="name" property.

    name = tree.xpath('//h1[@itemprop="name"]/text()')
    
We will use the same technique to dig the information about the app name, the developer and the price for the app, here's the code:

    name = tree.xpath('//h1[@itemprop="name"]/text()')[0]
    developer = tree.xpath('//div[@class="left"]/h2/text()')[0]
    price = tree.xpath('//div[@itemprop="price"]/text()')[0]
    
Now, let's write the code for getting intel on "Customers also bought" apps. We need to parse through the decendents of class="centre-stack", match with a wildcard character that says "give me everything from within there". And from all that data, make a list of anchor tags with class="name". Now give me the value at that href.

    links = tree.xpath('//div[@class="center-stack"]//*/a[@class="name"]/@href')

This can be iterated over. For example, we can print all the apps "Customers also bought" links like this,
    
    for link in links:
	print link
	
Finally, we'll call the App class to do something with the data, in this case, just print to console. We'll also append app names to the list of apps we came across.

    app = App(name, developer, price, link)
    self.apps.append(app)
    
<hr/>
Here's the full that prints the app details:

    #! /usr/bin/python
    from lxml import html
    import requests 

    class AppCrawler:
      def __init__(self, starting_url, depth):
	self.starting_url = starting_url
	self.depth = depth
	self.apps = []
	
      def crawl(self):
	# All the crawl logic goes here.
	self.get_app_from_link(self.starting_url)
	return
      
      def get_app_from_link(self, link):
	# Get information from link
	start_page = request.get(link)
	tree = html.fromstring(start_page.text)
	
	name = tree.xpath('//h1[@itemprop="name"]/text()')[0]
	developer = tree.xpath('//div[@class="left"]/h2/text()')[0]
	price = tree.xpath('//div[@itemprop="price"]/text()')[0]
	
	links = tree.xpath('//div[@class="center-stack"]//*/a[@class="name"]/@href')
	
	app = App(name, developer, price, link)
	self.apps.append(app)
	
    # Do something with the data. We'll just be printing it.
    # We can do some analytics or whatever.
    class App:
      def __init__(self, name, developer, price, links):
	self.name = name
	self.developer = developer
	self.price = price
	self.links = links
	
      def __str__(self):
	return ("Name" + self.name.encode('UTF-8') + "\r\nDeveloper: " + self.developer.encode('UTF-8') + "\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")
	
	
				    
    def main():
      # Execution starts here
      crawler = AppCrawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8', 0)
      crawler.crawl()
      for app in crawler.apps:
	print app
		    
    if __name__ == "__main__": main()
    
Here's the output on the console:
<pre><code>Name: Candy Crash Saga
Developer: By King.com Limited
Price: Free

</code></pre>

<hr/>

After this, we need to follow the links and actract the information for every app we come across.

The logic is to interate over the links, keeping track of the depth and fetching links everytime until depth variable is exhausted. We'll use __current_depth__ and __depth_links__ to keep track of this.

      self.starting_url = starting_url
      self.depth = depth
      self.current_depth = 0
      self.depth_links = []
      self.apps = []
      
Next, for every iteration, we append the new links found in that depth to depth_links and loop over that path and parse as long as _current_depth_ is less than _depth_. Putting that into code, here's how we interate over and fetch apps:

    while self.current_depth < self.depth:
      for link in self.depth_links[self.current_depth]:
        current_app = self.get_app_from_link(link)
        current_links.extend(current_app.links)
        self.app.append(current_app)
      self.current_depth += 1
      self.depth_links.append(current_links)
      
Once you put that over, you can change the depth in the main() function to see the lists of apps and their details printed on the console.

> Note that many websites out there would blacklist your ip address if they see that you're crawling very fast and prevent you from accessing _get_ requests. It's safer to put in a little bit of _wait_/_sleep_ time.


We'll import time module and sleep for a second between every iteration.

<hr/>

Here's the complete code:

    #! /usr/bin/python
    from lxml import html
    import requests
    import time

    class AppCrawler:
      def __init__(self, starting_url, depth):
	  self.starting_url = starting_url
	  self.depth = depth
	  self.current_depth = 0
	  self.depth_links = []
	  self.apps = []
	
      def crawl(self):
	# All the crawl logic goes here.
	app = self.get_app_from_link(self.starting_url)
	self.apps.append(app)
	self.depth_links.append(app.links)
	
	while self.current_depth < self.depth:
	  for link in self.depth_links[self.current_depth]:
	    current_app = self.get_app_from_link(link)
	    current_links.extend(current_app.links)
	    self.app.append(current_app)
	    time.sleep(1)
	  self.current_depth += 1
	  self.depth_links.append(current_links)
	
	return
      
      def get_app_from_link(self, link):
	# Get information from link
	start_page = request.get(link)
	tree = html.fromstring(start_page.text)
	
	name = tree.xpath('//h1[@itemprop="name"]/text()')[0]
	developer = tree.xpath('//div[@class="left"]/h2/text()')[0]
	price = tree.xpath('//div[@itemprop="price"]/text()')[0]
	
	links = tree.xpath('//div[@class="center-stack"]//*/a[@class="name"]/@href')
	
	app = App(name, developer, price, link)
	
	return app
	
    # Do something with the data. We'll just be printing it.
    # We can do some analytics or whatever.
    class App:
      def __init__(self, name, developer, price, links):
	self.name = name
	self.developer = developer
	self.price = price
	self.links = links
	
      def __str__(self):
	return ("Name" + self.name.encode('UTF-8') + "\r\nDeveloper: " + self.developer.encode('UTF-8') + "\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")
	
	
				    
    def main():
      # Execution starts here
      crawler = AppCrawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8', 0)
      crawler.crawl()
      for app in crawler.apps:
	print app
		    
    if __name__ == "__main__": main()

Further improvements to our crawler would be to remove duplicates (which is pretty easy). Add multi-threading support. Make a generic purpose crawler/scraper and so on. Hope you can take some information from this post to adapt it in how you can implement your own crawler for your own needs. 

Also, to crawl much larger amounts data in an efficient and systematic way there are a few libraries and modules for help. One of them is Beautiful Soup. This allows you to transverse the trees easily, use _children_, _parent_, _decendents_ like functions e.t.c. That would avoid writing xpath code. Another framework that you might be interested is Scrapy. It's a very robust scraper for production level usecases.