import argparse
import cv2
import os
import sys
import glob


def main(args):
    if not os.path.exists(args.path):
        print('No folder: ' + args.path)    
    else:
        imageList = glob.glob(os.path.join(args.path, '*.' + args.im_exti))
        if len(imageList) == 0:
            print('No .' + args.im_exti + ' images found in the specified dir: ' + args.path)
        else:
            for imagepath in imageList:
                print('Working on image: ' + imagepath)
                imgr = cv2.imread(imagepath)
                img = cv2.resize(imgr, (args.im_size,args.im_size), interpolation = cv2.INTER_AREA)
                cv2.imwrite(imagepath[:-4] + '.' + args.im_exto, img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-im_size', default=416,type=int,
                        help='pixel number for each img dimension')
    parser.add_argument('-path', default='images/',type=str,
                        help='path of the images to process')
    parser.add_argument('-im_exti', default='png',type=str,
                        help='Extension of input images')
    parser.add_argument('-im_exto', default='jpg',type=str,
                        help='Extension for output images')
    args = parser.parse_args()
    main(args)