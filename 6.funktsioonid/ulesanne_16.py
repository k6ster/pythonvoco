def teisenda_sekundid(sekundid):
    tunnid = sekundid // 3600
    minutid = sekundid % 3600 // 60
    sekundid = sekundid % 60
    return tunnid, minutid, sekundid


print(teisenda_sekundid(3675))
