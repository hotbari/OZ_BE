from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination

'''
# is_staff인 경우만 접근 가능
from rest_framework.permissions import BasePermission

class IsStaffOrReadOnly(BasePermission):
    """
    Staff인 경우에만 수정 가능하도록 허용하고, 그 외에는 읽기 전용으로 설정
    """
    def has_permission(self, request, view):
        # Staff인 경우에만 POST, PUT, DELETE 요청을 허용
        return request.user.is_staff
'''
    
    
    

# 등록완료 상태인 도서 리스트 불러오기
class Books(generics.ListAPIView):
    queryset = Book.objects.filter(is_exposed=True)
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
    

# 전체 도서 리스트 불러오기
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
    # permission_classes = [IsStaffOrReadOnly]


# 신규 도서 생성하기
class BookCreate(generics.CreateAPIView):
    serializer_class = BookSerializer
    # permission_classes = [IsStaffOrReadOnly]  # 인증된 사용자만 접근 가능하도록 권한 설정

    def perform_create(self, serializer):
        # 새로운 도서가 생성될 때 유저의 권한을 확인
        serializer.save(user=self.request.user)  # 새로운 도서의 작성자로 현재 유저를 지정


# 개별 도서 리스트 관리 및 개별 도서 정보 수정하기
class BookDetail(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsStaffOrReadOnly]

    def handle_exception(self, exc):
        if isinstance(exc, NotFound):
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)

'''
# 등록완료 상태인 도서 리스트 불러오기
class Books(APIView):
    
    def get(self, request):
        books_exposed = Book.objects.filter(is_exposed=True)
        serializer = BookSerializer(books_exposed, many=True)

        return Response(serializer.data)
    

# 전체 도서 리스트 관리
class BookList(APIView):
    
    # 전체 도서 리스트 불러오기
    def get(self, request):
        books_all = Book.objects.all()
        serializer = BookSerializer(books_all, many=True)

        return Response(serializer.data)
    
    # 신규 도서 생성
    def post(self, request):
        user_data = request.data
        serializer = BookSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# 개별 도서 리스트 관리
class BookDetail(APIView):
    
    # 개별 도서 정보 불러오기
    def get(self, request, pk):
        try :
            book_obj = Book.objects.get(pk=pk)

        except Book.DoesNotExist:
            raise NotFound
        
        serializer = BookSerializer(book_obj)
        return Response(serializer.data)

    # 개별 도서 정보 수정하기
    def put(self, request, pk):
        book_obj = Book.objects.get(pk=pk)
        user_data = request.data

        serializer = BookSerializer(book_obj, user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
'''


