# Enter script code
import time

def send_keys_with_timeout(keys, timeout=0.1):
    for key in keys:
        keyboard.send_key(key)
        time.sleep(timeout)

def send_complex_keys_with_timeout(keys, timeout=1):
    keyboard.send_keys(keys)
    time.sleep(timeout)

def send_keys_parse(keymaps):
    for keymap in keymaps:
        keys, format, timeout = keymap
        if format == 2:
            time.sleep(timeout)
        elif format == 1:
            timeout != 0 and send_complex_keys_with_timeout(keys, timeout) or send_complex_keys_with_timeout(keys)
        else:
            timeout != 0 and send_keys_with_timeout(keys, timeout) or send_keys_with_timeout(keys)

keymaps = (
('asciinema rec /tmp/demo.json', 0, 0),
('<ctrl>+m',                     1, 0),
('<ctrl>+ ',                     1, 0),
('img',                          0, 0),
('<ctrl>+u',                     1, 0),
('aptche',                       0, 0),
('<escape>',                     1, 0),
('img',                          0, 0),
('<ctrl>+ ',                     1, 0),
('<ctrl>+m',                     1, 0),
('<ctrl>+v',                     1, 0),
('100',                          0, 0),
('<ctrl>+v',                     1, 0),
('100',                          0, 0),
('<ctrl>+v',                     1, 0),
('/home/hanson/Pictures/',       0, 0),
('<tab>',                        1, 0.1),
('<tab>',                        1, 0.1),
('<tab>',                        1, 0.1),
('<shift>+<tab>',                1, 0.1),
('<tab>',                        1, 0.1),
(' ',                            0, 0),
('<ctrl>+v',                     1, 0),
('/tmp/test.png',                0, 0),
('<ctrl>+m',                     1, 0),
('exit',                         0, 0),
('<ctrl>+m',                     1, 0),
)
send_keys_parse(keymaps)

