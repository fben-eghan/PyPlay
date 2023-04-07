import xml.etree.ElementTree as ET

def remove_elements_by_numbers(xml_file, numbers, output_file):
    try:
        # parse the XML file
        with open(xml_file, 'rb') as f:
            tree = ET.parse(f)
        root = tree.getroot()

        # find the elements to remove
        elements_to_remove = [element for number in numbers for element in root.findall(f'.//*[contains(tag,"{number}")]')]

        # remove the elements
        for element in elements_to_remove:
            root.remove(element)

        # update the tradecount value
        root.set('tradecount', str(len(root)))

        # write the modified XML to the output file
        tree.write(output_file)

        # return success message
        print("Elements removed successfully.")
        return True

    except Exception as e:
        # return error message
        print(f"Error removing elements: {e}")
        return False

# example usage
numbers_to_remove = ['1234567', '2345678', '3456789']
success = remove_elements_by_numbers('input.xml', numbers_to_remove, 'output_tradefile.xml')
if success:
    print("Operation was successful!")
else:
    print("Operation failed.")
