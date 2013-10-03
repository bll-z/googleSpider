import urllib,urllib2
import base64
import json as m_json

# requests images from google based on a query_string
# returns dicktionary of title -> base64 string of the image
def request( query_string ):
	# escape the spaces
	query_string = query_string.replace( ' ', '%20' )
	# fetch the response
	response = urllib2.urlopen( 'https://ajax.googleapis.com/ajax/services/search/images?'+'v=1.0&q='+query_string ).read()
	# process the resulting json object
	json = m_json.loads( response )
	try:
		results = json[ 'responseData' ][ 'results' ]
	except TypeError:
		results = []
	processed_results = {}
	for result in results:
		title = result['title']
		url = base64.b64encode(urllib.urlopen(result['url']).read())
		if url:
			processed_results[title]=url
	return processed_results