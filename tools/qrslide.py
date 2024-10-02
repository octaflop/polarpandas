import qrcode

data = "https://github.com/octaflop/polarpandas"

img = qrcode.make(data)

img.save("polarpandas_github_repo_qr.png")

