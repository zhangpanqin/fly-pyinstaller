import win32clipboard

def copy_to_clipboard(text):
    # 打开剪贴板
    win32clipboard.OpenClipboard()
    # 清空剪贴板内容，并设置新的内容
    win32clipboard.EmptyClipboard()
    # 设置剪贴板内容为提供的文本，CF_UNICODETEXT表示以Unicode文本格式存储
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)
    # 关闭剪贴板
    win32clipboard.CloseClipboard()

if __name__ == '__main__':
    # 示例文本
    text = "Hello, Windows Clipboard!"
    copy_to_clipboard(text)
    print("文本已复制到剪贴板")