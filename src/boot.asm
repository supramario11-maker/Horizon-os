; boot.asm - Master Boot Initialization Block (Pure x86 Assembly)
[BITS 16]
[ORG 0x7C00]

start:
    cli                         ; Disable interrupts
    xor ax, ax                  ; Clear segment registers
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7C00              ; Set stack cursor below boot sector

    mov si, boot_msg
    call print_string_16

    ; Jump directly to 32-bit Protected Mode for Hypervisor Execution
    lgdt [gdt_descriptor]
    mov eax, cr0
    or eax, 0x1
    mov cr0, eax
    jmp CODE_SEG:init_pm

[BITS 16]
print_string_16:
    lodsb
    or al, al
    jz .done
    mov ah, 0x0E
    int 0x10
    jmp print_string_16
.done:
    ret

boot_msg db 'Horizon OS Stage 1 Assembly Boot Block Active...', 13, 10, 0

; Global Descriptor Table Definition
gdt_start:
    dd 0x0
    dd 0x0
gdt_code:
    dw 0xFFFF
    dw 0x0
    db 0x0
    db 10011010b
    db 11001111b
    db 0x0
gdt_data:
    dw 0xFFFF
    dw 0x0
    db 0x0
    db 10010010b
    db 11001111b
    db 0x0
gdt_end:

gdt_descriptor:
    dw gdt_end - gdt_start - 1
    dd gdt_start

CODE_SEG equ gdt_code - gdt_start
DATA_SEG equ gdt_data - gdt_start

[BITS 32]
init_pm:
    mov ax, DATA_SEG
    mov ds, ax
    mov ss, ax
    mov es, ax
    mov fs, ax
    mov gs, ax
    jmp 0x100000                ; Jump directly to the loaded kernel address space

times 510-($-$$) db 0
dw 0xAA55
