# -*- coding: utf8 -*-
# -*- coding: utf-8 -*-

import sys
from thread import threaded_crawler
from cache import MongoCache
from alexa_cb import AlexaCallback


def main(max_threads):
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    #cache.clear()
    threaded_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache, max_threads=max_threads, timeout=10)


if __name__ == '__main__':
    max_threads = int(sys.argv[1])
    main(max_threads)