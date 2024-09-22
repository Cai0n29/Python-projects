from sklearn.feature_extraction.text import TfidfVectorizer

#Dictionary
words = ["hello I'm Lorenzo", 
         "Hi I'm Cat", 
         "What are you doing Loranzo", 
         "Who do you think you are",
         "What you guys up to?"]

#The vectorizer
tfid_vec = TfidfVectorizer()
#Vectorized the words in the dictionary words
vect = tfid_vec.fit_transform(words)
print(tfid_vec.vocabulary_)