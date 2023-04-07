# 命令注入专题
专注于漏洞利用和防御。
主要是一些简单的Linux环境下的命令注入。

# 什么是RCE
远程命令/代码执行漏洞，简称RCE漏洞，可以让攻击者直接向后台服务器远程注入操作系统命令或者代码，从而控制后台系统。RCE分为远程命令执行ping和远程代码执行evel。

## 可能导致命令注入的函数
1. PHP
- system($cmd)
- exec($cmd, array $output)
- passthru($cmd)
- shell_exec($cmd)
- popen($cmd, $mode)
- proc_open($cmd, array $descriptorspec, array $pipes)

2. Python
- os.system()
- os.popen()
- subprocess.call()
- subprocess.run()
- subprocess.check_call()
- subprocess.check_output()
- pty.spawn
- commands.getstatusoutput(cmd)
- commands.getoutput(cmd)
- sh库，如sh.whoami()，sh.pwd()

3. Java
- java.lang.Runtime.getRuntime().exec(cmd)

## Linux命令的语法
1. |（管道符）
2. &（and符）
3. &&与||
4. ;(分号)
5. `（反引号）
6. 单引号和双引号
7. 输入输出重定向
8. 通配符
9. shell变量
10. $符

## 命令注入常见的绕过姿势
1. 空格绕过
2. 命令分隔符
3. 内联执行
4. 变量拼接执行
5. 花括号
6. 黑名单绕过

## 无回显的命令注入
1. 服务器和DNS日志
2. sleep
3. 利用暴露的服务
4. 反弹shell
5. 限制长度的利用
6. *的另一种用法
7. 四字绕过

## Linux下可以读取文件的工具
cat、tac、more、less、head、tail、nl、sort、grep、uniq、sed、awk、od
```shell
~$ sed '' /flag
flag{this_is_flag}

~$ awk 1 /flag
flag{this_is_flag}

~$ uniq /flag
flag{this_is_flag}

~$ grep '' /flag
flag{this_is_flag}

~$ od -c /flag
0000000   f   l   a   g   {   t   h   i   s   _   i   s   _   f   l   a
0000020   g   }  \n
0000023
```


# 参考

https://blog.csdn.net/Manuffer/article/details/120672448