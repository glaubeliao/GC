from PyQt5.QtCore import QThread, QObject, pyqtSignal


class Uno(QThread):
    signal = pyqtSignal(float) # 括號裡填寫訊號傳遞的引數
    #signal1 = pyqtSignal(int) # 括號裡填寫訊號傳遞的引數
    def __init__(self):
        super(Uno, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):

        i=1
        for line in open('Data.csv','r'):
            QThread.sleep(1)

            data=line.split(',')  #  Data 用,隔開
            data=float(data[1])
            data=data*10000
            #i=i+1

            #if i == 1:
                #ser.write(b'F')
                #print('do something 1')
            #elif i == 15:
                #ser.write(b'Q')
                #print('do something 2')

            #a=ser.readline()
            #b=int(a)
            print(data)
            self.signal.emit(float(data))
            i=i+1


class Count(QObject):

    finished = pyqtSignal()  # Give the class a finished signal

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True  # Provide a bool run condition for the class

    def Increase(self):
        i = 1
        while self.continue_run:  # Give the loop a stoppable condition
            print(i)
            QThread.sleep(1)
            i = i + 1
        self.finished.emit()      # Emit the finished signal when the loop is done


    def Stop(self):
        self.continue_run = False  # Set the run condition to false on stop


class Worker(QObject):

    finished = pyqtSignal()  # Give worker class a finished signal

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True  # Provide a bool run condition for the class

    def do_work(self):
        i = 1
        while self.continue_run:  # Give the loop a stoppable condition
            print(i)
            QThread.sleep(1)
            i = i + 1
        self.finished.emit()      # Emit the finished signal when the loop is done

    def stop(self):
        self.continue_run = False  # Set the run condition to false on stop



class test(QObject):

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        

    def A(self):
        print("A")

    def B(self):
        print("B")


class Plot(QObject):

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)


    def Static(self):
        title = "Basic pyqtgraph plot"
        x = np.linspace(-3*np.pi, 3*np.pi, 1000)
        y1 = np.sin(x)
        y2 = np.cos(x)
        y = y1 + y2
 
       # create plot window object
        plt = pg.plot()
 
       # some regular settings
        plt.showGrid(x = True, y = True)
        plt.addLegend()
        plt.setLabel('left', 'y')
        plt.setLabel('bottom', 'x')
        # plt.setXRange(0, 10)
        plt.setYRange(-2.5, 2.5)
        plt.setWindowTitle(title)
 
        plt.plot(x, y1, pen = 'g', name = 'sin(x)')
        plt.plot(x, y2, pen = 'r', name = 'cos(x)')
 
        pen = pg.mkPen(color='y', width=3, style=QtCore.Qt.DashLine) # DotLine
        plt.plot(x, y, pen = pen, name = 'sin(x)+cos(x)')


class Counter(QObject):

    finished = pyqtSignal()  # Give worker class a finished signal 
    
    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)

        # Provide a bool run condition for the class
        self.continue_run = True
        
    def continus(self):
        i = 1
        while self.continue_run:  # Give the loop a stoppable condition
            print(i)
            QThread.sleep(1)
            i = i + 1
        self.finished.emit()      # Emit the finished signal when the loop is done

    def stop(self):
        self.continue_run = False  # Set the run condition to false on stop

