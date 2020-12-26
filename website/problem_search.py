from website import app, db
from website.models import Problem

platforms = ['cf', 'cc', 'ac']
tags = ['dp', 'graphs', 'greedy', 'trees', 'bitmasks']

def tokenize(str):
	return str.split()

def extract_platforms(tokens):
	res = []
	for platform in platforms:
		if platform in tokens:
			res.append(platform)
	return res

def extract_tags(tokens):
	res = []
	for tag in tags:
		if tag in tokens:
			res.append(tag)
	return res

def is_disjoint(a, b):
	return set(a).isdisjoint(b)

def filter_by_tags(res, tags):
	ans = []
	for r in res:
		if not is_disjoint(r.keywords.split(),tags):
			ans.append(r)
	return ans
	#return res.filter(not is_disjoint(keywords,tags))


def find_platform_specific(platform, query_tokens):
	res = Problem.query.filter(Problem.platform == platform)

	if platform == 'cf':
		pass
	elif platform == 'cc':
		pass
	elif platform == 'ac':
		pass
	return res


def find_problems(query):
	query_tokens = tokenize(query)
	platforms = extract_platforms(query_tokens)
	res = []
	for platform in platforms:
		res_plat = find_platform_specific(platform, query_tokens)
		res += res_plat

	tags = extract_tags(query_tokens)
	res = filter_by_tags(res, tags)

	#query_keywords = extract_keywords(query_tokens)
	#res = filter_by_similarity(query_keywords)

	return res
