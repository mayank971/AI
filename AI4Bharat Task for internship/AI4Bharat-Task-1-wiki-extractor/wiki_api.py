from re import search
import wikipedia
import json
class Wikipedia_info(object):
    def __init__(self,keyword,m):
        self.keyword=keyword
        self.m=m
        self.search_results=wikipedia.search(keyword,results=self.m+5) # extra seach incase of disambiguation or pages not available)
        for y in self.search_results:
            if "(disambiguation)" in y:
                self.search_results.remove(y)


    def output_builder(self):
        self.json_object=[]
        count=0
        for y in self.search_results:
            
            try:
                url=wikipedia.page(y).url
                paragraph=wikipedia.summary(y,sentences=3).strip()
                self.json_object.append({"url":url,"paragraph":paragraph})
            except:
                continue
            if count==self.m-1:
                break
        return json.dumps(self.json_object,indent=2)