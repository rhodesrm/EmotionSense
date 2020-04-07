import config
import requests
import json
import operator
import urllib

# Set Up Azure API Connection:
KEY = config.faceApiKey
face_api_url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?'
# file url of face to examine goes here: 
image_url = 'https://manofmany.com/wp-content/uploads/2020/02/How-to-make-yourself-stop-being-angry-in-60seconds.jpg'
# add key to headers to get authorization
headers = {'Ocp-Apim-Subscription-Key': KEY}
# only return emotion attribute in response
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
}

# make POST request and store response in response variable
response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})

# extract json information until left with dictionary of emotions with corresponding values
data = response.json()
faceEmotion = data[0]['faceAttributes']
emotionDict = faceEmotion['emotion']

# get the emotion with the maximum value and store in clearestEmotion variable
clearestEmotion = max(emotionDict.items(), key=operator.itemgetter(1))[0]


# Set Up GIPHY API connection
giphyKey = config.giphyApiKey
giphySearchEndpoint = 'api.giphy.com/v1/gifs/search'
data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=" + clearestEmotion + "&api_key=giphyKey&limit=15").read())

