#include "queue.h"
#include <setjmp.h>
#include <cmocka.h>


// int main() {
//   /* Allocate space for the variable pointer. */
// int *value =(int *)malloc(sizeof(int));
//
//   /* Allocate space for the queue. */
// queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
//
// init(Q_t);
// enqueue(Q_t,4);
// enqueue(Q_t,3);
// enqueue(Q_t,7);
// enqueue(Q_t,8);
// enqueue(Q_t,9);
// enqueue(Q_t,10);
//
// is_empty(Q_t);
// dequeue(Q_t,value);
//
// printf("The value is: %d \n",*value );
// is_empty(Q_t);
// }

/* A test case that does nothing and succeeds. */
static void null_test_success(void **state) {
    (void) state; /* unused */
}

// test that the queue is empty at after creating it
static void empty(void **state) {
	(void) state; /* unused */

	  /* Allocate space for the queue. */
	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t);

		assert_int_equal(is_empty(Q_t), 1);

}


// test that the queue is full when all elements have values
static void full(void **state) {
	(void) state; /* unused */

	  /* Allocate space for the queue. */
	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t);
  for(int i = 0;i<8;i++){
    enqueue(Q_t,i);
  }

		assert_int_equal(is_empty(Q_t), 0);
    assert_int_equal(*Q_t->elements_counter, 5);


}

// test that am error is being returned when attempting to remove
// an element from an empty queue
static void remove_element_from_empty_queue (void **state) {
	(void) state; /* unused */
  int *value =(int *)malloc(sizeof(int));

	  /* Allocate space for the queue. */
	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t);

	assert_int_equal(dequeue(Q_t, value), -1);

}

// test that am error is being returned when attempting to add
// an element to a full queue
static void add_element_to_a_full_queue(void **state) {
	(void) state; /* unused */

	  /* Allocate space for the queue. */
	queue_t *Q_t = (queue_t *)malloc(sizeof(queue_t));
	init(Q_t);
  for(int i = 0;i<5;i++){
    enqueue(Q_t,i);
  }
  int num = 8;
		assert_int_equal( enqueue(Q_t,num), -1);

}

int main(void) {
    const struct CMUnitTest tests[] = {
				cmocka_unit_test(empty),
        cmocka_unit_test(full),
        cmocka_unit_test(null_test_success),
        cmocka_unit_test(add_element_to_a_full_queue),
        cmocka_unit_test(remove_element_from_empty_queue),

    };
    return cmocka_run_group_tests(tests, NULL, NULL);
}
