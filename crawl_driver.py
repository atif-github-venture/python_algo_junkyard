import beautifulsoup4

def crawl_urls(url_list, crawled_urls, driver, url):
    """ get a set of urls and crawl each url recursively"""

    # Once the url is parsed, add it to crawled url list
    crawled_urls.append(url)

    driver.get(url)
    html = driver.page_source.encode("utf-8")

    soup = BeautifulSoup(html)

    urls = soup.findAll("a")

    # Even if the url is not part of the same domain, it is still collected
    # But those urls not in the same domain are not parsed
    for a in urls:
        if (a.get("href")) and (a.get("href") not in url_list):
            url_list.append(a.get("href"))

    # Recursively parse each url within same domain
    for page in set(url_list):  # set to remove duplicates

        # Check if the url belong to the same domain
        # And if this url is already parsed ignore it
        if (urlparse(page).netloc == domain) and (page not in crawled_urls):

            # print this_url
            crawl_urls(url_list, crawled_urls, driver, page)

    # Once all urls are crawled return the list to calling function
    else:
        return crawled_urls, url_list