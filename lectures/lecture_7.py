'''if self.head == None:
    return
elif current.next == None:
    self.tail = self.head
    current.next = previous
    self.head = current
else:
    next = current.next
    current.next = previous
    self.reverse_list_recur(next, current)'''

choice = '1'
made_payment = False

if choice == '1' and made_payment:
    print("You have chosen option 1")
elif choice =='2':
    print("You have choisen option 2")
else:
    print("You have made an invalid choice")