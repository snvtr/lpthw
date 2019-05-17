from nose.tools import *

import main.SingleLinkedList
import main.SingleLinkedNode

def setup():
    pass

def teardown():
    pass

def test_SingleLinkedList_append():

    MyList = main.SingleLinkedList.SingleLinkedList()
    MyList.append(main.SingleLinkedNode.SingleLinkedNode('1', None))
    MyList.append(main.SingleLinkedNode.SingleLinkedNode('2', None))
    MyList.append(main.SingleLinkedNode.SingleLinkedNode('3', None))
    assert_equal(str(MyList), '[1, 2]\n[2, 3]\n[3, None]\n')
    
def test_SingleLinkedList_push():

    MyList = main.SingleLinkedList.SingleLinkedList()
    MyList.push(main.SingleLinkedNode.SingleLinkedNode('1', None))
    MyList.push(main.SingleLinkedNode.SingleLinkedNode('2', None))
    MyList.push(main.SingleLinkedNode.SingleLinkedNode('3', None))
    assert_equal(str(MyList), '[3, 2]\n[2, 1]\n[1, None]\n')

def test_SingleLinkedList_shift():

    MyList = main.SingleLinkedList.SingleLinkedList()
    MyList.append(main.SingleLinkedNode.SingleLinkedNode('1', None))
    MyList.append(main.SingleLinkedNode.SingleLinkedNode('2', None))
    MyList.append(main.SingleLinkedNode.SingleLinkedNode('3', None))
    assert_equal(MyList.shift(), '1')
    assert_equal(MyList.shift(), '2')
    assert_equal(MyList.shift(), '3')
    assert_equal(MyList.shift(), None)
