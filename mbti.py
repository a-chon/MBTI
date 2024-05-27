from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mbti = Column(String)

class MBTIDescription(Base):
    __tablename__ = 'mbti_descriptions'
    mbti = Column(String, primary_key=True)
    description = Column(String)

compatibility = {
    'INTJ': 'ESFJ',
    'INTP': 'ESFP',
    'ENTJ': 'ISFJ',
    'ENTP': 'ISFP',
    'INFJ': 'ESTJ',
    'ENFJ': 'ISTJ',
    'INFP': 'ESTP',
    'INFP': 'ESTP',
    'ENFP': 'ISTP',
    'ISTJ': 'ENFJ',
    'ISFJ': 'ENTJ',
    'ESTJ': 'INFJ',
    'ESFJ': 'INTJ',
    'ESTP': 'INFP',
    'ISTP': 'ENFP',
    'ISFP': 'ENTP',
    'ESFP': 'INTP'
}

engine = create_engine('sqlite:///mbti_app.db')

# データベースが存在しない場合は作成し、テーブルも作成する
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def register_user(name, mbti):
    new_user = User(name=name, mbti=mbti)
    session.add(new_user)
    session.commit()
    return {'message': 'User registered successfully'}

def get_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        mbti_description = session.query(MBTIDescription).filter_by(mbti=user.mbti).first()
        return {'name': user.name, 'mbti': user.mbti}
    return {'message': 'User not found'}

def get_compatibility_data():
    data = {}
    for mbti_type, best_match in compatibility.items():
        users = session.query(User).filter_by(mbti=mbti_type).all()
        data[mbti_type] = {'best_match': best_match, 'users': [user.name for user in users]}
    return data

# エントリーポイントとして直接呼び出す場合は、以下のようにします
if __name__ == '__main__':
    # ユーザー登録の例
    print(register_user('John', 'INTJ'))
    
    # ユーザー情報の取得の例
    print(get_user(1))
    
    # 相性データの取得の例
    print(get_compatibility_data())
