from appium.options.android import UiAutomator2Options


def get_capabilities():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "R5CX517EZJR"

    options.app_package = "com.lyxasellerapp"
    options.app_activity = "com.lyxasellerapp.MainActivity"

    options.no_reset = True
    options.set_capability(
    "appium:forceAppLaunch",
    True
)

    options.set_capability(
        "appium:uiautomator2ServerInstallTimeout",
        60000
    )

    options.set_capability(
        "appium:uiautomator2ServerLaunchTimeout",
        60000
    )

    options.set_capability(
        "appium:disableWindowAnimation",
        True
    )

    options.set_capability(
        "appium:ignoreHiddenApiPolicyError",
        True
    )

    return options