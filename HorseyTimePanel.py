
import bpy
from bpy.types import Panel, Operator
import bmesh
from .easybpy import create_object
class HorseyTime_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Grass gen!"
    bl_category = "HorseyTime Util"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        layout.label(text="Hello World")
        col = layout.column(align=True)
        row = col.row(align=True)
        col.operator(SimpleOperator.bl_idname, text="Generate grass!", icon="CONSOLE")

def getmid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)
def triangle(position,depth):
    if depth ==0:
        return
    else:
        i=0
        while i < depth:
            pass
    



def drawTriangle(points,bm):
    v1 = bm.verts.new((0, points[0][0], points[0][1]))
    
    v2 = bm.verts.new((0, points[1][0],points[1][1]))
    v3 = bm.verts.new((0, points[0][0],points[0][1]))
    v4 = bm.verts.new((0,points[2][0],points[2][1]))
    print("v1: ",points[0][0], points[0][1], "v2: ",  points[1][0],points[1][1], "v3", points[0][0],points[0][1], "v4", points[2][0],points[2][1])
    bm.faces.new((v1, v2,v4))
    # myTurtle.goto(points[0][0],points[0][1])
    # myTurtle.down()
    # myTurtle.begin_fill()
    # myTurtle.goto(points[1][0],points[1][1])
    # myTurtle.goto(points[2][0],points[2][1])
    # myTurtle.goto(points[0][0],points[0][1])
    # myTurtle.end_fill()

def mid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def drawsierpinski(points,degree,bm):
    
    drawTriangle(points,bm)
    if degree > 0:
        drawsierpinski([points[0], mid(points[0], points[1]), mid(points[0], points[2])], degree-1, bm)
        drawsierpinski([points[1],
                        mid(points[0], points[1]),
                        mid(points[1], points[2])],
                   degree-1, bm)
        drawsierpinski([points[2],
                        mid(points[2], points[1]),
                        mid(points[0], points[2])],
                   degree-1, bm)


   

class SimpleOperator(Operator):
    """Print object name in Console"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Grass Operator"

    def execute(self, context):
        #verts = [(1, 1, 1), (0, 0, 0)] 
        mesh = bpy.data.meshes.new("mesh")  
        obj = bpy.data.objects.new("MyObject", mesh)  
        col_ref=bpy.context.view_layer.active_layer_collection.collection
        col_ref.objects.link(obj)
        #obj = create_object()
        obj.select_set(True)
        bpy.ops.object.mode_set(mode='EDIT')

        bm = bmesh.from_edit_mesh(obj.data)

        # v1 = bm.verts.new((0, 0, 2.0))
        # v2 = bm.verts.new((0, 1.0, 0))
        # v3 = bm.verts.new((0, -1.0, 0))

        # bm.faces.new((v1, v2, v3))
        
        myPoints = [[-100,-50],[0,100],[100,-50]]
        drawsierpinski(myPoints,3,bm)
        bmesh.update_edit_mesh(obj.data)
        # bm = bmesh.new()   # create an empty BMesh
        # bm.from_mesh(obj)   # fill it in from a Mesh


        # # Modify the BMesh, can do anything here...
        # for v in bm.verts:
        #     v.co.x += 1.0


        # # Finish up, write the bmesh back to the mesh
        #bm.to_mesh(obj.data)
        #bm.free()  # free and prevent further access
        bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}