import requests
import json

url = "https://gitpod.io/public-api/gitpod.v1.WorkspaceService/StartWorkspace"

payload = {
  "workspaceId": "miyanmei0001-miyanmei-yebr8ss55pa"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 11; Infinix X6511B Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.56 Mobile Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'sec-ch-ua-platform': "\"Android\"",
  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Android WebView\";v=\"132\"",
  'sec-ch-ua-mobile': "?1",
  'connect-protocol-version': "1",
  'origin': "https://gitpod.io",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://gitpod.io/start/",
  'accept-language': "en,en-US;q=0.9",
  'priority': "u=1, i",
  'Cookie': "GCLB=COa_57b-6Y6N_QEQAw; gp-necessary=true; gp-analytical=true; gitpod-marketing-website-visited=true; gp-targeting=true; ajs_anonymous_id=a7c78c3a-28e1-47fd-b422-7381ae34008f; skip-signup-wall=true; _gcl_au=1.1.1341546114.1730610395; _ga=GA1.1.390662381.1730610397; gitpod_hashed_user_id=3c6fc21592609cbaac5e7d605ff9415f; _ga_VWLSB1WXM5=GS1.1.1732587675.3.0.1732587675.0.0.0; __Host-_gitpod_io_jwt2_=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IjAwMDEifQ.eyJpYXQiOjE3MzQ5NzQzMTIsImV4cCI6MTczNTU3OTExMiwiaXNzIjoiaHR0cHM6Ly9naXRwb2QuaW8iLCJzdWIiOiI1YjVkYzk1OS0yMmNjLTRhMWQtODM5NC0yZjkwNGZhZmYwNGUifQ.PqRIKrfD5UkWs3njInl3_QrxCZohQIisrtlLLgrOqKx0D58ghQWLphz9Js7vrvbEjAZlLbsC7eZTrvAnrzmILhaRtLYM5s687noPKnK9LKihTr1JDsZZ_icwY5fASp-7auwIUVy3H6He1SgbUEOotJtLmrHS6wAp2VTmouLrAMY2zff0437I2KFtYZ8wr8Z58cpLWAR7_auU8Z4htyclaDQGngeEvGY-3JUXE8ttX-3u4lkfTWZaDqi4kACMG9aMEq6Q7rBV5oEu-o3VZPFr6B_PXmHG7d32gEIw6UEVpN8sbpH6DW1qXt3K8vbgDxHK0gEvM1bW3-etUiNfvtv3hIZFC-C2rfEbwjLtBjGuu7Rq1TYTXWILs3OSRcuSn8aiQ6ZDFTDvHw67TknxpNSNmuzPST9-JLL8163_JlJ2GUDRNkiptrHJBihDZqxqRdrUyfF3y3YczroX5zlunmNer0Vod79SZ9aTepX7lfZsKR4krFL60-gyQHqEeqOxbRTbaCt4Zk0drlS7BJreZeyaalIKBAezfM6JfgihY2t1C3yBksZE0InrOK3cH3eT5PMDO4qHDxf271RAHdA2ubikTcOu5NXCPHP9s0--rK_Ii_rVGHs1F2lo10LMwGoyELHl0bDaXskmdyUDMDoebQnSKyQh8rhfQ4EZEu4oiXG8QfE"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)