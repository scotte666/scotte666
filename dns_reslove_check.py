#!/usr/bin/python
# -*- coding: utf-8 -*-
import  dns.resolver
import subprocess
domain_list=["www.goole.com","www.baidu.com"]
dns_list=["114.114.114.114","119.29.29.29","223.5.5.5","117.50.10.10","123.125.81.6"]
def sh():
    for d in domain_list:
        for  i in dns_list:
            cmd=f'/root/dns_reslove_check.sh {d} {i}'.format(d=d,i=i)
            print(cmd)
            process=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            output, _ = process.communicate()

def check_domain_available():
    for d in domain_list:
        for i in dns_list:
            try:
                ms=dns.resolver.Resolver()
                ms.nameservers=[i]
                answer=ms.query(d,"A")
                host=["88.88.88.88"]
                for i in answer:
                    if str(i)  in host:
                        print("域名正常")
                    else:
                        print("域名解析一场")
            except dns.resolver.NoNameservers:
                pass
check_domain_available()
