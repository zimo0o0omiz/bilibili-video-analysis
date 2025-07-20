# bilibili-video-analysis

B站视频解析真实地址

## 前言

> 最近，突然想下B站自己发布的视频，但是，emmm，找了半天，没看到下载的地方；无奈之下，打开了f12，pc端的页面看了一下，video标签是有了，but地址是不（用）正（不）经（了）的，然后顺手就调出了手机端模式，嗯，这次video标签也有了，地址也是很（可）正（以）经（用）的，于是这个脚本便诞生了

## 用法

1. 下载或者clone仓库
    ```shell script
    git clone https://github.com/zimo0o0omiz/bilibili-video-analysis.git
    ```
2. 安装依赖
    ```shell script
    pip install -r requirements.txt
    ```
3. 命令行执行
    ```shell script
    python index.py -u "https://www.bilibili.com/video/BV1C9uXzbEWF/?spm_id_from=333.1391.0.0&vd_source=c89d805105084bae4f67ab6bb6f2f3f4"
    ```
4. 输出真实地址
    ```shell script
    https://upos-sz-mirrorkodo.bilivideo.com/upgcxcode/24/74/193237424/193237424-1-16.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1595934868&gen=playurl&
    os=kodobv&oi=3084701242&trid=1f31cfcd168d4950875f2c4aff18730bh&platform=html5&upsig=a623f30125481a3913738ec4ac1a46ea&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&logo=80000000
    ```
5. enjoy it！！！