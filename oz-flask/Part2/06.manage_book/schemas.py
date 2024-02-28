## marshmallow를 사용하여 데이터의 직렬화 및 역직렬화를 담당하는 스키마를 정의

# 필요한 모듈 import
from marshmallow import Schema, fields

#Schema를 상속하여 BookSchema 정의
class BookSchema(Schema): 
    
    # 필드 정의
    id = fields.Int(dump_only=True) # 역직렬화 시에만 사용, 직렬화 시에는 무시됨
    title = fields.String(required=True)
    author = fields.String(required=True)
    