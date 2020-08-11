# 악용 시의 책임을 지지 않습니다..


import requests
import json
from bs4 import BeautifulSoup

search_query = input('검색어를 입력하세요 : \n')

video_headers = {
    'authority': 'www.youtube.com',
    'x-youtube-sts': '18484',
    'x-youtube-device': 'cbr=Chrome&cbrver=84.0.4147.105&ceng=WebKit&cengver=537.36&cos=Windows&cosver=10.0',
    'x-youtube-page-label': 'youtube.ytfe.desktop_20200805_1_RC1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'x-youtube-variants-checksum': '051bbe767c76cb5bb025880f2c42c8b3',
    'x-youtube-page-cl': '325146078',
    'x-spf-referer': 'https://www.youtube.com/results?search_query=%EC%9C%A0%EC%9E%AC%EC%84%9D',
    'x-youtube-utc-offset': '540',
    'x-youtube-client-name': '1',
    'x-spf-previous': 'https://www.youtube.com/results?search_query=%EC%9C%A0%EC%9E%AC%EC%84%9D',
    'x-youtube-client-version': '2.20200806.01.01',
    'dpr': '1.25',
    'x-youtube-identity-token': 'QUFFLUhqbjFQbnB1eDNuVlViNElVdE9FV3JvSTIycm9CZ3w=',
    'x-youtube-time-zone': 'Asia/Seoul',
    'x-youtube-ad-signals': 'dt=1597109807038&flash=0&frm&u_tz=540&u_his=3&u_java&u_h=864&u_w=1536&u_ah=824&u_aw=1536&u_cd=24&u_nplug=3&u_nmime=4&bc=31&bih=722&biw=613&brdim=0%2C0%2C0%2C0%2C1536%2C0%2C1536%2C824%2C630%2C722&vis=1&wgl=true&ca_type=image',
    'accept': '*/*',
    'x-client-data': 'CIe2yQEIpbbJAQjBtskBCKmdygEIsqHKAQiZtcoBCP+8ygEImb3KAQiLv8oBCOfGygEI58jKAQjpyMoBCLTLygE=',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.youtube.com/results?search_query=%EC%9C%A0%EC%9E%AC%EC%84%9D',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'VISITOR_INFO1_LIVE=LbYWghai1XU; SID=zgf2yonpJob2YTmHxx2UyI5Aczxz5zT2f2SlOqrhqaojs8mwvmQojD8ZqVMBUqEUyVIiPQ.; __Secure-3PSID=zgf2yonpJob2YTmHxx2UyI5Aczxz5zT2f2SlOqrhqaojs8mwLrBmW8dtpn3AahV9gyfE7A.; HSID=Ab0d7uq-HS-qWEKKg; SSID=A2YZ06uO4-bNk9_UY; APISID=6KrRiVUArtZYh1ha/Avxo4cDGkjJmcC7WI; SAPISID=Q7zkDtW6yOKJwknW/AdV_zdKFV2KQQrFfr; __Secure-3PAPISID=Q7zkDtW6yOKJwknW/AdV_zdKFV2KQQrFfr; LOGIN_INFO=AFmmF2swRgIhAPilRlzXpWVxMiMbOtuiwV4P3kyr0ouN7ovvRcLcWbHoAiEAhOQ2qdz5mjo1UOAzEdrQ5odzfiY2niPgGMG7cu30Ug8:QUQ3MjNmem9sZTNWalRvVkxTRlZMNFg0T3N0MnhWUk9rVFdSUEZxRGdKcDl2S3U0UFhvQmxXZEdRZ0o3Ty1jcF85OUZhV0llcDZDYXMwQW52cFJ4a3VxSEVJZzcyWWwycmhzSDJFOEYxZ3FFZ2pmNUc4Y2JQVm5FMlV2NktkN3FPMkM3ZFRvckFEQ1VCWmtkTVFyQ29OUGpmbUlJRUlzclZUdi1mUU1sdVdjTHB5bzlFQlE5TDhBVzJnOTliU0VWY3V6VEMwSjNhclAx; PREF=f4=4000000&al=ko; YSC=3w6JztKuvMo; SIDCC=AJi4QfHUGlG5K9f9g1eLCNhT-fTtc-D69LnVi_ZJ01AxaJIrp8QlTL5RVbpwKw1LipCZUlLceA; ST-1824pnx=oq=%EC%9C%A0%EC%9E%AC%EC%84%9D&gs_l=youtube.12..0i433i229k1l2j0i433k1j0i433i131k1l2j0i433k1l2j0i433i131k1j0i433k1j0j0i433k1l4.0.0.1.75592.1.1.0.0.0.0.497.497.4-1.1.0....0...1ac..64.youtube..0.1.497....0.cu0npcbATz4&itct=CBoQ7VAiEwick7XYgZLrAhVIDVgKHZImAuE%3D&csn=NPYxX9uxJbujlQSGyYDQCw',
}
headers = {
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20200806.01.01'
}
params = (
    ('search_query', search_query),
    ('pbj', '1'),
)

response = requests.get('https://www.youtube.com/results', headers=headers, params=params)

result = json.loads(response.text)
contents = result[1]['response']['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

video_id = []
for content in contents:
    keys = list(content.keys())
    if 'videoRenderer' in keys:
        video_id.append(content['videoRenderer']['videoId'])
    
for vid in video_id:

    params = (
        ('v', vid),
        ('pbj', '1'),
    )
    response = requests.get('https://www.youtube.com/watch',
                            headers=video_headers, params=params)

    result = json.loads(response.text)

    player_response = result[2]['player']['args']['player_response']
    p_json = json.loads(player_response)

    streaming_data = p_json['streamingData']['formats']

    for f in streaming_data:
        keys = list(f.keys())

        if 'url' in keys:
            print(f['url'])