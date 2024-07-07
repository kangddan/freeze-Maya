import maya.cmds as cmds
import maya.api.OpenMaya as om2

def freezeAll() -> None:
    sel = cmds.ls(sl=True, typ='transform')
    if not sel: return

    for obj in sel:
        localMatrix = om2.MMatrix(cmds.getAttr('{}.matrix'.format(obj)))
        offMatrix   = om2.MMatrix(cmds.getAttr('{}.offsetParentMatrix'.format(obj)))
        cmds.setAttr('{}.offsetParentMatrix'.format(obj), localMatrix*offMatrix, typ='matrix')
        cmds.xform(obj, m=om2.MMatrix(), ws=False)
    
def unfreezeAll() -> None:
    sel = cmds.ls(sl=True, typ='transform')
    if not sel: return
    
    for obj in sel:
        localMatrix = om2.MMatrix(cmds.getAttr('{}.matrix'.format(obj)))
        offMatrix   = om2.MMatrix(cmds.getAttr('{}.offsetParentMatrix'.format(obj)))
        cmds.setAttr('{}.offsetParentMatrix'.format(obj), om2.MMatrix(), typ='matrix')
        cmds.xform(obj, m=localMatrix*offMatrix, ws=False)
        #cmds.setAttr('{}.shear'.format(obj), 0.0, 0.0, 0.0, typ='double3')
        

        
