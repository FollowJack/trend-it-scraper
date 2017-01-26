#!/usr/bin/env bash
# Start scrapping
echo "Start - scrapping"
scrapy runspider src/scraper_heise.py -t csv -o resources/data/articles/heise_articles.csv
echo "End   - scrapping"