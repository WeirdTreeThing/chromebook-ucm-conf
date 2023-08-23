#!/usr/bin/env python3

import os
import sys
import json

variants = []
sku_ids = {}

with open("project-config.json", "r") as project:
    p_json = json.load(project)

configs = p_json['chromeos']['configs']

print("Variants:")
for config in configs:
    variant = config['name']
    if not variant in variants:
        variants.append(variant)
        print(variant)

variant = input("Choose a variant: ")

for config in configs:
    if config['audio']['main']['cras-config-dir'] == variant:
        if not config['audio']['main']['ucm-suffix'] in sku_ids:
            sku_ids[config['audio']['main']['ucm-suffix']] = []
        sku_ids[config['audio']['main']['ucm-suffix']].append(config['identity']['sku-id'])

for suffix in sku_ids:
    suffixes_formatted = ""
    for sku in sku_ids[suffix]:
        if suffixes_formatted == "":
            suffixes_formatted = str(sku)
        else:
            suffixes_formatted = f"{suffixes_formatted}|{str(sku)}"
    print(f"{suffix}: {suffixes_formatted}")
