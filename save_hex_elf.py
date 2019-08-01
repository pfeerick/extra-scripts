# Written by dsb
# Origin: https://community.platformio.org/t/how-to-build-without-uploading-specific-source-files-using-src-filter/8972/3

Import("env", "projenv")
from shutil import copyfile

def save_hex(*args, **kwargs):
    print("Copying hex output to project directory...")
    target = str(kwargs['target'][0])
    copyfile(target, 'output.hex')
    print("Done.")

def save_elf(*args, **kwargs):
    print("Copying elf output to project directory...")
    target = str(kwargs['target'][0])
    copyfile(target, 'output.elf')
    print("Done.")

env.AddPostAction("$BUILD_DIR/${PROGNAME}.elf", save_elf)   #post action for the target hex file
env.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", save_hex)   #post action for the target hex 
