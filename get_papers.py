import bs4
import requests
import os

base_url = 'https://link.springer.com/journal/11263/volumes-and-issues'


# 129 - 132   1 - 12

class MainPage:
    def __init__(self, volumn, issue):
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'no-cache',
            # 'cookie': 'idp_marker=a5f1e360-2d4d-4c45-86f8-cc05b7ab039d; user.uuid.v2="49564c55-0ec7-412d-b61b-04747a132fae"; sncc=P%3D17%3AV%3D52.0.0%26C%3DC01%2CC02%2CC03%2CC04%26D%3Dtrue; _ga=GA1.1.1865816296.1732349092; lantern=18b6e5ec-8d5a-4e05-8422-ad54f5bcab38; permutive-id=2511b707-2ed0-4b89-acb0-5fb5899b86cf; _hjSessionUser_5204389=eyJpZCI6IjNiNzkzOTc4LWMzMzMtNTMyNC05YTg5LTQ5MDIxMDM1Mjk4OSIsImNyZWF0ZWQiOjE3MzI0Mjg0Njc4NTgsImV4aXN0aW5nIjpmYWxzZX0=; _hjSessionUser_5176038=eyJpZCI6ImEwNGI5YThlLTkwMDUtNTcwZC1iYzljLTYxY2NkNDliZTRmNyIsImNyZWF0ZWQiOjE3MzI0Mjg0NjE2MDIsImV4aXN0aW5nIjp0cnVlfQ==; cto_bundle=w9qt7l9nanNxYzNFRUV0OHhzTHpjUkRoS0N6TTYlMkJtTWdwSmFhWG1CYXZZRmszR01qdGdzY244JTJGYlBzMjRoRGp3Y2JDdVNwdHFiMzhJdEQ2UHNCMzh2ZmdFNGtXR2slMkZoODdhNHR2dUpTZkduTWg1NGVWQTJTdWx6R01oMDNqUlBkNGclMkJ2S2pibXpUa2FhWTV5bzZBWFNLc3RXUSUzRCUzRA; _hjSessionUser_5176041=eyJpZCI6IjVlOTIxZTVkLTJmYTEtNWMwYy1hODIzLTYwMjNiNDE5NzljYSIsImNyZWF0ZWQiOjE3MzI0Mjg0ODc2ODUsImV4aXN0aW5nIjp0cnVlfQ==; AwinChannelCookie=other; _hjSessionUser_5176048=eyJpZCI6ImU5ZmZmMmE1LWRlMTUtNTFkOS04N2ExLTYzMDllNThjZjVjZCIsImNyZWF0ZWQiOjE3MzI0Mjg0NDcwNDgsImV4aXN0aW5nIjp0cnVlfQ==; idp_session=sVERSION_1b75a98df-ad47-4265-a7a4-6cd1b9717b75; idp_session_http=hVERSION_1b93b15a3-4d6f-4507-89d9-250fffa17284; _hjSession_5176048=eyJpZCI6IjZkYjFmN2Q5LTE1ODYtNGE5OC05NGRmLTZmZmZhYzE5NDhkNSIsImMiOjE3MzMwOTc5NzUyNDIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; Hm_lvt_e1214cdac378990dc262ce2bc824c85a=1732349092,1732428448,1733097976; HMACCOUNT=19D59CA6D6FA704F; sim-inst-token=""; trackid="azooxqlltdojeaxdvodtkbpqg"; Hm_lvt_aef3043f025ccf2305af8a194652d70b=1733098012; Hm_lpvt_aef3043f025ccf2305af8a194652d70b=1733098012; ajs_anonymous_id=d2f53456-680f-4e78-8256-c763e7baf9ab; optimizelyEndUserId=oeu1733099853538r0.5451765545840397; _hjSessionUser_5176049=eyJpZCI6IjZhZDIyNTgxLTdiZDgtNTRmNS1iYmFiLTU0NWY3ODFiZTdlMyIsImNyZWF0ZWQiOjE3MzMwOTk4NzU3MjMsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_5176049=eyJpZCI6IjBkZDZmMDc1LThkMGEtNDY5YS05NWUxLThmMzYwNDA2ODRjYyIsImMiOjE3MzMwOTk4NzU3MjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; Hm_lpvt_e1214cdac378990dc262ce2bc824c85a=1733099887; permutive-session=%7B%22session_id%22%3A%2250b2a63c-e76f-4336-909d-fb432af0446d%22%2C%22last_updated%22%3A%222024-12-02T00%3A38%3A06.904Z%22%7D; _uetsid=3f3c9550b04111efb94b73c9034ee7d6; _uetvid=9e2a7520a97111efbc28e76ddf33eb37; _fbp=fb.1.1733100698222.993089032386989014; _ga_B3E4QL2TPR=GS1.1.1733097975.3.1.1733100891.14.0.0; _ga_5V24HQ1XD5=GS1.1.1733097975.3.1.1733100891.0.0.0',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        }
        self.url = f'{base_url}/{volumn}-{issue}'
        self.response = requests.get(self.url, headers=self.headers)

    def get_pages(self):
        soup = bs4.BeautifulSoup(self.response.text, 'html.parser')
        page_block = soup.find('section', {'data-ga': 'journal-articles', 'data-test': 'article-listing'})
        if not page_block:
            return []
        pages = page_block.find_all('li')
        result = []
        for page in pages:
            a_tag = page.find('a', {
                'data-track': 'select_article',
                'data-track-category': 'article listing',
                'data-track-action': 'clicked article'
            })
            if a_tag and 'href' in a_tag.attrs:
                text = a_tag.text.strip()  # 获取a标签内的文本
                url = a_tag['href'].strip()  # 获取a标签的URL
                if not url.startswith('http'):  # 补全相对URL
                    url = f"https://link.springer.com{url}"
                result.append([text, url])

        return result


# https://link.springer.com/content/pdf/10.1007/s11263-024-02118-3.pdf
class ArticlePage:
    def __init__(self, name, title, url, volumn, issue):
        self.url = url
        self.title = title
        self.pdf_url = self.get_pdf_url()
        self.volume = volumn
        self.issue = issue
        self.save_path = f'{name.replace(" ", "")}/{volumn}/{issue}/{title}.pdf'

    def get_pdf_url(self):
        init_url = self.url
        pdf_url = init_url.replace("https://link.springer.com/article/", "https://link.springer.com/content/pdf/")
        return pdf_url

    def download_pdf(self):
        directory = os.path.dirname(self.save_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)  # 创建目录
            print(f"创建目录: {directory}")
        try:
            # 设置请求头和 cookies
            cookies = {
                'idp_marker': 'a5f1e360-2d4d-4c45-86f8-cc05b7ab039d',
                'user.uuid.v2': '"49564c55-0ec7-412d-b61b-04747a132fae"',
                'sncc': 'P%3D17%3AV%3D52.0.0%26C%3DC01%2CC02%2CC03%2CC04%26D%3Dtrue',
                '_ga': 'GA1.1.1865816296.1732349092',
                'lantern': '18b6e5ec-8d5a-4e05-8422-ad54f5bcab38',
                'permutive-id': '2511b707-2ed0-4b89-acb0-5fb5899b86cf',
                '_hjSessionUser_5204389': 'eyJpZCI6IjNiNzkzOTc4LWMzMzMtNTMyNC05YTg5LTQ5MDIxMDM1Mjk4OSIsImNyZWF0ZWQiOjE3MzI0Mjg0Njc4NTgsImV4aXN0aW5nIjpmYWxzZX0=',
                '_hjSessionUser_5176038': 'eyJpZCI6ImEwNGI5YThlLTkwMDUtNTcwZC1iYzljLTYxY2NkNDliZTRmNyIsImNyZWF0ZWQiOjE3MzI0Mjg0NjE2MDIsImV4aXN0aW5nIjp0cnVlfQ==',
                'cto_bundle': 'w9qt7l9nanNxYzNFRUV0OHhzTHpjUkRoS0N6TTYlMkJtTWdwSmFhWG1CYXZZRmszR01qdGdzY244JTJGYlBzMjRoRGp3Y2JDdVNwdHFiMzhJdEQ2UHNCMzh2ZmdFNGtXR2slMkZoODdhNHR2dUpTZkduTWg1NGVWQTJTdWx6R01oMDNqUlBkNGclMkJ2S2pibXpUa2FhWTV5bzZBWFNLc3RXUSUzRCUzRA',
                '_hjSessionUser_5176041': 'eyJpZCI6IjVlOTIxZTVkLTJmYTEtNWMwYy1hODIzLTYwMjNiNDE5NzljYSIsImNyZWF0ZWQiOjE3MzI0Mjg0ODc2ODUsImV4aXN0aW5nIjp0cnVlfQ==',
                'AwinChannelCookie': 'other',
                '_hjSessionUser_5176048': 'eyJpZCI6ImU5ZmZmMmE1LWRlMTUtNTFkOS04N2ExLTYzMDllNThjZjVjZCIsImNyZWF0ZWQiOjE3MzI0Mjg0NDcwNDgsImV4aXN0aW5nIjp0cnVlfQ==',
                'Hm_lvt_e1214cdac378990dc262ce2bc824c85a': '1732349092,1732428448,1733097976',
                'ajs_anonymous_id': 'd2f53456-680f-4e78-8256-c763e7baf9ab',
                'optimizelyEndUserId': 'oeu1733099853538r0.5451765545840397',
                '_fbp': 'fb.1.1733100698222.993089032386989014',
                'sim-inst-token': '""',
                'trackid': '"wcibivuusgcxonaaeollb1tvl"',
                'idp_session': 'sVERSION_1c78cd9c4-c598-44c7-bdbe-f91ff7fd9b7a',
                'idp_session_http': 'hVERSION_1c4107b63-0c22-4c86-9662-db74adfcaf6b',
                '_ga_B3E4QL2TPR': 'GS1.1.1733141791.4.1.1733141792.59.0.0',
                '_uetsid': '3f3c9550b04111efb94b73c9034ee7d6',
                '_uetvid': '9e2a7520a97111efbc28e76ddf33eb37',
                'Hm_lvt_aef3043f025ccf2305af8a194652d70b': '1733098012,1733141793',
                'Hm_lpvt_aef3043f025ccf2305af8a194652d70b': '1733141793',
                'HMACCOUNT': '1BB9A6A4870233B1',
                '_ga_5V24HQ1XD5': 'GS1.1.1733141793.4.0.1733141793.0.0.0',
                '_hjSessionUser_5176049': 'eyJpZCI6IjZhZDIyNTgxLTdiZDgtNTRmNS1iYmFiLTU0NWY3ODFiZTdlMyIsImNyZWF0ZWQiOjE3MzMwOTk4NzU3MjMsImV4aXN0aW5nIjp0cnVlfQ==',
                '_hjSession_5176049': 'eyJpZCI6ImYxMmM3MzJjLWZmNzMtNGU3Ny1hOGJkLWU3MjE2ZmYyYzI3MyIsImMiOjE3MzMxNDE3OTQwODIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
                'permutive-session': '%7B%22session_id%22%3A%22f30a460a-a35a-48c6-b43b-99f53bb1711e%22%2C%22last_updated%22%3A%222024-12-02T12%3A16%3A34.432Z%22%7D',
            }

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'no-cache',
                # 'cookie': 'idp_marker=a5f1e360-2d4d-4c45-86f8-cc05b7ab039d; user.uuid.v2="49564c55-0ec7-412d-b61b-04747a132fae"; sncc=P%3D17%3AV%3D52.0.0%26C%3DC01%2CC02%2CC03%2CC04%26D%3Dtrue; _ga=GA1.1.1865816296.1732349092; lantern=18b6e5ec-8d5a-4e05-8422-ad54f5bcab38; permutive-id=2511b707-2ed0-4b89-acb0-5fb5899b86cf; _hjSessionUser_5204389=eyJpZCI6IjNiNzkzOTc4LWMzMzMtNTMyNC05YTg5LTQ5MDIxMDM1Mjk4OSIsImNyZWF0ZWQiOjE3MzI0Mjg0Njc4NTgsImV4aXN0aW5nIjpmYWxzZX0=; _hjSessionUser_5176038=eyJpZCI6ImEwNGI5YThlLTkwMDUtNTcwZC1iYzljLTYxY2NkNDliZTRmNyIsImNyZWF0ZWQiOjE3MzI0Mjg0NjE2MDIsImV4aXN0aW5nIjp0cnVlfQ==; cto_bundle=w9qt7l9nanNxYzNFRUV0OHhzTHpjUkRoS0N6TTYlMkJtTWdwSmFhWG1CYXZZRmszR01qdGdzY244JTJGYlBzMjRoRGp3Y2JDdVNwdHFiMzhJdEQ2UHNCMzh2ZmdFNGtXR2slMkZoODdhNHR2dUpTZkduTWg1NGVWQTJTdWx6R01oMDNqUlBkNGclMkJ2S2pibXpUa2FhWTV5bzZBWFNLc3RXUSUzRCUzRA; _hjSessionUser_5176041=eyJpZCI6IjVlOTIxZTVkLTJmYTEtNWMwYy1hODIzLTYwMjNiNDE5NzljYSIsImNyZWF0ZWQiOjE3MzI0Mjg0ODc2ODUsImV4aXN0aW5nIjp0cnVlfQ==; AwinChannelCookie=other; _hjSessionUser_5176048=eyJpZCI6ImU5ZmZmMmE1LWRlMTUtNTFkOS04N2ExLTYzMDllNThjZjVjZCIsImNyZWF0ZWQiOjE3MzI0Mjg0NDcwNDgsImV4aXN0aW5nIjp0cnVlfQ==; Hm_lvt_e1214cdac378990dc262ce2bc824c85a=1732349092,1732428448,1733097976; ajs_anonymous_id=d2f53456-680f-4e78-8256-c763e7baf9ab; optimizelyEndUserId=oeu1733099853538r0.5451765545840397; _fbp=fb.1.1733100698222.993089032386989014; sim-inst-token=""; trackid="wcibivuusgcxonaaeollb1tvl"; idp_session=sVERSION_1c78cd9c4-c598-44c7-bdbe-f91ff7fd9b7a; idp_session_http=hVERSION_1c4107b63-0c22-4c86-9662-db74adfcaf6b; _ga_B3E4QL2TPR=GS1.1.1733141791.4.1.1733141792.59.0.0; _uetsid=3f3c9550b04111efb94b73c9034ee7d6; _uetvid=9e2a7520a97111efbc28e76ddf33eb37; Hm_lvt_aef3043f025ccf2305af8a194652d70b=1733098012,1733141793; Hm_lpvt_aef3043f025ccf2305af8a194652d70b=1733141793; HMACCOUNT=1BB9A6A4870233B1; _ga_5V24HQ1XD5=GS1.1.1733141793.4.0.1733141793.0.0.0; _hjSessionUser_5176049=eyJpZCI6IjZhZDIyNTgxLTdiZDgtNTRmNS1iYmFiLTU0NWY3ODFiZTdlMyIsImNyZWF0ZWQiOjE3MzMwOTk4NzU3MjMsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_5176049=eyJpZCI6ImYxMmM3MzJjLWZmNzMtNGU3Ny1hOGJkLWU3MjE2ZmYyYzI3MyIsImMiOjE3MzMxNDE3OTQwODIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; permutive-session=%7B%22session_id%22%3A%22f30a460a-a35a-48c6-b43b-99f53bb1711e%22%2C%22last_updated%22%3A%222024-12-02T12%3A16%3A34.432Z%22%7D',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
            }

            # 发起 GET 请求
            response = requests.get(self.pdf_url, headers=headers, cookies=cookies, verify=False, stream=True)

            # 检查响应状态码
            if response.status_code == 200:
                # 以二进制写入模式保存文件
                with open(self.save_path, 'wb') as pdf_file:
                    for chunk in response.iter_content(chunk_size=8192):  # 分块写入文件
                        pdf_file.write(chunk)
                print(f"PDF 下载成功: {self.save_path}")
            else:
                print(f"请求失败，状态码: {response.status_code}")
        except Exception as e:
            print(f"下载失败: {e}")

if __name__ == '__main__':
    # mainpage = MainPage(volumn=129, issue=1)
    # print(mainpage.get_pages())
    title = 'View Transfer on Human Skeleton Pose: Automatically Disentangle the View-Variant and View-Invariant Information for Pose Representation Learning'
    url = 'https://link.springer.com/article/10.1007/s11263-020-01354-7'
    name = 'International Journal of Computer Vision'
    articlepage = ArticlePage(name, title, url, 129, 1)
    print(articlepage.pdf_url)
    articlepage.download_pdf()
