import requests, os, random, string, json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'Add in web address for the from post'

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@yahoo.com'
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		'whatIsTheDataFIELDSubmitUsername': username,
		'whatIsTheDataFIELDSubmitPassword': password
	})

	print 'sending username %s and password %s' % (username, password)

#nw, preservce data, ALL, POST, Form Data, (get Request URL in Request method Post )
	
# TODO add .json with multiple user-agents to randomize UA when posting
# TODO first.last name should be reversed list feom names.json
