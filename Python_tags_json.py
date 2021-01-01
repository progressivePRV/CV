class tag:
    def __init__(self,tag):
        self.tag_name = tag
        self.attributes = []

    def insert_attribute(self,atr):
        self.attributes.append(atr)

    def print_attributes(self):
        for i in self.attributes:
            print(i)

    def __str__(self):
        
        for i in self.attributes:
        return output

##import json
##lines = []
##with open("HTML_tags.txt","r") as f1:
##    lines = f1.readlines()
t = tag("html")
t.insert_attribute("doctype")
print(t)
    
