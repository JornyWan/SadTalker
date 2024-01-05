import numpy as np
from scipy.io import loadmat
from annoy import AnnoyIndex
import imageio
import time

file_names = [f"overwatch##{i}_enhanced_img_array.npy" for i in range(1, 6)]
arrays = [np.load(file) for file in file_names]
arrays = np.vstack(arrays)


file_names = [f"overwatch##{i}.mat" for i in range(1, 6)]
mat_contents = [loadmat(file)['coeff_3dmm'] for file in file_names]
mat_contents = np.vstack(mat_contents)

f = 70 
t = AnnoyIndex(f, 'angular') 
for i in range(mat_contents.shape[0]):
    t.add_item(i, mat_contents[i])
t.build(30)

def find_most_similar_annoy(A, B, C, t):
    
    results = []
    for row in C:
        most_similar_index = t.get_nns_by_vector(row, 1)[0]   
        corresponding_image = B[most_similar_index]
        results.append(corresponding_image)
    results = np.stack(results, axis=0)
    
    return results


mat_contents = loadmat('overwatch##0.mat')['coeff_3dmm']
time1 = time.time()
corresponding_images = find_most_similar_annoy(mat_contents, arrays, mat_contents, t)
time2 = time.time()
imageio.mimsave('this_is_testing_video.mp4', corresponding_images, fps=float(25))
print('total time: {}'.format(time2-time1))