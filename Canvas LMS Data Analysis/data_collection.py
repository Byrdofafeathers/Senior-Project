"""
Created on Mon. October 16 2:18:00 2017 

Used to call Canvas API for quick and easy data collection 

@author: ByrdOfAFeather

"""
import requests 
import json 

class Collector:
	def __init__(self, url=None, header=None):
		self.header = header
		self.url = url

	def get_quiz(self, course_id, quiz_id, output_file_name='quiztest.json'):
		'''Grabs quiz data specified'''
		r = requests.put(
			'{}/api/v1/courses/{}/quizzes/{}/statistics'.format(self.url, course_id, quiz_id),
			headers=self.header)

		with open('{}'.format(output_file_name), 'w') as f:
			json.dump(r.json(), f)
	
		return r.json()

	def get_discussion(self, course_id, discussion_id, output_file_name='discussiontest.json'):
		'''Grabs discussion data specified'''
		r = requests.put(
			'{}/api/v1/courses/{}/discussion_topics/602154/view'.format(self.url, course_id, discussion_id),
			 headers=self.header)

		with open('{}'.format(output_file_name), 'w') as f:
			json.dump(r.json(), f)

		return r.json()