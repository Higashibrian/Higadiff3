from PIL import Image, ImageDraw, ImageChops, ImageFilter,ImageOps
import PIL
import os,csv,time, BHTest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from slacker import Slacker
import multiprocessing, subprocess, csv
import threading
import datetime

################################################################################################
#
#Reported fields
#Base64(Image)|#of Elements on Page|Link Text|Element IDs|  
################################################################################################
list_delimiter=('&*split|ter!')
sublist_delimiter=('!ret|tilps*&')

headcode='pass'#need to replace this with a real way to designate headcode.

visited_page_counter=0

def scan(domain):
	global domain_name
	global navs_list
	global metrics_list

	window_size=('1024','1024')

	driver = webdriver.PhantomJS()
	#^ This needs to be replaced with the custom browser choice

	driver.set_window_size(window_size)
	try:
		exec(headcode)
	except:
		print ('Failure in execution of headcode')
	while visited_page_counter <len(navs_list):
		visited_page_counter+=1
		current_page=domain_name+navs_list[visited_page_counter]
		driver.get(current_page)
		try:
			exec(loopcode)
		except:
			print ('Failure in execution of loopcode')
		print ('|---'+current_page+'--|')

		#insert code to wait for document to load here
		time.sleep(2)
		#^ delete this after code is written for document wait time.
		url=current_page
		Base64=driver.get_screenshot_as_base64()

		Page_elements=len(driver.find_elements_by_css_selector('*'))

		link_text=''
		element_ids=''		


def run():
	print ('run just started')
	global navs_list
	global timetorun
	global pw
	global url_list
	global page_info_list
	#####
	print ('get webdrivers')
	#condriver = set_browser(conselect) write a function: [set_browser] that will pull a value from a configuration file indicating the browser is ie,phantomjs, Firefox, etc.
	condriver=webdriver.PhantomJS
	condirect=''
	print ('got webdrivers')
	condriver.set_window_size(window_size)

	exec(headcode)

	print ('executed headcode')
	while timetorun < len(url_list):
		print ('start while')
		this=timetorun
		
		timetorun+=1
		print (conbase+navs_list[this])

		print ('---')
		condriver.get(conbase+navs_list[this])#

		url=''
		Base64=''
		Page_elements=''
		link_text=''
		element_ids=''






		direct=navs_list[this]
		print ('driver.get')
		time.sleep(2)
		try:
			exec(loopcode)
		except:
			print ('error in loopcode')
		print ((conbase+navs_list[this]))
		a=condriver.get_screenshot_as_base64()
		

		###change this section.
		###base 64 string should be written to a file with other metrics related to the page.
		###The screenshot should be taken last.
		###Elements and their positions can be examined against the differnce map?
		f = open(condom+"/pictures/"+str(this)+".png", "wb")
		f.write(a.decode('base64'))
		f.close()
		page_info_list.append((this,conbase+navs_list[this],varbase+navs_list[this]))
		# Add more metrics here and save to file

		print (str(this))
	condriver.quit()

start_time = time.time()
##
time.sleep(2)

"""
#If option to scan is selected run this code.
for x in range (0,threads):
	time.sleep(1)
	exec('mult'+str(x)+' = threading.Thread(target=run, args=())')
	exec('print (mult'+str(x)))
	exec('mult'+str(x)+'.start()')
	time.sleep(0)
"""

def compare(time,hd,rhd,cwd):
	#use date_time variable to create a new folder in Projects/sample_project/comparisons
	#Use csv or simply write to file.
	print ('to be continued')



def print_domains(higalist):
	print ('\n\nUse this configuration?')
	x=1
	for this in higalist:
		print ('|-----|'+str(this[0])+' = '+str(this[1]))
	input()
def open_uploads():
	subprocess.call(["open","-R", working_directory+'/upload'])	
	input('Drop any .csv files into the uploads folder')
 
	url_list=[]
	csv_sheets=0
	added_urls=0
	for item in os.listdir(working_directory+'/upload'):
		if item.endswith('.csv'):
			print ('checking '+item)
			csv_sheets+=1
			with open(working_directory+'/upload/'+item) as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					if domain_name in row[0].split('#')[0] and not row[0].split('#')[0] in url_list:
						url_list.append(row[0].split('#')[0])
						added_urls+=1
	print ('Checked '+str(csv_sheets)+' .csv files. Found '+str(added_urls)+ ' new URLs')

#def define_env(domain):

################################################################################################
timein=datetime.datetime.now()

#####path to image copy analysis

time_directory=str(timein.strftime('%m%d_%H%M'))
projects_directory=os.getcwd()+'/Projects'
try:
	os.mkdir(projects_directory)
except:
	pass

time_directory=str(timein.strftime('%m%d_%H%M'))
projects_directory=os.getcwd()+'/Projects'
current_projects=os.listdir(projects_directory)
working_directory=projects_directory+''
exit_value=1
print (projects_directory)
################################################################################################
while exit_value==1:
	print ('\n'+working_directory+'\n')
	current_projects=os.listdir(projects_directory)
	working_directory=projects_directory+''
	x=0
	print ('\n\n\nSelect an option:')
	for y in range (1,len(current_projects)):
		x=y
		print ('|-----('+str(x)+') '+current_projects[x])

	print ('|-----('+str(x+1)+') View projects on Hold\n|-----('+str(x+2)+') View Completed Projects\n|-----('+str(x+3)+') Start a new project.\n|-----('+str(x+4)+') Generate a project report.')
	initial_selection=input('|-Make your Selection:')
	try:
		int_selection=int(initial_selection)
	except:
		int_selection=0

	if int_selection<len(current_projects):
		domain=current_projects[int_selection].replace('_','.')
		print ('domain: '+domain)
		working_directory=working_directory+'/'+current_projects[int_selection]
		print ('\nyou have selected '+current_projects[int_selection]+'\n'+working_directory)
		option_select=input('|-----(1) Open the Comparisons directory\n|-----(2) Change Baseline Data\n|-----(3) Add a .csv file\n|-----(4) Define Environments\n|-Make your Selection:')
		if option_select == '1':
			subprocess.call(["open","-R", working_directory+'/comparisons'])
		elif int_selection==len(current_projects)+3:
			print ('excel report')
		elif option_select=='e':
			exit_value=0
			break
		elif option_select == '3':
			print(working_directory)
			open_uploads()
		elif option_select == '4':
			print ('Automatically make folders for Con, Var, Stage, and Live. Update environments tab in Environment_Info.xlsx file in Project folder with the Environments.')
			environments_list=[]
		elif option_select == '2':
			print ('another screen with options\n1. re-run complete screenshotting\n2. re-scan specific pages\n3. ')


			condom='con.'+domain.replace('.','-')+'.hdm-clgn.io'
			vardom='var.'+domain.replace('.','-')+'.hdm-clgn.io'

			stagedomsplit=domain.split('.')
			trail=len(stagedomsplit)-1
			if stagedomsplit[trail]=='com':
				stagedom=stagedomsplit[trail-1]
			else:
				stagedom=''
				for item in stagedomsplit:
					stagedom=stagedom+item
			stagedom=stagedom+'.celgenevalwp.com'
			environments_list.append(['con',condom])
			environments_list.append(['var',vardom])
			environments_list.append(['staging',stagedom])
			environments_list.append(['production',domain])

#			print (environments_list)
			print_domains(environments_list)
	elif int_selection==len(current_projects):
		print ('View projects on Hold')
		print (int_selection)
	elif int_selection==len(current_projects)+1:
		print (int_selection)
		print ('View Completed Projects')

	elif int_selection==len(current_projects)+2:
		print ('Start a new project')
		domain_name=input('Please enter the domain name \n\t:http://')
		filename=domain_name.replace('.','_')
		working_directory=working_directory+'/'+filename
		try:
			os.mkdir(working_directory)
			os.mkdir(working_directory+'/baseline')
			os.mkdir(working_directory+'/comparisons')
			os.mkdir(working_directory+'/upload')
		except:
			pass

	elif int_selection==len(current_projects)+3:
		print ('excel report')
	if 	initial_selection=='e':
		exit_value=0
		break

#####-begin multithreaded crawl here-#####



	#for item in url_list:
	#	print (item)
	###how to identify headcode? .hc extension?

print (('\n')	)
#####select webdriver#####

#####select webdriver#####

#resolutions 480, 720, 1024, 1280
#Chrome, PhantomJS, IE9


#####visit site####------------------###or###--------------------#####read from a file#####



