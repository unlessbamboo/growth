# 打包个人博客docker环境

# 1. NODE 基础环境
FROM node:10
# 2. 维护者信息
MAINTAINER unusebamboo unusebamboo@163.com
# 3. 工作目录
WORKDIR /hexo

# 4. 安装hexo(使用淘宝源)
RUN git config --global user.name "unusebamboo"
RUN git config --global user.email "unusebamboo@163.com"

RUN npm --registry https://registry.npm.taobao.org install hexo-cli -g
# 在docker高级版本(17.07 +), 直接设置docker客户端配置, 设置代理即可
RUN hexo init .

RUN npm --registry https://registry.npm.taobao.org install

# 5. 映射端口
EXPOSE 4000
# 6. 运行命令
# CMD ["/bin/bash"]
# 在compose需要设置一个持续运行的服务
CMD ["/usr/bin/env", "hexo", "server"]
