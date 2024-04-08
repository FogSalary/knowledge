
操作系统：Windows 11
测试日期：2024年4月1日

### Hexo安装

首先需要安装 
- Node.js
- Git

`npm install -g hexo-cli`

判断安装是否成功 `hexo -v`

创建一个新文件夹用于存放站点相关配置文件，进入文件夹目录
``` bash
hexo init
npm install
```

hexo 生成与本地服务启动

``` bash
hexo g
hexo s
```

hexo 个人博客部署

``` bash
hexo d

output:
INFO  Validating config
ERROR Deployer not found: git


npm install hexo-deployer-git --save
hexo d 
```


## Hexo 美化

`npm i hexo-theme-butterfly`









## Reference
[Hexo Doc](https://hexo.io/zh-cn/docs/)
[Node.js](https://nodejs.org/en)
[Github + Hexo 搭建个人博客教程](https://zhuanlan.zhihu.com/p/655349835)
[解决 hexo d 命令错误提示 Deployer not found: git](https://blog.csdn.net/Java_Mike/article/details/96456318)
[Hexo butterfly 主题美化](https://blog.csdn.net/JesseXW/article/details/135649752)

### Hexo 常用命令
``` bash
npm install hexo -g # 安装 hexo
npm update hexo -g # 升级
hexo init # 初始化博客

hexo n "我的博客"
hexo new "我的博客" # 新建文章
hexo g
hexo generate #生成
hexo s
hexo server # 启动服务预览
hexo d
hexo deploy # 部署

hexo server #Hexo会监视文件变动并自动更新，无须重启服务器
hexo server -s #静态模式
hexo server -p 5000 #更改端口
hexo server -i 192.168.1.1 #自定义 IP
hexo clean #清除缓存，若是网页正常情况下可以忽略这条命令

```