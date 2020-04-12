import pandas as pd
df = pd.read_csv('vgsales.csv')
df.shape  
df
df.values
df.describe()



#kaggle.com , read pandas documentations

# /music-csv
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
# music_data = pd.read_csv('music.csv')

# music_data
# prepareing / cleaning data
# X = music_data.drop(columns = ['genre'])
# y = music_data['genre']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model = DecisionTreeClassifier()
# # model.fit(X_train, y_train)
# model.fit(X, y)
# music_data
# predictions = model.predict([ [21, 1], [22, 0]])
# predictions
# mesure accuracy of model
model = joblib.load('music-recommender.joblib')
# joblib.dump(model, 'music-recommender.joblib')
#  predictions = model.predict([ [21, 1], [22, 0] ])
predictions = model.predict([[21, 1]])
# predictions = model.predict(X_test)
predictions
# score = accuracy_score(y_test, predictions)
# score

# Persisting model
