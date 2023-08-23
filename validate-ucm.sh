#!/bin/sh

# Script to check each HiFi file for any keywords from the ChromeOS UCM
# that should have been removed

failed=0
filtered_keywords=('cdev' 'FullySpecifiedUCM' 'DspName' 'sof' 'JackDev' 'JackSwitch' 'Line Out' 'CaptureChannelMap' 'IntrinsicSensitivity')

for keyword in "${filtered_keywords[@]}"; do
	find -name "HiFi*.conf" -exec grep "${keyword}" {} + && failed=1
done

if [ $failed = 1 ]; then
	echo "UCM validation failed"
	exit 1
else
	echo "UCM validation passed"
	exit 0
fi
