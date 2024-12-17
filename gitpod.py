import requests
import json

url = "https://gitpod.io/public-api/gitpod.v1.WorkspaceService/StartWorkspace"

payload = {
  "workspaceId": "miyan0001-miyan-6yujeqpe4x0"
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
  'Cookie': "GCLB=COa_57b-6Y6N_QEQAw; gp-necessary=true; gp-analytical=true; gitpod-marketing-website-visited=true; gp-targeting=true; ajs_anonymous_id=a7c78c3a-28e1-47fd-b422-7381ae34008f; skip-signup-wall=true; _gcl_au=1.1.1341546114.1730610395; _ga=GA1.1.390662381.1730610397; gitpod_hashed_user_id=3c6fc21592609cbaac5e7d605ff9415f; _ga_VWLSB1WXM5=GS1.1.1732587675.3.0.1732587675.0.0.0; __Host-_gitpod_io_jwt2_=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IjAwMDEifQ.eyJpYXQiOjE3MzQzOTk2NjYsImV4cCI6MTczNTAwNDQ2NiwiaXNzIjoiaHR0cHM6Ly9naXRwb2QuaW8iLCJzdWIiOiI1YjVkYzk1OS0yMmNjLTRhMWQtODM5NC0yZjkwNGZhZmYwNGUifQ.QgsLNPe5SF0JCRD0bQ-YtmQSGAa3g0p-KQrUAMVQlduD9FxXncIbP-y0Fa07lYrCRADWA6k1v70WA0uWUibAL9eKxUT2XmVLYwVDX1Jhc4MThBO1qK_o9qiQXvZ_W66Jw2J-N6NtFCwlRKdxSJSesFgJy_s_5inYKHDwOy5T4VdQS3hG0y0BU0E5SdW6uPUw1SfJ6dVt2xuEOuVq5_m7SOgFzOhN6y0z6mjfAB4o32sEnM4AgcU5nKzLiClwGC3N0-7L8I3Jwlau7hkRqz3LB2Aj6Gpqpdtgg4HYFesK7GxMdd5YyAPi661Ltx58Hi05eJvZBUAtpYNxW8eURSy3fmDrWD7_VouU1CEWnrXqoes1hPBiR4uzDZJ7EQy_dmACQFH99ogGFCxNQ1zHYXckTwCGvU9_Yu6-e6X7JreKlzvQkZFLEOrb4AK-83Tzb_k9xv6nnQx2bVPPn7rIci8dDQhowT7yKN_H5HcZABCUmAzgF_9QKAplBZjonZJjs2vH6IXk7ftGV3vOzLMlo56WBwrZhd1VD8sAfw3f7o83mjz3Neqzpv7rwrdpCbYzhm3jhuNbWynA8_k0KZlsdRHIwjLEr9e9re2VlvlD4kwpygij28gb2bZNjY4uB4RpOz7feotu9VqUUjkOdTx8QnF4cUWp0AHw0fuvl2Kj8K9wcwQ"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)