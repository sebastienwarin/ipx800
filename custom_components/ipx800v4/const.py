"""Constant for the ipx800v4 integration"""
DOMAIN = "ipx800v4"
GLOBAL_PARALLEL_UPDATES = 1

CONTROLLER = "controller"
UNDO_UPDATE_LISTENER = "undo_update_listener"

DEFAULT_TRANSITION = 0.5
REQUEST_REFRESH_DELAY = 0.6

CONF_DEVICES = "devices"

CONF_COMPONENT = "component"
CONF_ID = "id"
CONF_IDS = "ids"
CONF_EXT_ID = "ext_id"
CONF_TRANSITION = "transition"
CONF_TYPE = "type"

TYPE_RELAY = "relay"
TYPE_XPWM = "xpwm"
TYPE_XPWM_RGB = "xpwm_rgb"
TYPE_XPWM_RGBW = "xpwm_rgbw"
TYPE_XDIMMER = "xdimmer"
TYPE_VIRTUALOUT = "virtualout"
TYPE_VIRTUALIN = "virtualin"
TYPE_ANALOGIN = "analogin"
TYPE_DIGITALIN = "digitalin"
TYPE_X4VR = "x4vr"
TYPE_XTHL = "xthl"
TYPE_X4FP = "x4fp"

CONF_COMPONENT_ALLOWED = [
    "light",
    "switch",
    "sensor",
    "binary_sensor",
    "cover",
    "climate",
]

CONF_TYPE_ALLOWED = [
    TYPE_RELAY,
    TYPE_XPWM,
    TYPE_XPWM_RGB,
    TYPE_XPWM_RGBW,
    TYPE_XDIMMER,
    TYPE_VIRTUALOUT,
    TYPE_VIRTUALIN,
    TYPE_ANALOGIN,
    TYPE_DIGITALIN,
    TYPE_X4VR,
    TYPE_XTHL,
    TYPE_X4FP,
]
