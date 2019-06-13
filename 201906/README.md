# 今天主要熟悉git的相关使用。
### 相关重点如下：  
1. 安装配置Visual Studio Code跟git
2. 配置git同步到github  
    主要参照：  
    https://blog.csdn.net/fylstudio/article/details/79106331  
    https://www.runoob.com/git/git-remote-repo.html

3. git使用要点：  
#### git 配置
    1，用Git Bash  
    2，在文件夹上直接右键Git Bash Here  
    git config --global user.name "你自己的用户名"  
    git config --global user.email "你自己的邮箱"  
    git init   (初始化)  
    git add .  (暂存文件)  
    git add -A  (提交所有变化) 
    git add -u  {提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)}  
    git add .  {提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件}
    ssh-keygen -t rsa -C "你自己的邮箱"  (生成ssh公钥)  

#### GitHub配置  
    +号--Settings--SSH and GPG keys
#### 配置远程仓库
    git remote add  远程仓库的名称（随意） 刚才复制的远程仓库的地址（这个很重要，不能错）  
    ssh -T git@github.com  (测试配置是否正确)  
    git remote -v  (查看所有远程库)  
    git remote rm 项目名  (删除远程库)  
    git add 文件名     (添加文件)  
    git add 文件夹/    (添加文件夹)  
    git commit -m "添加 README.md 文件"   (提交到本地库并备注信息)  
    git pull 项目名 master  (拉取项目到本地)  
    git push 项目名 master  (推送项目到远程github仓库中)  
    git fetch 项目名  (从远程仓库下载新分支与数据)  
    git merge 项目名/master  (从远端仓库提取数据并尝试合并到当前分支)

#### 注意要点：
    必须先git add 文件或者文件夹，然后再git add . 暂存文件  
    再git commit -m "备注" 提交到本地  
    最后才能 git push 项目 到远程github仓库中。
