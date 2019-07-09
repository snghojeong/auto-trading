import time, base64, hmac, hashlib

nonce = str(time.time())
method = 'GET'
request_path = '/balances'

""" 필수 정보를 연결하여 prehash 문자열을 생성함 """
what = nonce + method + request_path # + request_body
""" base64로 secret을 디코딩함 """
key = base64.b64decode(secret)
""" hmac으로 필수 메시지에 서명하고 """
""" 그 결과물을 base64로 인코딩함 """
signature = hmac.new(key, what, hashlib.sha512)
return base64.b64encode(signature.digest())
