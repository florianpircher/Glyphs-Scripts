# MenuTitle: x-Height
from AppKit import NSUserDefaults

userDefaults = NSUserDefaults.standardUserDefaults()
userDefaults.setInteger_forKey_(2, "GSTransformMetricsOriginType")
userDefaults.setInteger_forKey_(3, "GSTransformMetricsOrigin")
