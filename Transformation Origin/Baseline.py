# MenuTitle: Baseline
from AppKit import NSUserDefaults

userDefaults = NSUserDefaults.standardUserDefaults()
userDefaults.setInteger_forKey_(2, "GSTransformMetricsOriginType")
userDefaults.setInteger_forKey_(2, "GSTransformMetricsOrigin")
