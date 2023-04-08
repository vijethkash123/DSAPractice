class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if head==None:
            return head
        if head.next==None:
            return head
        else:
            newHead = self.reverseList(head.next)
            # print(str(newHead.val)+"-----rev")
            # print(head.next.val)
            head.next.next = head
            head.next=None
        return newHead


if __name__ == "__main__":
    five = ListNode(5,None)
    four = ListNode(4,five)
    three = ListNode(3,four)
    two = ListNode(2,three)
    one = ListNode(1,two)
    # 1->2->3->4->5

    obj = Solution()
    ans = obj.reverseList(one)
    while ans:
        print(ans.val)
        ans = ans.next

'''
 If we have 1->2->3->4->5->None
 We iterate till head.next is None and then return head. Also se in recursive call we pass head.next
 In that case, returned is head = 4, newHead = 5. Because reverseList(4.next) is called -> then in 2nd if we check 5.next is None, so its true. So we return 5 as newHead
 and 4 will be head that called this from reverseList call.

Then we make head.next.next = head, So it's 4.next = 5 -> 5.next = head which means 5.next is assigned to 4. So the subProblem is reversed. 
Now the linked List looks like 5->4
then we make 4.next as None. So now linked list looks like 5->4->None.
Then we return 5->4->None as newHead where it will next be processed with head as 3.
head.next.next = head ---> 3.next.next is 4.next = 3 which is head.
So it becomes 5->4->3
head.next = None
5->4->3->None
and this continues untill we reverse the whole linked list.
'''