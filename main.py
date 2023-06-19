from fastapi import FastAPI 
import uvicorn
import re 



app = FastAPI()



@app.get('/')
async  def welcome():
    return {'message':'welcome to nexsol chatbot'}


@app.get('/chat')
async def chatbot(text:str):
    pattern1 = r'풍'
    result1 = re.search(pattern1,text)
    if result1:
        return '''행정안전부가 관장하고 민영보험사가 
                  운영하는 정책보험으로서 보험가입자가 
                  부담하여야 하는 보험료의 일부를 국가 및 지자체에서 
                  보조함으로써 국민은 저렴한 보험료로 예기치 못한 풍수해(태풍,홍수,호우,해일,강풍,풍랑,대설,지진)에 대해 스스로 대처할 수
                  있도록 하는 선진국형 재난관리제도입니다.'''
    pattern2 = r'(.*)대(.*)'
    result2 = re.search(pattern2,text)
    if result2 :
        return '''전체 풍수해보험의 대상은 주택(동산) 및 온실(비닐하우스),
                  소상공인 상가 및 공장입니다. 본 상품은 소상공인 대상 상가 및 공장이 가입 대상입니다.'''
    pattern3 = r'(.*) 있'
    result3 = re.search(pattern3,text)
    if result3:
        return '''보험에 가입한 대상시설물이 보험기간 중에 재난기준이상의 태풍, 
                  홍수, 호우, 해일, 강풍, 풍랑, 대설, 지진의 직접적인 결과로 피해를 입었을때 목적물의 손해 및 추가비용(온실의 잔존물 제거비용,
                  손해방지비용)을 약관에 따라 보상합니다.본 상품은 소상공인 상가 및 공장 대상으로 건물, 시설(기계)및 집기시설, 재고자산 등 가입하신 한도 금액 내에서 실제 피해를 보신 금액을 보상해 드립니다.'''
    pattern4 = r'(.*)비(.*)'
    result4 = re.search(pattern4,text)
    if result4:
        return '''소상공인 풍수해보험의 경우 지역별로 차이가 있습니다.
                  서울 OO구 소재 상가의 경우
                  총 보험료 : 140,000원
                  정부 지원 보험료 : 00000원
                  지자체 지원 보험료 : 00000원
                  가입자(신청자) 부담 보험료 : 000000원
                  정확한 보험료는 보험사로 직접 문의해 보셔야 합니다.
                  그러나 이번 OOO 지원 사업으로 선착순으로 무료로 신청하실 수가 있습니다.'''
    pattern5 = r'(.*) 하(.*)'
    result5 = re.search(pattern5,text)
    if result5:
        return '''가입신청하기를 누르시면 간편하게 가입하실 수 있습니다.
                  본 지원사업은 단체 계약으로 보험가입시작일은 당월 말일부터 시작 됩니다..'''
    
@app.get('/trail')
async def trail(user_input):
    lenght = len(user_input)
    return {'lenght_of_input':lenght}
    
if __name__ == '__main__':
    uvicorn.run(app)

