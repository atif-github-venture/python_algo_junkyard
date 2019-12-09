import requests
from lxml import html


URL_PATTERN = "http://www.wiseowl.co.uk/videos/default-{}.htm"

with requests.Session() as session:
    page_number = 1
    while True:
        response = session.get(URL_PATTERN.format(page_number))
        if response.status_code == 404:  # break once the page is not found
            break

        print("Processing page number {}..".format(page_number))

        tree = html.fromstring(response.text)
        for video_link in tree.xpath('//p[@class="woVideoListDefaultSeriesTitle"]//a'):
            title = video_link.text
            link = video_link.attrib['href']
            print(title, link)
        page_number += 1