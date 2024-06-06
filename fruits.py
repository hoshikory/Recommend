import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from difflib import SequenceMatcher

# 果物リスト
fruits = ["りんご", "バナナ", "オレンジ", "ぶどう", "いちご", "メロン", "パイナップル",
          "さくらんぼ", "キウイ", "レモン", "マンゴー", "スイカ", "グレープフルーツ", "ラズベリー",
          "ブルーベリー", "パッションフルーツ", "モモ", "アボカド", "パパイヤ", "ゴーヤ", 
          "ピーチ", "プラム", "ライチ", "クランベリー", "ハチミツメロン", "スターフルーツ",
          "ホワイトグレープ", "マンゴスチン", "ネクタリン", "シャインマスカット", "ブラックベリー",
          "キウイゴールド", "ブラッドオレンジ", "グアバ", "フィッジー", "サポテ", "キンカン",
          "ドラゴンフルーツ", "イチジク"]

def calculate_similarity(input_fruit):
    """
    入力された果物と果物リスト内の各果物の類似度を計算する関数
    """
    similarities = {}
    for fruit in fruits:
        similarity = SequenceMatcher(None, input_fruit, fruit).ratio()
        similarities[fruit] = similarity
    # 類似度が高い順にソート
    similarities = dict(sorted(similarities.items(), key=lambda item: item[1], reverse=True))
    return similarities

def plot_similarity(similarities):
    """
    類似度をグラフで表示する関数
    """
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(similarities)), list(similarities.values()), align='center')
    plt.yticks(range(len(similarities)), list(similarities.keys()))
    plt.xlabel('類似度')
    plt.title('入力された果物と各果物の類似度')
    plt.gca().invert_yaxis()  # 果物リストを逆順に表示
    
    # MS Gothicフォントを設定
    font_path = "C:/Windows/Fonts/msmincho.ttc"  # MS Minchoフォントのパス
    prop = fm.FontProperties(fname=font_path)
    plt.xticks(fontproperties=prop)
    plt.yticks(fontproperties=prop)

    # テキストエンコーディングをShift-JISに設定
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.family'] = 'MS Mincho'
    plt.rcParams['font.sans-serif'] = ['MS Mincho']

    plt.show()

def main():
    user_input = input("好きな果物を入力してください：")
    similarities = calculate_similarity(user_input)
    
    if similarities:
        # 類似度が高い順にソートされた辞書から1番目と2番目の果物を取得
        top_fruits = list(similarities.keys())[:3]
        # 入力した果物と類似度が一番高い果物が同じ場合、次点と３番手を表示
        if user_input == top_fruits[0]:
            top_fruits = top_fruits[1:3]
        else:
            top_fruits = top_fruits[:2]
        print(f"類似度が高い果物：{top_fruits[0]}（{similarities[top_fruits[0]]:.2f}）, {top_fruits[1]}（{similarities[top_fruits[1]]:.2f}）")
        plot_similarity(similarities)
    else:
        print("類似度が計算できませんでした。")

if __name__ == "__main__":
    main()
