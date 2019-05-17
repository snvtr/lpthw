import SingleLinkedList
import SingleLinkedNode

MyList = SingleLinkedList.SingleLinkedList()
MyList.append(SingleLinkedNode.SingleLinkedNode('1', None))
MyList.append(SingleLinkedNode.SingleLinkedNode('2', None))
MyList.append(SingleLinkedNode.SingleLinkedNode('3', None))
MyList.push(SingleLinkedNode.SingleLinkedNode('6', None))
print('%s' % MyList)
print('delete:')
print('%r' % MyList.shift())
print('%s' % MyList)


