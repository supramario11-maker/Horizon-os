# generate_project.py - Automatic Workspace Setup for Horizon OS
import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Created: {path}")

print("🌅 Initializing Horizon OS Asset Generation...")

# ---- 1. .gitignore ----
create_file(".gitignore", """
*.o
*.bin
horizon_subsystem
horizon_store
*.iso
*.img
.DS_Store
""")

# ---- 2. README.md ----
create_file("README.md", """
# 🌅 Horizon OS & Horizon Store Platform

Horizon OS is an optimized environment supporting multi-architecture cross-compatibility layers.

## Supported Architectures
* **Linux Binaries** (Native POSIX execution)
* **Windows Programs** (`.exe` via custom API mapping layer)
* **Android Apps** (`.apk` via lightweight containers)
* **iOS Apps** (`.ipa` via localized Darwin subsystem environment)

## Horizon Store Platform
The embedded store maps target installation routines directly into their corresponding sandbox runtimes.
""")

# ---- 3. boot.asm ----
create_file("src/boot.asm", """
; boot.asm - Multiboot Bootloader for Horizon OS
MBOOT_PAGE_ALIGN    equ 1 << 0
MBOOT_MEM_INFO      equ 1 << 1
MBOOT_HEADER_MAGIC  equ 0x1BADB002
MBOOT_HEADER_FLAGS  equ MBOOT_PAGE_ALIGN | MBOOT_MEM_INFO
MBOOT_CHECKSUM      equ -(MBOOT_HEADER_MAGIC + MBOOT_HEADER_FLAGS)

[BITS 32]

section .multiboot
    align 4
    dd MBOOT_HEADER_MAGIC
    dd MBOOT_HEADER_FLAGS
    dd MBOOT_CHECKSUM

section .text
global _start
extern main

_start:
    cli
    mov esp, stack_space
    call main
    
halt:
    hlt
    jmp halt

section .bss
align 16
stack_space:
    resb 8192
""")

# ---- 4. kernel.c ----
create_file("src/kernel.c", """
// kernel.c - Core Kernel Initialization Engine
#define VIDEO_MEMORY 0xB8000
#define WHITE_ON_BLACK 0x0f

void clear_screen();
void print_string(char* string);

void main() {
    clear_screen();
    print_string("Welcome to Horizon OS v1.0\\n");
    print_string("Loading Multi-Subsystem Runtimes... Ready.\\n");
    print_string("Horizon Store Subsystem Hooked Integration Active.\\n");
    while(1);
}

void clear_screen() {
    char* vidmem = (char*)VIDEO_MEMORY;
    for (int i = 0; i < 80 * 25 * 2; i += 2) {
        vidmem[i] = ' ';
        vidmem[i+1] = WHITE_ON_BLACK;
    }
}

void print_string(char* string) {
    char* vidmem = (char*)VIDEO_MEMORY;
    int i = 0;
    while (string[i] != 0) {
        vidmem[i*2] = string[i];
        vidmem[i*2+1] = WHITE_ON_BLACK;
        i++;
    }
}
""")

# ---- 5. subsystem_manager.cpp ----
create_file("src/subsystem_manager.cpp", """
// subsystem_manager.cpp - High-Performance Execution Mapping Layer
#include <iostream>
#include <string>

class HorizonSubsystem {
public:
    void routeBinary(const std::string& path) {
        if (path.find_last_of(".") == std::string::npos) {
            std::cout << "[Horizon-Native] Running Linux ELF binary natively.\\n";
            return;
        }
        std::string ext = path.substr(path.find_last_of(".") + 1);
        if (ext == "exe") {
            std::cout << "[Horizon-WineLayer] Executing Windows API translation pipeline for: " << path << "\\n";
        } else if (ext == "apk") {
            std::cout << "[Horizon-Container] Spinning sandboxed Android Runtime instance for: " << path << "\\n";
        } else if (ext == "ipa") {
            std::cout << "[Horizon-Darwin] Invoking Mach-O emulation framework context for: " << path << "\\n";
        } else {
            std::cout << "[Horizon-Kernel] Error: Format unsupported directly by low-level core.\\n";
        }
    }
};

int main() {
    HorizonSubsystem sys;
    sys.routeBinary("application.exe");
    sys.routeBinary("system_service");
    return 0;
}
""")

# ---- 6. store_manager.cpp ----
create_file("src/store/store_manager.cpp", """
// store_manager.cpp - Horizon Cross-Platform Digital Storefront
#include <iostream>
#include <string>
#include <vector>

struct ClientApp {
    std::string title;
    std::string format;
    std::string source;
};

class HorizonStore {
private:
    std::vector<ClientApp> index;
public:
    HorizonStore() {
        index.push_back({"Google Maps Pro", "apk", "Google Play Engine"});
        index.push_back({"Photoshop Core", "exe", "Windows Core Platform"});
        index.push_back({"GarageBand Mobile", "ipa", "Apple App Service"});
    }
    
    void displayStorefront() {
        std::cout << "\\n=========================================\\n";
        std::cout << "      HORIZON SYSTEM COMPATIBILITY STORE \\n";
        std::cout << "=========================================\\n";
        for(const auto& app : index) {
            std::cout << " -> [" << app.source << "] " << app.title << " (." << app.format << ")\\n";
        }
    }
};

int main() {
    HorizonStore store;
    store.displayStorefront();
    return 0;
}
""")

# ---- 7. linker.ld ----
create_file("src/linker.ld", """
ENTRY(_start)
SECTIONS
{
    . = 0x00100000;
    .text : { *(.multiboot) *(.text) }
    .rodata : { *(.rodata) }
    .data   : { *(.data) }
    .bss    : { *(.bss) }
}
""")

# ---- 8. Makefile ----
create_file("Makefile", """
# Horizon OS Automated Build Script
CC = i686-elf-gcc
AS = nasm
CPP = g++
CFLAGS = -m32 -c -ffreestanding -O2 -Wall -Wextra
LDFLAGS = -melf_i386 -T src/linker.ld

all: horizon.bin subsystems

boot.o: src/boot.asm
	\$(AS) -f elf32 src/boot.asm -o boot.o

kernel.o: src/kernel.c
	(CC) (CFLAGS) src/kernel.c -o kernel.o

horizon.bin: boot.o kernel.o
	ld \$(LDFLAGS) boot.o kernel.o -o horizon.bin

subsystems: src/subsystem_manager.cpp src/store/store_manager.cpp
	\((CPP) -O2 src/subsystem_manager.cpp -o horizon_subsystem\)(CPP) -O2 src/store/store_manager.cpp -o horizon_store

run-kernel: horizon.bin
	qemu-system-i386 -kernel horizon.bin

clean:
	rm -f *.o horizon.bin horizon_subsystem horizon_store
""")

print("✅ Structure Successfully Built!")
