'''
Created by auto_sdk on 2018.05.07
'''
from top.api.base import RestApi
class TbkDgOptimusMaterialRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.material_id = None
		self.page_no = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.tbk.dg.optimus.material'
