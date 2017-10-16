# http://ceur-ws.org/Vol-1925/paper11.pdf
import requests 
import json
from data_collection import Collector
from secrets import keys

nccs_token = keys[1]
ncvps_token = keys[0]
nccs_url = 'http://nccs.instructure.com'
ncvps_url = 'http://ncvps.instructure.com'
nccs_header = {'Authorization': 'Bearer {}'.format(nccs_token)}
ncvps_header = {'Authorization' : 'Bearer {}'.format(ncvps_token)}

NCVPS_Collector = Collector(url=ncvps_url, header=ncvps_header)
NCCS_Collector = Collector(url=nccs_url, header=nccs_header)


def main():

	NCVPS_Collector.get_discussion(10105, 602154, output_file_name='Calculus Data Mining/test.json')

	with open('Calculus Data Mining/discussion1.json') as discussion1: 
		discussion1 = json.load(discussion1)
	
	participant_dict = {} 
	for participants in discussion1['participants']:
		participant_dict[participants['id']] = participants['display_name']

	participant_posts = []
	for posts in discussion1['view']:
		participant_posts.append({participant_dict[posts['user_id']]:posts['message']})

	print(participant_dict)
	print(participant_posts)	



if __name__=="__main__": main()