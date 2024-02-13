"""
네이버에 근처 맛집 검색
근처 맛집 더보기 클릭
광고를 제외하고 스크롤 내리면서 스크래핑
광고 클래스명 UEzoS rTjJo cZnHG
일반 클래스명 UEzoS rTjJo

상호명 클릭하고 role=main을 리스트로 받아와서 해보자
받아올 데이터 : 
            이미지(store_image) K0PDV _div,
            상호명(store_name) Fc1rA,  
            정체성(store_main) DJJvD,
            새로오픈(store_new) h69bs DjPAB,
            영업상태(store_operate) y6tNq A_cdD
                영업 전 : U7pYf 클래스에서 place_blind 클래스로 시작 시간 보여줌
                영업 중 : U7pYf 클래스에서 place_blind 클래스로 라스트오더 시간 보여줌
                영업 종료:
            리뷰(reviews) PXMot,
            위치(store_location) LDgIH 
            찜해놨던 장소(pressed_store) yxkiA 클래스에서 aria-pressed="false"
"""