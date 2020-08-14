import os
import shutil
import argparse


def main():
    parser = argparse.ArgumentParser(description="combine train dataset with val dataset")
    parser.add_argument('-t', '--train_image_path', default='/media/chiyukunpeng/CHENPENG01/dataset/SVNH/mchar_train/',
                        help="path to train dataset")
    parser.add_argument('-v', '--val_image_path', default='/media/chiyukunpeng/CHENPENG01/dataset/SVNH/mchar_val/',
                        help="path to val dataset")
    parser.add_argument('-d', '--dst_image_path', default='./coco/images/', help="path to combined dataset")
    args = parser.parse_args()

    train_image_list = os.listdir(args.train_image_path)
    train_image_list.sort(key=lambda x: int(x[:-4]))
    val_image_list = os.listdir(args.val_image_path)
    val_image_list.sort(key=lambda x: int(x[:-4]))

    for img in train_image_list:
        shutil.copy(args.train_image_path + img, args.dst_image_path + img)
        print("train image {0}/{1} copied".format(img[:-4], len(train_image_list)))
    print("train dataset copied")
    for img in val_image_list:
        shutil.copy(args.val_image_path + img, args.dst_image_path + 'val_' + img)  # 防止重名
        print("val image {0}/{1}  copied".format(img[:-4], len(val_image_list)))
    print("val dataset copied")


if __name__ == '__main__':
    main()
