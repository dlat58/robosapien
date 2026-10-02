#COMMAND_BITS = 12
# Hexadecimal hex-map database for standard RoboSapien V2 moves
# Note most of these commands are wrong/V1
# Actual commands can be found here: https://markcra.com/robot/ir_codes_v2.php
COMMANDS = {
    # This is a nasty way of specifying bit count of comamnd words (12 for V2)
    "BIT_COUNT": 12,
    # https://markcra.com/robot/ir_codes.php
    "TURN_RIGHT": 0x80,
    "RIGHT_ARM_UP": 0x81,
    "RIGHT_ARM_OUT": 0x82,
    "TILT_BODY_RIGHT": 0x83,
    "RIGHT_ARM_DOWN": 0x84,
    "RIGHT_ARM_IN": 0x85,
    "WALK_FORWARD": 0x300, #0x86,
    "WALK_BACKWARD": 0x87,
    "TURN_LEFT": 0x88,
    "LEFT_ARM_UP": 0x89,
    "LEFT_ARM_OUT": 0x8A,
    "TILT_BODY_LEFT": 0x8B,
    "LEFT_ARM_DOWN": 0x8C,
    "LEFT_ARM_IN": 0x8D,
    "STOP": 0x8E,
    
    "RIGHT_TURN_STEP": 0xA0,
    "RIGHT_HAND_THUMP": 0xA1,
    "RIGHT_HAND_THROW": 0xA2,
    "SLEEP": 0xA3,
    "RIGHT_HAND_PICKUP": 0xA2,
    "STEP_FORWARD": 0xA6,
    "STEP_BACKWARD": 0xA7,
    "LEFT_TURN_STEP": 0xA8,
    "LEFT_HAND_THUMP": 0xA9,
    "LEFT_HAND_THROW": 0xAA,
    "LISTEN": 0xAB,
    "LEFT_HAND_PICKUP": 0xAC,
    "LEAN_FORWARD": 0xAD,
    "RESET": 0xAE,
    
    "WAKEUP": 0xB1,

    "RIGHT_HAND_STRIKE_3": 0xC0,
    "RIGHT_HAND_SWEEP": 0xC1,
    "BURP": 0xC2,
    "RIGHT_HAND_STRIKE_2": 0xC3,
    
    "RIGHT_HAND_STRIKE_1": 0xC5,
    "BULLDOZER": 0xC6,
    "OOPS": 0xC7,
    "LEFT_HAND_STRIKE_3": 0xC8,
    "LEFT_HAND_SWEEP": 0xC9,
    "WHISTLE": 0xCA,
    "LEFT_HAND_STRIKE_2": 0xCB,
    "TALKBACK": 0xCC,
    "LEFT_HAND_STRIKE_1": 0xCD,

    "HIGH_FIVE": 0x369,
    "HEY_BABY": 0x36B,
    "SPARE_CHANGE": 0x371,
    "ROAR": 0x374,

    "ROAM": 0x382,
    
    "DEMO0": 0xD0,
    "POWEROFF": 0xD1,
    "DEMO1": 0xD2,
    "DEMO2": 0xD3,
    "DANCE": 0xD4,
    "CHOP": 0xD6,
    "CHOP2": 0xD9,
    
    "SHUFFLE": 0xF6,
    "THROW": 0xFC,
    
    # Abbreviations
    "HIGH5": 0x369,
    "BULL": 0xC6
}

