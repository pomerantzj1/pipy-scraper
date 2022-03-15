import sys

sys.stdin.readline()
sys.stdin.readline()

keyword = sys.stdin.readline()
keywords = []
while keyword != '':
    keywords.append(keyword.strip('\n').lower())
    keyword = sys.stdin.readline()

sys.stdout.write(str(keywords))