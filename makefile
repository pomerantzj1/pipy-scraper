
keywords: jewishnamelist.txt create_name_list.py
	python create_name_list.py < jewishnamelist.txt > keywords.txt

queue: make_queue.py
	cat queue.txt
	python make_queue.py
	
scrape:
	python scrape_followers.py < queue.txt
	
jews: queue