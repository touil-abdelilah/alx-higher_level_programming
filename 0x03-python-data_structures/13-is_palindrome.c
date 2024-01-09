#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int len = 0, i = 0;
    int arr[10000];  /* Maximum assumed list length */

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (current != NULL)
    {
        arr[len] = current->n;
        current = current->next;
        len++;
    }

    while (i < len / 2)
    {
        if (arr[i] != arr[len - i - 1])
            return (0);
        i++;
    }
    return (1);
}
