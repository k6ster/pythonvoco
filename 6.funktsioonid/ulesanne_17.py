def teisenda_eurodeks(sendid):
    return sendid // 100, sendid % 100

print(teisenda_eurodeks(1237))
