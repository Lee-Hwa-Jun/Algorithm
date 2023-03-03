def solution(wallpaper):
    wallpaper_ = [[wallpaper[x][y] for x in range(len(wallpaper))] for y in range(len(wallpaper[0]))]
    lux,luy,rdx,rdy = len(wallpaper),len(wallpaper[0]),0,0
    for x in range(len(wallpaper)):
        if '#' in wallpaper[x] and lux > x:
            lux = x
        if '#' in wallpaper[x] and rdx < x:
            rdx = x
    for y in range(len(wallpaper_)):
        if '#' in wallpaper_[y] and luy > y:
            luy = y
        if '#' in wallpaper_[y] and rdy < y:
            rdy = y

    answer = [lux,luy,rdx+1,rdy+1]
    return answer