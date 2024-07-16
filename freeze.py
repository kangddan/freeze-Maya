import maya.cmds as cmds
import maya.api.OpenMaya as om2

def freezeAll() -> None:
    sel = cmds.ls(sl=True, typ='transform')
    if not sel: return

    for obj in sel:
        localMatrix = om2.MMatrix(cmds.getAttr('{}.matrix'.format(obj)))
        offMatrix   = om2.MMatrix(cmds.getAttr('{}.offsetParentMatrix'.format(obj)))
        cmds.setAttr('{}.offsetParentMatrix'.format(obj), localMatrix*offMatrix, typ='matrix')
        
        if cmds.nodeType(obj) == 'joint':
            cmds.setAttr('{}.jointOrient'.format(obj), 0.0, 0.0, 0.0, typ='double3')
        cmds.xform(obj, m=om2.MMatrix(), ws=False)
    
def unfreezeAll() -> None:
    sel = cmds.ls(sl=True, typ='transform')
    if not sel: return
    
    for obj in sel:
        localMatrix = om2.MMatrix(cmds.getAttr('{}.matrix'.format(obj)))
        offMatrix   = om2.MMatrix(cmds.getAttr('{}.offsetParentMatrix'.format(obj)))
        cmds.setAttr('{}.offsetParentMatrix'.format(obj), om2.MMatrix(), typ='matrix')
        
        if cmds.nodeType(obj) == 'joint':
            cmds.setAttr('{}.jointOrient'.format(obj), 0.0, 0.0, 0.0, typ='double3')
        cmds.xform(obj, m=localMatrix*offMatrix, ws=False)
        cmds.setAttr('{}.shear'.format(obj), 0.0, 0.0, 0.0, typ='double3')
        
# -----------------------------------------------------------------------------------

import cmdk

def freezeAll() -> None:
    sel = cmdk.ls(sl=True, typ='transform')
    if not sel: return

    for obj in sel:
        localMatrix = obj.getLocalMatrix()
        offMatrix   = obj.offsetParentMatrix.get()
        obj.offsetParentMatrix.set(localMatrix * offMatrix)
        
        if obj.type == 'joint':
            obj.jointOrient.set(0, 0, 0)
        obj.setLocalMatrix(cmdk.matrix())
        
def unfreezeAll() -> None:
    sel = cmdk.ls(sl=True, typ='transform')
    if not sel: return
    
    for obj in sel:
        localMatrix = obj.getLocalMatrix()
        offMatrix   = obj.offsetParentMatrix.get()
        obj.offsetParentMatrix.set(cmdk.matrix())
        
        if obj.type == 'joint':
            obj.jointOrient.set(0, 0, 0)
        obj.setLocalMatrix(localMatrix * offMatrix)
        obj.shear.set(0, 0, 0)
