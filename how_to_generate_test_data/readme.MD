# how to generate test data?

## 1, 创建工程，添加环境，建议使用虚拟环境

## 2, 利用如下命令安装所需工具包
    
       pip install -r requirements.txt

## 3, 切换到工程根目录，执行如下命令，生成数据库表对应的Model

       sqlacodegen mysql://adbibo:adbibo@127.0.0.1:3306/dms_test --outfile models.py 
       
## 4，将本目录下的settings.py拷到工程目录下，并配置数据库信息，参照example.py来对数据进行处理。


# 本示例主要是利用faker工具加上SQLAlchemy，了解这两个工具的使用即可快速方便地进行有效的数据处理了。