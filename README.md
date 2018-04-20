# reception_field_visualization
A visual tool for CNN feature map pixel reception field: Constructing the net by operators just like in deep-learning framewok. Then use  Visualizer to generate the reception-field image of layer you wanted. A simple example can be find in main function.

## Prerequisites
- Python
- OpenCV (pip install opencv-python)

## Operator Supported
- conv(input_, kernel=3, stride=1) : Standred Convolution Layer.
- deconv(input_, kernel=3, stride=1) : Standred Deconvolution Layer.
- dilated_conv(input_, rate=1) : Dilated Convolution Layer.

## Visualizer
- rect_size: The Pixel num of Rect in Image.
- line_width: The Width of Separator Lines.
- visual(input_): Generate Visible Images and Show.
- save(path): Save Visible Images in 'path'.
- show(): Show Visible Images.

# Visualization Result
## Convolution Layer (kernel = 3, stride = 1)
![](conv/0.jpg)  
![](conv/1.jpg)  
![](conv/2.jpg)  
![](conv/3.jpg)  
![](conv/4.jpg)  
![](conv/5.jpg)   
## Dilated Convolution Layer (rate = [1, 2, 5, 1, 2, 7])
![](dconv/1.jpg)  
![](dconv/2.jpg)  
![](dconv/3.jpg)  
![](dconv/4.jpg)  
![](dconv/5.jpg)  
![](dconv/6.jpg)   

# TODO
- User-defined dilated_conv kernel size.
- Wider Painting Color Range.
- Real Reception_field Size Compute API.
- Real Pixel Visual Image.(Bug fix)
