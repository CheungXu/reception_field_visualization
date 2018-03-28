# reception_field_visualization
A visual tool for CNN feature map pixel reception field: Constructing the net by operators just like in deep-learning framewok. Then use  Visualizer to generate the reception-field image of layer you wanted. A simple example can be find in main function.

# Operator Supported
- conv(input_, kernel_size=3) : Standred Convolution Layer.
- dilated_conv(input_, rate=1) : Dilated Comvolution Layer.

# Visualizer
- visual(input_): Generate Visible Images and Show.
- save(path): Save Visible Images in 'path'.
- show(): Show Visible Images.
