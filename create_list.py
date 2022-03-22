import sys


account = sys.stdin.readline()
queue = []
while account != '':
    queue.append(account.strip('\n').lower())
    account = sys.stdin.readline()

sys.stdout.write(str(queue))