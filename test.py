#coding:utf-8
import sys
sys.path.append("/home/hsuting/library/python/course_selection")
import course_selection
from course_selection import Course_selection

key = [
		{
			"number": 2,
			"name": "一類"
		}
	  ]
Course_selection("input", "1", key, 3)
