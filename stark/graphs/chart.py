# -*- coding: utf-8 -*-
from random import randint

class chart():
    def datas(self):
        datas1 = []
        datas2 = []
        data = []
        global x
        x='x'
        global y
        y='y'
        for i in range(0,12):
            datas1.append(randint(0,1000))
            datas2.append(randint(0, 1000))

        data=[data.append({x:i, y:randint(0, 1000)}) for i in datas1]

        data = ''' [
			{x:1, y: 450 },
			{x:2, y: 414},
			{x:3,y: 520 },
			{x:4, y: 460 },
			{x:5, y: 450 },
			{x:6, y: 500 },
			{x:7, y: 1500 },
			{x:9, y: 480 },
			{x:10, y: 410 },
			{ x:16,y: 500 },
			{x:17, y: 480 },
			{x:18, y: 510 }
		]'''
        x = [1, 2, 3, 4, 5]
        y1 = [150, 450, 200, 100, 300]
        y2 = [230, 220, 150, 400, 105, 50, 302]
        return data,x,y1,y2

i=chart()
i.datas()
