# Sticker Project Guide

本指南将指导你如何更换贴纸图片源、使用自动化脚本更新配置，并将项目托管到 Cloudflare Pages。

## 1. 更换/添加贴纸图片

所有贴纸图片都存储在 `public/img` 目录下。

### 目录结构规则
脚本会扫描 `public/img` 下的一级子文件夹，将每个子文件夹视为一个“角色”。
- **文件夹名** = 角色代码 (Character ID)
- **文件名** = 图片显示名称

**示例结构：**
```
public/img/
├── hero/              <-- 角色: hero
│   ├── Hero_01.png    <-- 名称: Hero 01
│   └── Hero_02.png    <-- 名称: Hero 02
└── villain/           <-- 角色: villain
    ├── Boss_A.jpg
    └── Boss_B.png
```

### 操作步骤
1.  打开 `public/img` 目录。
2.  创建你的角色文件夹（例如 `my_character`）。
3.  将 PNG/JPG 图片放入该文件夹中。
    *   建议文件名使用下划线 `_` 代替空格，脚本会自动将其转换为空格（例如 `Cool_Pose.png` -> `Cool Pose`）。

## 2. 自动生成配置文件

本项目包含一个 Python 脚本，可以自动扫描上述图片目录并生成 `src/characters.json` 配置文件。

### 前置要求
- 你的电脑上需要安装 [Python](https://www.python.org/)。

### 运行脚本
在项目根目录下，打开终端（Terminal / CMD / PowerShell），运行以下命令：

```bash
npm run generate
```
或者直接运行 Python 脚本：
```bash
python scripts/generate_characters.py
```

脚本运行成功后，会覆盖 `src/characters.json` 文件。

### 自定义文字颜色
如果你想为特定的角色设置默认的文字颜色（而不是默认的黑色），可以打开 `scripts/generate_characters.py` 文件，修改 `COLOR_MAP` 变量：

```python
# Color map for specific characters
# Format: "character_folder_name": "#HEXCOLOR"
COLOR_MAP = {
    "akari": "#ffd0d4",
    "yuzu": "#fef7c3",
    "aoi": "#868397",
    "rio": "#a69fc3",
    "riku": "#6e6061",
    "tsubaki": "#798288",
    "haruna": "#857674",
    "ayaka": "#d3ad99",
    "saki": "#e2e4e4",
    "koboshi": "#8b96a6",
    "akane": "#e2686c",
    "kaede": "#7d7e80",
    "arisu": "#ddf1f6",
    "chinatsu": "#d49486",
    "mia": "#d7d6d6",
    "tsumugi": "#7e5b5f",
    "setsuna": "#ecebeb"
}
```
未在表中定义的角色将使用默认颜色（`DEFAULT_COLOR`）。


## 3. 本地预览

在上传之前，建议在本地预览效果。

```bash
npm start
```
此时浏览器会打开 `http://localhost:3000`。确保图片加载正常，且点击 "copy" / "download" 不会报错。

## 4. 部署到 Cloudflare Pages

本项目是纯静态网站，非常适合部署到 Cloudflare Pages。

### 步骤
1.  **推送到 GitHub**
    - 确保你所有的修改都已经提交并通过 `git push` 推送到 GitHub 仓库。

2.  **登录 Cloudflare Dashboard**
    - 访问 [Cloudflare Dashboard](https://dash.cloudflare.com/) 并登录。
    - 进入 "Workers & Pages" 页面。

3.  **创建应用**
    - 点击 "Create application" -> "Pages" -> "Connect to Git"。

4.  **连接仓库**
    - 选择你的 GitHub 账号，并选择本项目的仓库。
    - 点击 "Begin setup"。

5.  **配置构建设置 (Build settings)**
    - **Project name**: 任意起名。
    - **Production branch**: `main` (或 master)。
    - **Framework preset**: 选择 **Create React App**。
    - **Build command**: `npm run build` (默认)。
    - **Build output directory**: `build` (默认)。

6.  **部署**
    - 点击 "Save and Deploy"。
    - 等待几分钟，Cloudflare 会自动构建并发布你的网站。

### 现在的状态
- **API 移除**: 本项目原本依赖的后端统计 API 已经被移除（改为静态模式），因此你不需要配置任何后端服务。
- **配置**: `src/utils/config.js` 和 `src/utils/log.js` 已经修改为纯前端逻辑。

## 常见问题

**Q: 我修改了 characters.json 手动调整了文字位置，重新运行脚本后配置丢失了怎么办？**
A: 是的，运行脚本会完全覆盖 `characters.json`。如果你有大量自定义的手动配置，建议在运行脚本前备份原文件，或者修改脚本 `scripts/generate_characters.py` 来保留现有的配置（这需要修改代码逻辑）。

**Q: 图片显示不出来？**
A: 检查 `public/img` 下的文件名是否包含特殊字符，或者文件是否损坏。确保运行了 `npm run generate` 更新配置。
