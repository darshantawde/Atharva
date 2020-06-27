yee = "map"
key = yee.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')

msg = yee.translate(key)
print(msg)