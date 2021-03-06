from core.advbase import *

class Mona(Adv):
    def prerun(self):
        self.dragondrive = self.dragonform.set_dragondrive(ModeManager(
            group='ddrive',
            x=True, fs=True, s1=True, s2=True
        ), drain=75)
        self.beast_eye = Selfbuff('beast_eye', 0.2, 30, 'utph', 'buff').ex_bufftime()
        Event('dragondrive').listener(self.ddrive_buff_off)

    def fs_proc(self, e):
        self.beast_eye.on()

    def fs_ddrive_proc(self, e):
        self.dmg_make('x_zorro', 2.0)

    def x_ddrive_proc(self, e):
        if e.base == 'x3':
            self.dmg_make('x_zorro', 2.0)
        if e.base == 'x5':
            self.dmg_make('x_zorro', 2.0)
            self.add_hp(5)

    def ddrive_buff_off(self, e):
        self.beast_eye.off()


class Mona_RNG(Mona):
    def s1_before(self, e):
        if e.group == 'ddrive':
            if random.random() <= 0.25:
                log('s1_ddrive', 'variant', 'plus')
                self.conf.s1_ddrive.attr = self.conf.s1_ddrive.attr_plus
            else:
                log('s1_ddrive', 'variant', 'base')
                self.conf.s1_ddrive.attr = self.conf.s1_ddrive.attr_base
        

variants = {
    None: Mona,
    'RNG': Mona_RNG
}
