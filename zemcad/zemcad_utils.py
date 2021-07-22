


# alagorithm
# 1. parse given file
#   - check if ext is cad or zem
#   - get extent from header
#   - get ekatte or eknm and apply to ekatte
#   - infer CRS
#   - check extent for spatial consistency
#   -

lookup_utm35n = []
lookup_utm34n = []
lookup_1970_k3 = []
lookup_1970_k5 = []
lookup_1970_k7 = []
lookup_1970_k9 = []
lookup_bg2005_geodetic = []
lookup_bg2005_35 = []
lookup_bg2005_34 = []


data_states = [
    {'state': 'perfect_match', 'actions': [1,2,3,4]},
    {'state': 'semi_match', 'actions': [1,2,3]},
    {'state': 'no_match', 'actions': []},
    {'state': 'missing_ekatte', 'actions': [1,2]},
]

perfect_match_state = {
    '': ''
}

semi_match_state = {

}

no_match_state = {

}

missing_ekatte_state = {

}




def task_register_file(fpath: str):
    registered_file = {}
    return registered_file


# data quality checks:
# - if not ekatte or eknm => move file to unknown and mark as need human in the loop
# - if extent is more than 30% outsize of lookups


ekatte_123 = {
    'ekatte': '12345',
    'infered_crs': None,
    'registration': [
        {'reg_date': '2021.06.07'},
        {}
    ],
    'last_known_state': {
        'extent_wgs84_utm34n': '',
        'extent_wgs84_utm35n': '',
        'extent_bgs2005_cadastral': '',
        'extent_bgs2005_u35': '',
        'extent_bgs2005_u34': '',
        'extent_bgs2005_': '',
        'extent_1970_k3': '',
        'extent_1970_k5': '',
        'extent_1970_k7': '',
        'extent_1970_k9': '',
        'extent_1950_3deg': '',
        'extent_1950_6deg': '',
        'extent_1930': '',
        'extent_ETRS89_epoh1989_u34': '',
        'extent_ETRS89_epoh1989_u35': ''
    }
}

