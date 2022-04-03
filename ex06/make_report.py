import json
import sys

import requests as requests

from analytics import Research
from config import *
import logging


def main(args):
	logging.basicConfig(filename='report.log', format='%(asctime)s %(message)s', encoding='utf-8', level=logging.DEBUG)
	if len(args) != 2:
		raise AttributeError("Usage: python3 first_constructor.py data.csv")
	reader = Research(args[1])
	data = reader.file_reader()
	analytics = reader.Analytics(data)
	heads, tails = analytics.counts()
	heads_percent, tails_percent = analytics.fractions(heads, tails)
	next_predict = analytics.predict_random(number_of_observations)
	next_heads, next_tails = reader.Analytics(next_predict).counts()
	report = report_template.format(
		all=heads + tails,
		heads=heads,
		tails=tails,
		heads_percent=heads_percent,
		tails_percent=tails_percent,
		n=number_of_observations,
		next_heads=next_heads,
		next_tails=next_tails
	)
	analytics.save_file(report, report_filename, report_file_extension)


if __name__ == '__main__':
	try:
		main(sys.argv)
		requests.post(webhook, json.dumps(message_success))
	except Exception as e:
		requests.post(webhook, json.dumps(message_fail))
		raise e
