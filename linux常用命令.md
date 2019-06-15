# Linux常用命令集合
* 简单自己常用命令
    1. cd
    2. ls
    3. passwd
    4. fdisk -l
    5. df -lh
    6. du -sh * 查看目录下各个文件或者目录的大小
    7. chattr -i .user.ini
    8. tar -xzvf .tar.gz  解压
    9. tar -czvf *.tar.gz * 压缩
    10. find ./* -mtime -5 -name *.php 查找最近5天修改的php文件
    11. chmod -R 777 * 
    12. chown -R www:www *
    13. cp  -r 源目录/* 指定目录
    14. mount  /dev/sdb1 /data
    15. hwclock         硬件时间  
        hwclock –w     硬件时间写入  
        hwclock --systohc  硬件时间同步系统时间
    16. ethtool eth0  查机器带宽
    17. date -s "2019-01-18 03:03:00"  重置时间
    18. screen -S abc  新建一个abc的窗口,断开也不会消失。
        screen -D abc  把窗口注销方便重新取回
        screen -r abc  取回窗口
        ctrl+a+d 断开窗口，保留状态。
    19. top 查看服务器状态
* 其他命令
https://github.com/xiaoqiangqiang2019/Python-100-Days/blob/master/Day31-35/31.%E7%8E%A9%E8%BD%ACLinux%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F.md    
    