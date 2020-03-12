import adv.adv_test
from core.advbase import *
from module.bleed import Bleed
from slot.a import *
from slot.d import *

def module():
    return Botan

class Botan(Adv):
    a3 = ('prep_charge',0.05)
    conf = {}
    conf['slots.a'] = RR() + Jewels_of_the_Sun()
    conf['slots.d'] = Shinobi()
    conf['acl'] = """
        `s3, not self.s3_buff and pin='prep'
        `s2
        `s1, cancel
    """

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff
    
    def prerun(self):
        self.bleed = Bleed("g_bleed",0).reset()

    def s1_proc(self, e):
        Bleed("s1", 1.46).on()

    def s2_proc(self, e):
        self.buff_class('s2',0.1,15,'crit','chance').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)