#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#include <sys/types.h>
#include <errno.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/select.h>
#include <unistd.h>
#include <termios.h>
#include <sys/stat.h>
/**********定时器头文件***************/
#include <sys/time.h> 
#include <signal.h> 
/***********进程间SOCKET通信头文件**********/
#include <sys/socket.h> 
#include <sys/un.h> 

#include <sys/ioctl.h>
#pragma pack(1)         //设定为1字节对齐
#define UNIX_DOMAIN2 "/tmp/UNIX2.domain" 

struct test
{
    char name[32];
    int  b;
    int  c;
    int  data[100];
}se;

int main(void)
{
    int                         connect_fd;
    int                         ret=0;
    static struct sockaddr_un   srv_addr; 

    printf("ipc通信线程\n");

    //创建用于通信的套接字，通信域为UNIX通信域 
    connect_fd=socket(AF_UNIX,SOCK_STREAM,0); 
    printf("%d\n",connect_fd); 
    if(connect_fd<0)
    { 
        perror("cannot create communication socket");
        printf("%d\n",connect_fd); 
        //continue;
    } 
    else
    {
        srv_addr.sun_family=AF_UNIX; 
        strcpy(srv_addr.sun_path,UNIX_DOMAIN2);
    
        //连接服务器 
        ret=connect(connect_fd,(struct sockaddr*)&srv_addr,sizeof(srv_addr)); 
        if(ret==-1)
        { 
            close(connect_fd); 
            printf("connect fail\n");
            //break;            //重新创建socket
        }
        else
        {   
            memset(&se, 0, sizeof(se));
            strcpy(se.name, "xxxxx");
            se.b=0x01020304;
            se.c=0x05060708;
            write(connect_fd, &se, sizeof(se));//将数据传送到外部应用程序,发送实际长度
            /*
            //write(connect_fd,&se,sizeof(struct test));
            memset(recv_php_buf,0,sizeof(recv_php_buf));                             //清空socket_buf
            //sleep(1);
            //fcntl(connect_fd,F_SETEL,O_NONBLOCK);
            read(connect_fd,recv_php_buf,sizeof(recv_php_buf));
            printf("receive over\n");
            for(i=0;i<20;i++)
            printf("%x ",recv_php_buf[i]);
            //printf("%x ",se.a);
            //printf("%x ",se.b);
            //printf("%x ",se.c);
            */
            sleep(1);
            close(connect_fd);
            //break;                            
        }
    }
    return 0;
}
