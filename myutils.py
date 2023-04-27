import openslide
import os
from PIL import Image

import yolox.predict as predict_yolox

Image.MAX_IMAGE_PIXELS = None


def compress(path, w, h, save):
    print('crop path:{}'.format(path))
    if os.path.isfile(path):
        print('\n处理单张图片')
        try:
            slide = openslide.open_slide(path)
            filename = ''
            for i in range(len(path.split('/')[-1].split('.')) - 1):
                if i >= 1:
                    filename += '.'
                filename += path.split('/')[-1].split('.')[i]
            slide.get_thumbnail((w, h))
            father_path = os.path.join(save, 'compress_result')
            if not os.path.exists(father_path):
                os.makedirs(father_path)
            save_path = os.path.join(father_path, filename + '.png')
            slide.save(save_path)
            slide.close()
        except Exception:
            raise IOError('路径中存在非图片文件')
    elif os.path.isdir(path):
        print('\n处理多张图片')
        try:
            for j in os.listdir(path):
                one_path = os.path.join(path, j)
                slide = openslide.open_slide(one_path)
                filename = ''
                for i in range(len(one_path.split('/')[-1].split('.')) - 1):
                    if i >= 1:
                        filename += '.'
                    filename += one_path.split('/')[-1].split('.')[i]
                slide.get_thumbnail((w, h))
                father_path = os.path.join(save, 'compress_result')
                if not os.path.exists(father_path):
                    os.makedirs(father_path)
                save_path = os.path.join(father_path, filename + '.png')
                slide.save(save_path)
                slide.close()
        except Exception:
            raise IOError('路径中存在非图片文件')
    else:
        raise ValueError('传入的路径错误')


def crop(path, size, save):
    print('\ncrop path:{}'.format(path))
    if os.path.isfile(path):
        print('\n处理单张图片')
        try:
            filename = ''
            for i in range(len(path.split('/')[-1].split('.')) - 1):
                if i >= 1:
                    filename += '.'
                filename += path.split('/')[-1].split('.')[i]
            image = Image.open(path)
            # print(image.size)
            row = int(image.size[0] / size)
            column = int(image.size[1] / size)
            image = image.resize(((row + 1) * size, (column + 1) * size))
            father_path = os.path.join(save, 'crop_results', filename)
            if not os.path.exists(father_path):
                os.makedirs(father_path)
            for r in range(1, row + 1):
                for c in range(1, column + 1):
                    box = ((r - 1) * size, (c - 1) * size, r * size, c * size)
                    cropped = image.crop(box)
                    cropped.save(
                        os.path.join(father_path, filename + '~' + str(r) + '_' + str(c) + '.png'))
                    cropped.close()
            image.close()
        except Exception:
            raise IOError('路径中存在非图片文件')
    elif os.path.isdir(path):
        print('\n处理多张图片')
        try:
            for j in os.listdir(path):
                one_path = os.path.join(path, j)
                filename = ''
                for i in range(len(one_path.split('/')[-1].split('.')) - 1):
                    if i >= 1:
                        filename += '.'
                    filename += one_path.split('/')[-1].split('.')[i]
                image = Image.open(one_path)
                # print(image.size)
                row = int(image.size[0] / size)
                column = int(image.size[1] / size)
                image = image.resize(((row + 1) * size, (column + 1) * size))
                father_path = os.path.join(save, 'crop_results', filename)
                if not os.path.exists(father_path):
                    os.makedirs(father_path)
                for r in range(1, row + 1):
                    for c in range(1, column + 1):
                        box = ((r - 1) * size, (c - 1) * size, r * size, c * size)
                        cropped = image.crop(box)
                        cropped.save(
                            os.path.join(father_path, filename + '~' + str(r) + '_' + str(c) + '.png'))
                        cropped.close()
                image.close()

        except Exception:
            raise IOError('路径中存在非图片文件')
    else:
        raise ValueError('传入的路径错误')


def predict(path, save):
    print('\npredict path:{}'.format(path))
    if not os.path.exists(os.path.join(save, 'predict_results')):
        os.makedirs(os.path.join(save, 'predict_results'))
    if os.path.isdir(path):
        try:
            filenames = os.listdir(path)
            for filename in filenames:
                names = os.listdir(os.path.join(path, filename))
                for name in names:
                    predict_image_path = os.path.join(path, filename, name)
                    save_image_path = os.path.join(save, 'predict_results', filename, name)
                    if not os.path.exists(os.path.join(save, 'predict_results', filename)):
                        os.makedirs(os.path.join(save, 'predict_results', filename))
                    # predict here
                    print('predict_image_path:{}'.format(predict_image_path))
                    print('save_image_path:{}'.format(save_image_path))
                    predict_yolox.predict(predict_image_path, save_image_path, "predict")
        except Exception:
            raise IOError('路径中存在非图片文件')
    else:
        raise ValueError('传入的路径错误')


def stitch(path, save):
    print('\nstitch path:{}'.format(path))
    if not os.path.exists(os.path.join(save, 'stitch_results')):
        os.makedirs(os.path.join(save, 'stitch_results'))
    if os.path.isdir(path):
        try:
            filenames = os.listdir(path)
            for filename in filenames:
                names = os.listdir(os.path.join(path, filename))
                temp_image = Image.open(os.path.join(path, filename, names[0]))
                size = temp_image.size[0]
                temp_image.close()
                max_row = 0
                max_column = 0
                for name in names:
                    row = int(name.split('~')[1].split('_')[0])
                    max_row = max(max_row, row)
                    column = int(name.split('~')[1].split('_')[1].split('.')[0])
                    max_column = max(max_column, column)
                image = Image.new('RGB', (max_row * size, max_column * size))
                for name in names:
                    row = int(name.split('~')[1].split('_')[0])
                    column = int(name.split('~')[1].split('_')[1].split('.')[0])
                    cropped = Image.open(os.path.join(path, filename, name))
                    box = ((row - 1) * size, (column - 1) * size, row * size, column * size)
                    image.paste(cropped, box)
                image.save(os.path.join(save, 'stitch_results', filename + '.png'))
                image.close()
        except Exception:
            raise IOError('路径中存在非图片文件')
    else:
        raise ValueError('传入的路径错误')
