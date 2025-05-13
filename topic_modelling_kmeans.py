
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

# Load dataset
df = pd.read_csv('sample_customer_reviews.csv')

# Text preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = text.split()
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Apply preprocessing
df['Cleaned_Review'] = df['Review'].apply(preprocess_text)

# Convert text to TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Cleaned_Review'])

# Apply K-Means clustering
k = 3  # number of clusters
model = KMeans(n_clusters=k, random_state=42)
model.fit(X)

# Assign clusters to reviews
df['Cluster'] = model.labels_

# Display top terms per cluster using WordCloud
terms = vectorizer.get_feature_names_out()
order_centroids = model.cluster_centers_.argsort()[:, ::-1]

for i in range(k):
    print(f"Cluster {i}:")
    cluster_words = [terms[ind] for ind in order_centroids[i, :10]]
    print("Top words:", cluster_words)
    wordcloud = WordCloud(background_color='white').generate(' '.join(cluster_words))
    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(f"Cluster {i} WordCloud")
    plt.show()
