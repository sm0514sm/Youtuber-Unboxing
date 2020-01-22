import requests

KEY = 'AIzaSyBHj4k3pWjk6Jgf0CFBnFMIWsciKQVYjQQ'
channelID = 'UCUpJs89fSBXNolQGOYKn0YQ'
URL = 'https://www.googleapis.com/youtube/v3/guideCategories?key={}&part=snippet&id={}'.format(KEY, channelID)
# response = requests.get(URL).text

listID = 'PLHqqPM2t7weIMhLb_1_xa7qyPOKW8OCiq'
playlistURL = 'https://www.googleapis.com/youtube/v3/playlistItems?key={}&playlistId={}&part=contentDetails'.format(KEY, listID)
response = requests.get(playlistURL).text

print(response)