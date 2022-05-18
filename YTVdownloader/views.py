
from django.shortcuts import render
from pytube import YouTube
from django.conf import settings
from django.views import generic
from .function import create_dir
import os, pathlib


class YoutubeDownloader(generic.FormView):

    def get(self, request, *args, **kwargs):
        
        return render(request, 'index.html')   


    def post(self, request, *args, **kwargs):
        try:
            
            # Web画面で指定したURLを取得
            link = request.POST['link']
            video = YouTube(link)
            #mp4形式で最低解像度のストリームを取得
            stream = video.streams.get_lowest_resolution()
            #動画ファイルの一時ダウンロード先フォルダ名の生成				
            temp_dir = create_dir(10)
            #ダウンロードディレクトリパスの取得
            download_dir = os.path.join(settings.BASE_DIR, temp_dir)
            #動画ファイルのダウンロード
            stream.download(download_dir)
            #ダウンロード先ディレクトリ配下にあるファイル情報を取得
            download_file = list(pathlib.Path(download_dir).glob('*'))
            #ファイル名の抽出
            file_name = str(download_file[0]).split("\\")[-1]
            print("file_name=", file_name)
            return render(request, 'index.html', {'temp_dir':temp_dir,
                                                  'file_name': file_name})
        except:
            return render(request, 'index.html', {'msg':'mp4 not created'})      
   
    
