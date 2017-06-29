# coding:utf-8

import time
import thread

def sort_node(number):
	time.sleep(number)
	print number
    
def sleep_sort(origin):
	for i in origin:
		thread.start_new_thread(sort_node, (i,))

sleep_sort([5, 8, 2, 3, 9, 1, 4])