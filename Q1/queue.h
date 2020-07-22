/* The Queue is assumed to be of fixed size the that size is 5.
*  The elements of the queue are assumed to be intergers.
*
*/


#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define QUEUE_IS_EMPTY 1
#define QUEUE_IS_FULL 2

struct queue {
  int* elements_counter;
	int* elements;
	int volatile* tail;
	int volatile* head;
};


typedef struct queue queue_t;

void init(queue_t* q);
int enqueue(queue_t* q, int val);
int dequeue(queue_t* q, int* val);
bool is_empty(queue_t* q);
