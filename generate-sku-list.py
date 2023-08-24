#!/usr/bin/env python3

import json

def format_skus(sku_ids, suffix):
    sku_ids_formatted = ""
    for sku in sku_ids[suffix]:
        if sku_ids_formatted == "":
            sku_ids_formatted = sku
        else:
            sku_ids_formatted = f"{sku_ids_formatted}|{sku}"
    return sku_ids_formatted

def load_project_config():
    with open("project-config.json", "r") as project:
        project_json = json.load(project)
    return project_json['chromeos']['configs']

def select_variant(configs):
    variants = []
    print("Variants:")
    for config in configs:
        if config['name'] in variants:
            continue
        variants.append(config['name'])
        print(config['name'])
    return input("Choose a variant: ")

def parse_sku_ids(configs, variant):
    sku_ids = {}
    for config in configs:
        if variant not in config['audio']['main']['cras-config-dir']:
            continue
        if config['audio']['main']['ucm-suffix'] not in sku_ids:
            sku_ids[config['audio']['main']['ucm-suffix']] = []
        sku_ids[config['audio']['main']['ucm-suffix']].append(config['identity']['sku-id'])
    return sku_ids

def print_sku_id_list(sku_ids):
    for suffix in sku_ids:
        sku_ids_formatted = format_skus(sku_ids, suffix)
        print(f"{suffix}: {sku_ids_formatted}")

def main():
    configs = load_project_config()
    variant = select_variant(configs)
    sku_ids = parse_sku_ids(configs, variant)
    print_sku_id_list(sku_ids)

main()
