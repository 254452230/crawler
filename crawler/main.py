from scrapy import cmdline


#you need to setup a main () here to use debugger
# google ing , I forgot the syntax
#ok

if __name__ == "__main__":
    cmdline.execute("scrapy crawl leetcode -o item.json".split())
