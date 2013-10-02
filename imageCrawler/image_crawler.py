import urllib,urllib2
import base64
import json as m_json

def request( query_string ):
	query_string = query_string.replace( ' ', '%20' )
	response = urllib2.urlopen( 'https://ajax.googleapis.com/ajax/services/search/images?'+'v=1.0&q='+query_string ).read()
	json = m_json.loads( response )
	results = json[ 'responseData' ][ 'results' ]
	processed_results = {}
	for result in results:
		title = result['title']
		url = base64.b64encode(urllib.urlopen(result['url']).read())
		if url:
			processed_results[title]=url
	return processed_results