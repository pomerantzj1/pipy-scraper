import sys, os

def filter_names(username, timestamp):
    
    try:
        os.mkdir("C:/Users/pomer/Documents/Rush/pipy-scraper/queues/{}/filtered".format(timestamp))
    except FileExistsError:
        pass

    input_file = open('C:/Users/pomer/Documents/Rush/pipy-scraper/queues/{}/nameslists/{}.txt'.format(timestamp, username), 'r')

    output_file = open('C:/Users/pomer/Documents/Rush/pipy-scraper/queues/{}/filtered/{}.txt'.format(timestamp, username), "w")
    output_file.write('Filtered Followers:\n\n')

    print('Opened queues/{}/nameslists/{}.txt'.format(timestamp, username))
    keyword_file = open('keywords.txt', 'r')
    keywords = eval(keyword_file.read())
    keyword_file.close()
    
    input_file.readline()
    input_file.readline()
    
    data = input_file.readline()
    while data != '':
        for keyword in keywords:
            if keyword in data.lower():
                output_file.write(str(data))
                break
        data = input_file.readline()
        
    input_file.close()
    output_file.close()
    print('Filtered.')
    return 

if __name__ == '__main__':
    filter_names()