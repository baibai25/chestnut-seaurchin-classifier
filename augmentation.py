import argparse
import os
import glob
import numpy as np
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator

np.random.seed(42)

# generate new data
def gen_data(files, save_path):
    
    for i, file in enumerate(files):
        # load image
        print(file)
        img = load_img(file)
        X = img_to_array(img)
        X = np.expand_dims(X, axis=0)
        
        # define augmentation paramters
        gen = ImageDataGenerator(
            horizontal_flip=True,
            vertical_flip=True,
            rotation_range = 90,
        )
        
        # generate and save image
        g = gen.flow(X, batch_size=1, save_to_dir=save_path, save_prefix='img', save_format='jpg')
        for i in range(4):
            batch = g.next()

def main():
    # parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', help='Input directory')
    parser.add_argument('-o', '--outout_dir', help='Output directory')
    args = parser.parse_args()

    files = glob.glob(args.input_dir + '/*')
    os.makedirs(args.outout_dir, exist_ok=True)
    gen_data(files, args.outout_dir)


if __name__ == '__main__':
    main()
