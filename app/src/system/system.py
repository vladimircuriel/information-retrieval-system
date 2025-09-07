import pandas as pd
import numpy as np

from typing import Any
from scipy.sparse._matrix import spmatrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.utils.utils import query_processing


class InformationRetrievalSystem:
    def __init__(self, df: pd.DataFrame, col: str) -> None:
        self.df: pd.DataFrame = df
        self.col: str = col
        self._get_tfidf_vectors()

    def _get_tfidf_vectors(self) -> None:
        self.vectorizer = TfidfVectorizer()
        self.tfidf_vectors: spmatrix = self.vectorizer.fit_transform(
            raw_documents=self.df[self.col]
        )

    def _get_topn_results(
        self, scores: np.ndarray[Any, Any], topn: int
    ) -> pd.DataFrame:
        df2: pd.DataFrame = self.df.copy()
        df2["score"] = scores

        sorted_indices = scores.argsort()[::-1]
        return df2.iloc[sorted_indices[:topn]][
            ["ID", "Major", "Course Title", "Course Description_Clean", "score"]
        ]

    def search(self, query: str, topn: int = 10) -> pd.DataFrame:
        query = query_processing(query=query)
        if query == "":
            return pd.DataFrame()

        query_vectorized: spmatrix = self.vectorizer.transform(raw_documents=[query])
        scores = cosine_similarity(X=query_vectorized, Y=self.tfidf_vectors).flatten()
        return self._get_topn_results(scores=scores, topn=topn)
