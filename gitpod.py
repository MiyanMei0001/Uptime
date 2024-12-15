import requests
import json

url = "https://gitpod.io/public-api/gitpod.v1.WorkspaceService/StartWorkspace"

payload = {
  "workspaceId": "miyan0001-miyan-gfjin8dx8nb"
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
  'Cookie': "GCLB=COa_57b-6Y6N_QEQAw; gp-necessary=true; gp-analytical=true; gitpod-marketing-website-visited=true; gp-targeting=true; ajs_anonymous_id=a7c78c3a-28e1-47fd-b422-7381ae34008f; skip-signup-wall=true; _gcl_au=1.1.1341546114.1730610395; _ga=GA1.1.390662381.1730610397; gitpod_hashed_user_id=3c6fc21592609cbaac5e7d605ff9415f; _ga_VWLSB1WXM5=GS1.1.1732587675.3.0.1732587675.0.0.0; __Host-_gitpod_io_jwt2_=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IjAwMDEifQ.eyJpYXQiOjE3MzQzMDE2NjksImV4cCI6MTczNDkwNjQ2OSwiaXNzIjoiaHR0cHM6Ly9naXRwb2QuaW8iLCJzdWIiOiI1YjVkYzk1OS0yMmNjLTRhMWQtODM5NC0yZjkwNGZhZmYwNGUifQ.J7fv2BxcrypMvG-G3LYCKZfxzTEX4bCTBrFpgwzNiYSR1Th5HBYDFVpJkcAv0Xt7K3LO7MK2hBgpqir3Glo63d_kVukIqkbNzLxW9K1pMi49bh5t7-m9Q6hNw6tBNxPaJI2jMPs1S-xOBH7DbhU-B8ix4GhUdcDfzx07z1Y1oHx5iNkhBiIky9jbZLIvOQkvNa8pNVm7gVX4a1smnYgA-OtIX7sA5iUFSS5uikK9aVd57SCwRk4Tn9xgKv8LpRRmkemkGVKTkvqC4ZpZiQ_x8qu1-JrUrKrIBNG3Un8nYBW4YLuzWRO8fd5Lj3LgtoGKLHwfMYKOS6eDqbs1JkrxTatw-a5XVvZm2h5OlxelGscCrPqDOsptUDMb9fcprEyGH9ZNHAlBP-XV-syEHSlnC5vf_sYU5zzZ44tECChi5oHVmHtWnJL3rPXO3WCYwj3X0JIio_Cr5ugDsx-MKlXN1zWl3xqW0aXLC-AD1hF1fVz71yOfKV7gue2qgworDM3rulT4yGqaiOommYZizZsBUD5Fj14sJ0Rlwi3RSUBXweW8Fambp0LIh7RLoTjYIYv5j0W2P8R__0GzotqV-vMaUSwXsXnzOz1fyN6QLb3_U439UEVe6-IbHseNgf9jbOq5bvsblCi5vJRnuR70b7GsuAWwjLDiIGsuqV1CiRfZhb8; _gitpod_io_ws_bb09b7a6-85fc-4311-985e-60e9564d686f_owner_=7UIZvsR3_ZCvOxQb0zSIeRerH4otcbD4"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)