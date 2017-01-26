#!/usr/bin/env bash
# Start scrapping
echo "Start - scrapping"
scrapy runspider src/scraper_heise.py -o heise_articles.json
echo "End   - scrapping"