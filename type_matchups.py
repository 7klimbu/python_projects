elements = {
    "normal": {"Weak": ["rock", "steel"], "Strong": [], "Null": ["ghost"]},
    "fire": {"Weak": ["fire", "water, ""rock", "dragon"], "Strong": ["grass", "ice", "bug", "steel"], "Null": []},
    "water": {"Weak": ["water", "grass", "dragon"], "Strong": ["fire", "ground", "rock"], "Null": []},
    "electric": {"Weak": ["electric", "grass", "dragon"], "Strong": ["water", "flying"], "Null": ["ground"]},
    "grass": {"Weak": ["fire", "grass", "poison", "bug", "dragon", "steel"], "Strong": ["water", "ground", "rock"], "Null": []},
    "ice": {"Weak": ["fire", "water", "ice", "steel"], "Strong": ["grass", "ground", "flying", "dragon"], "Null": []},
    "fighting": {"Weak": ["poison", "flying", "psychic", "bug"], "Strong": ["normal", "ice", "rock", "dark", "steel"], "Null": ["ghost"]},
    "poison": {"Weak": ["poison", "ground", "rock", "ghost"], "Strong": ["grass", "fairy"], "Null": ["steel"]},
    "ground": {"Weak": ["grass", "bug"], "Strong": ["fire", "electric", "poison", "rock"], "Null": ["flying"]},
    "flying": {"Weak": ["electric", "rock", "steel"], "Strong": ["grass", "fighting", "bug"], "Null": []},
    "psychic": {"Weak": ["psychic", "steel"], "Strong": ["fighting", "poison"], "Null": ["dark"]},
    "bug": {"Weak": ["fire", "fighting", "poison", "flying", "ghost", "steel", "fairy"], "Strong": ["grass", "psychic", "dark"], "Null": []},
    "rock": {"Weak": ["poison", "ground", "steel"], "Strong": ["fire", "ice", "flying", "bug"], "Null": []},
    "ghost": {"Weak": ["dark"], "Strong": ["psychic", "ghost"], "Null": ["normal"]},
    "dragon": {"Weak": ["steel"], "Strong": ["dragon"], "Null": ["fairy"]},
    "dark": {"Weak": ["fighting", "dark", "fairy"], "Strong": ["psychic", "ghost"], "Null": []},
    "steel": {"Weak": ["fire, water, electric"], "Strong": ["ice", "rock", "fairy"], "Null": []},
    "fairy": {"Weak": ["fire", "poison", "steel"], "Strong": ["fighting", "dragon", "dark"], "Null": []}
}
