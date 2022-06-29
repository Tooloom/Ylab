def int32_to_ip(int32):
    a = int32 // (256 * 256 * 256)
    int32 -= a * 256 * 256 * 256
    b = int32 // (256 * 256)
    int32 -= b * 256 * 256
    c = int32 // 256
    d = int32 % 256

    return f'{a}.{b}.{c}.{d}'


print(int32_to_ip(2154959208))
print(int32_to_ip(0))
print(int32_to_ip(2149583361))

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
