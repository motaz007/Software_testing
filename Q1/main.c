#include "queue.h"
#include <setjmp.h>
#include <cmocka.h>


// test that the queue is empty at after creating it
static void test_empty(void **state) {

	/* Allocate space for the queue. */
	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t, 8);

	assert_true(is_empty(Q_t));
  assert_int_equal(Q_t->max,8);
}


// test that the queue is full when all elements have values
static void test_full(void **state) {

	/* Allocate space for the queue.
	* and initiate a queue of size 5
	 */	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t,5);

	
  for(int i = 0;i<8;i++){
    enqueue(Q_t,i);
  }

		assert_true(!(is_empty(Q_t)));
    assert_int_equal(Q_t->max, 5);
}

// test that am error is being returned when attempting to remove
// an element from an empty queue
static void test_remove_element_from_empty_queue (void **state) {

  int *value =(int *)malloc(sizeof(int));

	/* Allocate space for the queue.
	* and initiate a queue of size 5
	 */	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t,5);

	assert_int_equal(dequeue(Q_t, value), -1);
}

// test that am error is being returned when attempting to add
// an element to a full queue
static void test_add_element_to_a_full_queue(void **state) {

	/* Allocate space for the queue.
	* and initiate a queue of size 5
	 */	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t,5);

  //filling the queue before testing
  for(int i = 0;i<5;i++){
    enqueue(Q_t,i);
  }

		assert_int_equal( enqueue(Q_t,8), -1);
}

// Test the enqueue function
static void test_enqueue(void **state) {

	/* Allocate space for the queue.
	* and initiate a queue of size 5
	 */	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t,5);

  //testing that the tail is the same as the last element of the queue
  for(int i = 0;i<4;i++){
		enqueue(Q_t,i);
		//debug printf("%d\n",*(Q_t->tail - 1) );
		//debug printf("%d \n",Q_t->elements[i] );
		assert_int_equal(Q_t->elements[i],*(Q_t->tail - 1));
  }
}

// Test the dequeue function
static void test_dequeue(void **state) {

	int *value =(int *)malloc(sizeof(int));

	 /* Allocate space for the queue.
	 * and initiate a queue of size 5
	  */
	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t,5);

  //fill the queue for the test
  for(int i = 0;i<5;i++){
		enqueue(Q_t,i);
  }

	for(int i = 0;i<5;i++){
		dequeue(Q_t,value);
		//debug printf("%d\n",*Q_t->head );
		//debug printf("%d\n",Q_t->elements[i] );
		//debug printf("%d\n",*value );
		assert_int_equal(*value,i);
	}


}

/**
 * Main entry point of the test.
*/
int main(void) {
    const struct CMUnitTest tests[] = {
				cmocka_unit_test(test_empty),
        cmocka_unit_test(test_full),
        cmocka_unit_test(test_add_element_to_a_full_queue),
        cmocka_unit_test(test_remove_element_from_empty_queue),
				cmocka_unit_test(test_enqueue),
				cmocka_unit_test(test_dequeue),

    };
    return cmocka_run_group_tests(tests, NULL, NULL);
}
