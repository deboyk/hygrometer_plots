# -*- coding: utf-8 -*-
"""
@author: DEBOYK
"""


#### IMPORT ####
from ipywidgets import Box, FileUpload, Layout, widgets

box_layout = Layout(display='flex', 
                   flex_flow='column', 
                   justify_content='space-around', 
                   align_items='center',
                   width='40%')


#### UPLOAD FILES ####
def upload_file_button():
    upload_file = FileUpload(
        description="Upload files", 
        accept='.csv', multiple=True, 
        button_style='info',
        #style = {'description_width':'initial', 'button_color':'darkred'}
        style = {'description_width':'initial', 'button_color':'DarkBlue'}

    )
    #upload_csv.style.button_color = 'darkred'
    box_file = Box(children=[upload_file], layout=box_layout)

    def handle_upload(change):
        file = []
        try:
            if upload_file.data != []:
                #box.close()
                for i, md in enumerate(upload_file.metadata):
                    temp_name=(md['name'])
                    file.append(temp_name)
                    with open(temp_name, "w+b") as wfp:
                        wfp.write(upload_file.data[i])
            else:
                print('Please use the Upload button to import files')
        except:
            print('')
        #upload_csv.style.button_color = 'green' #Update color when files uploaded
        upload_file.style.button_color = 'lightslategray' #Update color when files uploaded
    
    upload_file.observe(handle_upload, names=['value'])
    
    #def handle_upload_button(ev):
    #    upload_csv.style.button_color = 'green' #Update color when files uploaded

    #upload_csv.observe(handle_upload_button) 
                          
    return box_file, upload_file
