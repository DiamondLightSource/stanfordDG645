from iocbuilder import AutoSubstitution
from iocbuilder import *
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.modules.asyn import AsynIP

class stanfordDG645(AutoSubstitution, AutoProtocol):
    '''Support for Stanford DG645 digital delay generator'''
    #def __init__(self, **args):
    #    args["PORT"] = args["PORT"].PortName
    #    self.__super.__init__(**args)

    TemplateFile = 'stanfordDG645.template'
    ProtocolFiles = ['stanfordDG645.proto']
stanfordDG645.ArgInfo.descriptions["PORT"] = Ident ('Asyn port', AsynIP)
    

