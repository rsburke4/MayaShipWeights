import maya.cmds as cmds

# Make a new window
#


# This creates a blank attribute that can be painted onto the mesh
def createPaintAttribute(attrName):
	attrText = cmds.textField(attrName, query=True, text=True)
	print(attrText + ' ATTRIBUTE')
	objs = cmds.ls(sl=True)
	print(objs)
	for o in objs:
		print(o)
		shapes = cmds.listRelatives(o, shapes=True)
		for s in shapes:
			print(s)
			cmds.addAttr(s, longName=attrText, dataType='doubleArray')
			cmds.makePaintable('mesh', attrText, attrType='doubleArray')
	cmds.deleteUI(window, window=True)

def openFileDialog(fileBox):
	textFilter = "*.txt"
	returnText = cmds.fileDialog2(fileFilter=textFilter, dialogStyle=2, fileMode=0)
	cmds.textField(fileBox, edit=True, text=returnText[0])


# Writes the attribute weights to a file.
# This output has a similar structure to an OBJ file
def exportWeights(file, attr):
	filename = cmds.textField(file, query=True, text=True)
	attribute = cmds.textField(attr, query=True, text=True)
	object = cmds.ls(sl=True)
	shapes = cmds.listRelatives(shapes=True)

	weights = cmds.getAttr(shapes[0] + '.' + str(attribute))


	print('FILE' + filename)
	raw_filename = r'{}'.format(filename)
	fileObject = open(r'{}'.format(raw_filename), "w")

	i = 0
	for w in weights:
		fileObject.write("w " + str(w))
		fileObject.write('\n')
		i += 1

	triangles = cmds.polyEvaluate(f=True)
	for i in range(triangles):
		string = str(object[0]) + ".f[" + str(i) + "]"
		cmds.select(string, r=True)
		verts = cmds.polyInfo(fv=True)
		print("I: " + str(i) + " of " + str(triangles))
		numbers = []
		for word in verts[0].split():
			if str(word).isdigit():
				numbers.append(int(word))
		line = "f"
		for n in numbers:
			line = line + " " + str(n)
		fileObject.write(line + "\n")

	fileObject.close()

window = cmds.window( title="PaintExporter", iconName='Short Name', widthHeight=(300, 200) )
cmds.columnLayout( adjustableColumn=True )
#Add elements

# Make paintable attribute
cmds.text(label='Select Object in Scene to Add Attribute To')
cmds.text(label='Attribute Name')
name = cmds.textField()
cmds.textField( name, edit=True )

cmds.text(label='Pressing this will close the window')
cmds.text(label='Go paint the attribute, and come back')
cmds.button(label='Make Paintable Attribute', command=('createPaintAttribute("' + name + '")'))

# Export weight values to file
fileLocation = ''
fileLocationBox = cmds.textField()
cmds.textField(fileLocationBox, edit=True, en=False, text=fileLocation)
cmds.button(label='Chose File Location', command='openFileDialog(fileLocationBox)')

cmds.button( label='Export Weights As File', command='exportWeights(fileLocationBox, name)' )
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )

# After painting, normalize

# Create the window
cmds.setParent( '..' )
cmds.showWindow( window )

# Resize the main window
#

# This is a workaround to get MEL global variable value in Python
gMainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
cmds.window( gMainWindow, edit=True, widthHeight=(900, 777) )
