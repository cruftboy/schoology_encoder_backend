from flask import Flask, request, Response
import json
import os
import sys

app = Flask(__name__)



@app.route('/encode', methods=['POST'])
def encode():

	with open('codes.json','r') as j:
		codes = json.load(j)

	form = request.form.to_dict()
	print(form)
	sys.stdout.flush()
	text = form.get('text')

	print(text)

	codes['=['+str(len(codes))+']='] = text

	with open('codes.json','w') as j:
		print(codes)
		sys.stdout.flush()
		json.dump(codes,j)

	resp = Response('=['+str(len(codes)-1)+']=')
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

@app.route('/decode', methods=['POST'])
def decode():
	with open('codes.json','r') as j:
		codes = json.load(j)
	with open('whitelist.txt','r') as t:
		names = t.read()

	form = request.form.to_dict()
	print(form)
	sys.stdout.flush()
	user = form.get('user')
	text = codes.get(form.get('text'))

	if(user not in names):
		text = 'you do not have permission to use this extention'

	resp = Response(text)
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

port = int(os.environ.get('PORT',5000))
app.run(host='0.0.0.0', port = port)