import sys

def filter_names():
    username = input('What is the username of the file that needs to be filtered? ')

    input_file = open('C:/Users/pomer/Documents/Rush/instagram-follower-scraper/nameslists/{}.txt'.format(username), 'r')


    try:
        output_file = open('C:/Users/pomer/Documents/Rush/instagram-follower-scraper/filtered/{}.txt'.format(username), 'x')
        output_file.close()
        output_file = open('C:/Users/pomer/Documents/Rush/instagram-follower-scraper/filtered/{}.txt'.format(username), 'w')
    except FileExistsError:
        resp = input('File appears to exist. Overwrite file "{}.txt"? enter y for yes. '.format(username))
        if resp == 'y':
            output_file = open("C:/Users/pomer/Documents/Rush/instagram-follower-scraper/filtered/{}.txt".format(username), "w")
            output_file.write('Filtered Followers:\n\n')
        else:
            print('Error')
            return
    print('Opened /nameslists/{}.txt'.format(username))
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