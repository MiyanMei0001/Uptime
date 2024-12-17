import requests
import json

url = "https://gitpod.io/public-api/gitpod.v1.WorkspaceService/StartWorkspace"

payload = {
  "workspaceId": "miyan0001-miyan-v5agdvseqth"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 11; Infinix X6511B Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.43 Mobile Safari/537.36",
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
  'Cookie': "GCLB=COa_57b-6Y6N_QEQAw; gp-necessary=true; gp-analytical=true; gitpod-marketing-website-visited=true; gp-targeting=true; ajs_anonymous_id=a7c78c3a-28e1-47fd-b422-7381ae34008f; skip-signup-wall=true; _gcl_au=1.1.1341546114.1730610395; _ga=GA1.1.390662381.1730610397; gitpod_hashed_user_id=3c6fc21592609cbaac5e7d605ff9415f; _ga_VWLSB1WXM5=GS1.1.1732587675.3.0.1732587675.0.0.0; __Host-_gitpod_io_jwt2_=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IjAwMDEifQ.eyJpYXQiOjE3MzQ0NzUzMzgsImV4cCI6MTczNTA4MDEzOCwiaXNzIjoiaHR0cHM6Ly9naXRwb2QuaW8iLCJzdWIiOiI1YjVkYzk1OS0yMmNjLTRhMWQtODM5NC0yZjkwNGZhZmYwNGUifQ.Ngz9WzGnwx2zNduz9UnNTy3GOcquOHoTeETM9tB9j9elAEd8RHqrsSbY_OLYU0e9T2jD7xOi7r4hv2OFGo0qxU9dYbwzLFQ3Sq5HYz9GluS8rGFFXdpBtDnkWpCHsFqNKdK_iX0XtOoNqondvmXN8dgxOk-m6EsOnEgo2xkHBKi6JdAmRsxtXu5heIURSxU1fC0Yn3L_QzMgUknr3fbpl1EX8gpJIreRroxq8lAO0Ks4Rnh5gakuu7CFFen4mitixlhxmBciGvvIudD-Pl-KEY2DO87AMLufvMYD2UbZepUVAvQ00bEk_SiNZmtlBFAgJr25LRTnD7fipaKNXbiP-QuO92xjK48nuWuy8aE67UfNIgXVUDirTyBh1tjEJJZZ-_30Kw7tPHd9PQm3eaLHTMGe2iRE1oXxnzvJDg5VO0b1nYut4iZocwAyVMqjNKWw8yTI3_O6Um8FI5ija4qPC2A42XKbIZ1IcKtb3pALjJMD9_xsK2zhPfDQ7Mqz9M2YWjZk7LNNDXuR4qgs8sMINM7AQRKh30YObEY-R5Fw5SP4kWIubPYV5ijm1uxf-TLv0lzu5anSYtmD7bAuWR-y5znIb74pw9B77tjJ9WD12FfuNB3Tb7Ag5PTgr2ZdGK0I7rKgnZWY_QTZLfxosMQbPHZUiINvlw5y_CH6NuE8m6M"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)