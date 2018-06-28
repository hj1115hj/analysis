# urlencode test

from urllib.parse import urlencode
from urllib import parse

'''
urlencode
-- urlencode : dict,리스트안에 튜플을파 일을 ulr로 인코딩해준다.
   urllib.parse 안에있음

quote(), unquote()
-- 간단히 문자열만 인코딩 또는 디코딩 한는경우


quote_plus ()
--url에 한글로 검색어를 요청하기 위해서는 반드시 quote_plus 함수를 사용해야 합니다.
그리고 quote_plus함수 말고 quote라는 기본적인 함수도 있는데 이 함수와 quote_plus 함수의 차이점은 quote_plus는 공뱃을 + 
기호로 처리하고 quote 함수는 공백을 %20으로 인코딩합니다.
quote_plus가 권장하는 함수이지만, quote를 써도 검색이 제대로 되니까 무엇을 사용하든 상관없습니다.

'''


params = {'username': '한글' ,'password':1234}
encode1 = urlencode(params)
encode2 = urlencode(params,encoding='UTF-8', doseq=True)
print(encode1)
print(encode2)

print(parse.quote('한글'))  # %ED%95%9C%EA%B8%80
print(parse.unquote('%ED%95%9C%EA%B8%80'))  # 한글


print(parse.quote_plus("한글") )
print(parse.unquote('%ED%95%9C%EA%B8%80'))


