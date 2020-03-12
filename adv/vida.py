from core.advbase import *
from module.x_alt import Fs_alt

def module():
    return Vida

class Vida(Adv):
    a1 = ('fs',0.30)
    conf = {}
    conf['acl'] = """
        `s3, not self.s3_buff
        `s1
        `s2, fsc
        `fs, x=5
        """

    def prerun(self):
        conf_fs_alt = {'fs.dmg': 0.110, 'fs.hit': 6}
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt))

    def s2_proc(self, e):
        self.fs_alt.on(3)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)