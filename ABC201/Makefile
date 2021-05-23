all: a b

CC = gcc
CFLAGS = -O3 -std=c99 -Wall

a: a.c
	$(CC) $(CFLAGS) -o $@ $^ -lm

b: b.c
	$(CC) $(CFLAGS) -o $@ $^ -lm

clean:
	rm -f a b *.o 
	
