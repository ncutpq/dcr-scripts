### 1. 编写 cpp

### 2. 编写 CMakeLists.txt

### 3. 编写打包文件 setup.py

### 4. 在当前环境中安装自定义的扩展包
    在 setup.py 同级目录下执行命令： pip install . (执行完会生成build文件夹和egg-info文件夹，并在环境中安装自定义扩展包)

### 5. 使用自定义扩展包
    import + (setup.py-->setup-->ext_modules)

### 6. 卸载自定义扩展包
    pip uninstall XXX