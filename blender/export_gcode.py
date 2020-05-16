import bpy

scn = bpy.context.scene
obj = bpy.context.object

x_curve = obj.animation_data.action.fcurves.find('location', index=0)
y_curve = obj.animation_data.action.fcurves.find('location', index=1)
z_curve = obj.animation_data.action.fcurves.find('location', index=2)

with open('data_out.txt', 'w') as out_file:
    for f in range(scn.frame_start, scn.frame_end):
        x_pos = x_curve.evaluate(f)
        y_pos = y_curve.evaluate(f)
        z_pos = z_curve.evaluate(f)
        out_file.write('{},{:.3f},{:.3f},{:.3f}\n'.format(f,x_pos,y_pos,z_pos))