#!/usr/bin/env python
#-*- coding: utf-8 -*-

from crawler import cgbchina_crawler

cgbchina_url = "http://card.cgbchina.com.cn/Channel/11820301"
cgbchina_Crawler = cgbchina_crawler()
print cgbchina_Crawler.cgbchina(cgbchina_url)

	