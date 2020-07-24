CC = gcc
CFLAGS  = -g -Wall
LIBS=-l cmocka
INCLUDES=-I/Q1

SRCS = Q1/main.c Q1/queue.c
OBJS = $(SRCS:.c=.o)
MAIN = Unit_Tests



$(MAIN): $(OBJS)
	        $(CC) $(CFLAGS) $(INCLUDES) -o $(MAIN) $(OBJS) $(LIBS)
.c.o:
	        $(CC) $(CFLAGS) $(INCLUDES) -c $<  -o $@


.PHONY: clean

clean:
				rm -f Q1/*.o *~ core $(INCDIR)/*~
