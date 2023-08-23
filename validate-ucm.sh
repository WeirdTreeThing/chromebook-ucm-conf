#!/bin/sh

# Script to check each HiFi file for any keywords from the ChromeOS UCM
# that should have been removed, and also checks for any empty EnableSequence
# and disable Sequence lines

failed=0
filtered_keywords=('cdev' 'FullySpecifiedUCM' 'DspName' 'sof' 'JackDev' 'JackSwitch' 'Line Out' 'CaptureChannelMap' 'IntrinsicSensitivity')

for keyword in "${filtered_keywords[@]}"; do
	find -name "HiFi*.conf" -exec grep "${keyword}" {} + && failed=1
done

find -name "HiFi*.conf" -exec pcregrep -M  'EnableSequence \[(\n|.)\t\]' {} + && failed=1
find -name "HiFi*.conf" -exec pcregrep -M  'DisableSequence \[(\n|.)\t\]' {} + && failed=1

if [ $failed = 1 ]; then
	echo "UCM validation failed"
	exit 1
else
	echo "UCM validation passed"
	exit 0
fi
