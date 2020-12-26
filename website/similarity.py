import random
from website import app, db
import jellyfish


def similarity(problem, query):
	return jellyfish.jaro_distance(str(problem.keywords), query)