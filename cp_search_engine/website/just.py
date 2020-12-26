import json
import urllib.request
import requests

def extract_cf():
    urL = "https://codeforces.com/api/problemset.problems?tags=implementation"
    data = {}
    with urllib.request.urlopen(urL) as url:
        data = json.loads(url.read().decode())
	
    problems = data["result"]["problems"]
    lst = []
    for problem in problems:
        problem_link = r"https://codeforces.com/contest/" + str(problem["contestId"]) + r"/problem/" + problem["index"]
        lst.append(problem_link)

    if len(lst) != len(set(lst)):
        print("duplicates exist")
    else:
        print("no duplicates")
        
    
extract_cf()

