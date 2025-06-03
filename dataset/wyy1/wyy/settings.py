BOT_NAME = "wyy"

SPIDER_MODULES   = ["wyy.spider"]
NEWSPIDER_MODULE = "wyy.spider"

ITEM_PIPELINES = {
    'wyy.pipelines.WyymusicPipeline': 300,   # 路径要写成“包名.模块名.类名”
}

 #去除掉日志中其他描述性的信息，只输出我们需要的信息
LOG_LEVEL = "WARNING"  
 
USER_AGENT = 'edge' 
#默认为True，更改为False，即不遵守君子协定
ROBOTSTXT_OBEY = False     
 
#下载延迟，可以设为每下载一次暂停2秒，以防下载过快被禁止访问
DOWNLOAD_DELAY = 0.2
 
 
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',    #不要这条代码
}