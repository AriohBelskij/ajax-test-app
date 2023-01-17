import subprocess


def get_device_uuid() -> str:
    devices = subprocess.run(
        ["adb", "devices"], capture_output=True, text=True
    ).stdout
    try:
        return devices.split()[4]
    except IndexError:
        raise Exception("Now not have active devices")


def android_get_desired_capabilities() -> dict:
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "11",
        "resetKeyboard": True,
        "systemPort": 8301,
        "takesScreenshot": True,
        "udid": get_device_uuid(),
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
