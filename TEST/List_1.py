# a = [1, 3, 4, 5, 6, 9]
# b = [1, 2, 5, 6, 9]
# for i in range(1, min(len(a), len(b))+1):
#     if i == 1 and (a[-1] != b[-1]):
#         print("No")
#         break
#     else:
#         if a[-i] != b[-i]:
#             print("a和b的交叉点为", b[-i+1])
#             break
#         else:
#             pass
#coding:utf-8
class ListNode:
    def __init__(self):
        self.val = self
        self.next = None


def node(l1, l2):
    cur1 = l1
    cur2 = l2
    length1, length2 = 0, 0
    # 求两个链表长度
    while l1.next:
        l1 = l1.next#尾节点
        length1 += 1
    while l2.next:
        l2 = l2.next#尾节点
        length2 += 1

        # 长的链表先走
    if length1 > length2:
        for i in range((length1 - length2)):
            cur1 = cur1.next
    else:
        for i in range((length2 - length1)):
            cur2 = cur2.next
    while cur2 and cur1:
        if cur1.val == cur2.val:
            print("第一个交点:{0}".format( cur1.val))
            break
        else:
            cur1 = cur1.next
            cur2 = cur2.next






def creat_List(l,data):
    l.val = data[0]
    p = l
    for i in data[1:]:
        node = ListNode()
        node.val = i
        p.next = node
        p = p.next
    p.next = None
    return l


data1 = [1, 3, 4, 5, 6]
data2 = [2, 4, 5, 6]
L1 = ListNode()
L2 = ListNode()
l1 = creat_List(L1, data1)
l2 = creat_List(L2, data2)
for i in range(len(data1)):
    print(L1.val)
    L1 = L1.next
print("============================")
for i in range(len(data2)):
    print(L2.val)
    L2 = L2.next

node(l1,l2)





