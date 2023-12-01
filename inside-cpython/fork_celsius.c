/**
Build: gcc -o fork_celsius ./inside-cpython/fork_celsius.c
Usage: ./fork_celsius 10
**/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

static const double five_ninths = 5.0/9.0;

double celsius(double fahrenheit) {
    return (fahrenheit - 32) * five_ninths;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        return -1;
    }

    int number = atoi(argv[1]);

    for (int i = 1; i <= number; i++) {
        double f_value = 100 + (i*10);
        pid_t child = fork();

        /* Child process will continue from here: */
        if (child == 0) {
            double c_value = celsius(f_value);
            printf("%f F is %f C (PID %d)\n", f_value, c_value, getpid());
            exit(0);  // Exit process
        }
    }

    printf("Spawned %d processes from %d\n", number, getpid());
    return 0;
}