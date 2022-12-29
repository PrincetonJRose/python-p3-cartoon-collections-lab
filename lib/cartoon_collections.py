def roll_call_dwarves( dwarves ):
    pass
    [ print( f"{ index + 1 }. { dwarf }" ) for index, dwarf in enumerate( dwarves ) ]

def summon_captain_planet( elements ):
    pass
    return [ f'{ element.title() }!' for element in elements ]

def long_planeteer_calls( words ):
    pass
    for word in words:
        if len( word ) > 4:
            return True
    else: return False

def find_the_cheese( ingredients ):
    pass
    chesses = [ 'cheddar', 'gouda', 'camembert' ]
    for i in ingredients:
        if i in chesses:
            return i
    else: return None
