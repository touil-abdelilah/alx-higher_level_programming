#ifndef LISTS_H
#define LISTS_H

/* Definition for singly-linked list */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function prototype */
int check_cycle(listint_t *list);

#endif /* LISTS_H */
