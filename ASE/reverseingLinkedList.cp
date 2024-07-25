//reverse a linked list

#include <stdio.h>
#include <stdlib.h>

typedef struct myNode{
    int val;
    struct myNode* next;
} node;

node *start = NULL;

void insertAtEnd(int);
void print(node *);
void reversing();

int main(){
    int term;
    for(int i = 0; i < 5; i++){
        scanf("%d", &term);
        insertAtEnd(term);
    }
    print(start);
    reversing();
}

void insertAtEnd(int val){
    node *newptr = (node *)malloc(sizeof(node));
    if(start == NULL){
        start = newptr;
        newptr->next = NULL;
        newptr->val = val;
    }
    else{
        node *ptr = start;
        while(ptr->next != NULL){
            ptr = ptr->next;
        }
        ptr->next = newptr;
        newptr->val = val;
        newptr->next = NULL;
    }
}

void print(node *s){
    node *ptr = s;
    while(ptr != NULL){
        printf("%d\t", ptr->val);
        ptr = ptr->next;
    }
}

void reversing(){
    // node *newptr = (node *)malloc(sizeof(node));
    node *start2 = NULL;
    node *ptr = start;
    while(ptr != NULL){
        node *newptr = (node *)malloc(sizeof(node));
        if(start2 == NULL){
            newptr->val = ptr->val;
            newptr->next = NULL;
            start2 = newptr;
        }
        else{
            newptr->val = ptr->val;
            newptr->next = start2;
            start2 = newptr;
        }
        ptr = ptr->next;
    }
    printf("\nReversed list: \n");
    print(start2);
}