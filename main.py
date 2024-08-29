import random
import pygame as pg
from wfc_node import WFCNode

RUNNING : bool = True
WIDTH = 100
HEIGHT = 60
NODES: list[WFCNode] = [
    WFCNode((0, 0), "./imgs/blank.png", [0, 0, 0, 0]),
    WFCNode((0, 0), "./imgs/n.png",     [1, 0, 0, 0]),
    WFCNode((0, 0), "./imgs/e.png",     [0, 1, 0, 0]),
    WFCNode((0, 0), "./imgs/w.png",     [0, 0, 1, 0]),
    WFCNode((0, 0), "./imgs/s.png",     [0, 0, 0, 1]),
    WFCNode((0, 0), "./imgs/ns.png",    [1, 0, 0, 1]),
    WFCNode((0, 0), "./imgs/ew.png",    [0, 1, 1, 0]),
    WFCNode((0, 0), "./imgs/ne.png",    [1, 1, 0, 0]),
    WFCNode((0, 0), "./imgs/nw.png",    [1, 0, 1, 0]),
    WFCNode((0, 0), "./imgs/se.png",    [0, 1, 0, 1]),
    WFCNode((0, 0), "./imgs/sw.png",    [0, 0, 1, 1]),
    WFCNode((0, 0), "./imgs/new.png",   [1, 1, 1, 0]),
    WFCNode((0, 0), "./imgs/nes.png",   [1, 1, 0, 1]),
    WFCNode((0, 0), "./imgs/nws.png",   [1, 0, 1, 1]),
    WFCNode((0, 0), "./imgs/sew.png",   [0, 1, 1, 1]),
    WFCNode((0, 0), "./imgs/nwse.png",  [1, 1, 1, 1]),
]
DIR_OFFSETS = [
    (0, -1),
    (1, 0),
    (-1, 0),
    (0, 1)
]

def ReducePotentialNodes(possible_nodes: list[WFCNode], ngb_node: WFCNode, side_dir: int):
    print(f"ngb_node: {ngb_node}")
    temp = []
    for i in range(len(possible_nodes)-1, -1, -1):
        temp.append(possible_nodes[i].sides[side_dir])
        if  possible_nodes[i].sides[side_dir] != ngb_node.sides[3-side_dir]: del possible_nodes[i]
    print(temp)


if __name__ == "__main__":    
    pg.init()
    screen = pg.display.set_mode((WIDTH*16, HEIGHT*16))
    screen.fill((0, 0, 0))
    
    print("Finished Screen Setup")
    
    to_collapse: list[tuple[int, int]] = [(WIDTH//2, HEIGHT//2)]
    grid: list[list[WFCNode]] = [[WFCNode() for _ in range(HEIGHT)] for _ in range(WIDTH)]
    
    
    while len(to_collapse) > 0:
        x: int = to_collapse[0][0]
        y: int = to_collapse[0][1]

        possible_nodes: list[WFCNode] = NODES.copy()
    
        for i, dir in enumerate(DIR_OFFSETS):
            ngb = (x + dir[0], y + dir[1])
    
            if ngb[0] >= 0 and ngb[0] < WIDTH and ngb[1] >= 0 and ngb[1] < HEIGHT:
                try:
                    ngb_node = grid[ngb[0]][ngb[1]] 
                    if ngb_node.collapsed:
                        # print(f"{ngb}: side={ngb_node.sides[3 - i]}")
                        ReducePotentialNodes(possible_nodes, ngb_node, i)
                    else:
                        if ngb not in to_collapse: to_collapse.append(ngb)
                except: print(f"ERROR: {(ngb[0], ngb[1])}")
    
        if len(possible_nodes) == 0: 
            grid[x][y] = NODES[0]
            grid[x][y].collapsed = True
            print(f"({x}, {y}): No Match Found, Resorting To Default")
        else:
            grid[x][y] = possible_nodes[random.randrange(len(possible_nodes))]
    
        print(f"Drawing {(x, y)}: {grid[x][y].img_path}")
        grid[x][y].draw(screen, (x, y))
        del to_collapse[0]
        
        waiting = True

        pg.display.update()
        
        # while waiting:
        #     for ev in pg.event.get():
        #         if ev.type == pg.KEYUP and ev.key == pg.K_SPACE: waiting = False
    
while RUNNING:
    for ev in pg.event.get():
        if ev.type == pg.QUIT: RUNNING = False
    
    if pg.mouse.get_pressed()[0]: print(f"Mouse: ({pg.mouse.get_pos()[0]//16, pg.mouse.get_pos()[1]//16})")






