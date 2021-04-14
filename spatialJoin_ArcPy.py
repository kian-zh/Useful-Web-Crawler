import arcpy

target_features = [
    "research_c123_era_pro_sel500_nowater_grland_",
    "research_c123_era_pro_sel300_nowater_grland_",
    "research_c12_era_pro_sel500_nowater_grland_",
    "research_c12_era_pro_sel300_nowater_grland_",
    "research_c1_era_pro_sel500_nowater_grland_",
    "research_c1_era_pro_sel300_nowater_grland_"
]

join_features_basePath = "POIs\\"
join_features = [
    "_lodging",
    "_tour_attr",
    "_storage",
    "_comnity_wh",
    "_comrce_wh",
    "_comnity_pa",
    "_comrce_pa"
]

basePath = "D:\\LabData\\5023\\Project\\"

for target_feature in target_features:
    count = 0
    for join_feature in join_features:

        target = basePath + target_feature + str(count) + '.shp'
        join = join_features_basePath + join_feature
        count = count + 1
        out = basePath + target_feature + str(count) + '.shp'

        fm = arcpy.FieldMap()
        fms = arcpy.FieldMappings()
        fm.addInputField(join, "lat")
        type_name = fm.outputField
        type_name.name = join_feature
        fm.outputField = type_name
        fm.mergeRule = 'Count'
        fms.addFieldMap(fm)

        for field in arcpy.ListFields(target, '_*'):
            fmx = arcpy.FieldMap()
            fmx.addInputField(target, field.name)
            fms.addFieldMap(fmx)


        arcpy.SpatialJoin_analysis(target, join, out, "JOIN_ONE_TO_ONE", "KEEP_ALL", fms)
    print(target_feature)


target_features = [
    "research_c123_era_pro_sel500_nowater_grland_",
    "research_c123_era_pro_sel300_nowater_grland_",
    "research_c12_era_pro_sel500_nowater_grland_",
    "research_c12_era_pro_sel300_nowater_grland_",
    "research_c1_era_pro_sel500_nowater_grland_",
    "research_c1_era_pro_sel300_nowater_grland_"
]

basePath = "D:\\LabData\\5023\\Project\\"

codeblock = """
def getMain(_lodging, _tour_attr, _storage, _comnity_wh, _comrce_wh, _comnity_pa, _comrce_pa):
    maxWh = max(_lodging, _tour_attr, _storage, _comnity_wh, _comrce_wh)
    if(maxWh == 0):
        if(_comnity_pa>=_comrce_pa):
            return 'comnity'
        else:
            return 'comrce'
    else:
        if(_lodging == maxWh):
            return 'lodging'
        if(_tour_attr == maxWh):
            return 'tour'
        if(_storage == maxWh):
            return 'storage'
        if(_comnity_wh == maxWh):
            return 'comnity'
        if(_comrce_wh == maxWh):
            return 'comrce'
"""

for target_feature in target_features:
    target = basePath + target_feature + '7.shp'

    expression = "getMain(!_lodging!, !_tour_attr!, !_storage!, !_comnity_w!, !_comrce_wh!, !_comnity_p!, !_comrce_pa!)"

    arcpy.AddField_management(target, 'result', "TEXT", field_length=50)
    arcpy.CalculateField_management(target, 'result', expression, "PYTHON3", codeblock)