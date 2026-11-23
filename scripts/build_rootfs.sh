#!/bin/bash
# MicroOS Root Filesystem Generation Pipeline
# Assembles minimal, standards-compliant rootfs with BusyBox, MicroOS utilities, and Micro Arcade

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJ_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ROOTFS_DIR="$PROJ_DIR/rootfs"

echo "=== Assembling MicroOS Root Filesystem ==="

# 1. Clean and create directory structure
mkdir -p "$ROOTFS_DIR"
cd "$ROOTFS_DIR"
rm -rf bin sbin usr etc lib lib64 proc sys dev tmp run mnt root home var

mkdir -p bin sbin usr/bin usr/sbin usr/games usr/lib lib lib64 proc sys dev \
         etc/init.d etc/network tmp run mnt/ssd mnt/usb mnt/storage root home/micro \
         var/log var/run var/games var/lib/iwd var/lib/dpkg var/cache/apt

chmod 1777 tmp
chmod 0700 root
chmod 0755 home/micro

# 2. Integrate BusyBox
echo "  [BUSYBOX] Installing BusyBox multicall binaries and applets..."
BUSYBOX_BIN=$(which busybox || echo "/bin/busybox")
if [ ! -x "$BUSYBOX_BIN" ]; then
    echo "[ERROR] busybox not found in build environment!"
    exit 1
fi

cp "$BUSYBOX_BIN" bin/busybox
chmod 4755 bin/busybox

# Install BusyBox symlinks into bin, sbin, usr/bin, usr/sbin
for applet in $(./bin/busybox --list); do
    if [ ! -e "bin/$applet" ] && [ ! -e "sbin/$applet" ] && [ ! -e "usr/bin/$applet" ] && [ ! -e "usr/sbin/$applet" ]; then
        case "$applet" in
            init|halt|poweroff|reboot|mdev|ifconfig|route|ip|fdisk|fsck|modprobe|insmod|rmmod|lsmod)
                ln -sf /bin/busybox "sbin/$applet"
                ;;
            sh|ash|bash|login|mount|umount|cat|ls|cp|mv|rm|mkdir|rmdir|touch|chmod|chown|sync|sleep|date|uname|dmesg|kill|ps|ping|clear|hostname|uptime|udhcpc)
                ln -sf /bin/busybox "bin/$applet"
                ;;
            *)
                ln -sf /bin/busybox "usr/bin/$applet"
                ;;
        esac
    fi
done

# Ensure /bin/sh points to busybox ash
ln -sf /bin/busybox bin/sh
ln -sf /bin/busybox bin/ash

# 3. Install MicroOS Shell & System Utilities
echo "  [UTILS] Installing MicroOS custom CLI tools..."
rm -f usr/bin/hardware usr/bin/disks bin/mount bin/unmount bin/umount usr/bin/wifi usr/bin/net usr/bin/ping bin/ping usr/bin/apt usr/bin/sysinfo usr/bin/dashboard usr/bin/settings usr/bin/control usr/bin/diagnostics usr/bin/help

cp "$PROJ_DIR/hardware/hardware" usr/bin/hardware
chmod +x usr/bin/hardware

cp "$PROJ_DIR/storage/disks" usr/bin/disks
chmod +x usr/bin/disks

cp "$PROJ_DIR/storage/safe_mount" bin/mount
chmod +x bin/mount

cp "$PROJ_DIR/storage/safe_unmount" bin/unmount
chmod +x bin/unmount
ln -sf /bin/unmount bin/umount

cp "$PROJ_DIR/networking/wifi" usr/bin/wifi
chmod +x usr/bin/wifi

cp "$PROJ_DIR/networking/net" usr/bin/net
chmod +x usr/bin/net

cp "$PROJ_DIR/networking/ping" usr/bin/ping
chmod 4755 usr/bin/ping
ln -sf /usr/bin/ping bin/ping

mkdir -p usr/share/udhcpc
cp "$PROJ_DIR/configs/default.script" usr/share/udhcpc/default.script
chmod +x usr/share/udhcpc/default.script

cp "$PROJ_DIR/package-manager/apt" usr/bin/apt
chmod +x usr/bin/apt

cp "$PROJ_DIR/shell/sysinfo" usr/bin/sysinfo
chmod +x usr/bin/sysinfo

cp "$PROJ_DIR/shell/dashboard" usr/bin/dashboard
chmod +x usr/bin/dashboard

cp "$PROJ_DIR/shell/settings" usr/bin/settings
chmod +x usr/bin/settings
ln -sf /usr/bin/settings usr/bin/control

cp "$PROJ_DIR/shell/diagnostics" usr/bin/diagnostics
chmod +x usr/bin/diagnostics

cp "$PROJ_DIR/shell/help" usr/bin/help
chmod +x usr/bin/help

# 4. Install Micro Arcade Games
echo "  [ARCADE] Installing terminal arcade games into /usr/games..."
for g in snake tetris pong mines 2048 guess tictactoe spaceinvaders arcade; do
    if [ -f "$PROJ_DIR/build/games/$g" ]; then
        rm -f "usr/games/$g" "usr/bin/$g"
        cp "$PROJ_DIR/build/games/$g" usr/games/
        chmod +x "usr/games/$g"
        ln -sf "/usr/games/$g" "usr/bin/$g"
    fi
done

# 5. Install Init & Boot Scripts
echo "  [INIT] Installing /init orchestrator and inittab..."
cp "$PROJ_DIR/init/init" init
chmod 0755 init

cp "$PROJ_DIR/init/inittab" etc/inittab
chmod 0644 etc/inittab

cp "$PROJ_DIR/init/rcS" etc/init.d/rcS
chmod 0755 etc/init.d/rcS

cp "$PROJ_DIR/init/rcK" etc/init.d/rcK
chmod 0755 etc/init.d/rcK

# 6. Install Shell Configuration & Banner
cp "$PROJ_DIR/shell/profile" etc/profile
chmod 0644 etc/profile

# 7. Create standard system files (/etc/passwd, group, issue, fstab)
cat <<'EOF' > etc/passwd
root:x:0:0:root:/root:/bin/sh
micro:x:1000:1000:micro:/home/micro:/bin/sh
EOF

cat <<'EOF' > etc/group
root:x:0:
micro:x:1000:
audio:x:29:micro
video:x:44:micro
wheel:x:10:root,micro
EOF

cat <<'EOF' > etc/shadow
root:::0:99999:7:::
micro:::0:99999:7:::
EOF
chmod 0600 etc/shadow

cat <<'EOF' > etc/issue
MicroOS v2.0 (x86_64) - Minimal Linux. Maximum control.
\l on \n

EOF

cat <<'EOF' > etc/fstab
# /etc/fstab: static filesystem information
proc            /proc        proc     defaults          0 0
sysfs           /sys         sysfs    defaults          0 0
devpts          /dev/pts     devpts   mode=0620,gid=5   0 0
tmpfs           /run         tmpfs    mode=0755,nosuid  0 0
tmpfs           /tmp         tmpfs    mode=1777         0 0
EOF

# 8. Copy Essential Shared Libraries (libc, libm, ld-linux)
echo "  [LIBS] Staging minimal glibc shared libraries..."
LIBC_PATH=$(ldconfig -p | grep "libc.so.6" | awk '{print $NF}' | head -n1 || echo "/lib/x86_64-linux-gnu/libc.so.6")
LIBM_PATH=$(ldconfig -p | grep "libm.so.6" | awk '{print $NF}' | head -n1 || echo "/lib/x86_64-linux-gnu/libm.so.6")
LD_LINUX=$(ldconfig -p | grep "ld-linux-x86-64.so.2" | awk '{print $NF}' | head -n1 || echo "/lib64/ld-linux-x86-64.so.2")

for lib in "$LIBC_PATH" "$LIBM_PATH"; do
    if [ -f "$lib" ]; then
        cp -L "$lib" lib/
        strip --strip-unneeded lib/$(basename "$lib") 2>/dev/null || true
    fi
done

if [ -f "$LD_LINUX" ]; then
    cp -L "$LD_LINUX" lib64/
    ln -sf /lib64/$(basename "$LD_LINUX") lib/$(basename "$LD_LINUX") || true
fi

# Stage wireless utilities (iwd, iwctl) and dependencies
echo "  [WIFI] Staging iwd daemon and iwctl wireless controller..."
if [ -x /usr/libexec/iwd ]; then
    cp /usr/libexec/iwd usr/sbin/iwd
    chmod 0755 usr/sbin/iwd
    strip --strip-unneeded usr/sbin/iwd 2>/dev/null || true
fi
if [ -x /usr/bin/iwctl ]; then
    cp /usr/bin/iwctl usr/bin/iwctl
    chmod 0755 usr/bin/iwctl
    strip --strip-unneeded usr/bin/iwctl 2>/dev/null || true
fi

for l in "libell.so.0" "libreadline.so.8" "libtinfo.so.6"; do
    LPATH=$(ldconfig -p | grep "$l" | awk '{print $NF}' | head -n1 || true)
    if [ -f "$LPATH" ]; then
        cp -L "$LPATH" lib/
        strip --strip-unneeded "lib/$(basename "$LPATH")" 2>/dev/null || true
    fi
done

# 9. Copy Essential Kernel Modules
echo "  [MODS] Staging essential kernel modules in /lib/modules/7.0.0-43-generic..."
KMOD_DIR="lib/modules/7.0.0-43-generic"
mkdir -p "$KMOD_DIR"
if [ -d "$PROJ_DIR/kernel/modules" ]; then
    cp "$PROJ_DIR/kernel/modules"/*.ko* "$KMOD_DIR/" 2>/dev/null || true
fi

echo "=== Root Filesystem Assembly Complete ==="
echo "Size: $(du -sh "$ROOTFS_DIR" | cut -f1)"
