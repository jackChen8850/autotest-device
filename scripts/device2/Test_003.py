# -*- coding:utf-8 -*-

"""
@Title：JOOM测试-商品搜索T-sheet测试
@Desc：pass
@Author：yang
@Date Created：2018-05-03
@Date Last Modified：2018-05-03
@Step：
"""

from aw import *
from operatetest import *
import time

class Test_003(TestCase):
    def setUp(self):
        # Common.launchApp(self.ad, 'com.joom')
        self.log.info("Common.launchApp(self.ad, 'com.joom1111111111111')",keyword=True)
        self.log.info("Common.launchApp(self.ad, 'com.joom')",keyword=True)
        print("exec setUp")

        time.sleep(0.2)
        pass

    def test(self):
        # Common.touchById(self.ad, "com.joom:id/menu_search")
        print("exec test")
        # self.assertEquals(3, 5)
        time.sleep(0.2)
        # 3/0
        # self.assertEquals(3,5)
        # Common.touchById(self.ad, "com.joom:id/search_field")
        # Common.sendText(self.ad, "T-sheet", resourceId="com.joom:id/query_field")
        # Common.press(self.ad, "enter")
        # Common.sleep(self.ad, 5)

    def tearDown(self):
        # Common.closeApp(self.ad, 'com.joom')
        print("exec tearDown")
        # itiserror
        time.sleep(0.2)
        pass
