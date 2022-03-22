import json, requests

username = input('Enter username: ')
filtered_list = open('C:/Users/pomer/Documents/Rush/pipy-scraper/filtered/{}.txt'.format(username))

output = open('C:/Users/pomer/Documents/Rush/pipy-scraper/withbios/{}.txt'.format(username), 'w')

line = filtered_list.readline()
line = filtered_list.readline()

def main():
    line = filtered_list.readline()
    while line != '':
        data = line.split(':')
        bio = get_bio(data[1].strip())
        line = filtered_list.readline()


def get_bio(follower):
    response = requests.get('https://www.instagram.com/{}/?__a=1'.format(follower))
    print(response)
    dictionary = response.json()
    print(dictionary)
    return dictionary["graphql"]["user"]["biography"]

main()
    
filtered_list.close()
output.close()