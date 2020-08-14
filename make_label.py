import cv2
import json
import argparse


def main():
    parser = argparse.ArgumentParser(description="make label for combined datatset")
    parser.add_argument('-ti', '--train_image_path', default='/media/chiyukunpeng/CHENPENG01/dataset/SVNH/mchar_train/',
                        help="path to train dataset")
    parser.add_argument('-vi', '--val_image_path', default='/media/chiyukunpeng/CHENPENG01/dataset/SVNH/mchar_val/',
                        help="path to val dataset")
    parser.add_argument('-ta', '--train_annotation_path',
                        default='/media/chiyukunpeng/CHENPENG01/dataset/SVNH/mchar_train.json',
                        help="path to train annotation")
    parser.add_argument('-va', '--val_annotation_path',
                        default='/media/chiyukunpeng/CHENPENG01/dataset/SVNH/mchar_val.json',
                        help="path to val annotation")
    parser.add_argument('-l', '--label_path', default='./coco/labels/', help='path to combined labels')
    args = parser.parse_args()

    train_data = json.load(open(args.train_annotation_path))
    val_data = json.load(open(args.val_annotation_path))

    for key in train_data:
        f = open(args.label_path + key.replace('.png', '.txt'), 'w')
        img = cv2.imread(args.train_image_path + key)
        shape = img.shape
        label = train_data[key]['label']
        left = train_data[key]['left']
        top = train_data[key]['top']
        height = train_data[key]['height']
        width = train_data[key]['width']
        for i in range(len(label)):
            # 归一化
            x_center = 1.0 * (left[i] + width[i] / 2) / shape[1]
            y_center = 1.0 * (top[i] + height[i] / 2) / shape[0]
            w = 1.0 * width[i] / shape[1]
            h = 1.0 * height[i] / shape[0]
            # label, x_center, y_center, w, h
            f.write(str(label[i]) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(w) + ' ' + str(h) + '\n')
        f.close()
        print("train label {0}/{1} made".format(key[:-4], len(train_data)))

    for key in val_data:
        f = open(args.label_path + 'val_' + key.replace('.png', '.txt'), 'w')
        img = cv2.imread(args.val_image_path + key)
        shape = img.shape
        label = val_data[key]['label']
        left = val_data[key]['left']
        top = val_data[key]['top']
        height = val_data[key]['height']
        width = val_data[key]['width']
        for i in range(len(label)):
            # 归一化
            x_center = 1.0 * (left[i] + width[i] / 2) / shape[1]
            y_center = 1.0 * (top[i] + height[i] / 2) / shape[0]
            w = 1.0 * width[i] / shape[1]
            h = 1.0 * height[i] / shape[0]
            # label, x_center, y_center, w, h
            f.write(str(label[i]) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(w) + ' ' + str(h) + '\n')
        f.close()
        print("val label {0}/{1} made".format(key[:-4], len(val_data)))


if __name__ == '__main__':
    main()
