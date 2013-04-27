# This script will create a replica from gresd to grest
# Developed by: Shakir Ahmed
# Supervisor : Juan Tobar
# Create Date : 04/25/2013
# Import system modules
import sys
import string
import os
import time
import shutil
import pyodbc
import arcpy
from arcpy import env
env.overwriteOutput = 1
# Local variables:
RIM_PRSTF_AQU_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_AQU_APP_AREA_1"
RIM_PRSTF_DAF_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_DAF_APP_AREA_1"
RIM_PRSTF_ERP_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_ERP_APP_AREA_1"
RIM_PRSTF_JDS_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_JDS_APP_AREA_1"
RIM_PRSTF_LOK_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_LOK_APP_AREA_1"
RIM_PRSTF_MIT_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_MIT_APP_AREA_1"
RIM_PRSTF_OST_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_OST_APP_AREA_1"
RIM_PRSTF_PRE_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_PRE_APP_AREA_1"
RIM_PRSTF_SBL_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_SBL_APP_AREA_1"
RIM_PRSTF_WDF_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WDF_APP_AREA_1"
RIM_PRSTF_SWM_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_SWM_APP_AREA_1"
RIM_PRSTF_WDI_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WDI_APP_AREA_1"
RIM_PRSTF_WQE_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WQE_APP_AREA_1"
RIM_PRSTF_WUP_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WUP_APP_AREA_1"
RIM_PRSTF_WUP_DEW_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WUP_DEW_APP_AREA_1"
RIM_PRSTF_WUP_DIV_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WUP_DIV_APP_AREA_1"
RIM_PRSTF_WUP_PWS_APP_AREA_1 = "Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WUP_PWS_APP_AREA_1"
rim_grest_grestsde_sde = "Database Connections\\rim@grest_grestsde.sde"

# Process: Create Replica
arcpy.CreateReplica_management("'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_AQU_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_DAF_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_ERP_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_JDS_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_LOK_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_MIT_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_OST_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_PRE_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_SBL_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WDF_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_SWM_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WDI_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WQE_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WQE_APP_CRNT_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WUP_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WUP_DEW_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WUP_DIV_APP_AREA_1';'Database Connections\\rim@gresd_gresdsde.sde\\RIM.PRSTF_WUP_PWS_APP_AREA_1'", "ONE_WAY_REPLICA", rim_grest_grestsde_sde, "prstf_gresd_gret", "SIMPLE", "PARENT_DATA_SENDER", "USE_DEFAULTS", "DO_NOT_REUSE", "GET_RELATED", "", "DO_NOT_USE_ARCHIVING")

