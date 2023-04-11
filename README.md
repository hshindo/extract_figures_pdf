# Extract figures and captions from PDF

### Setup
* Python 3.9+
* PyTorch 最新版
* `pip install Pillow pymupdf`
* [yolov5](https://github.com/ultralytics/yolov5)
  * git cloneして，`pip install -r requirements.txt` を実行しておく．


### PDFを画像に変換
* ルートディレクトリを `/data/path` として，この中にpdfファイルを全て置く．
* 以下を実行
```
python pdf_to_image.py /data/path
```
* `/data/path` 内の全てのpdfファイルを一括処理する．
画像化したファイルは，`/data/path/images` に保存される．


### 図の領域を抽出
* `yolov5` ディレクトリに入って作業する．
* [yolov5x_publaynet_figure_800.pt](https://drive.google.com/file/d/1BnCZP4hwenl7DHqQc6R7wrtVwt8W_CLV/view?usp=share_link) をダウンロードして，`yolov5/`に置く．
* 以下を実行
```
python detect.py --weights yolov5x_publaynet_figure_800.pt --source /data/path/images --imgsz 800 --save-txt
```
* 結果は，`yolov5/runs/detect/exp` 以下に出力されているので，その中の`labels` を`/data/path/labels` へコピーする．


### 図の切り出しとキャプションを出力
* 以下を実行
```
python extract_figure.py /data/path
```
* 結果は，`figures` に出力される．
