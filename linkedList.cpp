#include<cstdio>
#include<cstdlib>
#include<cstring>

struct Node{
    int key;
    Node *next, *prev;
};
Node *nil;

Node* listSearch(int key) {
    Node *cur = nil->next;
    while ( cur != nil && cur->key != key){
        cur = cur->next;
    }
    return cur;
}

void init(){
    nil = (Node *)malloc(sizeof(Node));
    nil->next = nil;
    nil->prev = nil;
}

void insert(int key){
    Node *x = (Node *)malloc(sizeof(Node));
    x->key = key;
    x->next = nil->next;
    nil->next->prev = x;
    nil->next = x;
    x->prv = nil;
}


