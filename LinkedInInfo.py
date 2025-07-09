from linkedin_api import Linkedin
import pandas as pd
#hello my name is aaroh

# Ask user for their LinkedIn credentials
user_email = input("Enter your LinkedIn email address: ")
user_password = input("Enter your LinkedIn password: ")

def fetch_linkedin_info():
    api = Linkedin(user_email, user_password)
    desired_connection = input("Enter the name of who you want to query information for (firstname-lastname): ")
    profile_desired = api.get_profile(desired_connection)
    return profile_desired

def remove_dict_from_list(dict_list):
    merged_dict = dict()
    for i in dict_list:
        merged_dict.update(i)
    return merged_dict

def fetch_company_info(specific_info):
    if isinstance(specific_info, dict):
        if 'experience' in specific_info:
            company_name = specific_info['experience']
            if isinstance(company_name, list):
                for item in company_name:
                    if isinstance(item, dict) and 'companyName' in item:
                        return item['companyName']
            elif isinstance(company_name, dict):
                if 'companyName' in company_name:
                    return company_name['companyName']
            else:
                print("DataType Invalid")
        else:
            print("'experience' key not found")
    else:
        print("DataType Invalid")
    return None

def fetch_school_name(specific_info):
    def dict_case(specific_info):
        count = 0
        school_name_col = None
        for i in specific_info.keys():
            if i == 'education':
                count += 1
                if count == 1:
                    school_name = remove_dict_from_list(specific_info[i])
                    for j in school_name.keys():
                        if j == 'schoolName':
                            school_name_col = school_name[j]
        return school_name_col

    if isinstance(specific_info, dict):
        school_name_col = dict_case(specific_info)
    elif isinstance(specific_info, list):
        merged_dict = remove_dict_from_list(specific_info)
        school_name_col = dict_case(merged_dict)
    else:
        print('Enter a valid data type!')

    return school_name_col

def fetch_position_info(specific_info):
    def if_dict_sit(specific_info):
        count = 0
        for i in specific_info.keys():
            if i == 'experience':
                count += 1
                if count == 1:
                    pos_info = specific_info[i]
                    pos_info_dict = remove_dict_from_list(pos_info)
                    pos_name = pos_info_dict['title']
        return pos_name

    if isinstance(specific_info, dict):
        pos_name = if_dict_sit(specific_info)
    elif isinstance(specific_info, list):
        merged_dict = remove_dict_from_list(specific_info)
        pos_name = if_dict_sit(merged_dict)

    return pos_name

def fetch_specific_linkedin_info(profile_desired):
    info_desired = input("From these options: [education, experience, position] what information do you want to fetch: ")

    if info_desired == 'education':
        return fetch_school_name(profile_desired)
    elif info_desired == 'experience':
        return fetch_company_info(profile_desired)
    elif info_desired == 'position':
        return fetch_position_info(profile_desired)
    else:
        print('Info type not recognized, try again!')

    return None









