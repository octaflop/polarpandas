import qrcode

data = "https://github.com/octaflop/cyberpython"

img = qrcode.make(data)

img.save("cyberpython_github_repo_qr.png")

