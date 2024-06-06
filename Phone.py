import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 商品のリスト
products = [
    "Apple iPhone 13",
    "Samsung Galaxy S21",
    "Google Pixel 6",
    "Sony Xperia 1 III",
    "Huawei P50 Pro"
]

# TF-IDFベクトルの生成
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(products)

# 入力データの取得
input_data = input("Enter product description: ")

# 入力データのベクトル化
input_vector = vectorizer.transform([input_data])

# コサイン類似度の計算
cosine_similarities = cosine_similarity(input_vector, tfidf_matrix).flatten()

# 最も類似度の高い商品のインデックスを取得
highest_index = np.argmax(cosine_similarities)

# 結果の表示
print(f"Most similar product: {products[highest_index]} (Similarity: {cosine_similarities[highest_index]})")

# ベクトルの視覚化
def visualize_vectors(tfidf_matrix, input_vector, products):
    # PCAを使って2次元に次元削減
    pca = PCA(n_components=2)
    tfidf_matrix_2d = pca.fit_transform(tfidf_matrix.toarray())
    input_vector_2d = pca.transform(input_vector.toarray())

    # プロット
    plt.figure(figsize=(10, 7))

    # 商品ベクトルのプロット
    for i, product in enumerate(products):
        plt.arrow(0, 0, tfidf_matrix_2d[i, 0], tfidf_matrix_2d[i, 1], head_width=0.05, head_length=0.1, fc='blue', ec='blue')
        plt.text(tfidf_matrix_2d[i, 0], tfidf_matrix_2d[i, 1], product, fontsize=9)

    # 入力ベクトルのプロット
    plt.arrow(0, 0, input_vector_2d[0, 0], input_vector_2d[0, 1], head_width=0.05, head_length=0.1, fc='red', ec='red')
    plt.text(input_vector_2d[0, 0], input_vector_2d[0, 1], 'Input', fontsize=9, color='red')

    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.title('Product Descriptions in 2D Space')
    plt.grid()
    plt.show()

# ベクトルの視覚化関数を呼び出し
visualize_vectors(tfidf_matrix, input_vector, products)
