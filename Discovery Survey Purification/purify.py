import pandas as pd 
import matplotlib.pyplot as plt 

taught_class = 'Who taught this Class?.1'
taught_class_2 = 'Who taught this Class?'

least_fav_class = 'Least Favorite Class (any High School course you\'ve taken)'
fav_class = 'Favorite Class (any High School course you\'ve taken)'

classes = {
	'Pre': 'Math', 
	'Math': 'Math', 
	'AP World ': 'AP World', 
	'World History': 'World',
	'Earth': 'Science', 
	'Science': 'Science', 
	'English': 'English', 
	'Chemistry': 'Science', 
	'NC': 'Science', 
	'Physics': 'Science', 
	'AP Psych': 'AP Psych', 
	'Civics': 'Civics',
	'Spanish': 'Spanish',
	'writing': 'Creative Writing',
	'Physical Education': 'P/E',
	'Band': 'Band',
	'Drama': 'Theatre Arts',
	'Theatre Arts': 'Theatre Arts',
	'Psychology': 'Psychology',
	'Chorus': 'Chorus',
	'Theater': 'Theatre Arts',
	'PE': 'P/E'
}
teacher_list = ['Barham', 'Wilson', 'Walker', 'Scronce', 'Sigmon', 'Cochrane', 'Ramsuer', 'Dixon', 'Alison', 'Crosson', 'Britain', 'Henze', 'Ward', 'Wilkinson', 'Bozza', 'Williams', 'Smith', 'Amerto', 'Adams', 'Poff']
incorrect_dict = {'Ramseur': 'Ramsuer', 'Cochran': 'Cochrane', 'Schou': 'Schouweiler'}

survey = pd.DataFrame.from_csv('Class Evaluation.csv')

def replace(name, frame, section):
	list_of_replace = [i for i in frame[section] if name.lower() in str(i).lower()]
	for alterations in list_of_replace:
		frame = frame.replace(alterations, name)
	return frame


def misspelling(incorrect, correct, frame, section):
	list_of_replace = [i for i in frame[section] if incorrect.lower() in str(i).lower()]
	for alterations in list_of_replace:
		frame = frame.replace(alterations, correct)
	return frame

for replacements in teacher_list:
	survey = replace(replacements, survey, taught_class)
	survey = replace(replacements, survey, taught_class_2)

for misspellings, correctspellings in incorrect_dict.items():
	survey = misspelling(misspellings, correctspellings, survey, taught_class)
	survey = misspelling(misspellings, correctspellings, survey, taught_class_2)

for misspellings, correctspellings in classes.items():
	survey = misspelling(misspellings, correctspellings, survey, least_fav_class)
	survey = misspelling(misspellings, correctspellings, survey, fav_class)


print(survey['Who taught this Class?.1'].unique())
print(survey['Who taught this Class?'].unique())
print(survey['Least Favorite Class (any High School course you\'ve taken)'].unique())
print(survey['Favorite Class (any High School course you\'ve taken)'].unique())
survey.to_csv('Purified.csv')

