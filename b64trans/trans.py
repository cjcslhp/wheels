
data = input()
# data = ""

yourList = "IJLMNOPKABDEFGHCQRTUVWXSYZbcdefa45789+/6ghjklmnioprstuvqwxz0123y" 
tureList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
res = "".join([i if i == '=' else tureList[yourList.index(i)] for i in data])

print(res)

