#include <stdio.h>

#ifdef LINUX

#include <termios.h>
#include <sys/ioctl.h>
#include <sys/select.h>
#include <unistd.h>

static struct termios oldt, newt;
void stop();
void resume();

int kbhit() {
    resume();
    int bytesWaiting;
    ioctl(STDIN_FILENO, FIONREAD, &bytesWaiting);
    if (bytesWaiting) {
        printf("KBHIT!\n");
    }
    stop();
    return bytesWaiting > 0;
}

int getch() {
    printf("Waiting on ch...");
    resume();
    int ch = getchar();
    stop();
    return ch;
}

#endif

void init() {
    #ifdef LINUX
    tcgetattr( STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr( STDIN_FILENO, TCSANOW, &newt);
    #endif
    return;
}

void resume() {
    #ifdef LINUX
    tcsetattr( STDIN_FILENO, TCSANOW, &newt);
    #endif
    return;
}

int isInputReady() {
    return kbhit();
}

char getCharacter() {
    char ch = (char) getch();
    printf("%c", ch);
    return ch;
}

void stop() {
    #ifdef LINUX
    tcsetattr( STDIN_FILENO, TCSANOW, &oldt);
    #endif
    return;
}