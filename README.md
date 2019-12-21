
# chestnut-seaurchin-classifier

## Scraping
-k: Search words  
-l: Number of images to download 
```
python download.py -k keywords A, keywords B -l 1000
```

## Data augmentation
-i: Input directory  
-o: Output directory
```
python augmentation.py -i input_dir -o output_dir
```


## Building a object detector using YOLO
1. Download
```
git clone https://github.com/AlexeyAB/darknet.git
cd darknet/
make

wget https://pjreddie.com/media/files/darknet53.conv.74
```
2. Move labeled data

3. Define learning settings  
cfg/foo.data  
cfg/foo.names  
cfg/foo.cfg  

4. Training
```
./darknet detector train cfg/foo.data cfg/foo.cfg darknet53.conv.74 
```
