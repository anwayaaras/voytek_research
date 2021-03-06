import pandas as pd
import os
import re
import random
import urllib2
from time import sleep
from collections import namedtuple

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def some_func():
    entrez_ids = []
    strs = ["http://www.genecards.org/Search/Keyword?startPage=0&queryString=","D2", "&pageSize=", str(-1)]
    search_url = ''.join(strs)
    driver = webdriver.PhantomJS()
    driver.get(search_url)
    print (search_url)
    try:
        # Waits for DOM to render the search results table before accessing elements.
        check = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchResults")))
    finally:
        search_table = driver.find_element_by_id("searchResults")

    top_genes = search_table.find_elements_by_class_name("gc-gene-symbol")
    gene_urls = []
    for gene in top_genes:
        el = gene.find_element_by_tag_name("a")
        gene_urls.append(el.get_attribute("href"))

    for gene_url in gene_urls:
        driver.get(gene_url)
        try:
            # Waits for DOM to render the page table before accessing elements.
            check = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "gc-subsection")))
        finally:
            summaries = driver.find_elements_by_xpath('//*[@id="_summaries"]/div/ul/li/p')

        #import pdb;pdb.set_trace()
        
        print (summaries[0].text)

    driver.close()

    return entrez_ids

print some_func()
