// kernel.c - Core Kernel Logic
#define VIDEO_MEMORY 0xB8000
#define WHITE_ON_BLACK 0x0f

void main() {
    char* vidmem = (char*)VIDEO_MEMORY;
    char* msg = "Welcome to Horizon OS! Ready.";
    int i = 0;
    while(msg[i] != 0) {
        vidmem[i*2] = msg[i];
        vidmem[i*2+1] = WHITE_ON_BLACK;
        i++;
    }
    while(1);
}
