#understanding flickr api

#getting nightsky pictures from flickr


import flickrapi
import webbrowser

api_key=<'example_api_key'>
api_secret=<'example_secret_key'>

flickr=flickrapi.FlickrAPI(api_key,api_secret, format='parsed-json')


from pprint import pprint


search=flickr.photos.search(content_type='1', tags='nightsky', per_page='40', page='2')
url='https://flickr.com/photos/'

for i,j in search['photos'].items():
	if i == 'photo':
		photo_list =j
		for k in photo_list:
			webbrowser.open_new_tab(url+k['owner']+'/'+k['id'])

