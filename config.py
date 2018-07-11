import os

# configuration
CONFIG = {
    'items':  [
        {'pagename': 'jtbcnews', 'since': '2017-01-01', 'until': '2017-12-31'},
        {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-12-31'}
    ],
    'common': {
        'fetch': True,
        'result_directory': '__results__/crawling',
        'access_token' : "EAACEdEose0cBAMR1FpvZCUN5t1c2hR22wdViGBgzny0xjwRdUzsK75yFNmZAM2ghP7pg80pVZBwFdVc6LfRqrUT9v3yy7kgbZCJV6hppELOHNxUJf7n7yoqpZBJF5oxKT9GxgLSlbvZCMJGOp6rdj6gCZBZA2AvdxqTYrHzQg9NLtJKspivInkIhvr2QWDXCm4bZCSvIXTqt6lQZDZD",
        'base_url_fb_api' : "https://graph.facebook.com/v3.0",
        'fields' : 'id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)'


    }
}


if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])