# coding:utf-8
import requests
import re
import random


class Joke():
	_url = 'http://www.qiushibaike.com/text/'
	def getJoke(self):
		resp = requests.get(self._url)
		resp.encoding = 'utf-8'
		content = resp.content
		pageCount = re.findall(r'<span class="page-numbers">\n(.*?)\n</span>', content, re.S)[-1]
		page_url = self._url + 'page/'+str(random.randint(1, int(pageCount)+1)) +'/'
		resp = requests.get(page_url)
		resp.encoding = 'utf-8'
		content = resp.content
		jokes = re.findall(r'<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>', content, re.S)
		num = random.randint(0, 20)
		joke = jokes[num][0]
		joke = joke.replace("&acute;", chr(39)) #'替换单引号
		joke = joke.replace("&quot;", chr(34))    #'替换双引号
		joke = joke.replace("&lt;", "<")    #'替换<
		joke = joke.replace("&gt;", ">")    #'替换>
		joke = joke.replace("<br/>", chr(13)) #'替换回车符
		joke = joke.replace("&nbsp;", chr(32)) #'替换空格符
		joke = joke.replace("\n", "") #'替换空格符
		return joke + "\n" + jokes[num][1] + "赞"

def main():
	print Joke().getJoke()

if __name__ == '__main__':
	main()

