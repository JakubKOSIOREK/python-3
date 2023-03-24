"""
this is a program whose task is to encode selected text elements as:
- user name
- file name
- selected words
"""
import os,re, hashlib

root_path = os.path.dirname(os.path.abspath(__file__))
input_dir = 'input_data'
output_dir = 'output_data'
input_file_name = '20230312-test_file.csv'
extensions_list = ['png', 'doc', 'jpg', 'log', 'csv']
sensitive_words_list = ['Dell','Instrumentation']

#--------------------------------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------------------------------
def mask_method(x): return (f'MASKED_HASH({hashlib.md5(x.encode()).hexdigest()})')

def user_masking(x):
    if x.find("C:\\Users") != -1:
        u_name =line.split("\\")[2]               # split line item by '\\' delimiter, user name is always at [2] position
        u_name_masked = mask_method(u_name)
        return x.replace(f'\\{u_name}\\', f'\\USER_{u_name_masked}\\')# 
    else:
        return x

def file_name_masking(x, ext):
    ext_pos = x.find(f'.{ext}')                 # returns the lowest index or first occurrence of the extension
    if ext_pos != -1:
        bslash_pos = x.rfind('\\')              # returns the rightmost index of the '\\' if found in the given string
        if bslash_pos != -1:
            f_name = x[bslash_pos +1 : ext_pos] # the file name is between the last '\' and the 'ext'
        else:
            f_name = x[0 : ext_pos]
        f_name_masked = mask_method(f_name)
        return x.replace(f_name, f'FILE_{f_name_masked}')
    else:
        return x

def word_masking(x, word):
    if x.find(f'{word}') != -1:
        s_word_masked = mask_method(word)
        return x.replace(word, f'WORD_{s_word_masked}')
    else:
        return x
#--------------------------------------------------------------------------------------
# LOAD FILE WITH DATA TO MASK
#--------------------------------------------------------------------------------------
inf_path = f'{root_path}/{input_dir}/{input_file_name}'
f_to_mask = open(inf_path, 'r', encoding='UTF8')
#--------------------------------------------------------------------------------------
# CREATE OUTPUTS
#--------------------------------------------------------------------------------------
pattern = '[\w-]+?(?=\.)' # match the file name with the specific pattern
f_name = re.search(pattern, inf_path)
f_name = f_name.group()
outf_path = f'{root_path}/{output_dir}'
f_masked = f'{outf_path}/{f_name}_MASKED.csv'
f_masked = open(f_masked, 'w', encoding='UTF8')
#--------------------------------------------------------------------------------------
# MAIN CODE
#--------------------------------------------------------------------------------------
count = 0
while True:
    count += 1
    line = f_to_mask.readline().rstrip('\n')    # read line without '\n'
    split_line = line.split(',')    # split line by ',' delimiter
    no = 0  # number needed for split_line list number to over
    for item in split_line:
        #------------------------------------------------------------------------------
        # --- STEP 1: masking user name
        #------------------------------------------------------------------------------
        split_line[no] = user_masking(item)
        item = split_line[no]
        #------------------------------------------------------------------------------
        # --- STEP 2: masking file name
        #------------------------------------------------------------------------------
        for extension in extensions_list:
            split_line[no] = file_name_masking(item, extension)
            item = split_line[no]
        #------------------------------------------------------------------------------
        # --- STEP 3: masking sensitive words
        #------------------------------------------------------------------------------
        for s_word in sensitive_words_list:
            split_line[no] = word_masking(item, s_word)
            item = split_line[no]
        no += 1
    line = ",".join(split_line) # combining line items into a single string
    f_masked.writelines(line)
    f_masked.writelines('\n')

    if not line:
        break

f_masked.close()
f_to_mask.close()
