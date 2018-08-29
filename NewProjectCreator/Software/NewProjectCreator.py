##This Program Creates a simple folder structure for better Data Managment on new projects and to create a Standard.##
##Created By Lynton Brown 06/29/2018##

from Tkinter import Tk,Label,Checkbutton,Entry,Button,Frame,BooleanVar,END #Import used portions of Tkinter Module
from tkMessageBox import showwarning ##Import used portions of tkMessageBox
from os import path,path,mkdir,environ##Import used portions of os Module

class GUI(object): ##Main Class (root)
     def __init__(self, master): ##Inititilize Main
          self.master = master ##Define master
          master.title ("GUI Name") ##Create Title for GUI Window
          master.geometry("816x504") ##Define Window Size
          master.resizable (width = False, height = False)##Disable Max Button on Window

          master.columnconfigure(0,minsiz=187,weight=1) ##Column Definition (size)
          master.columnconfigure(1,minsiz=306,weight=1) ##Column Definition (size)
          master.columnconfigure(2,minsiz=160.3536,weight=1) ##Column Definition (size)
          master.columnconfigure(3,minsiz=160.3536,weight=1) ##Column Definition (size)

          master.rowconfigure(0,minsiz=98.2464,weight=1) ##Row Definition (size)
          master.rowconfigure(1,minsiz=323.2512,weight=1) ##Row Definition (size)
          master.rowconfigure(2,minsiz=56.6784,weight=1) ##Row Definition (size)
          master.rowconfigure(3,minsiz=39.3216,weight=1) ##Row Definition (size)

          self.projectNameLabel=projectNameLabel=Label(master,text='Project Name:',font=('BoldCourier',16)) ##Label Widget for projectNameEntry Box
          projectNameLabel.grid(row=0,column=0) ##Grid Label

          self.projectNameEntry=projectNameEntry=Entry(master,text='Enter Name Of Project',font=('Courier',16)) ##Entry Widget for Entering Name Of Project
          projectNameEntry.grid(row=0,column=1) ##Gid Entry Widget
          projectNameEntry.focus() ##Set Curser To Entry Widget

          self.includeStartingFilesVariable=includeStartingFilesVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.includeStartingFiles=includeStartingFiles=Checkbutton(master,text='Include\nStarting Files',borderwidth=2,relief='groove',variable=includeStartingFilesVariable,font=('Courier',16)) ##Checkbutton Widget for Including Starting Files
          includeStartingFiles.grid(row=0,column=2, columnspan=2) ##Grid Checkbutton Widget

          self.folderFrame=folderFrame=Frame(master,width=462, height=342, borderwidth=2,relief='groove') ##Frame Widget to Create Better GUI Layout
          folderFrame.grid(row=1,column=0,rowspan=2,columnspan=2) ##Grid Frame Widget

          folderFrame.columnconfigure(0,minsize=156,weight=1) ##Column Definition (size)
          folderFrame.columnconfigure(1,minsize=12.9984,weight=1) ##Column Definition (size)
          folderFrame.columnconfigure(2,minsize=149.0016,weight=1) ##Column Definition (size)
          folderFrame.columnconfigure(3,minsize=144,weight=1) ##Column Definition (size)

          folderFrame.rowconfigure(0,minsize=36,weight=1) ##Row Definition (size)
          folderFrame.rowconfigure(1,minsize=34.6656,weight=1) ##Row Definition (size)
          folderFrame.rowconfigure(2,minsize=42,weight=1) ##Row Definition (size)
          folderFrame.rowconfigure(3,minsize=12.9984,weight=1) ##Row Definition (size)
          folderFrame.rowconfigure(4,minsize=42,weight=1) ##Row Definition (size)
          folderFrame.rowconfigure(5,minsize=12.9984,weight=1) ##Row Definition (size)
          folderFrame.rowconfigure(6,minsize=42,weight=1) ##Row Definition (size)
          folderFrame.rowconfigure(7,minsize=12.9984,weight=1) ##Row Definition (size)
          folderFrame.rowconfigure(8,minsize=42,weight=1) ##Row Definition (size)
          folderFrame.rowconfigure(9,minsize=12.9984,weight=1) ##Row Definition (size)
          folderFrame.rowconfigure(10,minsize=49.872,weight=1) ##Row Definition (size)

          self.folderFrameLabel=folderFrameLabel=Label(folderFrame,text='Folders To Include',font=('BoldCourier',16)) ##Label Widget for Frame
          folderFrameLabel.grid(row=0,column=0,columnspan=4) ##Grid Label Widget

          self.mainFolderLabel=mainFolderLabel=Label(folderFrame,text='Main Folders',font=('BoldCourier',12)) ##Label Widget for Main Folders
          mainFolderLabel.grid(row=1,column=0) ##Grid Label Widget

          self.divider0=divider0=Frame(folderFrame,width=2,height=280,borderwidth=1,relief='sunken') ##Frame to act as Divider for Better GUI Layout
          divider0.grid(row=1,column=1,rowspan=10) ##Grid Divider

          self.subFolderLabel=subFolderLabel=Label(folderFrame,text='Sub-Folders',font=('BoldCourier',12)) ##Label Widget for Sub-Folders
          subFolderLabel.grid(row=1,column=2,columnspan=2) ##Grid Label Widget

          self.firmwareMainVariable=firmwareMainVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.firmwareMain=firmwareMain=Checkbutton(folderFrame,width=10,text='Firmware',borderwidth=2,relief='groove',anchor='w',variable=firmwareMainVariable,font=('Courier',12)) ##Checkbutton Widget for Firmware Main Folder
          firmwareMain.grid(row=2,column=0) ##Grid Ceckbutton Widget

          self.firmwareResourcesVariable=firmwareResourcesVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.firmwareResources=firmwareResources=Checkbutton(folderFrame,width=12,text='Resources',borderwidth=2,relief='groove',anchor='w',variable=firmwareResourcesVariable,font=('Courier',12)) ##Checkbutton Widget for Firmware-Resources Sub-Folder
          firmwareResources.grid(row=2,column=2) ##Grid Ceckbutton Widget

          self.firmwareArchiveVariable=firmwareArchiveVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.firmwareArchive=firmwareArchive=Checkbutton(folderFrame,width=8,text='Archive',borderwidth=2,relief='groove',anchor='w',variable=firmwareArchiveVariable,font=('Courier',12)) ##Checkbutton Widget for Firmware-Archive Sub-Folder
          firmwareArchive.grid(row=2,column=3) ##Grid Ceckbutton Widget

          self.divider1=divider1=Frame(folderFrame,width=400,height=2,borderwidth=1,relief='sunken') ##Frame to act as Divider for Better GUI Layout
          divider1.grid(row=3,column=0,columnspan=4) ##Grid Divider

          self.hardwareMainVariable=hardwareMainVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.hardwareMain=hardwareMain=Checkbutton(folderFrame,width=10,text='Hardware',borderwidth=2,relief='groove',anchor='w',variable=hardwareMainVariable,font=('Courier',12)) ##Checkbutton Widget for Hardware Main Folder
          hardwareMain.grid(row=4,column=0) ##Grid Ceckbutton Widget

          self.hardwarePartsVariable=hardwarePartsVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.hardwareParts=hardwareParts=Checkbutton(folderFrame,width=12,text='Parts',borderwidth=2,relief='groove',anchor='w',variable=hardwarePartsVariable,font=('Courier',12)) ##Checkbutton Widget for Hardware-Parts Sub-Folder
          hardwareParts.grid(row=4,column=2) ##Grid Ceckbutton Widget

          self.hardwareArchiveVariable=hardwareArchiveVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.hardwareArchive=hardwareArchive=Checkbutton(folderFrame,width=8,text='Archive',borderwidth=2,relief='groove',anchor='w',variable=hardwareArchiveVariable,font=('Courier',12)) ##Checkbutton Widget for Hardware-Archive Sub-Folder
          hardwareArchive.grid(row=4,column=3) ##Grid Ceckbutton Widget

          self.divider2=divider2=Frame(folderFrame,width=400,height=2,borderwidth=1,relief='sunken') ##Frame to act as Divider for Better GUI Layout
          divider2.grid(row=5,column=0,columnspan=4) ##Grid Divider

          self.resourcesMainVariable=resourcesMainVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.resourcesMain=resourcesMain=Checkbutton(folderFrame,width=10,text='Resources',borderwidth=2,relief='groove',anchor='w',variable=resourcesMainVariable,font=('Courier',12)) ##Checkbutton Widget for Resources Main Folder
          resourcesMain.grid(row=6,column=0) ##Grid Ceckbutton Widget

          self.resourcesDatasheetsVariable=resourcesDatasheetsVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.resourcesDatasheets=resourcesDatasheets=Checkbutton(folderFrame,width=12,text='Datasheets',borderwidth=2,relief='groove',anchor='w',variable=resourcesDatasheetsVariable,font=('Courier',12)) ##Checkbutton Widget for Resources-Datasheets Sub-Folder
          resourcesDatasheets.grid(row=6,column=2) ##Grid Ceckbutton Widget

          self.resourcesArchiveVariable=resourcesArchiveVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.resourcesArchive=resourcesArchive=Checkbutton(folderFrame,width=8,text='Archive',borderwidth=2,relief='groove',anchor='w',variable=resourcesArchiveVariable,font=('Courier',12)) ##Checkbutton Widget for Resources-Archive Sub-Folder
          resourcesArchive.grid(row=6,column=3) ##Grid Ceckbutton Widget

          self.divider3=divider3=Frame(folderFrame,width=400,height=2,borderwidth=1,relief='sunken') ##Frame to act as Divider for Better GUI Layout
          divider3.grid(row=7,column=0,columnspan=4) ##Grid Divider

          self.softwareMainVariable=softwareMainVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.softwareMain=softwareMain=Checkbutton(folderFrame,text='Software',width=10,borderwidth=2,relief='groove',anchor='w',variable=softwareMainVariable,font=('Courier',12)) ##Checkbutton Widget for Software Main Folder
          softwareMain.grid(row=8,column=0) ##Grid Ceckbutton Widget

          self.softwareResourcesVariable=softwareResourcesVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.softwareResources=softwareResources=Checkbutton(folderFrame,width=12,text='Resources',borderwidth=2,relief='groove',anchor='w',variable=softwareResourcesVariable,font=('Courier',12)) ##Checkbutton Widget for Software-Resources Sub-Folder
          softwareResources.grid(row=8,column=2) ##Grid Ceckbutton Widget

          self.softwareArchiveVariable=softwareArchiveVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.softwareArchive=softwareArchive=Checkbutton(folderFrame,width=8,text='Archive',borderwidth=2,relief='groove',anchor='w',variable=softwareArchiveVariable,font=('Courier',12)) ##Checkbutton Widget for Software-Archive Sub-Folder
          softwareArchive.grid(row=8,column=3) ##Grid Ceckbutton Widget

          self.divider4=divider4=Frame(folderFrame,width=400,height=2,borderwidth=1,relief='sunken') ##Frame to act as Divider for Better GUI Layout
          divider4.grid(row=9,column=0,columnspan=4) ##Grid Divider

          self.archiveMainVariable=archiveMainVariable=BooleanVar() ##Boolean to Hold Value of Checkbutton
          self.archiveMain=archiveMain=Checkbutton(folderFrame,width=10,text='Archive',borderwidth=2,relief='groove',anchor='w',variable=archiveMainVariable,font=('Courier',12)) ##Checkbutton Widget for Archive Main Folder
          archiveMain.grid(row=10,column=0) ##Grid Ceckbutton Widget

          self.instructionFrame=instructionFrame=Frame(master,width=300,height=288,borderwidth=2,relief='groove') ##Frame for Instructions
          instructionFrame.grid(row=1,column=2,columnspan=2) ##Grid Frame

          self.instuctionLabel=instructionLabel=Label(instructionFrame,text='Project Name will\nbe used as Folder Name.\r\nFolder can be found on\nDesktop after Creation.',font=('BoldCourier',16)) ##Label Holding Instructions
          instructionLabel.grid(row=0,column=0,pady=80,padx=30) ##Grid Label

          self.cancelButton=cancelButton=Button(master,text='Cancel', width=42,height=108,font=('BoldCourier',16),foreground='red',command=self.CancelCommand) ##Button Widget to Cancel/Close Program
          cancelButton.grid(row=2,column=2,padx=10) ##Grid Button Widget

          self.createButton=createButton=Button(master,text='Create',width=42,height=108,font=('BoldCourier',16),foreground='green',command=self.CreateCommand) ##Button Widget to Create Folder Structure
          createButton.grid(row=2,column=3,padx=10) ##Grid Button Widget

          self.versionNumber=versionNumber=Label(text='Ver. 0.1') ##Label to Display Version Number
          versionNumber.grid(row=3,column=3) ##Grid Label Widget

     def CancelCommand(self): ##Command called by Cancel Button
##          print'Cancel Pressed' ##Debug
          root.destroy() ##Stops GUI From Running

     def CreateCommand(self): ##Command called by Create Button
##          print'Create Pressed' ##Debug
          desktop=path.join(environ['USERPROFILE'], 'Desktop') ##Find User Desktop Path and hold as String
          if(self.projectNameEntry.get()): ##If a Project Name was Entered
               newProject=path.join(desktop+'\\'+self.projectNameEntry.get()) ##Create a File Path to the Users Desktop with the Project Name becoming to target folder
               if(path.isdir(newProject)): ##Check if Folder already Exisits
                    showwarning('Folder Warning','    Folder Already Exists\nPlease Choose New Name') ##Warning Message Box Widget
                    self.ClearProject() ##Clear Selections
               else:
                    mkdir(newProject) ##Make Directory Path
               if(self.firmwareMainVariable.get()): ##If firmwareMain was selected
                    firmwareFolder=newProject+'/Firmware' ##Create String holding Target Folders Path
                    mkdir(firmwareFolder) ##Make Directory Path
                    if(self.firmwareResourcesVariable.get()): ##If firmwareResources was selected
                         mkdir(firmwareFolder+'/Resources') ##Make Directory Path
                    if(self.firmwareArchiveVariable.get()): ##If firmwareArchive was selected
                         mkdir(firmwareFolder+'/Archive') ##Make Directory Path
                    if(self.includeStartingFilesVariable.get()): ##If includeStratingFiles was selected
                         firmwareStartingFiles=firmwareFolder+'/ArduinoFirmware' ##Create String holding Target Files Path
                         mkdir(firmwareStartingFiles) ##Make Directory Path
                         open(firmwareStartingFiles+'/ArduinoFirmware'+'.ino','w') ##Make File in Directory Path
               if(self.hardwareMainVariable.get()): ##If hardwareMain was selected
                    hardwareFolder=newProject+'/Hardware' ##Create String holding Target Folders Path
                    mkdir(hardwareFolder) ##Make Directory Path
                    if(self.hardwarePartsVariable.get()): ##If hardwareParts was selected
                         mkdir(hardwareFolder+'/Parts') ##Make Directory Path
                    if(self.hardwareArchiveVariable.get()): ##If hardwareArchive was selected
                         mkdir(hardwareFolder+'/Archive') ##Make Directory Path
               if(self.resourcesMainVariable.get()): ##If resourcesMain was selected
                    resourcesFolder=newProject+'/Resources' ##Create String holding Target Folders Path
                    mkdir(resourcesFolder) ##Make Directory Path
                    if(self.resourcesDatasheetsVariable.get()): ##If resourcesDatasheets was selected
                         mkdir(resourcesFolder+'/Datasheets') ##Make Directory Path
                    if(self.resourcesArchiveVariable.get()): ##If resourcesArchive was selected
                         mkdir(resourcesFolder+'/Archive') ##Make Directory Path
               if(self.softwareMainVariable.get()): ##If softwareMain was selected
                    softwareFolder=newProject+'/Software' ##Create String holding Target Folders Path
                    mkdir(softwareFolder) ##Make Directory Path
                    if(self.softwareResourcesVariable.get()): ##If softwareResources was selected
                         mkdir(softwareFolder+'/Resources') ##Make Directory Path
                    if(self.softwareArchiveVariable.get()): ##If softwareArchive was selected
                         mkdir(softwareFolder+'/Archive') ##Make Directory Path
                    if(self.includeStartingFilesVariable.get()): ##If includeStartingFiles was selected
                         open(softwareFolder+'/'+self.projectNameEntry.get()+'_Software.py','w') ##Make File in Directory Path
               if(self.archiveMainVariable.get()): ##If archiveMain was selected
                    archiveFolder=newProject+'/Archive' ##Create String holding Target Folders Path
                    mkdir(archiveFolder) ##Make Directory Path
               if(self.includeStartingFilesVariable.get()): ##If includeStartingFiles was selected
                    open(newProject+'/'+'ReadMe.txt','w') ##Make File in Directory Path
               self.ClearProject() ##Call ClearProjects Function
          else: ##else
               showwarning('System Warning', 'Project Has No Name') ##Waring Box Widget

     def ClearProject(self): ##ClearProject Command
               self.includeStartingFilesVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.firmwareMainVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.firmwareResourcesVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.firmwareArchiveVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.hardwareMainVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.hardwarePartsVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.hardwareArchiveVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.resourcesMainVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.resourcesDatasheetsVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.resourcesArchiveVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.softwareMainVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.softwareResourcesVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.softwareArchiveVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.archiveMainVariable.set(False) ##Set Variable to False and Deselect Checkbox Widget
               self.projectNameEntry.delete(0,END) ##Clear contents of Entry Widget

root = Tk() ##Root is Tk Module
root.protocol("WM_DELETE_WINDOW", root.destroy) ##Define Top 'X' Button on Window
GUI = GUI(root) ##GUI will be main root

root.mainloop() ##Run Main
