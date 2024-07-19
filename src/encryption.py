
def encrypt_name(name, shift=5):
    """
    对姓名进行模糊化处理。
    :param name: 原始姓名字符串。
    :param shift: 偏移量，控制模糊化程度。
    :return: 模糊化后的姓名字符串。
    """
    encrypted_name = ""
    for char in name.encode('utf-8'):
        # 对每个字符的ASCII值进行偏移
        encrypted_char = (char + shift) % 256
        encrypted_name += chr(encrypted_char)
    return encrypted_name

# 示例
original_name = "张三"
encrypted_name = encrypt_name(original_name)
print(f"模糊化后的姓名: {encrypted_name}")


def decrypt_name(encrypted_name, shift=5):
    """
    将模糊化处理后的姓名还原为原始姓名。
    :param encrypted_name: 模糊化后的姓名字符串。
    :param shift: 与加密时相同的偏移量。
    :return: 原始姓名字符串。
    """
    decrypted_name = ""
    for char in encrypted_name:
        # 反向偏移，还原字符
        decrypted_char = (ord(char) - shift) % 256
        decrypted_name += chr(decrypted_char)
    # 转换回原始编码
    return decrypted_name.encode('latin-1').decode('utf-8', errors='replace')

# 示例
decrypted_name = decrypt_name(encrypted_name)
print(f"还原后的姓名: {decrypted_name}")

# TODO 加密解密前后必须保持一致，否则无法还原。
# 本地保留一份明文，用于测试加密解密后是否一致