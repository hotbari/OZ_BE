# 필요한 모듈 import

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

book_blp = Blueprint('books','books',url_prefix='/books', description='Operations on books')

# 책 객체 저장할 빈 리스트
books = []

## '/books' URL에 대한 라우팅 정의
@book_blp.route('/')

# BookList에 대한 HTTP 요청 처리를 위해 MethodView 클래스 상속
class BookList(MethodView):
    
    # GET에 대한 데코레이터(응답 스키마 설정) : 여러개의 책 객체를 반환하므로 many=True
    @book_blp.response(200, BookSchema(many=True))
    # GET 메소드 처리하는 함수 정의
    def get(self):
        return books
    
    # POST에 대한 데코레이터
    # POST 메소드에 대한 요청 스키마 설정 *클라이언트 전송데이터와 BookSchema가 일치해야함
    @book_blp.arguments(BookSchema)
    # POST 메소드에 대한 응답 스키마
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        new_data['id'] = len(books) + 1
        books.append(new_data)
        return new_data # 새로운 책 객체 반환



## '/<int:book_id>' URL에 대한 라우팅 정의
@book_blp.route('/<int:book_id>')
class Book(MethodView):
    
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next( (book for book in books if book['id']==book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        return book
    
    
    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next( (book for book in books if book['id']==book_id), None)
        if book is None:
            abort(404, message="book not found")
            
        book.update(new_data)
        return book
    
    @book_blp.response(204)
    def delete(self, book_id):
        global books
        book = next( (book for book in books if book['id']==book_id), None)
        if book is None:
            abort(404, message="Book not found.")
            
        books = [book for book in books if book['id'] != book_id]
        return ''