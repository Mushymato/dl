from core.advbase import *

class Joker(Adv):    
    def prerun(self):
        self.dragondrive = self.dragonform.set_dragondrive(ModeManager(
            group='ddrive',
            x=True, fs=True, s1=True, s2=True
        ), drain=75)

    def fs_ddrive_proc(self, e):
        # need further investigation on how this works
        self.dmg_make('x_arsene', 2.9)

    def x_ddrive_proc(self, e):
        # need further investigation on how this works
        if e.base in ('x3', 'x6'):
            self.dmg_make('x_arsene', 2.56)

variants = {None: Joker}
