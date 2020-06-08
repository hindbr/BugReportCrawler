from mymodule import my_urlopen, bug_template
import os, sys
bug_items = open("./bug_item_file.txt","r")

if os.path.isfile("./success_data.txt"):
	pass
else:
	os.mknod("./success_data.txt")
if os.path.isfile("./failed_data.txt"):
	pass
else:
	os.mknod("./failed_data.txt")

project = sys.argv[1] 
bug_ids = bug_items.readlines()

bug_items.close()
print("Scraping....\n")

success_data_file = open("./success_data.txt","r")
success_data = success_data_file.readlines()
success_data_file.close()

for bug_item_url in bug_ids[0:20000]:
    bug_item_url = bug_item_url.strip()
    if bug_item_url + "\n" not in success_data:
        try:
            bs_obj = my_urlopen(bug_item_url)
            bug_template(bs_obj,project)
        except:
            success_data_file.close()
            failed_data_file = open("./failed_data.txt", "a+")
            print(bug_item_url + " failed!")
            failed_data_file.write(bug_item_url + "\n")
            failed_data_file.close()
            continue
        else:
            print(bug_item_url + " successful!")    
            success_data_file = open("./success_data.txt","a+")
            success_data_file.write(bug_item_url + "\n")
            success_data_file.close()
    else:
        print(bug_item_url + "'s data is already exist!")
	
print("Done! Bug data are stored in dir data.\n")
