# yaml is site-package library
# pip3 install PyYaml
import yaml

#read yaml
# with open('./test.yaml') as file_yaml:
#     text = yaml.load(file_yaml,Loader=yaml.FullLoader)
#     print(text)

#read various data type in same yaml
# with open('./test.yaml') as file_yaml:
#     text = yaml.load_all(file_yaml,Loader=yaml.FullLoader)
#     for one in text:
#         print(one)

#read Chinese from yaml
with open('./test.yaml', encoding='utf-8') as file_yaml:
    text = yaml.load_all(file_yaml,Loader=yaml.FullLoader)
    for one in text:
        print(one)