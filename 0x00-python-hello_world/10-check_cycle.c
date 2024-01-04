#include "lists.h"
#include <stdio.h>

/* Function to check for cycle */
int check_cycle(listint_t *list) {
    listint_t *slow = list, *fast = list;

    while (slow && fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast)
            return 1; /* Cycle detected */
    }

    return 0; /* No cycle found */
}
