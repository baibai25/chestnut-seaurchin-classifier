# Remove unpaired files
import glob, os, shutil

images = glob.glob('./img*jpg')
labels = glob.glob('./img*txt')

os.makedirs('./missed_label', exist_ok=True)

for i in range(len(images)):
    a = os.path.splitext(os.path.basename(images[i]))[0]
    
    flag = 0
    for j in range(len(labels)):
        b = os.path.splitext(os.path.basename(labels[j]))[0]
        
        if a == b:
            flag = 1
            break
        
    if flag == 0:
        shutil.move(images[i], './missed_label/')

