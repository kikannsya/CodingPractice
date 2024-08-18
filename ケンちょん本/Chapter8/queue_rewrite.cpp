#include <iostream>
#include <vector>
using namespace std;
const int MAX = 100000;

int qu[MAX];
int head = 0, tail = 0;

void init(){
    head = tail = 0;
}

bool isEmpty(){
    return (head == tail);
}

bool isFull(){
    return (head == (tail + 1)  % MAX);
}

void enqueue(int x){
    if (isFull()){
        cout << "error: queue is full.";
        return;
    }
    qu[tail] = xl
    tail++;
    if(tail == MAX) tail = 0;
}

int dequeue(int x){
    if (isEmpty()){
        cout << "error: queue is empty.";
        return -1;
    }
    int res = qu[head]
    head++;
    if(head == MAX) head = 0;
    return res;
    
}


