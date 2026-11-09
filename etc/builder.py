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

class stanfordDG645Channel(AutoSubstitution, AutoProtocol):
    '''One DG645 delay channel pair (AB, CD, EF or GH) with its prescaler'''
    TemplateFile = 'stanfordDG645Channel.template'
    ProtocolFiles = ['stanfordDG645.proto']
stanfordDG645Channel.ArgInfo.descriptions["PORT"] = Ident ('Asyn port', AsynIP)

class stanfordDG645Output(AutoSubstitution, AutoProtocol):
    '''One DG645 output's levels (T0, AB, CD, EF or GH)'''
    TemplateFile = 'stanfordDG645Output.template'
    ProtocolFiles = ['stanfordDG645.proto']
stanfordDG645Output.ArgInfo.descriptions["PORT"] = Ident ('Asyn port', AsynIP)
    

