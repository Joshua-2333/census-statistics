# readCensusExcel.py - Tabulates county population and census tracts

import openpyxl
import pprint

print("Opening workbook...")

wb = openpyxl.load_workbook("censuspopdata.xlsx")

sheet = wb["Population by Census Tract"]

county_data = {}

