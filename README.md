> 近日工作中, 需要对目录结构写注释( readme 中), 方便同事上手, 抽闲写个脚本自动生成.

### 使用
1. 拷贝 start.py 到你的项目==根目录==中;
2. 执行 `python start.py`;
3. 在根目录会生成一个 `menu_struct.md` 的文件;

### 注意
在 `IGNORES` 这个变量存储被忽略的文件夹, 比如: `.git`、`node_modules`, 这些文件夹里的文件应该被忽略.

mac 使用无误, windows/linux 没有测试.

### 效果
一个 react 项目的目录结构:
![](http://onqlql2jb.bkt.clouddn.com/menu_struct1.png)

生成的文件结构如下:
```
├──.babelrc # babel 配置
├──.git # git 生成的
├──.gitignore # git 忽略文件
├──.idea # webstorm 编辑器生成的
├──.vscode # vscode 生成的
├──menuStruct.py # 目录生成脚本
├──node_modules # node 依赖包
├──package.json # node 依赖配置
├──public # 公用文件
|   ├──favicon.ico # 图标
|   └──index.html # 程序将挂载在此文件上
├──script # 开发脚本
|   ├──build.js
|   ├──config.js
|   ├──dev.js
|   ├──paths.js
|   ├──webpack.config.base.js
|   ├──webpack.config.dev.js
|   └──webpack.config.prod.js
└──src # 程序目录
|   ├──actions # 集中管理 actions
|   |   ├──common.js
|   |   ├──engine.js
|   |   └──user.js
|   ├──api # 封装 api, 偏于管理
|   |   ├──common.js
|   |   ├──engine.js
|   |   ├──fixurl.js
|   |   ├──index.js
|   |   ├──mock
|   |   |   ├──index.js
|   |   |   └──stores.js
|   |   └──user.js
|   ├──app.css # 全局样式文件
|   ├──assets # 存储静态资源
|   |   └──img
|   |   |   ├──loginbg.png
|   |   |   ├──logo.header.png
|   |   |   └──logo_blue.png
|   ├──components # 存储组件
|   |   ├──FFanBread # 公用面包屑导航
|   |   |   └──index.js
|   |   ├──FFanErrorNotify # 公用错误提醒
|   |   |   └──index.js
|   |   ├──FFanHeader # 公用 Head
|   |   |   └──index.js
|   |   └──FFanSider # 公用 Sider
|   |   |   ├──index.css
|   |   |   └──index.js
|   ├──constants # 常量集中管理
|   |   ├──actionTypes.js # 所有的 action type
|   |   └──index.js
|   ├──containers # 集中管理 react 容器
|   |   ├──app.js
|   |   ├──devTools.js
|   |   ├──header.js
|   |   ├──index.dev.js
|   |   ├──index.prod.js
|   |   ├──Root.dev.js
|   |   ├──Root.js
|   |   ├──Root.prod.js
|   |   └──store.js
|   ├──index.js # 入口脚本
|   ├──logo.svg # 项目 logo
|   ├──reducers # 集中管理 react reducers
|   |   ├──common.js
|   |   ├──engine.js
|   |   ├──index.js
|   |   ├──store.js
|   |   └──user.js
|   ├──routes.js # 路由配置
|   ├──store # react store
|   |   ├──configureStore.dev.js
|   |   ├──configureStore.js
|   |   └──configureStore.prod.js
|   ├──util.js # 自定义工具库
|   └──views # 页面
|   |   ├──about # 关于页面
|   |   |   └──index.js
|   |   ├──app 
|   |   |   └──index.js
|   |   ├──engine # 引擎页面
|   |   |   ├──attributeManagement.js
|   |   |   └──checkPointManagement.js
|   |   ├──error # 错误页面
|   |   |   └──index.js
|   |   ├──home # home 页面
|   |   |   └──index.js
|   |   ├──login # 登录页面
|   |   |   └──index.js
|   |   └──route.js # 页面路由
```
