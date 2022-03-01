import cv2
import os
def save_img():
    video_path = os.getcwd() # 获取当前位置所在文件夹 
    # print(video_path)
    videos = os.listdir(video_path) # 获取当前文件夹下所有文件名称，返回一个列表
    # print(videos)
    
    for video_name in videos:
        file_name = video_name.split('.')[0] # 获得文件名
        folder_name = video_path + '_' +file_name # 生成文件夹名
        os.makedirs(folder_name, exist_ok=True) # 新建文件夹
        vc = cv2.VideoCapture(video_path+'/'+video_name) #
        c=0
        rval=vc.isOpened() # 判断是否打开

        while rval:  
            c = c + 1
            rval, frame = vc.read()
            pic_path = folder_name+'/' # 新生成文件夹的目录
            if rval:
                cv2.imwrite(pic_path + str(c) + '.jpg', frame) # 逐帧生成jpg文件
                cv2.waitKey(1) # 等待1ms
            else:
                break
        vc.release() # 释放
        print('save_success',end=':')
        print(folder_name)
save_img()
