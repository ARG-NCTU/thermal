#imgtransform

import cv2
import os
import glob
import tqdm
import numpy as np
class TermalProcess:
    def __init__(self, datadir = '/home/leowamg/catkin_ws/src/thermal_cam/images'):
        self.datadir = datadir
        self.bags = sorted(os.listdir(self.datadir))
        print(f'Folder in dataset :', len(self.bags) ,' -----> ', self.bags, '\n')
        self.thermal_image_paths = [[] for _ in self.bags]
        for i, bag in enumerate (self.bags):
            # thermal_image_dir = os.path.join(self.datadir, bag, 'thermal_image_compressed')
            # thermal_image_pattern = os.path.join(thermal_image_dir, '*.jpg')
            thermal_image_pattern = os.path.join(self.datadir, '*.jpg')
            self.thermal_image_paths[i].extend(glob.glob(thermal_image_pattern))
            print(f'Thermal image number in bag {bag}:', len(self.thermal_image_paths[i]))
    def custom_jet_colormap(self, img=None, vmin=50, vmax=200):
        jet_range = 255  # The range of the jet colormap
        if img is None:
            print('Image not found')
            return None
        else:
            ## 1
            # normalized_image = img.astype(np.float32) / 255.0
            # vmin = normalized_image.min()
            # vmax = normalized_image.max()
            # normalized_image = (img - vmin) / (vmax - vmin)
            # mapped_image = (normalized_image * jet_range).astype(np.uint8)
            # img_jet = cv2.applyColorMap(mapped_image, cv2.COLORMAP_JET)
            # print(f"vmin: {(vmin*255).astype(np.uint8)}, vmax: {(vmax*255).astype(np.uint8)}")
            ## 2
            # for i in range(img.shape[0]):
            #     for j in range(img.shape[1]):
            #         img[i][j] = (img[i][j] - vmin)
            #         img[i][j] *= 1.5
            #         if img[i][j] < vmin:
            #             img[i][j] = 0
            #         elif img[i][j] > vmax:
            #             img[i][j] = 255
            # img_jet = cv2.applyColorMap(img, cv2.COLORMAP_JET)
            # img_jet = cv2.convertScaleAbs(img_jet, alpha=255.0 / (vmax - vmin), beta=-vmin * 255.0 / (vmax - vmin))
            # 3
            # img_jet = cv2.applyColorMap(img, cv2.COLORMAP_WINTER)
            # 4
            normalized_image = img.astype(np.float32) / 255.0
            min_intensity = 0.34  # Adjust as needed
            max_intensity = 0.66  # Adjust as needed
            stretched_image = np.clip((normalized_image - min_intensity) / (max_intensity - min_intensity), 0, 1)
            equalized_image = cv2.equalizeHist((normalized_image * 255).astype(np.uint8)) / 255.0
            # Create a colormap mapping from black to blue and white to red
            img_jet = cv2.applyColorMap((stretched_image * 255).astype(np.uint8), cv2.COLORMAP_TURBO)
            # img_jet = cv2.applyColorMap((stretched_image * 255).astype(np.uint8), cv2.COLORMAP_WINTER)
            # or
            # img_jet = cv2.applyColorMap((equalized_image * 255).astype(np.uint8), cv2.COLORMAP_TURBO)
            return img_jet
    def main(self):
        for j in tqdm.tqdm(range(len(self.bags))):
            for k in tqdm.tqdm(range(len(self.thermal_image_paths[j])), desc=f'Processing {self.bags[j]}', leave=True):
                print(self.thermal_image_paths[j][k])
                filename = os.path.basename(self.thermal_image_paths[j][k])
                #directory = os.path.join(self.datadir, self.bags[j], 'thermal_image_converted')
                img = cv2.imread(self.thermal_image_paths[j][k], cv2.IMREAD_GRAYSCALE)
                print(img)
                img_new = self.custom_jet_colormap(img, vmin=50, vmax=180)
                # cv2.imshow('img', img_new)
                # cv2.waitKey(500)。s
                # os.makedirs(directory, exist_ok=True)
                # cv2.imwrite(os.path.join(directory, filename), img_new)

                os.makedirs(self.datadir+"/thermal_image_converted", exist_ok=True)
                cv2.imwrite(os.path.join(self.datadir+"/thermal_image_converted", filename), img_new)
        print('\n ===== Finish ===== \n')
if __name__ =='__main__':
    termal_processing = TermalProcess(datadir = '/home/leowamg/catkin_ws/src/thermal_cam/images/1012_14_29')
    termal_processing.main()