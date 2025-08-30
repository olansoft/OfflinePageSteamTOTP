import base64

with open("main.html", "rb") as f:
    data = f.read()

encoded = base64.b64encode(data).decode("utf-8")
print("data:text/html;base64," + encoded + "#secret=")
