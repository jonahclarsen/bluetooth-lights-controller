from bleak import BleakScanner

# Uses Bleak to search for BTLE devices
# Takes 'device_of_interest' as a string or list of strings
# Scans through BTLE devices to find devices that match any of the strings in 'device_of_interest'
# H6001 usually show up under "minger"
# H6005 usually show up under "ihoment"
# None for no filter
async def search_btle(filter_keywords=["minger", "ihoment"]):
    # Check if device_of_interest is a single string or a list of strings
    if isinstance(filter_keywords, str):
        search_terms = [filter_keywords.lower()]  # Convert to list for consistent handling
    else:
        search_terms = [term.lower() for term in filter_keywords]  # Ensure all search terms are lowercase

    devices = await BleakScanner.discover()

    found_devices = []

    for device in devices:
        split_BLEDevice = str(device).split(": ")
        address = split_BLEDevice[0]
        name = split_BLEDevice[1].lower()

        if filter_keywords is None: # No filter
            found_devices.append({"address": address, "name": name})
        else:
            # Check if any of the search terms are present in the device name
            if any(term in name for term in search_terms):
                found_devices.append({"address": address, "name": name})

    print("Found devices:", found_devices)
    return found_devices