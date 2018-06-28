from analysis_fb.collect.api import web_request as wr

url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'

def success_fetch_userlist(response):
    print(response)


wr.json_request(url=url,
                success=success_fetch_userlist)

def error_fetch_user_list(e) :
    print(e)

wr.json_request(url=url,
                success=success_fetch_userlist,
                error = error_fetch_user_list)


s='''dddd
ddd
ddd
'''
#print(s)


json_result = wr.json_request(url)
print(json_result)
