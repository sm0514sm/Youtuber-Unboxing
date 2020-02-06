import json
from pprint import pprint
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

with open('youtube_video.json', encoding='UTF-8-sig') as fs:
    videos = json.load(fs)

movies = {k:{'view_count':0,'like_count':0,'dislike_count':0,'comment_count':0} for k in range(1, 208)}

for video in videos:
    idx = video['fields']['movie']
    movies[idx]['view_count'] += video['fields']['view_count']
    movies[idx]['like_count'] += video['fields']['like_count']
    movies[idx]['dislike_count'] += video['fields']['dislike_count']
    movies[idx]['comment_count'] += video['fields']['comment_count']

df = pd.DataFrame.from_dict(movies, orient='index')
x = df.values
X = StandardScaler().fit_transform(x)
pca = PCA(n_components=2)
principalComp = pca.fit_transform(X)
pc = pd.DataFrame(data = principalComp, columns = ['pc1'])

with open('movie_data.json', encoding='UTF-8-sig') as fs:
    movies = json.load(fs)

for idx, movie in enumerate(movies):
    movies[idx]['fields']['youtube_score'] = pc['pc1'][idx]

with open('youtube_video_test2.json', "w", encoding='UTF-8-sig') as fs:
    fs.write(json.dumps(movies, ensure_ascii=False))
