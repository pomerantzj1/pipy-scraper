
keywords: jewishnamelist.txt create_name_list.py
	python create_name_list.py < jewishnamelist.txt > keywords.txt

#queue: make_queue.py
#	cat queue.txt
#	python make_queue.py
	
queue:
	python create_list.py < queue.txt > account_list.txt
	
scrape:
	python scrape_followers.py < queue.txt
	
jews:
	make queue
	python scrape_followers.py