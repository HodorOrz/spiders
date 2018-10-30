#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urlparse
import scrapy
from l024.items import L0L0Item
import pdb

class DmozSpider(scrapy.Spider):
    name = "rxt"
    # allowed_domains = ["xinli001.com"]
    start_urls = [
        "http://1024.clsmik.pw/pw/thread-htm-fid-3.html"
    ]

    def parse(self, response):
        rootpath = response.xpath('//*[@id="ajaxtable"]//tbody/tr/td[2]/h3/a')
        print "----------------------------------------"
        for it in rootpath:
            item = L0L0Item()
            # pdb.set_trace()
            item['link'] = urlparse.urljoin(response.url,it.xpath('@href').extract_first())
            item['title'] = it.xpath('text()').extract_first()
            if item['title']:

                yield item
            else:
                pass