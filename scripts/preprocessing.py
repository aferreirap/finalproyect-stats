import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import cv2

def processing(img,height=int,width=int):
    dim = (width,height)
    size =  cv2.resize(img,dim, interpolation=cv2.INTER_LINEAR)
    norm = np.zeros((255, 255))
    norm_img = cv2.normalize(size, norm, 0, 255, cv2.NORM_MINMAX)
    
    return  cv2.GaussianBlur(norm_img, (5, 5), 0)

def get_images():
    df = pd.DataFrame(columns=['App','Image'])

    app_images = [x for x in os.listdir(('./data/images')) if str(x) != '.DS_Store']

    for image in app_images:
        try: 
            crude  = np.asarray(Image.open(f'./data/images/{image}')) #transforming image to array
            processed_img = processing(crude,255,255) #resizing, normalizing and bluring image
        except IOError:
            pass
        image_name = image[:-4]
        df = df.append({'App' : image_name, 'Image': processed_img} , ignore_index=True)
    return df

app_data = pd.read_csv('./data/subset_data.csv')

app_images = get_images()
img = Image.fromarray(app_images.iloc[50,1])
img.show()

app_images.to_csv('./data/subset_images_df.csv')