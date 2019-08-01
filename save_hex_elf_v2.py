try:
    import configparser
except ImportError:
    import ConfigParser as configparser

config = configparser.ConfigParser()
config.read("platformio.ini")

def save_hex(**kwargs):
    target = str(kwargs['target'][0])
    savename = target.split('\\')[-2]   # name of environment
    savepath = config.get('env:{}'.format(savename), "savepath")
    savefile = '{}\{}.hex'.format(savepath, savename)
    copyfile(target, savefile)
    
def save_elf(**kwargs):
    target = str(kwargs['target'][0])
    savename = target.split('\\')[-2]   # name of environment
    savepath = config.get('env:{}'.format(savename), "savepath")
    savefile = '{}\{}.elf'.format(savepath, savename)
    copyfile(target, savefile)
