#include "queue.h"

 void init(queue_t* q){
	printf("Queue initlization \n");

  //Initialize elements_counter to zero
  q->elements_counter = (int * )malloc(sizeof(int));
  *q->elements_counter = 0;

	/* Allocate space for the elements of the queue.
	*  Assuming the the queue size is fixed and equal 5
	*/
	q->elements = (int * )malloc(5 * sizeof(int));

	/* Initialize pointers. */
	q->tail = q->head = &q->elements[0];

}

int enqueue(queue_t* q, int val){
 	printf("enqueue\n");

	int volatile* nextTail;

  // return an error in case of attempting to add
  // an element to a full queue
  if(*q->elements_counter == 5)  return -1;

  (*q->elements_counter)++;
printf("%d \n", *q->elements_counter );
  //Update the pointer of the current element
  nextTail = q->tail + 1;

	if (nextTail == &q->elements[4]) {
		/* Wrap around. */
		nextTail = &q->elements[0];
	}

	if (nextTail == q->head) {

		return 0;
	} else {
		*q->tail = val;
		q->tail = nextTail;
		return 1;
	}

}

int dequeue(queue_t* q, int* val){
 printf("dequeue\n");

// return an error in case of attempting to remove
// an element from an empty queue
if(is_empty(q)== QUEUE_IS_EMPTY) return -1;
(*q->elements_counter)--;

 *val = *(q->head++);

 if (q->head == &q->elements[4]) {
   /* Wrap around. */
   q->head = &q->elements[0];
 }

 return 1;}

bool is_empty(queue_t* q){
printf("is empty\n");
if (*q->elements_counter == 0) {
  /* Queue is empty. */

  printf("Queue is empty\n");
  return QUEUE_IS_EMPTY;
}else {
  /*Queue is not empty*/
  printf("Queue is not empty\n");
  return 0;

}

}
