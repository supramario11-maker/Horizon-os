# 🌅 Horizon OS

Horizon OS is an optimized, experimental operating system designed to explore multi-architecture runtime execution natively inside a lean kernel environment. 

The goal of Horizon OS is to eventually support multiple binary runtimes simultaneously:
* **Linux Binaries** (Native Execution)
* **Windows Execution** (`.exe` via integrated Win32 API translation)
* **Android Applications** (`.apk` via lightweight containerization)
* **iOS Applications** (`.ipa` via Darwing subsystem emulation)

## 🛠️ Project Structure
* `src/boot.asm` - The x86 Multiboot assembly entry point.
* `src/kernel.c` - Core C initialization code handling video memory text printing.
* `src/subsystem_manager.cpp` - The routing engine managing format translation layers.
* `Makefile` - Orchestrates compilation scripts.

## 🚀 Getting Started

### Prerequisites
You will need a GNU/Linux environment (or WSL), `nasm`, a cross-compiler toolchain, and `qemu`.

```bash
sudo apt install build-essential nasm qemu-system-x86
```

### Compiling and Running
To build the kernel and running subsystems, execute:
```bash
make all
```

To test the raw OS kernel inside the QEMU emulator:
```bash
make run-kernel
```
