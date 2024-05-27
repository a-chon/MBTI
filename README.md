<<<<<<< HEAD
# 作成したPyPI名
MBTI-dictionary

このmbti-dictionaryパッケージでは、人の名前とMBTIを登録し、MBTIごとに相性のいい相手を列挙するプログラムを作成した。

# インストール方法
$ pip install MBTI-dictionary==0.0.1

# 実行例
ユーザー登録の例
print(register_user('John', 'INTJ'))
->{'message': 'User registered successfully'}

ユーザー情報の取得の例
print(get_user(1))
->{'name': 'John', 'mbti': 'INTJ'}
    
相性データの取得の例
print(get_compatibility_data())
->{'INTJ': {'best_match': 'ESFJ', 'users': ['John', 'John']}, 'INTP': {'best_match': 'ESFP', 'users': []}, 'ENTJ': {'best_match': 'ISFJ', 'users': []}, 'ENTP': {'best_match': 'ISFP', 'users': []}, 'INFJ': {'best_match': 'ESTJ', 'users': []}, 'ENFJ': {'best_match': 'ISTJ', 'users': []}, 'INFP': {'best_match': 'ESTP', 'users': []}, 'ENFP': {'best_match': 'ISTP', 'users': []}, 'ISTJ': {'best_match': 'ENFJ', 'users': []}, 'ISFJ': {'best_match': 'ENTJ', 'users': []}, 'ESTJ': {'best_match': 'INFJ', 'users': []}, 'ESFJ': {'best_match': 'INTJ', 'users': []}, 'ESTP': {'best_match': 'INFP', 'users': []}, 'ISTP': {'best_match': 'ENFP', 'users': []}, 'ISFP': {'best_match': 'ENTP', 'users': []}, 'ESFP': {'best_match': 'INTP', 'users': []}}


# 新規性や有用性
MBTIが人気だが、人のMBTIを聞いてもイマイチ覚えられなかったりする。なのでMBTIを登録できるDictionary機能をつけた。かつ、MBTIごとに相性の良いMBTIがあるので、それぞれのMBTIで相性のいいMBTIに登録された人物を列挙してjson形式で返すプログラムを作成した。
MBTIは個人の性格を理解するためのツールとして広く知られているが、その情報を整理して提供するアプリはまだ多くない。このプログラムは、MBTIに基づいてユーザーの情報を管理し、相性に関するデータを提供することで、MBTIの理解を促進する一助となる。
ユーザーは自分のタイプと相性に関するデータを見ることで、自己理解や他者理解を深めることができる。また、他のユーザーのタイプと相性に関する情報を見ることで、新しい洞察を得ることも可能である。
