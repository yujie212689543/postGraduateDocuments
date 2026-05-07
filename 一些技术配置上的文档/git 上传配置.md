# 方案一：（正在用）上传使用代理路径
### 🔹检查代理设置（如果你在用梯子/加速器）
***实际端口号为：127.0.0.1:6478***

如果你正在使用代理软件（Clash、V2Ray、机场等），Git 本身**不会自动走代理**，需要手动设置。

1. **先确认代理地址和端口**  
    打开你的代理软件，找到它的本地 HTTP/HTTPS 端口号（通常类似 `127.0.0.1:7890` 或 `localhost:10809`）。
    
2. **给 Git 配置代理**  
    打开终端（CMD 或 Git Bash），输入以下命令（请换成你自己的地址和端口）：
    
    
    ~~~bash
    
    git config --global http.proxy http://127.0.0.1:7890
    git config --global https.proxy http://127.0.0.1:7890
    ~~~
    如果你的代理是 SOCKS5，则用：
    
    ~~~bash
    
    git config --global http.proxy socks5://127.0.0.1:7890
    git config --global https.proxy socks5://127.0.0.1:7890
    ~~~
    
    配置完成后，再在 Obsidian 里推送试试。
    
3. **如何撤销代理（如果没用）**  
    如果设置后反而不能用了，运行下面命令取消：
    
    ~~~bash
    
    git config --global --unset http.proxy
    git config --global --unset https.proxy
    ~~~

# 方案二：使用SSH
