import pygame
from pygame.locals import *


class Obj():
    show = True
    alive=True
    name=""
    inited = 0
    got = 0
    Rplac=[0,0]
    def __init__(self, backgroundColor=[0, 0, 0], rector=[], locat=[0, 0], color=[0, 255, 0], name="", speedx=[], way=0,
                 **dic):
        self.BaseColor = (0, 0, 0)
        self.baseline = [[0, 0], [0, 0]]
        self.name = name
        assert len(locat) == 2
        self.locat = locat
        self.color = color
        assert len(rector) == 2
        self.rec = rector
        self.object = 0
        self.bgcolor = backgroundColor
        self.way = way
        self.Toprint = self.printees()
        for k in dic:
            self.__dict__[k] = dic[k]

    class printees():
        rect = []
        Rplac = []
        locat = []

        def __init__(self, color=[], rect=[], locat=[], ):
            pass

    def __sub__(self, other):
        return [self.locat[k] - other[k] for k in range(2)]

    def upd(self,obj):
        print("shall be changed")


class Shower:
    pressed = []
    printe = []

    def __init__(self, 宽=500, 高=500, backgroundColor=[255,255,255], headless=False):
        self.宽, self.高 = 宽, 高
        if not headless: self.init()
        self.headless = headless
        self.running = True
        self.objlis = []
        self.backgroundColor = backgroundColor
        self.font = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 17)
        self.keys = pygame.key
        self.mouse = pygame.mouse

    def init(self, title="Toms'"):
        pygame.init()
        self.screen = pygame.display.set_mode((self.宽, self.高))
        pygame.display.set_caption(title)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):pass

    def set_headless(self, headless):
        if self.headless == headless: return None
        if self.headless:
            self.init()
        else:
            self.close()
        self.headless = headless

    def close(self):
        pygame.display.quit()

    def surfPrint(self, got):
        text_surface = self.font.render(str(got), True, (0, 0, 255))
        self.printe.append(text_surface)


    def add_dynamic_object(self,obj):
        self.objlis.append(obj)

    # def add_static_object


    def get_objects_by_name(self, name):
        get = []
        for n in self.objlis:
            if n.name == name:
                get.append(n)
        return get

    def get_objects_by_index(self, index):
        get = []
        for n in self.objlis:
            if "index" not in n.__dict__: continue
            if n.index == index:
                get.append(n)
        return get

    def get_object_by_index(self, index):
        try:
            return self.get_objects_by_index(index)[0]
        except:
            return None

    def update(self,):
        if self.pause:return
        self.pressed = pygame.key.get_pressed()
        if self.pressed[K_ESCAPE]: self.running = 0
        for k in self.objlis:
            k.upd(i for i in self.objlis if i is not k)
            if not k.alive:
                self.objlis.remove(k)

    clear_print = True

    def bliter(self):
        for k in self.objlis:
            if k.show:


                try:
                    self.screen.blit(k.object, k-k.Rplac)
                except Exception as e:
                    print(k.name, k.locat, k.Rplac)
                    raise e
                if True:
                    self.screen.blit(self.font.render(str(k.name), True, (0, 0, 255)), k.locat)
        i = 0
        for n in self.printe:
            self.screen.blit(n, (10, 20 + i * 30))
            i += 1
        self.drawer()
        if not self.headless: pygame.display.update()
        if self.clear_print: self.printe = []

    events = []

    def drawer(self):
        pass

    pause=False
    def runner(self, blit=True):
        # self.pressed=pygame.key.get_pressed()
        self.screen.fill(self.backgroundColor)
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: self.running = False
                elif event.key==K_BACKQUOTE:self.pause = not self.pause
            elif event.type == QUIT:
                self.running = False
        if self.running:
            if blit: self.bliter()
        else:
            pygame.display.quit()
