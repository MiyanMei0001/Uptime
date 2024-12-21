import requests
import json

url = "https://gitpod.io/public-api/gitpod.v1.WorkspaceService/StartWorkspace"

payload = {
  "workspaceId": "miyan0001-miyan-od6vwosancp"
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
  'Cookie': "GCLB=COa_57b-6Y6N_QEQAw; gp-necessary=true; gp-analytical=true; gitpod-marketing-website-visited=true; gp-targeting=true; ajs_anonymous_id=a7c78c3a-28e1-47fd-b422-7381ae34008f; skip-signup-wall=true; _gcl_au=1.1.1341546114.1730610395; _ga=GA1.1.390662381.1730610397; gitpod_hashed_user_id=3c6fc21592609cbaac5e7d605ff9415f; _ga_VWLSB1WXM5=GS1.1.1732587675.3.0.1732587675.0.0.0; __Host-_gitpod_io_jwt2_=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IjAwMDEifQ.eyJpYXQiOjE3MzQ3NzkyNjQsImV4cCI6MTczNTM4NDA2NCwiaXNzIjoiaHR0cHM6Ly9naXRwb2QuaW8iLCJzdWIiOiI1YjVkYzk1OS0yMmNjLTRhMWQtODM5NC0yZjkwNGZhZmYwNGUifQ.eGZbuceNIYv2RWiu0lL-olSYxwZzZzmkUdWatA7l8HexbsHh_nAqy0fJ92qxzwlHOJ-5GLsRsnhdCQBvypSoF1gigY3oqyzYJncffyeusJcHeUgoKhvABMCTvHTAYU3bNzee9dcv9-FX4ypDEW4jIrut0vjpEoo9KGGorkydxppCo6_tmtn8n5wOduPek7h6WSzbk8Yq3S7XqWrnKKsdC8_W_D5hQIKxYxhK2MQ38VrpaVpr2lgrnYUF_quTyr53ESWowEzEMquLzrCQXiCASgvbK6RoVjHnWWBmHe_yU9AwgqQgZJ6UsXhBW0EjSk19kTR67Vh_3C99gmC5UIJ-SkKkwP7CAeF3aZriej0nsQLvHme-oq5nYkpbZ82IA6z_133AOkMR5cuJb_s3QzdKgrozJL3suJpqH7BG6QU4yuMFXAQKS9p7rqjCX3EasEGJNtxZsUYUEzb5klPkL2r9qaOP4Q9RpOcjEBDqfd9Ec2CzNowxGzJHZtvtWVf3BcjRK9sAWthMrhgYiD_xluIhMsF3XBUX3Th_aQ8bgDqUV-YJCLwH0rQwiztbeG6wMNx7ctP2TvhsWx-MWNWHGCsMYcC2jnn1mNU_1acp5wcATfCMGnFgNqF9fJjD7Qh7f7chemmxPDQj69BraJP_0-xgwCO7Gn747PvR5pAaJweWb0s"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)