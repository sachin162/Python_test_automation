import itertools
import selenium.webdriver as wd
loc_list_of_links="//div[@id='content']//ul//li//a"

#AB Testing
loc_ab_heading ="//div[@id='content']//h3"
loc_ab_para ="//div[@id='content']//p"

#Add Remove elements
add_remove_head = "//div[@id='content']//h3"
add_btn = "//div[@class='example']//button"
del_btn="//div[@class='example']//div//button"

#Basic Authentication

#Broken Image
image_head ="//div[@id='content']//h3"

#Challenging DOM
btn = "//a[@class='button']"
alert_btn_chal_DOM = "//a[@class='button alert']"
success_btn_chal_DOM = "//a[@class='button success']"

#Challenging DOM , Table
table_loc = []
def construct_dynamic_xpath_for_CD_table():
    xpath = "//tbody//tr//td[6]"
    for i in range(1,11):
        for j in range(1,7):
            gen_xpath = f"//tbody//tr[{i}]//td[{j}]"
            table_loc.append(gen_xpath)
            print(gen_xpath)


construct_dynamic_xpath_for_CD_table()
print(table_loc)


#checkboxes
check_head ="//div[@id='content']//h3"
checkboxes_loc = "//form[@id='checkboxes']//input"

#context_menu
context_head ="//div[@id='content']//h3"
right_click_hotspot = "//div[@id='hot-spot']"

#Digest Authorization pop up

#Disappearing Element
loc_elements = "//ul//li"
disapper_head = "//div[@id='content']//h3"
disapper_para = "//p"

#Drag and Drop
drag_drop_loc_head ="//div[@id='content']//h3"
drag_drop_a_col_txt = "//div[@id='column-a']//header"
drag_drop_b_col_txt = "//div[@id='column-b']//header"
drag_drop_a_col = "//div[@id='column-a']"
drag_drop_b_col = "//div[@id='column-b']"

#DropDowns
DropDown_head = "//div[@id='content']//h3"
Select_drop_down_ele = "//select[@id='dropdown']"

#Dynamic Contents
Dynamic_cont_head = "//div[@id='content']//h3"
dynamic_content_text = "//br//following-sibling::div[@class='row']//div[@id='content']//div//div[2]"

#Dynamic Controls
checkBox = "//input[@id='checkbox']"
remove_btn = "//form[@id='checkbox-example']//button"
input_text_box = "//form[@id='input-example']//input"
enable_disable_btn = "//form[@id='input-example']//button"
headings = "//div[@id='content']//div//h4"


#Modal Windows
modal_head ="//div[@id='modal']//div[2]//div//h3"
modal_desc = "//div[@class='modal-body']//p"
modal_close= "//div[@class='modal-footer']//p"

#exit intent
#mouse out of viewport to view the modal window
#How to move out of view port

#File Downloader
file_down_head = "//div[@id='content']//h3"
list_of_files = "//div[@class='example']//a"


#File Uploader
file_upload_head = "//div[@class='example']//h3"
upload_btn = "//input[@id='file-submit']"
choose_file_btn ="//input[@id='file-upload']"
drg_drp_div = "//div[@id='drag-drop-upload']"

#FLoating Menu
float_menu_ele = "//div[@id='menu']//ul//li"
float_menu_head = "//div[@class='example']//h3"

#GeoLocation
Geo_Location_head = "//div[@class='example']//h3"
where_am_i_btn = "//p[@id='demo']//following-sibling::button"
latitude_val = "//div[@id='lat-value']"
longitude_val = "//div[@id='long-value']"
map_link = "//div[@id='map-link']"


#Horizontal Slider
hor_slider_head = "//div[@class='example']//h3"
slider = "//input[@type='range']"
slider_div_css = "div[class='sliderContainer']"

#Hovers
images_hover_area = "div[class='figure']"
image_details_after_hover  = "div[class='figcaption']>h5"

#Infinite Scroll

#Input
input_num_box = "input[type='number']"


#JqueryUI
jquery_head = "//div[@class='example']//h3"

#JavaScript Alerts
JavaScript_btns = "div[class='example']>ul>li>button"
javascript_results = "p[id='result']"

#KeyPress
keyPress_results = "p[id='result']"

#LargeDOM
large_dom_rows = "table[id='large-table']>tbody>tr"
large_dom_each_data = "table[id='large-table']>tbody>tr>td"

#Multiple_windows
mul_windows_head = "div[class='example']>h3"
mul_windows_link = "div[class='example']>a"

#FRames


#Notification messages


#Redirect_links


#SecureFile Download
secure_file_links = "div[class='example']>a"

#Shadow DOMS


#Shifting Content


#SortedTables






