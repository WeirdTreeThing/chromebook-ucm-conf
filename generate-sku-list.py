#!/usr/bin/env python3

import os
import sys
import json

variant = ""
ucm_suffixes = []
sku_ids = {}

with open("project-config.json", "r") as project:
    p_json = json.load(project)

configs = p_json['chromeos']['configs']

for config in configs:
    if config['audio']['main']['cras-config-dir'] == variant:
        if not config['audio']['main']['ucm-suffix'] in ucm_suffixes:
            ucm_suffixes.append(config['audio']['main']['ucm-suffix'])
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
