# These are initialisation sequences for ST7701S displays. The contents are somewhat arcane.


def cmd(c, *args):
    """
    Create a command sequence
    :param c: The command (8 bit)
    :param args: zero or more arguments (8 bit values)
    :return: a list with the command, the argument count and the arguments
    """
    return [c, len(args)] + list(args)


ST7701S_1_INIT = (
    cmd(0x01)
    + cmd(0xFF, 0x77, 0x01, 0x00, 0x00, 0x10)
    + cmd(0xC0, 0x3B, 0x00)
    + cmd(0xC1, 0x0D, 0x02)
    + cmd(0xC2, 0x31, 0x05)
    + cmd(0xCD, 0x08)
    + cmd(
        0xB0,
        0x00,
        0x11,
        0x18,
        0x0E,
        0x11,
        0x06,
        0x07,
        0x08,
        0x07,
        0x22,
        0x04,
        0x12,
        0x0F,
        0xAA,
        0x31,
        0x18,
    )
    + cmd(
        0xB1,
        0x00,
        0x11,
        0x19,
        0x0E,
        0x12,
        0x07,
        0x08,
        0x08,
        0x08,
        0x22,
        0x04,
        0x11,
        0x11,
        0xA9,
        0x32,
        0x18,
    )
    + cmd(0xFF, 0x77, 0x01, 0x00, 0x00, 0x11)
    + cmd(0xB0, 0x60)
    + cmd(0xB1, 0x32)
    + cmd(0xB2, 0x07)
    + cmd(0xB3, 0x80)
    + cmd(0xB5, 0x49)
    + cmd(0xB7, 0x85)
    + cmd(0xB8, 0x21)
    + cmd(0xC1, 0x78)
    + cmd(0xC2, 0x78)
    + cmd(0xE0, 0x00, 0x1B, 0x02)
    + cmd(0xE1, 0x08, 0xA0, 0x00, 0x00, 0x07, 0xA0, 0x00, 0x00, 0x00, 0x44, 0x44)
    + cmd(0xE2, 0x11, 0x11, 0x44, 0x44, 0xED, 0xA0, 0x00, 0x00, 0xEC, 0xA0, 0x00, 0x00)
    + cmd(0xE3, 0x00, 0x00, 0x11, 0x11)
    + cmd(0xE4, 0x44, 0x44)
    + cmd(
        0xE5,
        0x0A,
        0xE9,
        0xD8,
        0xA0,
        0x0C,
        0xEB,
        0xD8,
        0xA0,
        0x0E,
        0xED,
        0xD8,
        0xA0,
        0x10,
        0xEF,
        0xD8,
        0xA0,
    )
    + cmd(0xE6, 0x00, 0x00, 0x11, 0x11)
    + cmd(0xE7, 0x44, 0x44)
    + cmd(
        0xE8,
        0x09,
        0xE8,
        0xD8,
        0xA0,
        0x0B,
        0xEA,
        0xD8,
        0xA0,
        0x0D,
        0xEC,
        0xD8,
        0xA0,
        0x0F,
        0xEE,
        0xD8,
        0xA0,
    )
    + cmd(0xEB, 0x02, 0x00, 0xE4, 0xE4, 0x88, 0x00, 0x40)
    + cmd(0xEC, 0x3C, 0x00)
    + cmd(
        0xED,
        0xAB,
        0x89,
        0x76,
        0x54,
        0x02,
        0xFF,
        0xFF,
        0xFF,
        0xFF,
        0xFF,
        0xFF,
        0x20,
        0x45,
        0x67,
        0x98,
        0xBA,
    )
    + cmd(0xFF, 0x77, 0x01, 0x00, 0x00, 0x13)
    + cmd(0xE5, 0xE4)
    + cmd(0x3A, 0x60)
)

# This is untested
ST7701S_7_INIT = (
    cmd(
        0xFF,
        0x77,
        0x01,
        0x00,
        0x00,
        0x10,
    )
    + cmd(0xC0, 0x3B, 0x00)
    + cmd(0xC1, 0x0B, 0x02)
    + cmd(0xC2, 0x07, 0x02)
    + cmd(0xCC, 0x10)
    + cmd(0xCD, 0x08)
    + cmd(
        0xB0,
        0x00,
        0x11,
        0x16,
        0x0E,
        0x11,
        0x06,
        0x05,
        0x09,
        0x08,
        0x21,
        0x06,
        0x13,
        0x10,
        0x29,
        0x31,
        0x18,
    )
    + cmd(
        0xB1,
        0x00,
        0x11,
        0x16,
        0x0E,
        0x11,
        0x07,
        0x05,
        0x09,
        0x09,
        0x21,
        0x05,
        0x13,
        0x11,
        0x2A,
        0x31,
        0x18,
    )
    + cmd(
        0xFF,
        0x77,
        0x01,
        0x00,
        0x00,
        0x11,
    )
    + cmd(0xB0, 0x6D)
    + cmd(0xB1, 0x37)
    + cmd(0xB2, 0x81)
    + cmd(0xB3, 0x80)
    + cmd(0xB5, 0x43)
    + cmd(0xB7, 0x85)
    + cmd(0xB8, 0x20)
    + cmd(0xC1, 0x78)
    + cmd(0xC2, 0x78)
    + cmd(0xD0, 0x88)
    + cmd(
        0xE0,
        3,
        0x00,
        0x00,
        0x02,
    )
    + cmd(
        0xE1,
        0x03,
        0xA0,
        0x00,
        0x00,
        0x04,
        0xA0,
        0x00,
        0x00,
        0x00,
        0x20,
        0x20,
    )
    + cmd(
        0xE2,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
    )
    + cmd(
        0xE3,
        0x00,
        0x00,
        0x11,
        0x00,
    )
    + cmd(0xE4, 0x22, 0x00)
    + cmd(
        0xE5,
        0x05,
        0xEC,
        0xA0,
        0xA0,
        0x07,
        0xEE,
        0xA0,
        0xA0,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
    )
    + cmd(
        0xE6,
        0x00,
        0x00,
        0x11,
        0x00,
    )
    + cmd(0xE7, 0x22, 0x00)
    + cmd(
        0xE8,
        0x06,
        0xED,
        0xA0,
        0xA0,
        0x08,
        0xEF,
        0xA0,
        0xA0,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
    )
    + cmd(
        0xEB,
        0x00,
        0x00,
        0x40,
        0x40,
        0x00,
        0x00,
        0x00,
    )
    + cmd(
        0xED,
        0xFF,
        0xFF,
        0xFF,
        0xBA,
        0x0A,
        0xBF,
        0x45,
        0xFF,
        0xFF,
        0x54,
        0xFB,
        0xA0,
        0xAB,
        0xFF,
        0xFF,
        0xFF,
    )
    + cmd(
        0xEF,
        0x10,
        0x0D,
        0x04,
        0x08,
        0x3F,
        0x1F,
    )
    + cmd(
        0xFF,
        0x77,
        0x01,
        0x00,
        0x00,
        0x13,
    )
    + cmd(0xEF, 0x08)
    + cmd(
        0xFF,
        0x77,
        0x01,
        0x00,
        0x00,
        0x00,
    )
    + cmd(0x3A, 0x66)
)

NV3052C_INIT = {
    cmd(0xFF, 0x30, 0x52, 0x01)
    + cmd(0xE3, 0x00)
    + cmd(0x0A, 0x11)
    + cmd(0x23, 0xA0)
    + cmd(0x24, 0x32)
    + cmd(0x25, 0x12)
    + cmd(0x26, 0x2E)
    + cmd(0x27, 0x2E)
    + cmd(0x29, 0x02)
    + cmd(0x2A, 0xCF)
    + cmd(0x32, 0x34)
    + cmd(0x38, 0x9C)
    + cmd(0x39, 0xA7)
    + cmd(0x3A, 0x27)
    + cmd(0x3B, 0x94)
    + cmd(0x42, 0x6D)
    + cmd(0x43, 0x83)
    + cmd(0x81, 0x00)
    + cmd(0x91, 0x67)
    + cmd(0x92, 0x67)
    + cmd(0xA0, 0x52)
    + cmd(0xA1, 0x50)
    + cmd(0xA4, 0x9C)
    + cmd(0xA7, 0x02)
    + cmd(0xA8, 0x02)
    + cmd(0xA9, 0x02)
    + cmd(0xAA, 0xA8)
    + cmd(0xAB, 0x28)
    + cmd(0xAE, 0xD2)
    + cmd(0xAF, 0x02)
    + cmd(0xB0, 0xD2)
    + cmd(0xB2, 0x26)
    + cmd(0xB3, 0x26)
    + cmd(0xFF, 0x30, 0x52, 0x02)
    + cmd(0xB1, 0x0A)
    + cmd(0xD1, 0x0E)
    + cmd(0xB4, 0x2F)
    + cmd(0xD4, 0x2D)
    + cmd(0xB2, 0x0C)
    + cmd(0xD2, 0x0C)
    + cmd(0xB3, 0x30)
    + cmd(0xD3, 0x2A)
    + cmd(0xB6, 0x1E)
    + cmd(0xD6, 0x16)
    + cmd(0xB7, 0x3B)
    + cmd(0xD7, 0x35)
    + cmd(0xC1, 0x08)
    + cmd(0xE1, 0x08)
    + cmd(0xB8, 0x0D)
    + cmd(0xD8, 0x0D)
    + cmd(0xB9, 0x05)
    + cmd(0xD9, 0x05)
    + cmd(0xBD, 0x15)
    + cmd(0xDD, 0x15)
    + cmd(0xBC, 0x13)
    + cmd(0xDC, 0x13)
    + cmd(0xBB, 0x12)
    + cmd(0xDB, 0x10)
    + cmd(0xBA, 0x11)
    + cmd(0xDA, 0x11)
    + cmd(0xBE, 0x17)
    + cmd(0xDE, 0x17)
    + cmd(0xBF, 0x0F)
    + cmd(0xDF, 0x0F)
    + cmd(0xC0, 0x16)
    + cmd(0xE0, 0x16)
    + cmd(0xB5, 0x2E)
    + cmd(0xD5, 0x3F)
    + cmd(0xB0, 0x03)
    + cmd(0xD0, 0x02)
    + cmd(0xFF, 0x30, 0x52, 0x03)
    + cmd(0x08, 0x09)
    + cmd(0x09, 0x0A)
    + cmd(0x0A, 0x0B)
    + cmd(0x0B, 0x0C)
    + cmd(0x28, 0x22)
    + cmd(0x2A, 0xE9)
    + cmd(0x2B, 0xE9)
    + cmd(0x34, 0x51)
    + cmd(0x35, 0x01)
    + cmd(0x36, 0x26)
    + cmd(0x37, 0x13)
    + cmd(0x40, 0x07)
    + cmd(0x41, 0x08)
    + cmd(0x42, 0x09)
    + cmd(0x43, 0x0A)
    + cmd(0x44, 0x22)
    + cmd(0x45, 0xDB)
    + cmd(0x46, 0xdC)
    + cmd(0x47, 0x22)
    + cmd(0x48, 0xDD)
    + cmd(0x49, 0xDE)
    + cmd(0x50, 0x0B)
    + cmd(0x51, 0x0C)
    + cmd(0x52, 0x0D)
    + cmd(0x53, 0x0E)
    + cmd(0x54, 0x22)
    + cmd(0x55, 0xDF)
    + cmd(0x56, 0xE0)
    + cmd(0x57, 0x22)
    + cmd(0x58, 0xE1)
    + cmd(0x59, 0xE2)
    + cmd(0x80, 0x1E)
    + cmd(0x81, 0x1E)
    + cmd(0x82, 0x1F)
    + cmd(0x83, 0x1F)
    + cmd(0x84, 0x05)
    + cmd(0x85, 0x0A)
    + cmd(0x86, 0x0A)
    + cmd(0x87, 0x0C)
    + cmd(0x88, 0x0C)
    + cmd(0x89, 0x0E)
    + cmd(0x8A, 0x0E)
    + cmd(0x8B, 0x10)
    + cmd(0x8C, 0x10)
    + cmd(0x8D, 0x00)
    + cmd(0x8E, 0x00)
    + cmd(0x8F, 0x1F)
    + cmd(0x90, 0x1F)
    + cmd(0x91, 0x1E)
    + cmd(0x92, 0x1E)
    + cmd(0x93, 0x02)
    + cmd(0x94, 0x04)
    + cmd(0x96, 0x1E)
    + cmd(0x97, 0x1E)
    + cmd(0x98, 0x1F)
    + cmd(0x99, 0x1F)
    + cmd(0x9A, 0x05)
    + cmd(0x9B, 0x09)
    + cmd(0x9C, 0x09)
    + cmd(0x9D, 0x0B)
    + cmd(0x9E, 0x0B)
    + cmd(0x9F, 0x0D)
    + cmd(0xA0, 0x0D)
    + cmd(0xA1, 0x0F)
    + cmd(0xA2, 0x0F)
    + cmd(0xA3, 0x00)
    + cmd(0xA4, 0x00)
    + cmd(0xA5, 0x1F)
    + cmd(0xA6, 0x1F)
    + cmd(0xA7, 0x1E)
    + cmd(0xA8, 0x1E)
    + cmd(0xA9, 0x01)
    + cmd(0xAA, 0x03)
    + cmd(0xFF, 0x30, 0x52, 0x00)
    + cmd(0x36, 0x0A)
	+ cmd(0x11, 0x00)
    + cmd(0x29, 0x00)
}


ST7701S_INITS = {
    1: ST7701S_1_INIT,
    # 7: ST7701S_7_INIT,
    8: NV3052C_INIT,
}
