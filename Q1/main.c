#include "queue.h"
#include <setjmp.h>
#include <cmocka.h>


// test that the queue is empty at after creating it
static void empty(void **state) {

	/* Allocate space for the queue. */
	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t, 8);

	assert_true(is_empty(Q_t));
  assert_int_equal(Q_t->max,8);
}


// test that the queue is full when all elements have values
static void full(void **state) {

	/* Allocate space for the queue. */
	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t,5);
  for(int i = 0;i<8;i++){
    enqueue(Q_t,i);
  }

		assert_true(!(is_empty(Q_t)));
    assert_int_equal(Q_t->max, 5);
}

// test that am error is being returned when attempting to remove
// an element from an empty queue
static void remove_element_from_empty_queue (void **state) {

  int *value =(int *)malloc(sizeof(int));

	/* Allocate space for the queue. */
	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t,5);

	assert_int_equal(dequeue(Q_t, value), -1);
}

// test that am error is being returned when attempting to add
// an element to a full queue
static void add_element_to_a_full_queue(void **state) {

	  /* Allocate space for the queue. */
	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t,5);

  //filling the queue before testing
  for(int i = 0;i<5;i++){
    enqueue(Q_t,i);
  }
  
		assert_int_equal( enqueue(Q_t,8), -1);
}


/**
 * Main entry point of the test.
*/
int main(void) {
    const struct CMUnitTest tests[] = {
				cmocka_unit_test(empty),
        cmocka_unit_test(full),
        cmocka_unit_test(add_element_to_a_full_queue),
        cmocka_unit_test(remove_element_from_empty_queue),

    };
    return cmocka_run_group_tests(tests, NULL, NULL);
}
