import os
import datetime
#
def list_files(folder_path):
    # Initialize an empty list to store file information
    file_list_dxf = []
    file_list_prs = []
    complete_list = []

    # Iterate through all files in the specified folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Get the full path of the file
            file_path = os.path.join(root, file_name)

            # Get the file extension
            _, file_extension = os.path.splitext(file_name)

            # Get the last update time of the file
            last_update_time = os.path.getmtime(file_path)
            last_update_datetime = datetime.datetime.fromtimestamp(last_update_time)

            if file_extension == '.DXF':
                file_list_dxf.append({
                        'file_name': file_name.split('.')[0],
                        'last_update_datetime_dxf': last_update_datetime,
                })
            
            if file_extension == '.PRS':
                file_list_prs.append({
                        'file_name': file_name.split('.')[0],
                        'last_update_datetime_prs': last_update_datetime,
                })
            

    for item_prs in file_list_prs:
        for item_dxf in file_list_dxf:
            if item_dxf['file_name'] == item_prs['file_name']:
                complete_list.append({'file_name': item_dxf['file_name'],
                                    'last_update_datetime_dxf': item_dxf['last_update_datetime_dxf'],
                                    'last_update_datetime_prs': item_prs['last_update_datetime_prs']
                                    })
                #print(f"File: {item_dxf['file_name']}.dxf, Last update: {item_dxf['last_update_datetime_dxf']}")

    
    print(file_list_prs[0]['file_name'])
    return complete_list

def main():
    # Specify the folder path
    folder_path = "C:/Users/rbattisti/Desktop/DXF" #These bars bebcause of unicode error

    # Get the list of files in the folder
    files = list_files(folder_path)

    # Print the list of files with their extensions and last update date
    for file_info in files:
        print(f"File: {file_info['file_name']} | Date_DXF {file_info['last_update_datetime_dxf']} | Date_prs: {file_info['last_update_datetime_prs']}")
    
    #print(files)

if __name__ == "__main__":
    main()
