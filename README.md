# chestnut-seaurchin-classifier
<img src="https://github.com/baibai25/chestnut-seaurchin-classifier/blob/master/images/1.jpeg" width=60%>

## Our goal
Our goal is to accurately classify sea urchins and chestnuts. 
The ultimate goal is to correctly predict `chestnuts in the water`.

## Article (Japanese)
https://qiita.com/baibai25/items/93dfd703ccba6e097ba5

## Demo
You can easily try to demo.

1. Download model
https://drive.google.com/open?id=1Yoq3Nwx72zXTtANvEqp_aNCvoo3wtk_A

2. Run with YOLO

```
./darknet detector test cfg/foo.data cfg/foo.cfg unikuri_best.weights test_img.jpg
```

### Translation
kuri means chestnut.
uni means sea urchin.

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

For more details, refer to the https://github.com/AlexeyAB/darknet?files=1.

## Result
<img src="https://github.com/baibai25/chestnut-seaurchin-classifier/blob/master/images/plot.png" width=60%>
<img src="https://github.com/baibai25/chestnut-seaurchin-classifier/blob/master/images/2.jpeg" width=60%>
