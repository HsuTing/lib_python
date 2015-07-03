#coding:utf-8
import sys
sys.path.append("/home/hsuting/lib_python/course_selection")
import courseselection
from courseselection import courseselection

"""
key = [
		{
			"number": 2,
			"name": "一類"
		}
	  ]
courseselection("record", "curriculum/一類", key, 3)
"""

key = [
        {
            "number": 2,
            "name": "二、三類"
        }
      ]
courseselection("record", "curriculum/二、三類", key, 3)

