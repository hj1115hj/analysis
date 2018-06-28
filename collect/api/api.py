# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request


def fb_gen_url(
        base_url_fb_api='',
        node='',
        **params):
    url = '%s/%s/?%s' % (base_url_fb_api, node, urlencode(params))
    return url


def fb_name_to_id(base_url_fb_api='',pagename='',access_token=''):
    url = fb_gen_url(base_url_fb_api=base_url_fb_api,node=pagename, access_token=access_token)
    json_result = json_request(url=url)
    return json_result.get("id")


def fb_fetch_posts(pagename, since, until, access_token='',base_url_fb_api='' , fields=''):
    url = fb_gen_url(
        base_url_fb_api= base_url_fb_api,
        node=fb_name_to_id(base_url_fb_api=base_url_fb_api,pagename=pagename, access_token=access_token)+"/posts",
        fields=fields,
        since=since,
        until=until,
        limit=50,
        access_token=access_token)

    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        url = None if paging is None else paging.get("next")
        isnext = url is not None

        yield posts