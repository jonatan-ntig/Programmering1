a = "  Erik Andersson 990314-2714  "
a = a.strip()
i = a.rfind(' ') + 1
j = a.find("-")
b = a[i:j]
print(b)
print(f"{b[4:6]}/{b[2:4]}")
