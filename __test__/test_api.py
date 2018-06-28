from analysis_fb.collect.api import api


'''
url = api.fb_gen_url(node='jtbcnews', a=10, b=10, s='kickscar')

print(url)
'''


'''
id = api.fb_name_to_id("jtbcnews")
print(id)

'''

'''

url =api.fb_fetch_success_url('jtbcnews', '2010-01-01','2017-12-31')

print(url)
'''

ACCESS_TOKEN = "EAACEdEose0cBAFDwwaXJ8otTKpIj1c2o87NyScQDKP2vmLZCFq1oeALJgRi6EdmXpax0ux1S64TZCQog6Gr2mWrqsBBUGirCO3zXaHTZBCOauhWA9IyoP8GyNU8VhVHwsdwk0zQASh169VGPamypeYfyZBx4iZCeZCtTDDrXEVZBF7pYj91lqIIdkOw8aa1cCBLjQoM7zDk1AZDZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"
pagename ='jtbcnews'
url = api.fb_gen_url(
    node=api.fb_name_to_id(pagename) + "/posts",
    fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
    since='2017-01-01',
    until='2017-12-31',
    limit=50,
    access_token=ACCESS_TOKEN)


for posts in api.fb_fetch_posts('jtbcnews', '2010-01-01','2017-12-31'):
    print(posts)

