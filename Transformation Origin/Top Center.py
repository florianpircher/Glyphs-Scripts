# MenuTitle: • ​​Top Center
from AppKit import NSUserDefaults

userDefaults = NSUserDefaults.standardUserDefaults()
userDefaults.setInteger_forKey_(0, "GSTransformMetricsOriginType")
userDefaults.setInteger_forKey_(7, "GSTransformGridCorner")
