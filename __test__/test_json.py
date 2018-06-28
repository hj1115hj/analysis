#test json

import sys
from urllib.request import Request, urlopen  #모듈 가져오기
from datetime import *
import json
#
#\ url = 'http://www.naver.com'
#request = Request(url)    #리퀘스트 객체 생성

try:
    url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
    request = Request(url)
    resp = urlopen(request) #응답 받기
    resp_body = resp.read().decode("utf-8")            #응답 읽기 (바디 내용)  - 바이트로 통신    인코딩 했으면 디코딩도 해야함


    print(type(resp_body),":")
    json_result = json.loads(resp_body)
    print(type(json_result),":",json_result)

    data= json_result['data']
    print(type(data), ":",data) #안드로이드 방식과 똑같음


except Exception as e:
    print('%s %s' % (e, datetime.now()), file = sys.stderr)