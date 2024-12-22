import requests
import json

url = "https://gitpod.io/public-api/gitpod.v1.WorkspaceService/StartWorkspace"

payload = {
  "workspaceId": "miyan0001-miyan-90008ynfu79"
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
  'Cookie': "GCLB=COa_57b-6Y6N_QEQAw; gp-necessary=true; gp-analytical=true; gitpod-marketing-website-visited=true; gp-targeting=true; ajs_anonymous_id=a7c78c3a-28e1-47fd-b422-7381ae34008f; skip-signup-wall=true; _gcl_au=1.1.1341546114.1730610395; _ga=GA1.1.390662381.1730610397; gitpod_hashed_user_id=3c6fc21592609cbaac5e7d605ff9415f; _ga_VWLSB1WXM5=GS1.1.1732587675.3.0.1732587675.0.0.0; __Host-_gitpod_io_jwt2_=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IjAwMDEifQ.eyJpYXQiOjE3MzQ4NzA0NDEsImV4cCI6MTczNTQ3NTI0MSwiaXNzIjoiaHR0cHM6Ly9naXRwb2QuaW8iLCJzdWIiOiI1YjVkYzk1OS0yMmNjLTRhMWQtODM5NC0yZjkwNGZhZmYwNGUifQ.Y6h1DMhpFF89XkbLn2sdw-lYV7bcayqk5ptO7IkxE6oeow_WraVck5WcWKzGP7lKaSM9RwW3hWCBmpPDcS728bJ9hGYJSWDmFNZ9YI7tzRNGOg_Wo3yPXtlUkmvlqnHErA_WXKoQ6QOd1FpzIoMpNocIeCccbGJ5h7K0nEEbpEGVgnY9HPZTG3J9xoEX_Z_wVUmuQBGZ5qn2d6TcRawc9bmKuUsiSf6IQQG_KPvDpAyaqnfVlAHHLDFiGGihE2LZVYsxq52974yd1CNW7yR8cgtEnL8pdF17oVVvysTESWW31gDpZCc4k3Z8M-HdFa_MqxxCZUug2NVGLwZ0rNFJ3U8ib5j4AVEZVF-eQiYV8LC4s15u3Q6g2Ocfgy3uGPKB_YzyE5b9GpoD1Tt5eEuj7ceGhmtMmAshmQ5b9_mBgSNttxm29NLSB_qnTQ9HWDu-J5ey7PtdsT4xXxj_dMIgma-tIHvGokBALjsLt5rfUsG_iEaO2tyxVMlfkld4WlOyjodEWfmAZCzd7maD7BZSLZU9wVsqr01d9QCYNf5nFGinU8KehFA6wzEL2BcAm5DDV0IevcIWBOAWFKqt6OCbCu7TNF54ttwPrpWxYFqLkWsBcF_OBR-o0tZI4-LklsQDW5jaaBngHcbVdtHrbUbICoEjG_AhVNGh5J7Cv8_OT-0"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)