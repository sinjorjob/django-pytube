import random, string


def create_dir(n):
    """一時フォルダ名生成関数"""
    return 'media\\' + ''.join(random.choices(string.ascii_letters + string.digits, k=n))


 