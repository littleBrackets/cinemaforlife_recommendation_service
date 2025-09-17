from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class ContentBasedRecommender:
    def __init__(self, movies):
        self.movies = movies
        self.titles = [m.primarytitle for m in movies]
        self.genres = [m.genres or "" for m in movies]
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.genres)

    def recommend(self, title, top_n=5):
        try:
            idx = self.titles.index(title)
        except ValueError:
            return []
        cosine_similarities = linear_kernel(self.tfidf_matrix[idx:idx+1], self.tfidf_matrix).flatten()
        related_indices = cosine_similarities.argsort()[-top_n-1:-1][::-1]
        recommendations = [(self.movies[i].tconst, self.titles[i], cosine_similarities[i]) for i in related_indices]
        return recommendations
