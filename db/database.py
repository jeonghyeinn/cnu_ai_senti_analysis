from pymongo import MongoClient

# 회원
# - 회원가입(Create)
# - 회원 목록(Read)
# - 회원 수정(Update)
# - 회원 삭제(Delete)

# 상품
# - 상품 등록(Create)
# - 상품 목록(Read)
# - 상품 수정(Update)
# - 상품 삭제(Delete)

# 게시판
# - 게시글 등록(Create)
# - 게시글 목록(Read)
# - 게시글 수정(Update)
# - 게시글 삭제(Delete)

# -> CRUD 작업  DAO(Data Acess Object) 만듦
# 게시글 -> BoardDAO.py  (한 곳에 코드를 다 넣으면 가독성도 떨어지고, 복잡하므로 나누는 것임)
# 회원 -> MemberDAO.py


# 1. Connection 작업(공통 : Common)
def db_conn():
    client = MongoClient('127.0.0.1', 27017)  # MongoDB 찾아감
    db = client['movie']                      # Database 선택
    collection = db.get_collection('review')  # Collection 선택
    return collection


# 2. Review 저장(Create)
def create_review(data):
    collection = db_conn()  # MongoDB Connection
    collection.insert_one(data)


# 3. Review 조회(Read)
def read_review():
    collection = db_conn()  # MongoDB Connection
