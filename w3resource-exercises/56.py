"""
56 - Write a Python program to get height and the width of console window.
""" 

def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))

    return tw, th

if __name__ == '__main__':
    print('Number of columns and Rows: ', terminal_size())