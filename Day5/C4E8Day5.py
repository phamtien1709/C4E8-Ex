px = 2
py = 1
bx = 3
by = 3
cx = 5
cy = 5

screen_width = 7
screen_height = 7
def check_lose(bx,by,screen_height,screen_width):
    if [bx,by] == [0,0] or [bx,by] == [0,screen_height-1] or [bx,by] == [screen_width-1,0] or [bx,by] == [screen_width-1,screen_height-1]:
        return True
    return False

def show_map(screen_height,screen_width,px,py,bx,by,cx,cy):
    for y in range(screen_height):
        for x in range(screen_width):
            if x == px and y == py:
                print("T ", end="")
            elif x == bx and y == by:
                print("B ", end="")
            elif x == cx and y == cy:
                print("x ", end="")
            else:
                print("- ", end="")
        print()

def in_map(x, y, screen_width, screen_height):
    if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
        return False
    return True
def check_box(bx,by,px,py):
    if bx == px and by == py:
        return True
    return False
def check_win(cx,cy,bx,by):
    if cx == bx and cy == by:
        return True
    return False
def move(x, y, dx, dy):
    return [x + dx, y + dy]
win = True
while win:
    show_map(screen_height, screen_width, px, py, bx, by, cx, cy)
    choice = input("What do you want? U - D - L - R: ").upper()

    dx = 0
    dy = 0

    if choice == "W":
        dy = -1
    elif choice == "S":
        dy = 1
    elif choice == "A":
        dx = -1
    elif choice == "D":
        dx = 1

    [next_px, next_py] = move(px, py, dx, dy)

    if check_box(bx,by,next_px,next_py):
        [next_bx,next_by] = move(bx,by,dx,dy)
        if check_lose(next_bx, next_by, screen_height, screen_width):
            show_map(screen_height,screen_width,next_px,next_py,next_bx,next_by,cx,cy)
            restart = input("YOU LOSE!! DO YOU WANT TO RESTART??(Y/N)\t")
            if restart.upper() == "Y":
                px = 2
                py = 1
                bx = 3
                by = 3
                cx = 5
                cy = 5
            else:
                print("See you again!")
                win = False
        else:
            if not in_map(next_bx, next_by, screen_width, screen_height):
                print("Can't move!!!")
            else:
                bx = next_bx
                by = next_by
                px = next_px
                py = next_py
    else:
        if not in_map(next_px, next_py, screen_width, screen_height):
            print("Go away!!!")
        else:
            px = next_px
            py = next_py

    if check_win(cx,cy,bx,by) and win == True:
        show_map(screen_height, screen_width, px, py, bx, by, cx, cy)
        print("CONGRATULATION!! YOU WIN!")
        win = False
