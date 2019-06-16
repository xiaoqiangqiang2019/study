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
    +号--Settings--SSH and GPG keys(id_rsa.pub填入这个密匙)
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
    git checkout 分支名 (切换到分支)  
    git pull main 分支名 (拉取主仓库的分支名 分支最新的代码到本地，跟本地分支名 合并)

#### 拉取项目注意要点：
    * 拉取项目之前，新建的文件夹必须初始化git init,然后再git remote add 配置远程仓库  
      然后通过git fetch和git merge下载项目到本地  

      ** git pull可以理解为：git fetch跟git merge **
     
        * 保险点的做法
         git fetch orgin master //将远程仓库的master分支下载到本地当前branch中  
         git log -p master  ..origin/master //比较本地的master分支和origin/master分支的差别  
    　   git merge origin/master //进行合并

        * 也可以用以下指令：
         git fetch origin master:tmp //从远程仓库master分支获取最新，在本地建立tmp分支  
         git diff tmp //將當前分支和tmp進行對比  
         git merge tmp //合并tmp分支到当前分支

#### 提交项目主要要点：
        * 必须先git add 文件或者文件夹，然后再git add . 暂存文件  
          再git commit -m "备注" 提交到本地  
          最后才能 git push 项目 到远程github仓库中。

#### 给其他人的github项目提交pull request
	      fork那个项目  
	      然后在自己fork好的项目上 use ssh 的方式  clone 到本地开发环境中修改代码  
	      git add -A  
	      git commit -m "some change"  
	      git push  
	      然后回到自己fork好的项目页面 clone or download 左下方有个 Pull request  
	      点击 就可以提交这个pull request给原作者了

### 新建目录复制项目只要执行以下操作
* 在文件夹上直接右键Git Bash Here
* git init   (初始化)
* git remote add  远程仓库的名称（随意） 刚才复制的远程仓库的地址（这个很重要，不能错）          