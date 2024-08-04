import xml.etree.ElementTree as ET
import json
# import requests

# Step 1: Download the XML file
url = 'https://www.mbsonline.gov.au/internet/mbsonline/publishing.nsf/Content/Downloads-2021-11/$File/MBS-XML-211101.zip'

# Download the zip file
# response = requests.get(url)
# with open('MBS-XML-211101.zip', 'wb') as file:
#     file.write(response.content)

# Unzip the file to extract the XML
# import zipfile
# with zipfile.ZipFile('MBS-XML-211101.zip', 'r') as zip_ref:
#     zip_ref.extractall('MBS_XML')

# Step 2: Parse the XML file
xml_file_path = "/Users/venkateshnagilla/Downloads/MBS-XML.211101.xml"

def extract_mbs_items(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    mbs_items = []

    # Iterate through each item in the XML
    for item in root.findall(".//item"):  # Update the path as per the actual XML structure
        main_mbs = item.find("mainMbs").text if item.find("mainMbs") is not None else None
        description = item.find("description").text if item.find("description") is not None else None
        
        if description and "not in association with" in description:
            exclusions = [exclusion.text for exclusion in item.findall(".//excludingExclusions/exclusion")]  # Update the path as per the actual XML structure
            mbs_items.append({
                "mainMbs": main_mbs,
                "excludingExclusions": exclusions
            })

    return mbs_items

# Step 3: Extract the MBS items
mbs_items = extract_mbs_items(xml_file_path)

# Step 4: Save the extracted data to a JSON file
json_file_path = "output.json"
with open(json_file_path, "w") as json_file:
    json.dump(mbs_items, json_file, indent=4)

print(f"Extracted data has been saved to {json_file_path}")
