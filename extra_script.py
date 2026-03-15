Import("env")

from os.path import join
from shutil import copyfile

# Đường dẫn file firmware
build_dir = env.subst("$BUILD_DIR")
firmware_elf = join(build_dir, "firmware.elf")
firmware_hex = join(build_dir, "firmware.hex")

# Lệnh chuyển ELF -> HEX
env.AddPostAction(
    "$BUILD_DIR/${PROGNAME}.elf",
    env.VerboseAction(
        f"$OBJCOPY -O ihex -R .eeprom {firmware_elf} {firmware_hex}",
        "Generating HEX file..."
    )
)

print("Extra script loaded: HEX export enabled.")