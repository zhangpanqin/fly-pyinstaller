import PyInstaller.__main__

if __name__ == '__main__':
    PyInstaller.__main__.run([
        '--clean',
        '--name=dj',
        '--onefile',
        '--uac-admin',
        '--windowed',
        '--add-data=resource:resource',
        'main.py',
    ])
