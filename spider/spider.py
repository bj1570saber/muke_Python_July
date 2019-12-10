from urllib import request
import ssl
import re

class Spider():
    url = 'https://www.youtube.com/'
    root_pattern = '<div class="yt-lockup-dismissable">([\s\S]*?)</div> ([\s\S]*?)</div>'
#<div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/TheEllenShow" class="yt-uix-sessionlink       spf-link " data-sessionlink="itct=CF8QlDUYBiITCI3qy_zKqeYCFdujxAod7vcNVg">TheEllenShow</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div>

    # ? non greedy make the retrieve process stop at first </div>
    <a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/channel/UCf9_s9ii6BZ-klpgmtIi3WQ">Team Fearless</a>
    name_pattern = '<a class="yt-simple-endpoint style-scope yt-formatted-string"([\s\S]*?)>'

    def __fetch_content(self):
        # 生成证书上下文(unverified 就是不验证https证书)
        context = ssl._create_unverified_context()
        
        r = request.urlopen(Spider.url, context=context)
        htmls = r.read() # bytes
        htmls = str(htmls, encoding = 'utf-8')
        return htmls

    def __analysis(self, htmls):
        #print(htmls)
        file1 = open("afile.txt","w") 
        file1.write(htmls) 
        file1.close()
        root_html = re.findall(Spider.root_pattern, htmls)
        file2 = open("output_file.txt","w") 
        file2.write(str(root_html)) 
        file2.close()
        #print(root_html)
        a = 1

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)

spider = Spider()
spider.go()

