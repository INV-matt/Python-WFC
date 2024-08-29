import pygame as pg


class WFCNode:
    def __init__(self, position: tuple[int, int] = (0, 0), image: str = "./imgs/blank.png", sides: list[int] = [0, 0, 0, 0], collapsed = False) -> None:
        self.pos: tuple[int, int] = position
        self.img_path: str = image
        self.sides: list[int] = sides
        self.collapsed = collapsed
        self.image = pg.image.load(self.img_path)

    def draw(self,screen: pg.Surface, pos: tuple[int,int]):
        self.pos = pos
        self.collapsed = True
        screen.blit(self.image, (self.pos[0] * self.image.get_width(), self.pos[1] * self.image.get_height()))
        # pg.draw.rect(screen, (255, 0, 0), pg.Rect(self.pos[0] * self.image.get_width(), self.pos[1] * self.image.get_height(), self.image.get_width(), self.image.get_height()), 1)

    def __str__(self) -> str:
        return f"{self.pos}: {self.image} [collapsed: {self.collapsed}]" 

