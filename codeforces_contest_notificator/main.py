import requests


contests = requests.get('http://codeforces.com/api/contest.list').json()
