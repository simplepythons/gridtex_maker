# gridtex maker

It is a python tool to create a grid-like texture file (4096 x 4096 png) for inputting images  

Usage  
```python
python run.py level "input_images_directory" "output_image_path"
```
level:  
1, 141 x 32 blocks (tile 29 x 29 pixels)  
2, 70 x 16 blocks (tile 58 x 58 pixels)  
3, 35 x 8 blocks (tile 116 x 116 pixels)  
4, 17 x 4 blocks (tile 232 x 232 pixels)  
5, 8 x 2 blocks (tile 464 x 464 pixels)  
6, 4 x 1 blocks (tile 928 x 928 pixels)  
7, error  

level 4 example:  
If there is a png file, it will replace the number with the png image.  

![test](test.png)
