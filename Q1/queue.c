#include "queue.h"


/**
 * @brief Initiate the circular queue.
 * @param[in] q a pointer to the queue struct.
 * @param[in] size the size of the queue.
*/
void init(queue_t* q, int size){
  //Debug: printf("Queue initlization \n");

  //Initialize size of the buffer
  // q->max = (int * )malloc(sizeof(int));
  q->max = size;
  q->status = QUEUE_IS_EMPTY;
	/* Allocate space for the elements of the queue.*/
	q->elements = (int * )malloc(size * sizeof(int));

	/* Initialize pointers. */
	q->tail = q->head = &q->elements[0];

}

/**
 * @brief adding elements to the circular queue.
 * @param[in] q a pointer to the queue struct.
 * @param[in] val the elements to add to of the queue.
*/
int enqueue(queue_t* q, int val){
 	//Debug: printf("enqueue\n");

	int volatile* nextTail;

  // return an error in case of attempting to add
  // an element to a full queue
  if(q->full){
    printf("Queue is full\n");
    return -1;
  }

  //Update the pointer of the current element
  nextTail = q->tail + 1;


	if (nextTail == &q->elements[(q->max)]) {
		/* Wrap around. */
		nextTail = &q->elements[0];

	}

  //If the tail reaches the head, the queue is full
	if (nextTail == q->head )
  {
      q->full = true;
      q->status = QUEUE_IS_FULL;
      *q->tail = val;

      return 0;

  }else{

		*q->tail = val;
		q->tail = nextTail;
    return 1;
  }
}

/**
 * @brief remove an element from the circular queue.
 * @param[in] q a pointer to the queue struct.
 * @param[in] val a pointer that will take the value of an element
 * from the queue.
*/
int dequeue(queue_t* q, int* val){
  //Debug: printf("dequeue\n");
  int volatile* nextHead;


  // return an error in case of attempting to remove
  // an element from an empty queue
  if(is_empty(q)) return -1;


  *val = *q->head;
   nextHead = q->head + 1;

  if (nextHead == &q->elements[q->max]) {
    /* Wrap around. */
    nextHead = &q->elements[0];
  }

  if(q->head == q->tail && (q->status != QUEUE_IS_EMPTY)){
    q->status = QUEUE_IS_EMPTY;
    return 0;
  }else{
    q->head = nextHead;
    return 1;

  }
}

/**
 * @brief check if the queue is empty or not.
 * @param[in] q a pointer to the queue struct.
*/
bool is_empty(queue_t* q)
{
  //debug printf("is empty\n");
  if(q->status == QUEUE_IS_EMPTY)
    return 1;
  else{
    return 0;
  }
}
