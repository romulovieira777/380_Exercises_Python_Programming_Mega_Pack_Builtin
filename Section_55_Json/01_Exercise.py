"""
Exercise No. 01

The following object is given:

    employees_json = '''
    {"IT": [{"employee_id": "0010", "stack": ["Python", "Java", "AWS", "Docker", "Linux"], "experience": 5},
    {"employee_id": "0360", "stack": ["Python", "AWS", "Docker", "Linux", "Azure"], "experience": 6},
    {"employee_id": "0323", "stack": ["Python", "AWS", "JavaScript"]}],
    "Marketing": [{"employee_id": "0863", "stack": ["Google Analytics", "Google Ads", "Facebook Ads"]},
    {"employee_id": "0543", "stack": ["Google Ads", "Facebook Ads"]}]}
    '''

Using the built-in json module load the above text into the dictionary named employees.

In response, print the contents of the employees dictionary to the console.

Expected result:
    {'IT': [{'employee_id': '0010', 'stack': ['Python', 'Java', 'AWS', 'Docker', 'Linux'], 'experience': 5},
    {'employee_id': '0360', 'stack': ['Python', 'AWS', 'Docker', 'Linux', 'Azure'], 'experience': 6},
    {'employee_id': '0323', 'stack': ['Python', 'AWS', 'JavaScript']}], 'Marketing': [
    {'employee_id': '0863', 'stack': ['Google Analytics', 'Google Ads', 'Facebook Ads']},
    {'employee_id': '0543', 'stack': ['Google Ads', 'Facebook Ads']}]}
"""
import json

employees_json = '''
{"IT": [{"employee_id": "0010", "stack": ["Python", "Java", "AWS", "Docker", "Linux"], "experience": 5},
{"employee_id": "0360", "stack": ["Python", "AWS", "Docker", "Linux", "Azure"], "experience": 6},
{"employee_id": "0323", "stack": ["Python", "AWS", "JavaScript"]}],
"Marketing": [{"employee_id": "0863", "stack": ["Google Analytics", "Google Ads", "Facebook Ads"]},
{"employee_id": "0543", "stack": ["Google Ads", "Facebook Ads"]}]}
'''

employees = json.loads(employees_json)
print(employees)
