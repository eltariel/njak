class Keyboard:
    usage_page = 0x07

    # UNDEF = 0x0001				# Page 0x07: Keyboard Error Roll Over
    # UNDEF = 0x0002				# Page 0x07: Keyboard POST Fail
    # UNDEF = 0x0003				# Page 0x07: Keyboard Error Undefined
    KEY_A = 0x0004				# Page 0x07: Keyboard a and A
    KEY_B = 0x0005				# Page 0x07: Keyboard b and B
    KEY_C = 0x0006				# Page 0x07: Keyboard c and C
    KEY_D = 0x0007				# Page 0x07: Keyboard d and D
    KEY_E = 0x0008				# Page 0x07: Keyboard e and E
    KEY_F = 0x0009				# Page 0x07: Keyboard f and F
    KEY_G = 0x000a				# Page 0x07: Keyboard g and G
    KEY_H = 0x000b				# Page 0x07: Keyboard h and H
    KEY_I = 0x000c				# Page 0x07: Keyboard i and I
    KEY_J = 0x000d				# Page 0x07: Keyboard j and J
    KEY_K = 0x000e				# Page 0x07: Keyboard k and K
    KEY_L = 0x000f				# Page 0x07: Keyboard l and L
    KEY_M = 0x0010				# Page 0x07: Keyboard m and M
    KEY_N = 0x0011				# Page 0x07: Keyboard n and N
    KEY_O = 0x0012				# Page 0x07: Keyboard o and O
    KEY_P = 0x0013				# Page 0x07: Keyboard p and P
    KEY_Q = 0x0014				# Page 0x07: Keyboard q and Q
    KEY_R = 0x0015				# Page 0x07: Keyboard r and R
    KEY_S = 0x0016				# Page 0x07: Keyboard s and S
    KEY_T = 0x0017				# Page 0x07: Keyboard t and T
    KEY_U = 0x0018				# Page 0x07: Keyboard u and U
    KEY_V = 0x0019				# Page 0x07: Keyboard v and V
    KEY_W = 0x001a				# Page 0x07: Keyboard w and W
    KEY_X = 0x001b				# Page 0x07: Keyboard x and X
    KEY_Y = 0x001c				# Page 0x07: Keyboard y and Y
    KEY_Z = 0x001d				# Page 0x07: Keyboard z and Z
    KEY_1 = 0x001e				# Page 0x07: Keyboard 1 and !
    KEY_2 = 0x001f				# Page 0x07: Keyboard 2 and @
    KEY_3 = 0x0020				# Page 0x07: Keyboard 3 and #
    KEY_4 = 0x0021				# Page 0x07: Keyboard 4 and $
    KEY_5 = 0x0022				# Page 0x07: Keyboard 5 and %
    KEY_6 = 0x0023				# Page 0x07: Keyboard 6 and ^
    KEY_7 = 0x0024				# Page 0x07: Keyboard 7 and &
    KEY_8 = 0x0025				# Page 0x07: Keyboard 8 and *
    KEY_9 = 0x0026				# Page 0x07: Keyboard 9 and (
    KEY_0 = 0x0027				# Page 0x07: Keyboard 0 and )
    KEY_ENTER = 0x0028				# Page 0x07: Keyboard Return (ENTER)
    KEY_ESC = 0x0029				# Page 0x07: Keyboard ESCAPE
    KEY_BACKSPACE = 0x002a			# Page 0x07: Keyboard DELETE (Backspace)
    KEY_TAB = 0x002b				# Page 0x07: Keyboard Tab
    KEY_SPACE = 0x002c				# Page 0x07: Keyboard Spacebar
    KEY_MINUS = 0x002d				# Page 0x07: Keyboard - and _
    KEY_EQUAL = 0x002e				# Page 0x07: Keyboard = and +
    KEY_LEFTBRACE = 0x002f			# Page 0x07: Keyboard [ and {
    KEY_RIGHTBRACE = 0x0030			# Page 0x07: Keyboard ] and }
    KEY_BACKSLASH = 0x0031			# Page 0x07: Keyboard \ and |
    KEY_BACKSLASH = 0x0032			# Page 0x07: Keyboard Non-US # and ~
    KEY_SEMICOLON = 0x0033			# Page 0x07: Keyboard ; and :
    KEY_APOSTROPHE = 0x0034			# Page 0x07: "Keyboard ' and """
    KEY_GRAVE = 0x0035				# Page 0x07: Keyboard ` and ~
    KEY_COMMA = 0x0036				# Page 0x07: "Keyboard , and <"
    KEY_DOT = 0x0037				# Page 0x07: Keyboard . and >
    KEY_SLASH = 0x0038				# Page 0x07: Keyboard / and ?
    KEY_CAPSLOCK = 0x0039			# Page 0x07: Keyboard Caps Lock
    KEY_F1 = 0x003a				# Page 0x07: Keyboard F1
    KEY_F2 = 0x003b				# Page 0x07: Keyboard F2
    KEY_F3 = 0x003c				# Page 0x07: Keyboard F3
    KEY_F4 = 0x003d				# Page 0x07: Keyboard F4
    KEY_F5 = 0x003e				# Page 0x07: Keyboard F5
    KEY_F6 = 0x003f				# Page 0x07: Keyboard F6
    KEY_F7 = 0x0040				# Page 0x07: Keyboard F7
    KEY_F8 = 0x0041				# Page 0x07: Keyboard F8
    KEY_F9 = 0x0042				# Page 0x07: Keyboard F9
    KEY_F10 = 0x0043				# Page 0x07: Keyboard F10
    KEY_F11 = 0x0044				# Page 0x07: Keyboard F11
    KEY_F12 = 0x0045				# Page 0x07: Keyboard F12
    KEY_SYSRQ = 0x0046				# Page 0x07: Keyboard Print Screen
    KEY_SCROLLLOCK = 0x0047			# Page 0x07: Keyboard Scroll Lock
    KEY_PAUSE = 0x0048				# Page 0x07: Keyboard Pause
    KEY_INSERT = 0x0049				# Page 0x07: Keyboard Insert
    KEY_HOME = 0x004a				# Page 0x07: Keyboard Home
    KEY_PAGEUP = 0x004b				# Page 0x07: Keyboard Page Up
    KEY_DELETE = 0x004c				# Page 0x07: Keyboard Delete Forward
    KEY_END = 0x004d				# Page 0x07: Keyboard End
    KEY_PAGEDOWN = 0x004e			# Page 0x07: Keyboard Page Down
    KEY_RIGHT = 0x004f				# Page 0x07: Keyboard Right Arrow
    KEY_LEFT = 0x0050				# Page 0x07: Keyboard Left Arrow
    KEY_DOWN = 0x0051				# Page 0x07: Keyboard Down Arrow
    KEY_UP = 0x0052				# Page 0x07: Keyboard Up Arrow
    KEY_NUMLOCK = 0x0053			# Page 0x07: Keyboard Num Lock and Clear
    KEY_KPSLASH = 0x0054			# Page 0x07: Keypad /
    KEY_KPASTERISK = 0x0055			# Page 0x07: Keypad *
    KEY_KPMINUS = 0x0056			# Page 0x07: Keypad -
    KEY_KPPLUS = 0x0057				# Page 0x07: Keypad +
    KEY_KPENTER = 0x0058			# Page 0x07: Keypad ENTER
    KEY_KP1 = 0x0059				# Page 0x07: Keypad 1 and End
    KEY_KP2 = 0x005a				# Page 0x07: Keypad 2 and Down Arrow
    KEY_KP3 = 0x005b				# Page 0x07: Keypad 3 and PageDn
    KEY_KP4 = 0x005c				# Page 0x07: Keypad 4 and Left Arrow
    KEY_KP5 = 0x005d				# Page 0x07: Keypad 5
    KEY_KP6 = 0x005e				# Page 0x07: Keypad 6 and Right Arrow
    KEY_KP7 = 0x005f				# Page 0x07: Keypad 7 and Home
    KEY_KP8 = 0x0060				# Page 0x07: Keypad 8 and Up Arrow
    KEY_KP9 = 0x0061				# Page 0x07: Keypad 9 and Page Up
    KEY_KP0 = 0x0062				# Page 0x07: Keypad 0 and Insert
    KEY_KPDOT = 0x0063				# Page 0x07: Keypad . and Delete
    KEY_102ND = 0x0064				# Page 0x07: Keyboard Non-US \ and |
    KEY_COMPOSE = 0x0065			# Page 0x07: Keyboard Application
    KEY_POWER = 0x0066				# Page 0x07: Keyboard Power
    KEY_KPEQUAL = 0x0067			# Page 0x07: Keypad =
    KEY_F13 = 0x0068				# Page 0x07: Keyboard F13
    KEY_F14 = 0x0069				# Page 0x07: Keyboard F14
    KEY_F15 = 0x006a				# Page 0x07: Keyboard F15
    KEY_F16 = 0x006b				# Page 0x07: Keyboard F16
    KEY_F17 = 0x006c				# Page 0x07: Keyboard F17
    KEY_F18 = 0x006d				# Page 0x07: Keyboard F18
    KEY_F19 = 0x006e				# Page 0x07: Keyboard F19
    KEY_F20 = 0x006f				# Page 0x07: Keyboard F20
    KEY_F21 = 0x0070				# Page 0x07: Keyboard F21
    KEY_F22 = 0x0071				# Page 0x07: Keyboard F22
    KEY_F23 = 0x0072				# Page 0x07: Keyboard F23
    KEY_F24 = 0x0073				# Page 0x07: Keyboard F24
    KEY_OPEN = 0x0074				# Page 0x07: Keyboard Execute
    KEY_HELP = 0x0075				# Page 0x07: Keyboard Help
    KEY_PROPS = 0x0076				# Page 0x07: Keyboard Menu
    KEY_FRONT = 0x0077				# Page 0x07: Keyboard Select
    KEY_STOP = 0x0078				# Page 0x07: Keyboard Stop
    KEY_AGAIN = 0x0079				# Page 0x07: Keyboard Again
    KEY_UNDO = 0x007a				# Page 0x07: Keyboard Undo
    KEY_CUT = 0x007b				# Page 0x07: Keyboard Cut
    KEY_COPY = 0x007c				# Page 0x07: Keyboard Copy
    KEY_PASTE = 0x007d				# Page 0x07: Keyboard Paste
    KEY_FIND = 0x007e				# Page 0x07: Keyboard Find
    KEY_MUTE = 0x007f				# Page 0x07: Keyboard Mute
    KEY_VOLUMEUP = 0x0080			# Page 0x07: Keyboard Volume Up
    KEY_VOLUMEDOWN = 0x0081			# Page 0x07: Keyboard Volume Down
    # UNDEF = 0x0082				# Page 0x07: Keyboard Locking Caps Lock
    # UNDEF = 0x0083				# Page 0x07: Keyboard Locking Num Lock
    # UNDEF = 0x0084				# Page 0x07: Keyboard Locking Scroll Lock
    KEY_KPCOMMA = 0x0085			# Page 0x07: Keypad Comma
    # UNDEF = 0x0086				# Page 0x07: Keypad Equal Sign
    KEY_RO = 0x0087				# Page 0x07: Keyboard International1
    KEY_KATAKANAHIRAGANA = 0x0088		# Page 0x07: Keyboard International2
    KEY_YEN = 0x0089				# Page 0x07: Keyboard International3
    KEY_HENKAN = 0x008a				# Page 0x07: Keyboard International4
    KEY_MUHENKAN = 0x008b			# Page 0x07: Keyboard International5
    KEY_KPJPCOMMA = 0x008c			# Page 0x07: Keyboard International6
    # UNDEF = 0x008d				# Page 0x07: Keyboard International7
    # UNDEF = 0x008e				# Page 0x07: Keyboard International8
    # UNDEF = 0x008f				# Page 0x07: Keyboard International9
    KEY_HANGEUL = 0x0090			# Page 0x07: Keyboard LANG1
    KEY_HANJA = 0x0091				# Page 0x07: Keyboard LANG2
    KEY_KATAKANA = 0x0092			# Page 0x07: Keyboard LANG3
    KEY_HIRAGANA = 0x0093			# Page 0x07: Keyboard LANG4
    KEY_ZENKAKUHANKAKU = 0x0094			# Page 0x07: Keyboard LANG5
    # UNDEF = 0x0095				# Page 0x07: Keyboard LANG6
    # UNDEF = 0x0096				# Page 0x07: Keyboard LANG7
    # UNDEF = 0x0097				# Page 0x07: Keyboard LANG8
    # UNDEF = 0x0098				# Page 0x07: Keyboard LANG9
    # UNDEF = 0x0099				# Page 0x07: Keyboard Alternate Erase
    # UNDEF = 0x009a				# Page 0x07: Keyboard SysReq/Attention
    # UNDEF = 0x009b				# Page 0x07: Keyboard Cancel
    # UNDEF = 0x009c				# Page 0x07: Keyboard Clear
    # UNDEF = 0x009d				# Page 0x07: Keyboard Prior
    # UNDEF = 0x009e				# Page 0x07: Keyboard Return
    # UNDEF = 0x009f				# Page 0x07: Keyboard Separator
    # UNDEF = 0x00a0				# Page 0x07: Keyboard Out
    # UNDEF = 0x00a1				# Page 0x07: Keyboard Oper
    # UNDEF = 0x00a2				# Page 0x07: Keyboard Clear/Again
    # UNDEF = 0x00a3				# Page 0x07: Keyboard CrSel/Props
    # UNDEF = 0x00a4				# Page 0x07: Keyboard ExSel
    # UNDEF = 0x00b0				# Page 0x07: Keypad 00
    # UNDEF = 0x00b1				# Page 0x07: Keypad 000
    # UNDEF = 0x00b2				# Page 0x07: Thousands Separator
    # UNDEF = 0x00b3				# Page 0x07: Decimal Separator
    # UNDEF = 0x00b4				# Page 0x07: Currency Unit
    # UNDEF = 0x00b5				# Page 0x07: Currency Sub-unit
    KEY_KPLEFTPAREN = 0x00b6			# Page 0x07: Keypad (
    KEY_KPRIGHTPAREN = 0x00b7			# Page 0x07: Keypad )
    # UNDEF = 0x00b8				# Page 0x07: Keypad {
    # UNDEF = 0x00b9				# Page 0x07: Keypad }
    # UNDEF = 0x00ba				# Page 0x07: Keypad Tab
    # UNDEF = 0x00bb				# Page 0x07: Keypad Backspace
    # UNDEF = 0x00bc				# Page 0x07: Keypad A
    # UNDEF = 0x00bd				# Page 0x07: Keypad B
    # UNDEF = 0x00be				# Page 0x07: Keypad C
    # UNDEF = 0x00bf				# Page 0x07: Keypad D
    # UNDEF = 0x00c0				# Page 0x07: Keypad E
    # UNDEF = 0x00c1				# Page 0x07: Keypad F
    # UNDEF = 0x00c2				# Page 0x07: Keypad XOR
    # UNDEF = 0x00c3				# Page 0x07: Keypad ^
    # UNDEF = 0x00c4				# Page 0x07: Keypad %
    # UNDEF = 0x00c5				# Page 0x07: Keypad <
    # UNDEF = 0x00c6				# Page 0x07: Keypad >
    # UNDEF = 0x00c7				# Page 0x07: Keypad &
    # UNDEF = 0x00c8				# Page 0x07: Keypad &&
    # UNDEF = 0x00c9				# Page 0x07: Keypad |
    # UNDEF = 0x00ca				# Page 0x07: Keypad ||
    # UNDEF = 0x00cb				# Page 0x07: Keypad :
    # UNDEF = 0x00cc				# Page 0x07: Keypad #
    # UNDEF = 0x00cd				# Page 0x07: Keypad Space
    # UNDEF = 0x00ce				# Page 0x07: Keypad @
    # UNDEF = 0x00cf				# Page 0x07: Keypad !
    # UNDEF = 0x00d0				# Page 0x07: Keypad Memory Store
    # UNDEF = 0x00d1				# Page 0x07: Keypad Memory Recall
    # UNDEF = 0x00d2				# Page 0x07: Keypad Memory Clear
    # UNDEF = 0x00d3				# Page 0x07: Keypad Memory Add
    # UNDEF = 0x00d4				# Page 0x07: Keypad Memory Subtract
    # UNDEF = 0x00d5				# Page 0x07: Keypad Memory Multiply
    # UNDEF = 0x00d6				# Page 0x07: Keypad Memory Divide
    # UNDEF = 0x00d7				# Page 0x07: Keypad +/-
    # UNDEF = 0x00d8				# Page 0x07: Keypad Clear
    # UNDEF = 0x00d9				# Page 0x07: Keypad Clear Entry
    # UNDEF = 0x00da				# Page 0x07: Keypad Binary
    # UNDEF = 0x00db				# Page 0x07: Keypad Octal
    # UNDEF = 0x00dc				# Page 0x07: Keypad Decimal
    # UNDEF = 0x00dd				# Page 0x07: Keypad Hexadecimal
    KEY_LEFTCTRL = 0x00e0			# Page 0x07: Keyboard Left Control
    KEY_LEFTSHIFT = 0x00e1			# Page 0x07: Keyboard Left Shift
    KEY_LEFTALT = 0x00e2			# Page 0x07: Keyboard Left Alt
    KEY_LEFTMETA = 0x00e3			# Page 0x07: Keyboard Left GUI
    KEY_RIGHTCTRL = 0x00e4			# Page 0x07: Keyboard Right Control
    KEY_RIGHTSHIFT = 0x00e5			# Page 0x07: Keyboard Right Shift
    KEY_RIGHTALT = 0x00e6			# Page 0x07: Keyboard Right Alt
    KEY_RIGHTMETA = 0x00e7			# Page 0x07: Keyboard Right GUI
    KEY_PLAYPAUSE = 0x00e8			# Page 0x07:
    KEY_STOPCD = 0x00e9				# Page 0x07:
    KEY_PREVIOUSSONG = 0x00ea			# Page 0x07:
    KEY_NEXTSONG = 0x00eb			# Page 0x07:
    KEY_EJECTCD = 0x00ec			# Page 0x07:
    KEY_VOLUMEUP = 0x00ed			# Page 0x07:
    KEY_VOLUMEDOWN = 0x00ee			# Page 0x07:
    KEY_MUTE = 0x00ef				# Page 0x07:
    KEY_WWW = 0x00f0				# Page 0x07:
    KEY_BACK = 0x00f1				# Page 0x07:
    KEY_FORWARD = 0x00f2			# Page 0x07:
    KEY_STOP = 0x00f3				# Page 0x07:
    KEY_FIND = 0x00f4				# Page 0x07:
    KEY_SCROLLUP = 0x00f5			# Page 0x07:
    KEY_SCROLLDOWN = 0x00f6			# Page 0x07:
    KEY_EDIT = 0x00f7				# Page 0x07:
    KEY_SLEEP = 0x00f8				# Page 0x07:
    KEY_COFFEE = 0x00f9				# Page 0x07:
    KEY_REFRESH = 0x00fa			# Page 0x07:
    KEY_CALC = 0x00fb				# Page 0x07:


class GenericDesktop:
    usage_page = 0x01

    KEY_POWER = 0x0081				# Page 0x01: System Power Down
    KEY_SLEEP = 0x0082				# Page 0x01: System Sleep
    KEY_WAKEUP = 0x0083				# Page 0x01: System Wake Up
    # UNDEF = 0x0084				# Page 0x01: System Context Menu
    # UNDEF = 0x0085				# Page 0x01: System Main Menu
    # UNDEF = 0x0086				# Page 0x01: System App Menu
    # UNDEF = 0x0087				# Page 0x01: System Menu Help
    # UNDEF = 0x0088				# Page 0x01: System Menu Exit
    # UNDEF = 0x0089				# Page 0x01: System Menu Select
    # UNDEF = 0x008a				# Page 0x01: System Menu Right
    # UNDEF = 0x008b				# Page 0x01: System Menu Left
    # UNDEF = 0x008c				# Page 0x01: System Menu Up
    # UNDEF = 0x008d				# Page 0x01: System Menu Down
    # UNDEF = 0x008e				# Page 0x01: System Cold Restart
    # UNDEF = 0x008f				# Page 0x01: System Warm Restart
    # UNDEF = 0x00a0				# Page 0x01: System Dock
    # UNDEF = 0x00a1				# Page 0x01: System Undock
    # UNDEF = 0x00a2				# Page 0x01: System Setup
    # UNDEF = 0x00a3				# Page 0x01: System Break
    # UNDEF = 0x00a4				# Page 0x01: System Debugger Break
    # UNDEF = 0x00a5				# Page 0x01: Application Break
    # UNDEF = 0x00a6				# Page 0x01: Application Debugger Break
    # UNDEF = 0x00a7				# Page 0x01: System Speaker Mute
    # UNDEF = 0x00a8				# Page 0x01: System Hibernate
    # UNDEF = 0x00b0				# Page 0x01: System Display Invert
    # UNDEF = 0x00b1				# Page 0x01: System Display Internal
    # UNDEF = 0x00b2				# Page 0x01: System Display External
    # UNDEF = 0x00b3				# Page 0x01: System Display Both
    # UNDEF = 0x00b4				# Page 0x01: System Display Dual
    # UNDEF = 0x00b5				# Page 0x01: System Display Toggle Int/Ext
    # UNDEF = 0x00b6				# Page 0x01: System Display Swap Prim./Sec.
    # UNDEF = 0x00b7				# Page 0x01: System Display LCD Autoscale


class Consumer:
    usage_page = 0x0C

    # UNDEF = 0x0030				# Page 0x0c: Power
    # UNDEF = 0x0031				# Page 0x0c: Reset
    # UNDEF = 0x0032				# Page 0x0c: Sleep
    # UNDEF = 0x0033				# Page 0x0c: Sleep After
    KEY_SLEEP = 0x0034				# Page 0x0c: Sleep Mode
    KEY_MENU = 0x0040				# Page 0x0c: Menu
    # UNDEF = 0x0041				# Page 0x0c: Menu Pick
    # UNDEF = 0x0042				# Page 0x0c: Menu Up
    # UNDEF = 0x0043				# Page 0x0c: Menu Down
    # UNDEF = 0x0044				# Page 0x0c: Menu Left
    KEY_RIGHT = 0x0045				# Page 0x0c: Menu Right
    # UNDEF = 0x0046				# Page 0x0c: Menu Escape
    # UNDEF = 0x0047				# Page 0x0c: Menu Value Increase
    # UNDEF = 0x0048				# Page 0x0c: Menu Value Decrease
    # UNDEF = 0x0081				# Page 0x0c: Assign Selection
    # UNDEF = 0x0082				# Page 0x0c: Mode Step
    KEY_LAST = 0x0083				# Page 0x0c: Recall Last
    # UNDEF = 0x0084				# Page 0x0c: Enter Channel
    # UNDEF = 0x0085				# Page 0x0c: Order Movie
    KEY_PC = 0x0088				# Page 0x0c: Media Select Computer
    KEY_TV = 0x0089				# Page 0x0c: Media Select TV
    # KEY_WWW = 0x008a				# Page 0x0c: Media Select WWW
    KEY_DVD = 0x008b				# Page 0x0c: Media Select DVD
    KEY_PHONE = 0x008c				# Page 0x0c: Media Select Telephone
    KEY_PROGRAM = 0x008d			# Page 0x0c: Media Select Program Guide
    KEY_VIDEOPHONE = 0x008e			# Page 0x0c: Media Select Video Phone
    KEY_GAMES = 0x008f				# Page 0x0c: Media Select Games
    KEY_MEMO = 0x0090				# Page 0x0c: Media Select Messages
    KEY_CD = 0x0091				# Page 0x0c: Media Select CD
    KEY_VCR = 0x0092				# Page 0x0c: Media Select VCR
    KEY_TUNER = 0x0093				# Page 0x0c: Media Select Tuner
    KEY_QUIT = 0x0094				# Page 0x0c: Quit
    KEY_HELP = 0x0095				# Page 0x0c: Help
    KEY_TAPE = 0x0096				# Page 0x0c: Media Select Tape
    KEY_TV2 = 0x0097				# Page 0x0c: Media Select Cable
    KEY_SAT = 0x0098				# Page 0x0c: Media Select Satellite
    # UNDEF = 0x0099				# Page 0x0c: Media Select Security
    KEY_PVR = 0x009a				# Page 0x0c: Media Select Home
    KEY_CHANNELUP = 0x009c			# Page 0x0c: Channel Increment
    KEY_CHANNELDOWN = 0x009d			# Page 0x0c: Channel Decrement
    # UNDEF = 0x009e				# Page 0x0c: Media Select SAP
    KEY_VCR2 = 0x00a0				# Page 0x0c: VCR Plus
    # UNDEF = 0x00a1				# Page 0x0c: Once
    # UNDEF = 0x00a2				# Page 0x0c: Daily
    # UNDEF = 0x00a3				# Page 0x0c: Weekly
    # UNDEF = 0x00a4				# Page 0x0c: Monthly
    KEY_PLAY = 0x00b0				# Page 0x0c: Play
    KEY_PAUSE = 0x00b1				# Page 0x0c: Pause
    KEY_RECORD = 0x00b2				# Page 0x0c: Record
    KEY_FASTFORWARD = 0x00b3			# Page 0x0c: Fast Forward
    KEY_REWIND = 0x00b4				# Page 0x0c: Rewind
    KEY_NEXTSONG = 0x00b5			# Page 0x0c: Scan Next Track
    KEY_PREVIOUSSONG = 0x00b6			# Page 0x0c: Scan Previous Track
    KEY_STOPCD = 0x00b7				# Page 0x0c: Stop
    KEY_EJECTCD = 0x00b8			# Page 0x0c: Eject
    # UNDEF = 0x00b9				# Page 0x0c: Random Play
    # UNDEF = 0x00ba				# Page 0x0c: Select Disc
    # UNDEF = 0x00bb				# Page 0x0c: Enter Disc
    KEY_MEDIA_REPEAT = 0x00bc			# Page 0x0c: Repeat
    # UNDEF = 0x00be				# Page 0x0c: Track Normal
    # UNDEF = 0x00c0				# Page 0x0c: Frame Forward
    # UNDEF = 0x00c1				# Page 0x0c: Frame Back
    # UNDEF = 0x00c2				# Page 0x0c: Mark
    # UNDEF = 0x00c3				# Page 0x0c: Clear Mark
    # UNDEF = 0x00c4				# Page 0x0c: Repeat From Mark
    # UNDEF = 0x00c5				# Page 0x0c: Return To Mark
    # UNDEF = 0x00c6				# Page 0x0c: Search Mark Forward
    # UNDEF = 0x00c7				# Page 0x0c: Search Mark Backwards
    # UNDEF = 0x00c8				# Page 0x0c: Counter Reset
    # UNDEF = 0x00c9				# Page 0x0c: Show Counter
    # UNDEF = 0x00ca				# Page 0x0c: Tracking Increment
    # UNDEF = 0x00cb				# Page 0x0c: Tracking Decrement
    # UNDEF = 0x00cc				# Page 0x0c: Stop / Eject
    KEY_PLAYPAUSE = 0x00cd			# Page 0x0c: Play / Pause
    # UNDEF = 0x00ce				# Page 0x0c: Play / Skip
    KEY_MUTE = 0x00e2				# Page 0x0c: Mute
    KEY_BASSBOOST = 0x00e5			# Page 0x0c: Bass Boost
    # UNDEF = 0x00e6				# Page 0x0c: Surround Mode
    # UNDEF = 0x00e7				# Page 0x0c: Loudness
    # UNDEF = 0x00e8				# Page 0x0c: MPX
    KEY_VOLUMEUP = 0x00e9			# Page 0x0c: Volume Increment
    KEY_VOLUMEDOWN = 0x00ea			# Page 0x0c: Volume Decrement
    # UNDEF = 0x0181				# Page 0x0c: AL Launch Button Config. Tool
    # KEY_BOOKMARKS = 0x0182			# Page 0x0c: AL Programmable Button Config.
    KEY_CONFIG = 0x0183				# Page 0x0c: AL Consumer Control Config.
    KEY_WORDPROCESSOR = 0x0184			# Page 0x0c: AL Word Processor
    KEY_EDITOR = 0x0185				# Page 0x0c: AL Text Editor
    KEY_SPREADSHEET = 0x0186			# Page 0x0c: AL Spreadsheet
    KEY_GRAPHICSEDITOR = 0x0187			# Page 0x0c: AL Graphics Editor
    KEY_PRESENTATION = 0x0188			# Page 0x0c: AL Presentation App
    KEY_DATABASE = 0x0189			# Page 0x0c: AL Database App
    KEY_MAIL = 0x018a				# Page 0x0c: AL Email Reader
    KEY_NEWS = 0x018b				# Page 0x0c: AL Newsreader
    KEY_VOICEMAIL = 0x018c			# Page 0x0c: AL Voicemail
    KEY_ADDRESSBOOK = 0x018d			# Page 0x0c: AL Contacts / Address Book
    KEY_CALENDAR = 0x018e			# Page 0x0c: AL Calendar / Schedule
    # UNDEF = 0x018f				# Page 0x0c: AL Task / Project Manager
    # UNDEF = 0x0190				# Page 0x0c: AL Log / Journal / Timecard
    KEY_FINANCE = 0x0191			# Page 0x0c: AL Checkbook / Finance
    KEY_CALC = 0x0192				# Page 0x0c: AL Calculator
    # UNDEF = 0x0193				# Page 0x0c: AL A/V Capture / Playback
    KEY_FILE = 0x0194				# Page 0x0c: AL Local Machine Browser
    # UNDEF = 0x0195				# Page 0x0c: AL LAN/WAN Browser
    KEY_WWW = 0x0196				# Page 0x0c: AL Internet Browser
    # UNDEF = 0x0197				# Page 0x0c: AL Remote Networking/ISP Connect
    # UNDEF = 0x0198				# Page 0x0c: AL Network Conference
    KEY_CHAT = 0x0199				# Page 0x0c: AL Network Chat
    # UNDEF = 0x019a				# Page 0x0c: AL Telephony / Dialer
    # UNDEF = 0x019b				# Page 0x0c: AL Logon
    KEY_LOGOFF = 0x019c				# Page 0x0c: AL Logoff
    # UNDEF = 0x019d				# Page 0x0c: AL Logon / Logoff
    KEY_COFFEE = 0x019e				# Page 0x0c: AL Terminal Lock / Screensaver
    # UNDEF = 0x019f				# Page 0x0c: AL Control Panel
    # UNDEF = 0x01a0				# Page 0x0c: AL Command Line Processor / Run
    # UNDEF = 0x01a1				# Page 0x0c: AL Process / Task Manager
    # UNDEF = 0x01a2				# Page 0x0c: AL Select Task / Application
    # UNDEF = 0x01a3				# Page 0x0c: AL Next Task / Application
    # UNDEF = 0x01a4				# Page 0x0c: AL Previous Task / Application
    # UNDEF = 0x01a5				# Page 0x0c: AL Preemptive Halt Task / App.
    KEY_HELP = 0x01a6				# Page 0x0c: AL Integrated Help Center
    KEY_DOCUMENTS = 0x01a7			# Page 0x0c: AL Documents
    # UNDEF = 0x01a8				# Page 0x0c: AL Thesaurus
    # UNDEF = 0x01a9				# Page 0x0c: AL Dictionary
    # UNDEF = 0x01aa				# Page 0x0c: AL Desktop
    KEY_SPELLCHECK = 0x01ab			# Page 0x0c: AL Spell Check
    # UNDEF = 0x01ac				# Page 0x0c: AL Grammar Check
    # UNDEF = 0x01ad				# Page 0x0c: AL Wireless Status
    # UNDEF = 0x01ae				# Page 0x0c: AL Keyboard Layout
    # UNDEF = 0x01af				# Page 0x0c: AL Virus Protection
    # UNDEF = 0x01b0				# Page 0x0c: AL Encryption
    # UNDEF = 0x01b1				# Page 0x0c: AL Screen Saver
    # UNDEF = 0x01b2				# Page 0x0c: AL Alarms
    # UNDEF = 0x01b3				# Page 0x0c: AL Clock
    # UNDEF = 0x01b4				# Page 0x0c: AL File Browser
    # UNDEF = 0x01b5				# Page 0x0c: AL Power Status
    KEY_MEDIA = 0x01b6				# Page 0x0c: AL Image Browser
    KEY_SOUND = 0x01b7				# Page 0x0c: AL Audio Browser
    # UNDEF = 0x01b8				# Page 0x0c: AL Movie Browser
    # UNDEF = 0x01b9				# Page 0x0c: AL Digital Rights Manager
    # UNDEF = 0x01ba				# Page 0x0c: AL Digital Wallet
    KEY_MESSENGER = 0x01bc			# Page 0x0c: AL Instant Messaging
    KEY_INFO = 0x01bd				# Page 0x0c: AL OEM Features / Tips Browser
    # UNDEF = 0x01be				# Page 0x0c: AL OEM Help
    # UNDEF = 0x01bf				# Page 0x0c: AL Online Community
    # UNDEF = 0x01c0				# Page 0x0c: AL Entertainment Content Browser
    # UNDEF = 0x01c1				# Page 0x0c: AL Online Shopping Browser
    # UNDEF = 0x01c2				# Page 0x0c: AL SmartCard Information / Help
    # UNDEF = 0x01c3				# Page 0x0c: AL Market / Finance Browser
    # UNDEF = 0x01c4				# Page 0x0c: AL Customized Corp. News Browser
    # UNDEF = 0x01c5				# Page 0x0c: AL Online Activity Browser
    # UNDEF = 0x01c6				# Page 0x0c: AL Research / Search Browser
    # UNDEF = 0x01c7				# Page 0x0c: AL Audio Player
    KEY_NEW = 0x0201				# Page 0x0c: AC New
    KEY_OPEN = 0x0202				# Page 0x0c: AC Open
    KEY_CLOSE = 0x0203				# Page 0x0c: AC Close
    KEY_EXIT = 0x0204				# Page 0x0c: AC Exit
    # UNDEF = 0x0205				# Page 0x0c: AC Maximize
    # UNDEF = 0x0206				# Page 0x0c: AC Minimize
    KEY_SAVE = 0x0207				# Page 0x0c: AC Save
    KEY_PRINT = 0x0208				# Page 0x0c: AC Print
    KEY_PROPS = 0x0209				# Page 0x0c: AC Properties
    KEY_UNDO = 0x021a				# Page 0x0c: AC Undo
    KEY_COPY = 0x021b				# Page 0x0c: AC Copy
    KEY_CUT = 0x021c				# Page 0x0c: AC Cut
    KEY_PASTE = 0x021d				# Page 0x0c: AC Paste
    # UNDEF = 0x021e				# Page 0x0c: AC Select All
    KEY_FIND = 0x021f				# Page 0x0c: AC Find
    # UNDEF = 0x0220				# Page 0x0c: AC Find and Replace
    KEY_SEARCH = 0x0221				# Page 0x0c: AC Search
    KEY_GOTO = 0x0222				# Page 0x0c: AC Go To
    KEY_HOMEPAGE = 0x0223			# Page 0x0c: AC Home
    KEY_BACK = 0x0224				# Page 0x0c: AC Back
    KEY_FORWARD = 0x0225			# Page 0x0c: AC Forward
    KEY_STOP = 0x0226				# Page 0x0c: AC Stop
    KEY_REFRESH = 0x0227			# Page 0x0c: AC Refresh
    # UNDEF = 0x0228				# Page 0x0c: AC Previous Link
    # UNDEF = 0x0229				# Page 0x0c: AC Next Link
    KEY_BOOKMARKS = 0x022a			# Page 0x0c: AC Bookmarks
    # UNDEF = 0x022b				# Page 0x0c: AC History
    # UNDEF = 0x022c				# Page 0x0c: AC Subscriptions
    KEY_ZOOMIN = 0x022d				# Page 0x0c: AC Zoom In
    KEY_ZOOMOUT = 0x022e			# Page 0x0c: AC Zoom Out
    KEY_ZOOMRESET = 0x022f			# Page 0x0c: AC Zoom
    # UNDEF = 0x0230				# Page 0x0c: AC Full Screen View
    # UNDEF = 0x0231				# Page 0x0c: AC Normal View
    # UNDEF = 0x0232				# Page 0x0c: AC View Toggle
    KEY_SCROLLUP = 0x0233			# Page 0x0c: AC Scroll Up
    KEY_SCROLLDOWN = 0x0234			# Page 0x0c: AC Scroll Down
    # UNDEF = 0x0236				# Page 0x0c: AC Pan Left
    # UNDEF = 0x0237				# Page 0x0c: AC Pan Right
    # UNDEF = 0x0239				# Page 0x0c: AC New Window
    # UNDEF = 0x023a				# Page 0x0c: AC Tile Horizontally
    # UNDEF = 0x023b				# Page 0x0c: AC Tile Vertically
    # UNDEF = 0x023c				# Page 0x0c: AC Format
    # UNDEF = 0x023d				# Page 0x0c: AC Edit
    # UNDEF = 0x023e				# Page 0x0c: AC Bold
    # UNDEF = 0x023f				# Page 0x0c: AC Italics
    # UNDEF = 0x0240				# Page 0x0c: AC Underline
    # UNDEF = 0x0241				# Page 0x0c: AC Strikethrough
    # UNDEF = 0x0242				# Page 0x0c: AC Subscript
    # UNDEF = 0x0243				# Page 0x0c: AC Superscript
    # UNDEF = 0x0244				# Page 0x0c: AC All Caps
    # UNDEF = 0x0245				# Page 0x0c: AC Rotate
    # UNDEF = 0x0246				# Page 0x0c: AC Resize
    # UNDEF = 0x0247				# Page 0x0c: AC Flip horizontal
    # UNDEF = 0x0248				# Page 0x0c: AC Flip Vertical
    # UNDEF = 0x0249				# Page 0x0c: AC Mirror Horizontal
    # UNDEF = 0x024a				# Page 0x0c: AC Mirror Vertical
    # UNDEF = 0x024b				# Page 0x0c: AC Font Select
    # UNDEF = 0x024c				# Page 0x0c: AC Font Color
    # UNDEF = 0x024d				# Page 0x0c: AC Font Size
    # UNDEF = 0x024e				# Page 0x0c: AC Justify Left
    # UNDEF = 0x024f				# Page 0x0c: AC Justify Center H
    # UNDEF = 0x0250				# Page 0x0c: AC Justify Right
    # UNDEF = 0x0251				# Page 0x0c: AC Justify Block H
    # UNDEF = 0x0252				# Page 0x0c: AC Justify Top
    # UNDEF = 0x0253				# Page 0x0c: AC Justify Center V
    # UNDEF = 0x0254				# Page 0x0c: AC Justify Bottom
    # UNDEF = 0x0255				# Page 0x0c: AC Justify Block V
    # UNDEF = 0x0256				# Page 0x0c: AC Indent Decrease
    # UNDEF = 0x0257				# Page 0x0c: AC Indent Increase
    # UNDEF = 0x0258				# Page 0x0c: AC Numbered List
    # UNDEF = 0x0259				# Page 0x0c: AC Restart Numbering
    # UNDEF = 0x025a				# Page 0x0c: AC Bulleted List
    # UNDEF = 0x025b				# Page 0x0c: AC Promote
    # UNDEF = 0x025c				# Page 0x0c: AC Demote
    # UNDEF = 0x025d				# Page 0x0c: AC Yes
    # UNDEF = 0x025e				# Page 0x0c: AC No
    KEY_CANCEL = 0x025f				# Page 0x0c: AC Cancel
    # UNDEF = 0x0260				# Page 0x0c: AC Catalog
    # UNDEF = 0x0261				# Page 0x0c: AC Buy / Checkout
    # UNDEF = 0x0262				# Page 0x0c: AC Add to Cart
    # UNDEF = 0x0263				# Page 0x0c: AC Expand
    # UNDEF = 0x0264				# Page 0x0c: AC Expand All
    # UNDEF = 0x0265				# Page 0x0c: AC Collapse
    # UNDEF = 0x0266				# Page 0x0c: AC Collapse All
    # UNDEF = 0x0267				# Page 0x0c: AC Print Preview
    # UNDEF = 0x0268				# Page 0x0c: AC Paste Special
    # UNDEF = 0x0269				# Page 0x0c: AC Insert Mode
    # UNDEF = 0x026a				# Page 0x0c: AC Delete
    # UNDEF = 0x026b				# Page 0x0c: AC Lock
    # UNDEF = 0x026c				# Page 0x0c: AC Unlock
    # UNDEF = 0x026d				# Page 0x0c: AC Protect
    # UNDEF = 0x026e				# Page 0x0c: AC Unprotect
    # UNDEF = 0x026f				# Page 0x0c: AC Attach Comment
    # UNDEF = 0x0270				# Page 0x0c: AC Delete Comment
    # UNDEF = 0x0271				# Page 0x0c: AC View Comment
    # UNDEF = 0x0272				# Page 0x0c: AC Select Word
    # UNDEF = 0x0273				# Page 0x0c: AC Select Sentence
    # UNDEF = 0x0274				# Page 0x0c: AC Select Paragraph
    # UNDEF = 0x0275				# Page 0x0c: AC Select Column
    # UNDEF = 0x0276				# Page 0x0c: AC Select Row
    # UNDEF = 0x0277				# Page 0x0c: AC Select Table
    # UNDEF = 0x0278				# Page 0x0c: AC Select Object
    KEY_REDO = 0x0279				# Page 0x0c: AC Redo / Repeat
    # UNDEF = 0x027a				# Page 0x0c: AC Sort
    # UNDEF = 0x027b				# Page 0x0c: AC Sort Ascending
    # UNDEF = 0x027c				# Page 0x0c: AC Sort Descending
    # UNDEF = 0x027d				# Page 0x0c: AC Filter
    # UNDEF = 0x027e				# Page 0x0c: AC Set Clock
    # UNDEF = 0x027f				# Page 0x0c: AC View Clock
    # UNDEF = 0x0280				# Page 0x0c: AC Select Time Zone
    # UNDEF = 0x0281				# Page 0x0c: AC Edit Time Zones
    # UNDEF = 0x0282				# Page 0x0c: AC Set Alarm
    # UNDEF = 0x0283				# Page 0x0c: AC Clear Alarm
    # UNDEF = 0x0284				# Page 0x0c: AC Snooze Alarm
    # UNDEF = 0x0285				# Page 0x0c: AC Reset Alarm
    # UNDEF = 0x0286				# Page 0x0c: AC Synchronize
    # UNDEF = 0x0287				# Page 0x0c: AC Send/Receive
    # UNDEF = 0x0288				# Page 0x0c: AC Send To
    KEY_REPLY = 0x0289				# Page 0x0c: AC Reply
    # UNDEF = 0x028a				# Page 0x0c: AC Reply All
    KEY_FORWARDMAIL = 0x028b			# Page 0x0c: AC Forward Msg
    KEY_SEND = 0x028c				# Page 0x0c: AC Send
    # UNDEF = 0x028d				# Page 0x0c: AC Attach File
    # UNDEF = 0x028e				# Page 0x0c: AC Upload
    # UNDEF = 0x028f				# Page 0x0c: AC Download (Save Target As)
    # UNDEF = 0x0290				# Page 0x0c: AC Set Borders
    # UNDEF = 0x0291				# Page 0x0c: AC Insert Row
    # UNDEF = 0x0292				# Page 0x0c: AC Insert Column
    # UNDEF = 0x0293				# Page 0x0c: AC Insert File
    # UNDEF = 0x0294				# Page 0x0c: AC Insert Picture
    # UNDEF = 0x0295				# Page 0x0c: AC Insert Object
    # UNDEF = 0x0296				# Page 0x0c: AC Insert Symbol
    # UNDEF = 0x0297				# Page 0x0c: AC Save and Close
    # UNDEF = 0x0298				# Page 0x0c: AC Rename
    # UNDEF = 0x0299				# Page 0x0c: AC Merge
    # UNDEF = 0x029a				# Page 0x0c: AC Split
    # UNDEF = 0x029b				# Page 0x0c: AC Distribute Horizontally
    # UNDEF = 0x029c				# Page 0x0c: AC Distribute Vertically
