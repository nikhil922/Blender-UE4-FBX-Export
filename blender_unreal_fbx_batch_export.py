########################################### 
########################################### 
####          UNREAL TOOLS v1.01       #### 
####            NIKHIL JEEWA           ####
####                2014               ####  
########################################### 
########################################### 
import bpy 
import os
########################################### 
#####        $#!t just got unreal      ####
########################################### 
		
class UnrealTools(bpy.types.Panel): 
    bl_space_type="VIEW_3D"
    bl_region_type="TOOLS"
    bl_category = "Unreal"
    bl_label = "Unreal Tools"

    def draw(self, context): 
        layout = self.layout          
        col = layout.column(align=True) 
        col.label(text="Unreal Units Setup:")
        col.label(text="[1cm Blender = 1cm Unreal]")   
        row = col.row(align=True)  
        row.operator("wm.unreal_units", text="Unreal Units", icon='LOGIC')
        row.operator("wm.blender_units", text="Blender Units", icon='BLENDER')		
        
        row = col.row(align=True)
        col.label(text="Shade Smooth object or edge, face, vertex:")
        row=col.row(align=True)
        row.operator("wm.sel_vertex", text="Vertex", icon='VERTEXSEL') 
        row.operator("wm.sel_edge", text="Edge", icon='EDGESEL') 
        row.operator("wm.sel_face", text="Face", icon='FACESEL')   
        row = col.row(align=True)
        row.operator("wm.smooth", text="Shade Smooth [Ctrl F]", icon='MOD_SUBSURF')
        
        row = col.row(align=True) 
        col.label(text="Tools:")  
        row = col.row(align=True) 
        row.operator("object.join",text="Join [Ctrl J]",icon='AUTOMERGE_OFF') 
        row.operator("mesh.separate",text="Seperate [P]",icon='UV_ISLANDSEL') 
        row.operator("object.duplicate_move",text="Duplicate [Shift+D]",icon='ROTATECOLLECTION')

        col.label(text="Selection Tools:")        
        row = col.row(align=True)         
        row.operator("wm.swap", text=" Invert All [Ctrl I]",icon="ALIGN")
        row.operator("wm.everything", text=" All Select [A]",icon="STICKY_UVS_LOC")
        row.operator("view3d.select_border", text=" Border    Select",icon="VIEW3D_VEC") 
        row.operator("view3d.select_circle", text=" Circle Select",icon="ALIASED")           
        row.operator("object.select_pattern", text=" Pattern...Search Select",icon="SEQ_LUMA_WAVEFORM")       
        
        row = col.row(align=True)
        col.label(text="Origin to Center of Grid [Select Vertex]:")
        row = col.row(align=True)
        row.operator("wm.origin_vertex",text="O-V-CoG Origin to Vertex Center of Grid",icon='VERTEXSEL')
        row.operator("wm.origin_com",text="O-CoM-CoG Origin to Center of Mass-Center of Grid",icon='FORCE_FORCE')
		
        row=col.row(align=True)
        col.label(text="Freeze Transformation of object: [Ctrl+A]")
        row = col.row(align=True)
        row.operator("wm.freeze_loc",text="Freeze Location",icon='FILE_REFRESH')
        row.operator("wm.freeze",text="Freeze Rotation+Scale",icon='FILE_REFRESH')        
        
        col = layout.column(align=True) 
        col.label(text="Blender>Unreal FBX Batch Export:")
        
        row = col.row(align=True)  
        row.operator("wm.batch_export", text="Batch Export", icon='EXPORT')
		
        row=col.row(align=True)
        row.operator("object.toggle_console", text="Console",icon='CONSOLE')
		
class wm_unreal_Units(bpy.types.Operator):
    bl_idname="wm.unreal_units"
    bl_label="Minimal Operator"

    def execute(self,context):
        bpy.context.scene.unit_settings.system='METRIC'
        bpy.context.scene.unit_settings.scale_length = 0.01
        bpy.context.space_data.clip_end = 800000
        bpy.context.space_data.clip_start = 0.1
        bpy.context.space_data.grid_lines = 1024
		#bpy.context.space_data.grid_scale = 0.5
        return {'FINISHED'}
    
class wm_blender_Units(bpy.types.Operator):
    bl_idname="wm.blender_units"
    bl_label="Minimal Operator"

    def execute(self,context):
        bpy.context.scene.unit_settings.system='NONE'
        bpy.context.scene.unit_settings.scale_length = 1
        bpy.context.space_data.clip_end = 500
        bpy.context.space_data.clip_start = 1
        bpy.context.space_data.grid_lines = 16
        return {'FINISHED'}	

class wm_smooth(bpy.types.Operator):
    bl_idname="wm.smooth"
    bl_label="Minimal Operator"

    def execute(self,context):
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.faces_shade_smooth()
        bpy.ops.object.mode_set(mode='OBJECT')
        return{'FINISHED'}
		
class wm_origin_vertex(bpy.types.Operator):
    bl_idname="wm.origin_vertex"
    bl_label="Minimal Operator"
	
    def execute(self,context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.mode_set(mode='OBJECT')		
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = 0
        bpy.context.object.location[2] = 0
        return{'FINISHED'}
		
class wm_origin_com(bpy.types.Operator):
    bl_idname="wm.origin_com"
    bl_label="Minimal Operator"

    def execute(self,context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.mode_set(mode='OBJECT')		
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = 0
        bpy.context.object.location[2] = 0
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = 0
        bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        return{'FINISHED'}
		
class wm_freeze_loc(bpy.types.Operator):
    bl_idname="wm.freeze_loc"
    bl_label="Minimal Operator"
    def execute(self,context):
        bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
        return {'FINISHED'}
		
class wm_freeze(bpy.types.Operator):
    bl_idname="wm.freeze"
    bl_label="Minimal Operator"
	
    def execute(self,context):
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        return {'FINISHED'}
    
#################### BATCH EXPORT ###################
class wm_batch_export(bpy.types.Operator):
    bl_idname="wm.batch_export"
    bl_label="Minimal Operator"
    
    def execute(self,context):
        basedir = os.path.dirname(bpy.data.filepath)
        if not basedir:
            raise Exception("Blend file is not saved")
                    
        collision=[]    
        mesh=[]
        lod=[]
        print ("")
        selection = bpy.context.selected_objects
        bpy.ops.object.select_all(action='DESELECT')

        for obj in selection:
            if not obj.name.startswith("UBX_") and not obj.name.startswith("USP_") and not obj.name.startswith("UCX_"):
                if not obj.name.endswith("_1") and not obj.name.endswith( "_2") and not obj.name.endswith( "_3") and not obj.name.endswith( "_4") and not obj.name.endswith( "_5") and not obj.name.endswith( "_6"):
                    mesh.append(obj)
                    print (mesh)

        bpy.ops.object.select_by_type(type='MESH')
        col = bpy.context.selected_objects
        for obj in col:
            if obj.name.startswith("UBX_") or obj.name.startswith("USP_") or obj.name.startswith("UCX_"):
                collision.append(obj)
            if obj.name.endswith("_1") or obj.name.endswith( "_2") or obj.name.endswith( "_3") or obj.name.endswith( "_4") and not obj.name.endswith( "_5") or obj.name.endswith( "_6"):
                lod.append(obj)    
        
        bpy.ops.object.select_all(action='DESELECT')
        for obj in mesh:    
            meshX=obj.name
            meshXo=obj
            obj.select=True
            hasCollision=0
            for obj in collision:
                colX = (obj.name[4:])
                if colX==meshX:
                    hasCollision=1
                    obj.select=True
                    locc = obj.location.xyz
                    rotXc = obj.rotation_euler[0]
                    rotYc = obj.rotation_euler[1]
                    rotZc = obj.rotation_euler[2]    
                    scac = obj.scale.xyz
                    obj.location.xyz = [0,0,0]
                    obj.rotation_euler = [0,0,0]
                    obj.scale.xyz = [1,1,1]
                    locm = meshXo.location.xyz
                    rotXm = meshXo.rotation_euler[0]
                    rotYm = meshXo.rotation_euler[1]
                    rotZm = meshXo.rotation_euler[2]    
                    scam = meshXo.scale.xyz
                    meshXo.location.xyz = [0,0,0]
                    meshXo.rotation_euler = [0,0,0]
                    meshXo.scale.xyz = [1,1,1]
                    name = bpy.path.clean_name(meshX)
                    fn = os.path.join(basedir, name)
                    bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True,axis_forward='-Z', axis_up='Y')
                    obj.location.xyz = (locc)        
                    obj.rotation_euler = [rotXc,rotYc,rotZc]
                    obj.scale.xyz =(scac) 
                    meshXo.location.xyz = (locm)        
                    meshXo.rotation_euler = [rotXm,rotYm,rotZm]
                    meshXo.scale.xyz =(scam) 
                    obj.select=False
                    for obj in lod:
                        lodX=(obj.name[:-2])
                        if lodX==meshX:
                            meshXo.select=False
                            obj.select=True
                            loc = obj.location.xyz
                            rotX = obj.rotation_euler[0]
                            rotY = obj.rotation_euler[1]
                            rotZ = obj.rotation_euler[2]    
                            sca = obj.scale.xyz
                            bpy.ops.object.location_clear()
                            bpy.ops.object.rotation_clear()
                            bpy.ops.object.scale_clear()
                            name =bpy.path.clean_name(obj.name)
                            fn = os.path.join(basedir,name)
                            bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True,axis_forward='-Z', axis_up='Y')
                            obj.location.xyz = (loc)        
                            obj.rotation_euler = [rotX,rotY,rotZ]
                            obj.scale.xyz =(sca) 
                            meshXo.select=True
                            obj.select=False
                    bpy.ops.object.select_all(action='DESELECT')
            if hasCollision==0:
                locm = meshXo.location.xyz
                rotXm = meshXo.rotation_euler[0]
                rotYm = meshXo.rotation_euler[1]
                rotZm = meshXo.rotation_euler[2]    
                scam = meshXo.scale.xyz
                meshXo.location.xyz = [0,0,0]
                meshXo.rotation_euler = [0,0,0]
                meshXo.scale.xyz = [1,1,1]
                name = bpy.path.clean_name(meshX)
                fn = os.path.join(basedir, name)
                bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True,axis_forward='-Z', axis_up='Y')
                meshXo.location.xyz = (locm)        
                meshXo.rotation_euler = [rotXm,rotYm,rotZm]
                meshXo.scale.xyz =(scam) 
                obj.select=False
                for obj in lod:
                    lodX=(obj.name[:-2])
                    if lodX==meshX:
                        meshXo.select=False
                        obj.select=True
                        loc = obj.location.xyz
                        rotX = obj.rotation_euler[0]
                        rotY = obj.rotation_euler[1]
                        rotZ = obj.rotation_euler[2]    
                        sca = obj.scale.xyz
                        bpy.ops.object.location_clear()
                        bpy.ops.object.rotation_clear()
                        bpy.ops.object.scale_clear()
                        name =bpy.path.clean_name(obj.name)
                        fn = os.path.join(basedir,name)
                        bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True,axis_forward='-Z', axis_up='Y')
                        obj.location.xyz = (loc)        
                        obj.rotation_euler = [rotX,rotY,rotZ]
                        obj.scale.xyz =(sca) 
                        meshXo.select=True
                        obj.select=False
                    bpy.ops.object.select_all(action='DESELECT')
                                         
        for obj in selection:
            obj.select = True
                        
        return {'FINISHED'}
###########################################  
     
if __name__== "__main__": 
    bpy.utils.register_module(__name__) 
