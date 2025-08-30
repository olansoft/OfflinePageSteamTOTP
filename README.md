# 本地 Steam 验证码生成器

一个网页形式的、完全离线的 Steam 验证码生成器。
包括 HTML 文件和 Data URI 形式。

## 🚀 使用方法

### 基本使用

1. 打开 `main.html` 文件
2. 在输入框中粘贴您的 Steam Secret（Base32 或 Base64 格式）
3. 点击"复制"按钮将验证码复制到剪贴板

### 参数使用

如果您直接使用 html 文件，

您可以通过 URL 参数直接传入 Secret:

```
file:///path/to/main.html?secret=YOUR_SECRET_HERE
```

或使用锚点方式：

```
file:///path/to/main.html#secret=YOUR_SECRET_HERE
```

如果您使用 Data URI，只能使用锚点方式传入 Secret：

```
data:text/html;base64,<base64内容>#secret=YOUR_SECRET_HERE
```

您可以将预置了 Secret 的 Data URI 保存为浏览器书签，方便随时使用。

## 生成 Data URI

运行 `gen_datauri.py` 脚本可以从 html 文件 生成 Data URI：

```bash
python gen_datauri.py
```

`datauri.txt` 文件中已经包含了生成的 Data URI，您需要在 `#secret=` 后面添加您的 Secret。

## 🎯 支持的密钥格式

自动检测输入的密钥格式

### Base32 格式
Aegis, Stratum, 2FAS 等验证器应用使用的密钥
```
MNOHW7WKXFI7RZWGEQGMVFTRU7GAFIA=
```

### Base64 格式
Steam 的 `shared_secret`
```
cnOgv/KdpLoP6Nbh0GMkXkPXALQ=
```

## 注意事项

当您将 Secret 直接写入 URL 或 Data URI 并保存为书签时，请确保书签的隐私安全。