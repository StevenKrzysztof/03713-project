from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QAction, QMenu, QMenuBar
import os
import time
import tkinter as tk
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSignal, QTimer
from PyQt5.QtMultimedia import *


from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QMenu
import Maskshow
import Distributionshow
import JenMain2
import test



##Part one
#The pages window of the GUI

# The home page window when you start the program
class right_widget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.right_widget = QtWidgets.QWidget()  # create the window
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # set the layout form

        self.right_recommend_label = QtWidgets.QLabel("")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  
        self.right_recommend_layout = QtWidgets.QGridLayout()  # use gridlayout
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        #set the location of the label

        self.right_layout.addWidget(self.right_recommend_label, 2, 0, 1, 8, Qt.AlignTop)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                border-image:url(./images/bg9.png);
                background:white;
                border-top:10px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
            }
            QLabel#right_lable{
                border:none;
                font-size:30px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
            QToolButton{
                border:none;
                background:blue;
                width:100px;
                height:100px;
                border-top:1px solid darkRed;
                border-bottom:1px solid darkRed;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
                border-top-left-radius:20px;
                border-bottom-left-radius:20px;
            }
            QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')


##main window
#Same layout as the home page window
class MainWindow(QWidget):
    def __init__(self, name, Layout):
        super().__init__()
        self.name = name
        self.Layout = Layout
        self.init_ui()

    def init_ui(self):
        self.right_widget = QtWidgets.QWidget()  
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  

        self.Layout.addWidget(self.right_widget, 0, 2, 12, 10)  

        self.right_recommend_label1 = QtWidgets.QLabel(" ")
        #self.right_recommend_label1.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  
        self.right_recommend_layout = QtWidgets.QGridLayout()  
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label1, 2, 0, 1, 8, Qt.AlignTop)

        self.right_layout.addWidget(self.right_recommend_widget, 7, 0, 2, 9, Qt.AlignTop)

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                border-image:url(./images/bg9.png);
                background:white;
                border-top:10px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
            }
            QLabel#right_lable{
                border:none;
                font-size:40px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
            QToolButton{
                border:none;
                background:blue;
                width:100px;
                height:100px;
                border-top:1px solid darkRed;
                border-bottom:1px solid darkRed;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
                border-top-left-radius:20px;
                border-bottom-left-radius:20px;
            }
            QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')


#  readme window

class HelpWindow(QWidget):
    def __init__(self, name, Layout):
        super().__init__()
        self.name = name
        self.Layout = Layout
        self.init_ui()
#General design as home page
    def init_ui(self):
        self.right_widget = QtWidgets.QWidget()  
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  

        self.Layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列

        self.right_recommend_label1 = QtWidgets.QLabel("Here may help you understand our software")
        self.right_recommend_label1.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  
        self.right_recommend_layout = QtWidgets.QGridLayout()  
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label1, 1, 0, 1, 9, Qt.AlignTop)

        self.right_layout.addWidget(self.right_recommend_widget, 4, 0, 2, 9, Qt.AlignTop)

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                border-image:url(./images/readme.png);
                background:white;
                border-top:10px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
            }
            QLabel#right_lable{
                border:none;
                font-size:30px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
            QToolButton{
                border:none;
                background:blue;
                width:100px;
                height:100px;
                border-top:1px solid darkRed;
                border-bottom:1px solid darkRed;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
                border-top-left-radius:20px;
                border-bottom-left-radius:20px;
            }
            QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')


# Operation Window for cell segmentation
class SegmentationWindow(QWidget):
    def __init__(self, name, Layout):
        super().__init__()
        self.name = name
        self.Layout = Layout
        self.init_ui()

    def doMain(self):
        os.chdir('..')	
        obj = JenMain.PromFinder(kmer_size=1000)
        obj.train(r'./train',
                'refTSS_v3.0_chr18.hg38.csv',
                'rf',
                use_existing=True)
        obj.predict(r'./test',
                'refTSS_v3.0_chr21.hg38.bed',
                'rf',
                r'./models/rf',
                use_existing=True)
        # sys.exit(app2.exec_())
#Set a Button that could allow user to upload file and start the process
    # def do_btn31(self, event):  # 文件：文件夹
    #     dir = QFileDialog.getExistingDirectory(self,
    #                                            "choose file",
    #                                            "D:/CMU/semester2/")  # choose file
    #     #Run Segmentation_QT.py
    #     self.demo = JenMain('GREY')
    #     self.demo.show()
       
#General design as home page
    def init_ui(self):
        self.right_widget = QtWidgets.QWidget()  
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  

        self.Layout.addWidget(self.right_widget, 0, 2, 12, 10)  

        self.right_recommend_label1 = QtWidgets.QLabel("Choose Chromosome from Here")
        self.right_recommend_label1.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  
        self.right_recommend_layout = QtWidgets.QGridLayout()  
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

#Set the button for Segmentation start
        self.recommend_button_11 = QtWidgets.QToolButton()
        self.recommend_button_11.setText("chromosome file")  
        self.recommend_button_11.clicked.connect(self.doMain)
        self.recommend_button_11.setIcon(QtGui.QIcon('./images/chrom.png'))  # the picture of the button
        self.recommend_button_11.setIconSize(QtCore.QSize(40, 80))  # size of button
        self.recommend_button_11.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # set the form of text

        

        self.right_recommend_layout.addWidget(self.recommend_button_11, 0, 0)
        

        self.right_layout.addWidget(self.right_recommend_label1, 2, 0, 1, 8, Qt.AlignTop)

        self.right_layout.addWidget(self.right_recommend_widget, 7, 0, 2, 9, Qt.AlignTop)

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                border-image:url(./images/segbackground.png);
                background:white;
                border-top:10px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
            }
            QLabel#right_lable{
                border:none;
                font-size:40px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
            QToolButton{
                border:none;
                background:blue;
                width:100px;
                height:100px;
                border-top:1px solid darkRed;
                border-bottom:1px solid darkRed;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
                border-top-left-radius:20px;
                border-bottom-left-radius:20px;
            }
            QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')


# SVM window
class FilterWindow(QWidget):
    def __init__(self, name, Layout):
        super().__init__()
        self.name = name
        self.Layout = Layout
        self.init_ui()

    
#Set a button for cell detecting process
    def do_btn32(self, event):  
        dir = QFileDialog.getExistingDirectory(self,
                                               "choose file",
                                               "D:/CMU/semester2/")  # upload file
        print(dir)
        # dir2 = QFileDialog.getExistingDirectory(self,
        #                                        "choose file",
        #                                        "D:/CMU/semester2/")  # upload file
        # print(dir2)
        # dir3 = QFileDialog.getExistingDirectory(self,
        #                                        "choose file",
        #                                        "D:/CMU/semester2/")  # upload file
        # print(dir3)
        # def run_function():
        #     output_text = f"Here is our output\n"
        #     os.chdir('..')	
        #     obj = JenMain2.PromFinder(kmer_size=1000)
        #     obj.train(dir,
        #             'refTSS_v3.0_human_coordinate.hg38.bed',
        #             'dl_svm',
        #             use_existing=True)
        #     metrics_list, pred_label = obj.predict(dir2,
        #                                         'mouse_chr19_test.csv',
        #                                             'dl_svm',
        #                                             dir3,
        #                                             use_existing=True)
        #     output_text += f"{pred_label}\n"

            
        #     # your function code here
        #     return output_text
        # root = tk.Tk()
        # root.title("My Python Script Output")

        # # Add a label to display the output
        # output_label = tk.Label(root, text="")
        # output_label.pack()

        # # Define a button that generates and displays the output
        # generate_button = tk.Button(root, text="Generate Output", command=lambda: output_label.config(text=JenMain2.run_function()))
        # generate_button.pack()

        # # Set the window position
        # screen_width = root.winfo_screenwidth()
        # screen_height = root.winfo_screenheight()
        # x = int((screen_width - 600) / 2)
        # y = int((screen_height - 600) / 2)
        # root.geometry("600x600+{}+{}".format(x+50, y-50))

        # root.mainloop()
        
    def do_btn33(self, event):  
           test.run()

            
        # os.chdir('..')	
        # obj = JenMain.PromFinder(kmer_size=1000)
        # obj.train(r'./train',
        #         'refTSS_v3.0_chr18.hg38.csv',
        #         'rf',
        #         use_existing=True)
        # obj.predict(r'./test',
        #         'refTSS_v3.0_chr21.hg38.bed',
        #         'rf',
        #         r'./models/rf',
        #         use_existing=True)


#Same design as segmentation window
    def init_ui(self):
        self.right_widget = QtWidgets.QWidget()  
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  

        self.Layout.addWidget(self.right_widget, 0, 2, 12, 10)  

        self.right_recommend_label1 = QtWidgets.QLabel("")
        self.right_recommend_label1.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  
        self.right_recommend_layout = QtWidgets.QGridLayout()  
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_11 = QtWidgets.QToolButton()
        #self.recommend_button_11.setText("Process")  
        self.recommend_button_11.clicked.connect(self.do_btn32)
        self.recommend_button_11.setIcon(QtGui.QIcon('./images/chrom.png'))  
        self.recommend_button_11.setIconSize(QtCore.QSize(100, 80))  
        self.recommend_button_11.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  

        self.right_recommend_layout.addWidget(self.recommend_button_11, 0, 0)

        self.recommend_button_33 = QtWidgets.QToolButton()
        self.recommend_button_33.setText("Process")  
        self.recommend_button_33.clicked.connect(self.do_btn33)
        self.recommend_button_33.setIcon(QtGui.QIcon('./images/chrom.png'))  
        self.recommend_button_33.setIconSize(QtCore.QSize(100, 80))  
        self.recommend_button_33.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  

        self.right_recommend_layout.addWidget(self.recommend_button_33, 0, 1)

        self.right_layout.addWidget(self.right_recommend_label1, 2, 0, 1, 8, Qt.AlignTop)

        self.right_layout.addWidget(self.right_recommend_widget, 7, 0, 2, 9, Qt.AlignTop)

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                border-image:url(./images/bgCH.png);
                background:white;
                border-top:10px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
            }
            QLabel#right_lable{
                border:none;
                font-size:40px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
            QToolButton{
                border:none;
                background:black;
                width:45px;
                height:55px;
                border-top:1px solid darkRed;
                border-bottom:1px solid darkRed;
                border-top-right-radius:5px;
                border-bottom-right-radius:5px;
                border-top-left-radius:5px;
                border-bottom-left-radius:5px;
            }
            QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

#------------------------------------------------------------------------------
#CNN model
class CNNWindow(QWidget):
    def __init__(self, name, Layout):
        super().__init__()
        self.name = name
        self.Layout = Layout
        self.init_ui()

    
#Set a button for SELF chosen data
    def do_btn11(self, event):  
        dir = QFileDialog.getExistingDirectory(self,
                                               "choose file",
                                               r"./")  # upload file
        print(dir)
        dir2 = QFileDialog.getExistingDirectory(self,
                                               "choose file",
                                               r"./")  # upload file
        print(dir2)
        
        def run_function():
            output_text = f"Here is our output\n"
            os.chdir('..')	
            obj = JenMain2.PromFinder(kmer_size=1000)
            obj.train(dir,
                    'refTSS_v3.0_human_coordinate.hg38.bed',
                    'dl',
                    use_existing=True)
            metrics_list, pred_label = obj.predict(dir2,
                                                'mouse_chr19_test.csv',
                                                    'dl',
                                                    r'./models/dl',
                                                    use_existing=True)
            output_text += f"{pred_label}\n"

            
            # your function code here
            return output_text
        root = tk.Tk()
        root.title("My Python Script Output")

        # Add a label to display the output
        output_label = tk.Label(root, text="")
        output_label.pack()

        # Define a button that generates and displays the output
        generate_button = tk.Button(root, text="Generate Output", command=lambda: output_label.config(text=run_function()))
        generate_button.pack()

        # Set the window position
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - 600) / 2)
        y = int((screen_height - 600) / 2)
        root.geometry("600x600+{}+{}".format(x+50, y-50))

        root.mainloop()
        
    def do_btn12(self, event):  
        def run_function():
            output_text = f"Here is our output\n"
            os.chdir('..')	
            obj = JenMain2.PromFinder(kmer_size=1000)
            obj.train(r'./human',
                    'refTSS_v3.0_human_coordinate.hg38.bed',
                    'dl',
                    use_existing=True)
            metrics_list, pred_label = obj.predict(r'./mouse',
                                                'mouse_chr19_test.csv',
                                                    'dl',
                                                    r'./models/dl',
                                                    use_existing=True)
            output_text += f"{pred_label}\n"

            
            # your function code here
            return output_text
        root = tk.Tk()
        root.title("My Python Script Output")

        # Add a label to display the output
        output_label = tk.Label(root, text="")
        output_label.pack()

        # Define a button that generates and displays the output
        generate_button = tk.Button(root, text="Generate Output", command=lambda: output_label.config(text=run_function()))
        generate_button.pack()

        # Set the window position
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - 600) / 2)
        y = int((screen_height - 600) / 2)
        root.geometry("600x600+{}+{}".format(x+50, y-50))

        root.mainloop()


    def init_ui(self):
        self.right_widget = QtWidgets.QWidget()  
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  

        self.Layout.addWidget(self.right_widget, 0, 2, 12, 10)  

        self.right_recommend_label1 = QtWidgets.QLabel("")
        self.right_recommend_label1.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  
        self.right_recommend_layout = QtWidgets.QGridLayout()  
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_11 = QtWidgets.QToolButton()
        #self.recommend_button_11.setText("Process")  
        self.recommend_button_11.clicked.connect(self.do_btn11)
        self.recommend_button_11.setIcon(QtGui.QIcon('./images/chrom.png'))  
        self.recommend_button_11.setIconSize(QtCore.QSize(100, 80))  
        self.recommend_button_11.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  

        self.right_recommend_layout.addWidget(self.recommend_button_11, 0, 0)

        self.recommend_button_12 = QtWidgets.QToolButton()
        self.recommend_button_12.setText("Process")  
        self.recommend_button_12.clicked.connect(self.do_btn12)
        self.recommend_button_12.setIcon(QtGui.QIcon('./images/chrom.png'))  
        self.recommend_button_12.setIconSize(QtCore.QSize(100, 80))  
        self.recommend_button_12.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  

        self.right_recommend_layout.addWidget(self.recommend_button_12, 0, 1)

        self.right_layout.addWidget(self.right_recommend_label1, 2, 0, 1, 8, Qt.AlignTop)

        self.right_layout.addWidget(self.right_recommend_widget, 7, 0, 2, 9, Qt.AlignTop)

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                border-image:url(./images/bgCH.png);
                background:white;
                border-top:10px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
            }
            QLabel#right_lable{
                border:none;
                font-size:40px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
            QToolButton{
                border:none;
                background:black;
                width:45px;
                height:55px;
                border-top:1px solid darkRed;
                border-bottom:1px solid darkRed;
                border-top-right-radius:5px;
                border-bottom-right-radius:5px;
                border-top-left-radius:5px;
                border-bottom-left-radius:5px;
            }
            QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')


#------------------------------------------------------------------------------
#Random Forest model
class RFWindow(QWidget):
    def __init__(self, name, Layout):
        super().__init__()
        self.name = name
        self.Layout = Layout
        self.init_ui()

    
#Set a button for SELF chosen data
    def do_btn21(self, event):  
        dir = QFileDialog.getExistingDirectory(self,
                                               "choose file",
                                               r"./")  # upload file
        print(dir)
        dir2 = QFileDialog.getExistingDirectory(self,
                                               "choose file",
                                               r"./")  # upload file
        print(dir2)
        
        def run_function():
            output_text = f"Here is our output\n"
            os.chdir('..')	
            obj = JenMain2.PromFinder(kmer_size=1000)
            obj.train(dir,
                    'refTSS_v3.0_human_coordinate.hg38.bed',
                    'rf',
                    use_existing=True)
            metrics_list, pred_label = obj.predict(dir2,
                                                'mouse_chr19_test.csv',
                                                    'rf',
                                                    r'./models/rf',
                                                    use_existing=True)
            output_text += f"{pred_label}\n"

            
            # your function code here
            return output_text
        root = tk.Tk()
        root.title("My Python Script Output")

        # Add a label to display the output
        output_label = tk.Label(root, text="")
        output_label.pack()

        # Define a button that generates and displays the output
        generate_button = tk.Button(root, text="Generate Output", command=lambda: output_label.config(text=run_function()))
        generate_button.pack()

        # Set the window position
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - 600) / 2)
        y = int((screen_height - 600) / 2)
        root.geometry("600x600+{}+{}".format(x+50, y-50))

        root.mainloop()
        
    def do_btn22(self, event):  
        def run_function():
            output_text = f"Here is our output\n"
            os.chdir('..')	
            obj = JenMain2.PromFinder(kmer_size=1000)
            obj.train(r'./human',
                    'refTSS_v3.0_human_coordinate.hg38.bed',
                    'rf',
                    use_existing=True)
            metrics_list, pred_label = obj.predict(r'./mouse',
                                                'mouse_chr19_test.csv',
                                                    'rf',
                                                    r'./models/rf',
                                                    use_existing=True)
            output_text += f"{pred_label}\n"

            
            # your function code here
            return output_text
        root = tk.Tk()
        root.title("My Python Script Output")

        # Add a label to display the output
        output_label = tk.Label(root, text="")
        output_label.pack()

        # Define a button that generates and displays the output
        generate_button = tk.Button(root, text="Generate Output", command=lambda: output_label.config(text=run_function()))
        generate_button.pack()

        # Set the window position
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - 600) / 2)
        y = int((screen_height - 600) / 2)
        root.geometry("600x600+{}+{}".format(x+50, y-50))

        root.mainloop()


    def init_ui(self):
        self.right_widget = QtWidgets.QWidget()  
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  

        self.Layout.addWidget(self.right_widget, 0, 2, 12, 10)  

        self.right_recommend_label1 = QtWidgets.QLabel("")
        self.right_recommend_label1.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  
        self.right_recommend_layout = QtWidgets.QGridLayout()  
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_21 = QtWidgets.QToolButton()
        #self.recommend_button_11.setText("Process")  
        self.recommend_button_21.clicked.connect(self.do_btn11)
        self.recommend_button_21.setIcon(QtGui.QIcon('./images/chrom.png'))  
        self.recommend_button_21.setIconSize(QtCore.QSize(100, 80))  
        self.recommend_button_21.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  

        self.right_recommend_layout.addWidget(self.recommend_button_21, 0, 0)

        self.recommend_button_22 = QtWidgets.QToolButton()
        self.recommend_button_22.setText("Process")  
        self.recommend_button_22.clicked.connect(self.do_btn12)
        self.recommend_button_22.setIcon(QtGui.QIcon('./images/chrom.png'))  
        self.recommend_button_22.setIconSize(QtCore.QSize(100, 80))  
        self.recommend_button_22.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  

        self.right_recommend_layout.addWidget(self.recommend_button_22, 0, 1)

        self.right_layout.addWidget(self.right_recommend_label1, 2, 0, 1, 8, Qt.AlignTop)

        self.right_layout.addWidget(self.right_recommend_widget, 7, 0, 2, 9, Qt.AlignTop)

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                border-image:url(./images/bgCH.png);
                background:white;
                border-top:10px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
            }
            QLabel#right_lable{
                border:none;
                font-size:40px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
            QToolButton{
                border:none;
                background:black;
                width:45px;
                height:55px;
                border-top:1px solid darkRed;
                border-bottom:1px solid darkRed;
                border-top-right-radius:5px;
                border-bottom-right-radius:5px;
                border-top-left-radius:5px;
                border-bottom-left-radius:5px;
            }
            QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')


#------------------------------------------------------------------------------
#SVM + CNN model
class SVMCNNWindow(QWidget):
    def __init__(self, name, Layout):
        super().__init__()
        self.name = name
        self.Layout = Layout
        self.init_ui()

    
#Set a button for SELF chosen data
    def do_btn41(self, event):  
        dir = QFileDialog.getExistingDirectory(self,
                                               "choose file",
                                               r"./")  # upload file
        print(dir)
        dir2 = QFileDialog.getExistingDirectory(self,
                                               "choose file",
                                               r"./")  # upload file
        print(dir2)
        
        def run_function():
            output_text = f"Here is our output\n"
            os.chdir('..')	
            obj = JenMain2.PromFinder(kmer_size=1000)
            obj.train(dir,
                    'refTSS_v3.0_human_coordinate.hg38.bed',
                    'dl_svm',
                    use_existing=True)
            metrics_list, pred_label = obj.predict(dir2,
                                                'mouse_chr19_test.csv',
                                                    'dl_svm',
                                                    r'./models/dl_svm',
                                                    use_existing=True)
            output_text += f"{pred_label}\n"

            
            # your function code here
            return output_text
        root = tk.Tk()
        root.title("My Python Script Output")

        # Add a label to display the output
        output_label = tk.Label(root, text="")
        output_label.pack()

        # Define a button that generates and displays the output
        generate_button = tk.Button(root, text="Generate Output", command=lambda: output_label.config(text=run_function()))
        generate_button.pack()

        # Set the window position
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - 600) / 2)
        y = int((screen_height - 600) / 2)
        root.geometry("600x600+{}+{}".format(x+50, y-50))

        root.mainloop()
        
    def do_btn42(self, event):  
        def run_function():
            output_text = f"Here is our output\n"
            os.chdir('..')	
            obj = JenMain2.PromFinder(kmer_size=1000)
            obj.train(r'./human',
                    'refTSS_v3.0_human_coordinate.hg38.bed',
                    'dl_svm',
                    use_existing=True)
            metrics_list, pred_label = obj.predict(r'./mouse',
                                                'mouse_chr19_test.csv',
                                                    'dl_svm',
                                                    r'./models/dl_svm',
                                                    use_existing=True)
            output_text += f"{pred_label}\n"

            
            # your function code here
            return output_text
        root = tk.Tk()
        root.title("My Python Script Output")

        # Add a label to display the output
        output_label = tk.Label(root, text="")
        output_label.pack()

        # Define a button that generates and displays the output
        generate_button = tk.Button(root, text="Generate Output", command=lambda: output_label.config(text=run_function()))
        generate_button.pack()

        # Set the window position
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - 600) / 2)
        y = int((screen_height - 600) / 2)
        root.geometry("600x600+{}+{}".format(x+50, y-50))

        root.mainloop()


    def init_ui(self):
        self.right_widget = QtWidgets.QWidget()  
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  

        self.Layout.addWidget(self.right_widget, 0, 2, 12, 10)  

        self.right_recommend_label1 = QtWidgets.QLabel("")
        self.right_recommend_label1.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  
        self.right_recommend_layout = QtWidgets.QGridLayout()  
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_41 = QtWidgets.QToolButton()
        #self.recommend_button_11.setText("Process")  
        self.recommend_button_41.clicked.connect(self.do_btn11)
        self.recommend_button_41.setIcon(QtGui.QIcon('./images/chrom.png'))  
        self.recommend_button_41.setIconSize(QtCore.QSize(100, 80))  
        self.recommend_button_41.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  

        self.right_recommend_layout.addWidget(self.recommend_button_41, 0, 0)

        self.recommend_button_42 = QtWidgets.QToolButton()
        self.recommend_button_42.setText("Process")  
        self.recommend_button_42.clicked.connect(self.do_btn12)
        self.recommend_button_42.setIcon(QtGui.QIcon('./images/chrom.png'))  
        self.recommend_button_42.setIconSize(QtCore.QSize(100, 80))  
        self.recommend_button_42.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  

        self.right_recommend_layout.addWidget(self.recommend_button_42, 0, 1)

        self.right_layout.addWidget(self.right_recommend_label1, 2, 0, 1, 8, Qt.AlignTop)

        self.right_layout.addWidget(self.right_recommend_widget, 7, 0, 2, 9, Qt.AlignTop)

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                border-image:url(./images/bgCH.png);
                background:white;
                border-top:10px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
            }
            QLabel#right_lable{
                border:none;
                font-size:40px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
            QToolButton{
                border:none;
                background:black;
                width:45px;
                height:55px;
                border-top:1px solid darkRed;
                border-bottom:1px solid darkRed;
                border-top-right-radius:5px;
                border-bottom-right-radius:5px;
                border-top-left-radius:5px;
                border-bottom-left-radius:5px;
            }
            QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

#------------------------------------------------------------------------------
#CNN + RF model
class CNNRFWindow(QWidget):
    def __init__(self, name, Layout):
        super().__init__()
        self.name = name
        self.Layout = Layout
        self.init_ui()

    
#Set a button for SELF chosen data
    def do_btn51(self, event):  
        dir = QFileDialog.getExistingDirectory(self,
                                               "choose file",
                                               r"./")  # upload file
        print(dir)
        dir2 = QFileDialog.getExistingDirectory(self,
                                               "choose file",
                                               r"./")  # upload file
        print(dir2)
        
        def run_function():
            output_text = f"Here is our output\n"
            os.chdir('..')	
            obj = JenMain2.PromFinder(kmer_size=1000)
            obj.train(dir,
                    'refTSS_v3.0_human_coordinate.hg38.bed',
                    'dl_rf',
                    use_existing=True)
            metrics_list, pred_label = obj.predict(dir2,
                                                'mouse_chr19_test.csv',
                                                    'dl_rf',
                                                    r'./models/dl_rf',
                                                    use_existing=True)
            output_text += f"{pred_label}\n"

            
            # your function code here
            return output_text
        root = tk.Tk()
        root.title("My Python Script Output")

        # Add a label to display the output
        output_label = tk.Label(root, text="")
        output_label.pack()

        # Define a button that generates and displays the output
        generate_button = tk.Button(root, text="Generate Output", command=lambda: output_label.config(text=run_function()))
        generate_button.pack()

        # Set the window position
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - 600) / 2)
        y = int((screen_height - 600) / 2)
        root.geometry("600x600+{}+{}".format(x+50, y-50))

        root.mainloop()
        
    def do_btn52(self, event):  
        def run_function():
            output_text = f"Here is our output\n"
            os.chdir('..')	
            obj = JenMain2.PromFinder(kmer_size=1000)
            obj.train(r'./human',
                    'refTSS_v3.0_human_coordinate.hg38.bed',
                    'dl_rf',
                    use_existing=True)
            metrics_list, pred_label = obj.predict(r'./mouse',
                                                'mouse_chr19_test.csv',
                                                    'dl_rf',
                                                    r'./models/dl_rf',
                                                    use_existing=True)
            output_text += f"{pred_label}\n"

            
            # your function code here
            return output_text
        root = tk.Tk()
        root.title("My Python Script Output")

        # Add a label to display the output
        output_label = tk.Label(root, text="")
        output_label.pack()

        # Define a button that generates and displays the output
        generate_button = tk.Button(root, text="Generate Output", command=lambda: output_label.config(text=run_function()))
        generate_button.pack()

        # Set the window position
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - 600) / 2)
        y = int((screen_height - 600) / 2)
        root.geometry("600x600+{}+{}".format(x+50, y-50))

        root.mainloop()


    def init_ui(self):
        self.right_widget = QtWidgets.QWidget()  
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  

        self.Layout.addWidget(self.right_widget, 0, 2, 12, 10)  

        self.right_recommend_label1 = QtWidgets.QLabel("")
        self.right_recommend_label1.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  
        self.right_recommend_layout = QtWidgets.QGridLayout()  
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_51 = QtWidgets.QToolButton()
        #self.recommend_button_11.setText("Process")  
        self.recommend_button_51.clicked.connect(self.do_btn11)
        self.recommend_button_51.setIcon(QtGui.QIcon('./images/chrom.png'))  
        self.recommend_button_51.setIconSize(QtCore.QSize(100, 80))  
        self.recommend_button_51.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  

        self.right_recommend_layout.addWidget(self.recommend_button_51, 0, 0)

        self.recommend_button_52 = QtWidgets.QToolButton()
        self.recommend_button_52.setText("Process")  
        self.recommend_button_52.clicked.connect(self.do_btn12)
        self.recommend_button_52.setIcon(QtGui.QIcon('./images/chrom.png'))  
        self.recommend_button_52.setIconSize(QtCore.QSize(100, 80))  
        self.recommend_button_52.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  

        self.right_recommend_layout.addWidget(self.recommend_button_52, 0, 1)

        self.right_layout.addWidget(self.right_recommend_label1, 2, 0, 1, 8, Qt.AlignTop)

        self.right_layout.addWidget(self.right_recommend_widget, 7, 0, 2, 9, Qt.AlignTop)

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                border-image:url(./images/bgCH.png);
                background:white;
                border-top:10px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:20px;
                border-bottom-right-radius:20px;
            }
            QLabel#right_lable{
                border:none;
                font-size:40px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
            QToolButton{
                border:none;
                background:black;
                width:45px;
                height:55px;
                border-top:1px solid darkRed;
                border-bottom:1px solid darkRed;
                border-top-right-radius:5px;
                border-bottom-right-radius:5px;
                border-top-left-radius:5px;
                border-bottom-left-radius:5px;
            }
            QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')



#This is the window of the left bar, which generates all the funcitons of our program
class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  
        self.main_layout = QtWidgets.QGridLayout()  
        self.main_widget.setLayout(self.main_layout)  

#Set the left bar buttons
        self.windowList = []

        self.left_widget = QtWidgets.QWidget()  
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  
        self.left_widget.setLayout(self.left_layout)  

        self.right_widget = right_widget()

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  
        self.main_layout.addWidget(self.right_widget.right_widget, 0, 2, 12, 10)  
        self.setCentralWidget(self.main_widget)  
        self.left_close = QtWidgets.QPushButton("")  # Button for closing the program
        self.left_fix = QtWidgets.QPushButton("")  # button for fix the window
        self.left_mini = QtWidgets.QPushButton("")  # button for minimization

#Buttons for functions
#Main function classification
        self.left_label_4 = QtWidgets.QPushButton("Home Page")
        self.left_label_4.setObjectName('left_label')
        self.left_label_1 = QtWidgets.QPushButton("Choose model")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("Pick chromosome")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("Instruction")
        self.left_label_3.setObjectName('left_label')
#button for each function
        self.left_label_4.clicked.connect(self.Main)
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "About Us")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_2.clicked.connect(self.Us)
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='lightSteelBlue'), "Prediction Results")
        self.left_button_4.clicked.connect(self.MaskShow)
        self.left_button_4.setObjectName('left_button')

        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='lightSteelBlue'), "Random Forest")
        self.left_button_6.clicked.connect(self.distribution)
        self.left_button_6.setObjectName('left_button')

        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='lightSteelBlue'), "read   me")
        self.left_button_9.setObjectName('left_button')
        self.left_button_9.clicked.connect(self.Help)

        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='lightSteelBlue'), "SVM")
        self.left_button_8.setObjectName('left_button')
        self.left_button_8.clicked.connect(self.Segmentation)

        self.left_button_11 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='lightSteelBlue'), "SVM+CNN")
        self.left_button_11.setObjectName('left_button')
        self.left_button_11.clicked.connect(self.Segmentation)

        self.left_button_12 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='lightSteelBlue'), "CNN+RF")
        self.left_button_12.setObjectName('left_button')
        self.left_button_12.clicked.connect(self.Segmentation)

        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='lightSteelBlue'), "CNN")
        self.left_button_7.setObjectName('left_button')
        self.left_button_7.clicked.connect(self.MaskShow)

        self.left_button_10 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='lightSteelBlue'), "Input Training Data")
        self.left_button_10.setObjectName('left_button')
        self.left_button_10.clicked.connect(self.Filterwind)

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_fix, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 3, 0, 1, 3)
        #self.left_layout.addWidget(self.left_button_2, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_4, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_10, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_11, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_12, 7, 0, 1, 3)

        self.left_close.setFixedSize(15, 15)  
        self.left_fix.setFixedSize(15, 15)  
        self.left_mini.setFixedSize(15, 15) 

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_fix.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_close.clicked.connect(QCoreApplication.instance().quit)
        self.left_close.clicked.connect(self.close)
        self.left_mini.clicked.connect(self.showMinimized)
        self.left_fix.clicked.connect(self.showMaximized)

        self.left_widget.setStyleSheet("\
            QPushButton{border:none;color:white;}\
            QPushButton#left_label{\
                border:none;\
                border-bottom:1px solid white;\
                font-size:18px;\
                font-weight:700;\
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;\
            }\
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}\
            QWidget#left_widget{\
                background:gray;\
                border-top:1px solid white;\
                border-bottom:1px solid white;\
                border-left:1px solid white;\
                border-top-left-radius:10px;\
                border-bottom-left-radius:10px;\
            }"
                                       )

        #self.setWindowOpacity(0.9)  # Opacity
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 

        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # hide the flages

        self.main_layout.setSpacing(0)

#Set connector for video playing
    # def video(self):        
    #     self.video1 = video.myMainWindow()
    #     self.video1.show()
        
        
#Set connector for mask picture show
    def MaskShow(self):        
        self.box = Maskshow.MainDemo()
        self.box.show()
        

    
#Set connector for heatmap show
    def distribution(self):       
        self.box1 = Distributionshow.MainDemo()
        self.box1.show()

       

       

    def Segmentation(self, img_path):
        Segment_window = SegmentationWindow("Segment", self.main_layout)
        self.windowList.append(Segment_window)
        
        self.right_widget.right_widget.close()

    def Filterwind(self, img_path):
        Filter_window = FilterWindow("Filter", self.main_layout)
        self.windowList.append(Filter_window)
        
        self.right_widget.right_widget.close()

    def CNNwind(self, img_path):
        Filter_window = CNNWindow("CNN", self.main_layout)
        self.windowList.append(CNN_window)
        
        self.right_widget.right_widget.close()

    def RF(self, img_path):
        Filter_window = RFWindow("RF", self.main_layout)
        self.windowList.append(RF_window)
        
        self.right_widget.right_widget.close()

    def SVMCNN(self, img_path):
        Filter_window = SVMCNNWindow("SVMCNN", self.main_layout)
        self.windowList.append(SVMCNN_window)
        
        self.right_widget.right_widget.close()

    def CNNRF(self, img_path):
        Filter_window = CNNRFWindow("CNNRF", self.main_layout)
        self.windowList.append(CNNRF_window)
        
        self.right_widget.right_widget.close()


    def Main(self):
        Main_window = MainWindow("Main", self.main_layout)
        self.right_widget.right_widget.close()
        self.windowList.append(Main_window)
       

    def Help(self):
        Help_window = HelpWindow("Main2", self.main_layout)
        self.right_widget.right_widget.close()
        self.windowList.append(Help_window)
        


# run the GUI


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
