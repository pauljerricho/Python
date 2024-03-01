import requests


client_id = '73e9a8ff878655ca59c5980a8ac0620e' #'자신의 App ID'
client_secret =  '73e9a8ff878655ca59c5980a8ac0620e658e2d0fc1fdca1ae2ef7bc1d4584e120feacbea' # '자신의 Secret Key'
access_token = '발급 받은 access token'
code = '발급 받은 가장 최신의 Authentication Code'
redirect_uri = '자신의 블로그 주소'
blogName = '블로그 이름 (https://XXX.tistory.com 에서 XXX의 값)'
tag = '테스트, test'					#등록할 태그값, 쉼표로 구분
output = 'json'						#고정값
grant_type = 'authorization_code'   #고정값 
visibility = 0  #0은 비공개, 3은 공개 발행
category =  1039213


def getToken():
    url = 'https://www.tistory.com/oauth/access_token?'
    data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri,
            'code': code,
            'grant_type': grant_type
            }
    r = requests.get(url, data)
    print (r.text)


def getCategory():
    url = 'https://www.tistory.com/apis/category/list?'
    data = {
            'access_token': access_token,
            'output': output,
            'blogName': blogName,
            }
    r = requests.get(url, data)
    print (r.text)


def postWrite(content):
        title = '자동 포스팅 테스트'
        url = 'https://www.tistory.com/apis/post/write?'
        data = {
                 'access_token': access_token,
                 'output': output,
                 'blogName': blogName,
                 'title': title,
                 'content': content,
                 'visibility': visibility,
                 'category': category,
                 'tag': tag,
                 }
        r = requests.post(url, data=data)
        print ('자동 포스팅 성공')
        return r.text


if __name__ == '__main__':
    # getToken()    #최초 토큰 발급시에만 수행
    # getCategory()  #최초 카테고리 확인시에만 수행
	postWrite('테스트 등록 글입니다.')