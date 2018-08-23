import pymel.core as pm
class LODwindow(object):
	WINDOW_NAME = 'LOD_window'
	def tagNodes(self,nodeList,res='Low'):
		for node in nodeList:
			if not node.hasAttr('gameRes'):
				node.addAttr('gameRes',type='string')
			node.gameRes.set(res,type= 'string')
	
	def create(self):
		try:
			pm.deleteUI(self.WINDOW_NAME,window=True)
		except:pass
		
		with pm.window(self.WINDOW_NAME) as res_window:
			with pm.columnLayout(adjustableColumn=True):
				with pm.horizontalLayout():
					pm.text(label='Resolution')
					with pm.optionMenu() as self.res_menu:
						pm.menuItem(l='Low')
						pm.menuItem(l='Med')
						pm.menuItem(l='Hig')
					set_res_btn = pm.button(
						label:'Set LOD',
						command=pm.Callback(self.on_set_res_btn)
					)
				pm.separator(style='in',height=4)
				with pm.horizontalLayout() as h1:
					pm.text(label = 'Low')
					select_low_btn=pm.button(
						label='Select All',
						command=pm.Callback(
							self.on_select_btn,
							'Low'
						)
					)
	def on_select_btn(self,*args):
		poly_meshes=[
			i for i in pm.ls(
				type=pm.nt.Transform
				)if type(type(i.getShape())== pm.nt.mesh)
			]
			if poly_meshes:
				pm.select(
					[i for i in polymeshes if(
						i.hasAttr('gameRes') and
						i.gameRes.get()==args[0]
						)
					]
				)
				self.status_line.setText(
					'Selected %s resolution meshes' %args[0]
				)
			else:
				self.status_line.setText(
					'Nothing has been Selected' 
				)
					