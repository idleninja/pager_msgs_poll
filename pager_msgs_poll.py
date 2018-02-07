#!/usr/bin/env python2.7

# Produced by Brett Gross
# This script was created to scrape and produce a log
# from the website "pokesags.goduckyourself.org" as it
# was being used to log unencrypted pager messages.
#
# This was affecting UW medical pagers and was suspected
# that a local medical facility may also be affected. No confirmation
# could be made. And the site was taken offline within the day.

import dryscrape
from bs4 import BeautifulSoup
from time import sleep


def main():
        local_proxy_name = ""
        local_proxy_port = "8080"
	sess = dryscrape.Session(base_url="https://pokesags.goduckyourself.org")
	sess.set_proxy(local_proxy_name, local_proxy_port)

	while True:
		sess.visit("/")
		sleep(1)
		resp = sess.body().split("\r\n")

		outfile = open("pager_msgs.txt", "a")
		outfile.writelines("\n".join(resp))
		outfile.close()
		sleep(5)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt):
        print("^C")
        exit()
