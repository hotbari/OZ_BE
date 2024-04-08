# 페이지 교체 알고리즘 - 선입선출

class PageReplacementFIFO:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []

    def access_page(self, page):
        if page not in self.pages:
            if len(self.pages) >= self.capacity:
                self.pages.pop(0) # 수용가능 개수보다 많으면 가장 먼저 들어온 것 뺌
            self.pages.append(page)

    
    def status(self):
        print('현재 페이지 상태: ', self.pages)


# 3칸까지 페이지 교체 정책 모델
page_replacement = PageReplacementFIFO(capacity=3)

page_replacement.status()


page_replacement.access_page(3)
page_replacement.status()

page_replacement.access_page(2)
page_replacement.status()

page_replacement.access_page(1)
page_replacement.status()

page_replacement.access_page(4)
page_replacement.status()