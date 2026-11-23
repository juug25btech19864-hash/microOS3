# MicroOS v2.0 Release Notes

**Minimal Linux. Maximum Control.**

MicroOS v2.0 is an ultra-lightweight, bootable x86_64 Linux operating system upgraded with a modern Windows 11/macOS-inspired terminal experience, complete network management, real Wi-Fi stack, and an interactive Control Center.

## Highlights
- **Under 50 MB Hard Limit**: Base bootable medium occupies **31 MB (33112064 bytes)**, strictly meeting project constraints.
- **Modern Terminal Experience**: Clean, colorized terminal styling inspired by modern Windows Terminal and macOS Terminal, featuring Unicode box banners and emerald prompts (`micro@micro ~ $`).
- **Interactive Control Center (`dashboard`)**: 8-module Control Center for rapid access to system metrics, networking, storage, retro arcade games, and settings.
- **Unified Network Management (`net`)**: Live network status card, interface enumeration, route tracking, and DNS inspection.
- **Native Wi-Fi Controller (`wifi`)**: Full interactive menu, network scanning, secure interactive password masking, and `iwd`/`iwctl` subsystem integration.
- **Diagnostic Network Stack (`ping` & `diagnostics`)**: Intelligent ICMP ping reporting packet loss and latency statistics with descriptive offline hints, plus automated 8-point system diagnostic test runner.
- **Dynamic Help Architecture (`help`)**: Category-grouped reference with support for specific subcommands (`help wifi`, `help net`, `help ping`, etc.) and unknown command detection.
- **Dual Boot Architecture**: Seamlessly boots on modern UEFI systems and legacy BIOS machines.
- **Built-in Micro Arcade**: 8 standalone offline C terminal arcade games (`snake`, `tetris`, `pong`, `mines`, `2048`, `guess`, `tictactoe`, `spaceinvaders`, and `arcade` menu launcher).
- **Persistent Debian APT**: Independent persistent userspace architecture supporting Debian-compatible packages on attached SSD storage.
