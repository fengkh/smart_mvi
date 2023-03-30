import openslide
import os


def compress(path, w, h):
    print('crop path:{}'.format(path))
    if os.path.isfile(path):
        print('\n处理单张图片')
        try:
            slide = openslide.open_slide(path)
            filepath = ""
            filename = ''
            for i in range(len(path.split('/')) - 1):
                filepath += path.split('.')[i]
            for i in range(len(path.split('/')[-1].split('.')) - 1):
                filename += path.split('/')[-1].split('.')[i]
            slide.get_thumbnail((w, h))
            save_path = os.path.join(filepath, filename + '.png')
            slide.save(save_path)
            slide.close()
        except:
            raise IOError('路径中存在非图片文件')
    elif os.path.isdir(path):
        print('\n处理多张图片')
        try:
            for j in os.listdir(path):
                slide = openslide.open_slide(path)
                filepath = ""
                filename = ''
                for i in range(len(path.split('/')) - 1):
                    filepath += path.split('.')[i]
                for i in range(len(path.split('/')[-1].split('.')) - 1):
                    filename += path.split('/')[-1].split('.')[i]
                slide.get_thumbnail((w, h))
                save_path = os.path.join(filepath, filename + '.png')
                slide.save(save_path)
                slide.close()
        except:
            raise IOError('路径中存在非图片文件')
    else:
        raise ValueError('传入的路径错误')
