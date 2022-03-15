import sys

def main():
    cont = input('Would you like to queue up a new username? Enter y for yes: ')
    if cont == 'y':
        write = input('Would you like to overwrite the queue? Enter y for yes: ')
        if write == 'y':
            queue_file = open('queue.txt', 'w')
        else:
            queue_file = open('queue.txt', 'a')
    else:
        print('No usernames will be queued.')
        return

    while cont == 'y':
        username = input('What is the username that you would like to add? ')
        queue_file.write(username + '\n')
        cont = input('Would you like to queue up another new username? Enter y for yes: ')

    queue_file.close()
    print('Username queue created.')
    print()

if __name__ == '__main__':
    main()