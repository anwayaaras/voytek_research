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
import pdb


#################################################################################################################################
def convert_to_csv(txt_file,csv_file):
    import csv
    in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
    out_csv = csv.writer(open(csv_file, 'wb'))
    out_csv.writerows(in_txt)

#################################################################################################################################


def scrape_website(gene_name):
    score_threshold= 90
    strs = ["http://www.genecards.org/Search/Keyword?startPage=0&queryString=",gene_name, "&pageSize=", str(-1)]  
    search_url = ''.join(strs)
    driver = webdriver.PhantomJS()
    driver.get(search_url)

    try:
        # Waits for DOM to render the search results table before accessing elements.
        check = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, "searchResults")))
    except:
        return []
    else:
        search_table = driver.find_element_by_id("searchResults")
   
    #MAX_URLS= 5         #Since there might be many hits, taking the top 5 for now
    top_genes = search_table.find_elements_by_class_name("gc-gene-symbol")
    gene_urls = []
    i=1
    for gene in top_genes:

        el = gene.find_element_by_tag_name("a")
        xpath_value='//*[@id="searchResults"]/tbody/tr['+str(i)+']/td[8]'
        score=gene.find_element_by_xpath(xpath_value)
        if float(score.text)> score_threshold:
            gene_urls.append(el.get_attribute("href"))
            #print el.text
        i+=1
        
    print gene_urls 
    #pdb.set_trace()
    

    gene_data=[]
    for gene_url in gene_urls:
        driver.get(gene_url)
        try:
            #check = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "gc-subsection")))
            wait = WebDriverWait(driver, 10)

        finally:
            summaries = driver.find_elements_by_xpath('//*[@id="summaries"]/div/ul/li/p')
            summaries+= driver.find_elements_by_xpath('//*[@id="summaries"]/div/p')
            print summaries
            for summary in summaries:
                gene_data.append(summary.text)

        
    return gene_data

#################################################################################################################################



def scrape_main():
    entrez_genes = open('gene_info_20_genes.csv','r')
    summary_file = open('genecards_scrapped.csv','w')

    for line in entrez_genes:
        line=line.strip()
        line=line.split("\t")
        entrez_id=line[0]
        print "entrez_id",entrez_id
        gene_name=line[1]
        summary=scrape_website(gene_name)
        summary_file.write("\n\n"+entrez_id+"\t"+gene_name+"\t"+str(summary))


#################################################################################################################################
def histogram_from_dict(word_count_dict):
    import pylab as pl
    import numpy as np

    d = word_count_dict
    X = np.arange(len(d))
    pl.bar(X, d.values(), align='center', width=0.5)
    pl.xticks(X, d.keys(), rotation='vertical')
    ymax = max(d.values()) + 1
    pl.ylim(0, ymax)
    pl.show()

#################################################################################################################################


def scrape_top_genes_per_word (word):
    max_genes = 20
    strs = ["http://www.genecards.org/Search/Keyword?startPage=0&queryString=",word, "&pageSize=", str(-1)]  
    search_url = ''.join(strs)
    driver = webdriver.PhantomJS()
    driver.get(search_url)

    try:
        # Waits for DOM to render the search results table before accessing elements.
        check = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchResults")))
    except:
        print "no results: ",word
        return 1
    else:
        search_table = driver.find_element_by_id("searchResults")
   
    #MAX_URLS= 5         #Since there might be many hits, taking the top 5 for now
    top_genes = search_table.find_elements_by_class_name("gc-gene-symbol")
    genes_score = {}
    i=1
    for gene in top_genes:
        el = gene.find_element_by_tag_name("a")
        xpath = """//*[@id="searchResults"]/tbody/tr[""" + str(i) + ']/td[8]'
        score = gene.find_element_by_xpath(xpath)
        genes_score[str(el.text)] = float(score.text)

        i+=1
        if i==max_genes:
            break

    import operator
    genes_score_list = sorted(genes_score.items(), key=operator.itemgetter(1))[::-1]
    #histogram_from_dict(genes_score)
    return genes_score_list

#################################################################################################################################
def get_genes_words( input_file, output_file):
    inputw = open ( input_file , "r")
    output = open(output_file , 'w')
    for word in inputw:
        
        genes = []
        while genes == []:
            genes = scrape_top_genes_per_word(word)
        if genes == 1:
            genes = []
        print word,genes
        output.write(word+"\t"+str(genes)+"\n")

#get_genes_words( "input_neurosynth_terms", "results_neurosynth_words_extract_genes_final")
#convert_to_csv("results_neurosynth_words_extract_genes_final","results_neurosynth_words_extract_genes_final.csv")
print scrape_top_genes_per_word ('prefrontal cortex')




#scrape_main()
#print scrape_website('drd2')       NOT WORKING!!
#print scrape_top_genes_per_word ('alzheimer')


#################################################################################################################################

#################################################################################################################################

#################################################################################################################################

#################################################################################################################################

#################################################################################################################################

