TOP=../..
include $(TOP)/configure/CONFIG

# The templates use UDFS, which does not exist before base 3.15, and make does
# not check them, so without this an IOC would only fail when loading them
ifeq ($(EPICS_VERSION).$(EPICS_REVISION),3.14)
$(error stanfordDG645 needs EPICS base 3.15 or later. On R3.14 use release 1-3)
endif
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# In a Diamond Support Module, install
# templates like this
#
#DB += motor.template
#DB += basic_motor.template
DB += stanfordDG645.template
DB += stanfordDG645Channel.template
DB += stanfordDG645Output.template

#----------------------------------------------------
# In a Diamond IOC Application, build db files from
# template files like this
#
#DB += BL06I-MO-IOC-01.db
#DB += BL06I-MO-IOC-01_sim.db

#USES_TEMPLATE += $(MOTOR)/db/motor.template
#USES_TEMPLATE += $(MOTOR)/db/basic_motor.template

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
