#include<iostream>   
using namespace std;
class Node {
    public:
    int data;
     Node* next;
     Node() {
        this->data =0;
        this->next = NULL;
     }
     Node(int data){
        this->data = data;
        this->next = NULL;
     }
};
void insertAtHead(Node* &head,Node*&tail,int data){
    if(head ==NULL){
        Node* newNode=new Node(data);
        head=newNode;
        tail=newNode;
        return;
    }
              Node* newNode= new Node(data);
              newNode->next =head; 
              head=newNode;
}
void insertAtTail(Node* &head,Node* &tail,int data){
             if(head ==NULL){
        Node* newNode=new Node(data);
        head=newNode;
        tail=newNode;
        return;
    }
      
       Node* newNode = new Node(data);

            if(tail==NULL){
         
                  tail = newNode;
                  head=newNode;
           }
      else{ 
          tail ->next = newNode;
     }
}
void print(Node* & head){
    Node* temp  = head;
    while(temp != NULL){
        cout<<temp->data<<" ";
        temp= temp->next;
    }
}
int findLength(Node* &head){
    int len=0;
    Node* temp =head;
    while(temp != NULL){
        temp = temp -> next;
        len++;
    }
    return len;
}
void insertAtPosition(int data,int position,Node*&head,Node*&tail){
    if(head==NULL){
        Node* newNode=new Node(data);
        head=newNode;
        tail=newNode;
        return;
    }
    //step 1 find the position : prev& current 
    if(position == 0){
        insertAtHead(head,tail,data);
        return;     
    }
    int len=findLength(head);
    if(position >= len){
        insertAtTail(head,tail,data);
        return;
    }
    int i=1;
    Node* prev = head;
    while(i<position){
        prev=prev->next;
        i++;
    }
    Node* curr=prev->next;

    //step 2
    Node* newNode=new Node(data);
    //step3
    newNode -> next = curr;
    //step 4
    prev->next = newNode;
       if (position == len) {
        tail = newNode;
    }
}

int main(){
     Node* head = NULL;
     Node* tail = NULL;
     insertAtHead(head,tail,20);
     insertAtHead(head,tail,50);
     insertAtHead(head,tail,60);
     insertAtHead(head,tail,90);
      insertAtTail(head,tail,77);
     
            print(head);
            cout<<endl;
            cout<<"head :"<<head->data<<endl;
            cout<<"tail :"<<tail->data<<endl;
            insertAtPosition(101,6,head,tail);
            cout<<endl;
            print(head);
            cout<<endl;
            cout<<"head :"<<head->data<<endl;
            cout<<"tail :"<<tail->data<<endl;
    return 0;

}