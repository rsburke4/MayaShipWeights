# Maya Ship Weighting

This is a python script for Maya, designed specifically to address the need to distribute weight across the hull of a ship.
However, this script can be used for any application in which adding a paintable attribute to a mesh and writing the weights to a file proves useful.

Add this script to your Maya shelf, or copy and paste it in the script editor to open a new window. Select the mesh you would like to add a new attribute to.
Type the name of the attribute you would like to add into the box, then select "Make Paintable Attribute" to assign it to your mesh.
From there you should be able to paint a weighted attribute value from 0 to 1 on the mesh with the weight painting tool. When you are ready to export these weights as a file,
open the window script window again and type the name of the attribute you would like to export into the box. The press "Choose File Location" and decide where to save it.
Finally, click on "Export Weights As File" to export these weights.

The speed at which the script exports the weights depends heavily on the number of vertices the painted mesh contains. It is unlikely that the script will freeze or crash,
however Maya may appear to be unresponsive while the weights export.
