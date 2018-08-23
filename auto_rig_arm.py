import pymel.core as pm
#scriptName = __name__
newWindow = 'auto_Arm_Maker'

class AutoRigArm(object):
    WINDOW_NAME = 'auto_Arm_Maker'
    def create(self):
        try:
            pm.deleteUI(self.WINDOW_NAME, window=True)
        except: pass
    with pm.window(self.WINDOW_NAME) as rig_window:
        with newWindow:
            with columnLayout(rowSpcaing=5):
                with frameLayout():
                    label1='Ori_1'
                    label2='Ori_2'
                    label3='Ori_3'