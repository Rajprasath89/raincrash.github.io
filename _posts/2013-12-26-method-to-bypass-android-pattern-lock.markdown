---
author: sricharanchiruvolu
comments: true
date: 2013-12-26 12:47:00+00:00
layout: post
slug: method-to-bypass-android-pattern-lock
title: Method to bypass android pattern lock !!
wordpress_id: 154
---

You'll need:  
Linux distro of your choice  
Android phone  
Android USB Data cable  
Android ADB  
Execution:  
1. Connect your phone to your PC  
using USB cable.  
2. Install ADB via terminal  
3. Boot into any Linux distro you have.  
4.Open up terminal and type :  
  
sudo apt-get install android-tools-adb  
  
This will install ADB.  
  
For disabling the pattern lock via terminal, go to android shell. Use the following code:  
  
adb devices  
adb shell  
cd data/system  
su  
rm *.key  
Unlock pattern should be here.  
  
Disconnect your phone and reboot. Just  
try some random gesture and it will  
unloc
