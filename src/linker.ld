ENTRY(_start)
SECTIONS
{
    . = 0x40080000; /* Maps directly to native ARM64 virtual environment boot steps */
    .text : { *(.text) }
    .data : { *(.data) }
    .bss  : { *(.bss) }
}
