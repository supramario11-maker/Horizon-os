// kernel.c - ARM64 Embedded System Vector initialization
void main() {
    // Standard RAM diagnostic address location pointer assignment
    volatile char* uart = (volatile char*)0x09000000; 
    char* msg = "Welcome to Horizon OS (ARM64 Mobile Build Mode Active)\n";
    
    int i = 0;
    while (msg[i] != 0) {
        *uart = msg[i]; // Forward payload characters straight to core terminal channels
        i++;
    }
    
    while(1); // Keep CPU alive safely
}

void _start() {
    main();
}
