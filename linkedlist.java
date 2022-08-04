class Node{
  int value=0;
  Node link=null;
  public Node(int value,Node link){
     this.value=value;
     this.link=link;
  }
}
class Main{
   public static void main(String args[]){
       Node head=new Node(16,null);
       System.out.println(head.value);
   
   }

}
