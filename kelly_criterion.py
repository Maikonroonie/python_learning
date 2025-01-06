def kelly_criterion(initial_capital, win_probability, reward_ratio, safety_margin=0.1):
    """
    Oblicza, ile zainwestować z początkowego kapitału, aby zoptymalizować wzrost
    i zachować zapas w przypadku porażki.
    
    Args:
    - initial_capital (float): Kapitał początkowy.
    - win_probability (float): Prawdopodobieństwo wygranej (np. 0.5 dla 50%).
    - reward_ratio (float): Stosunek zysku do stawki (np. 2 dla zysku 2:1).
    - safety_margin (float): Margines bezpieczeństwa, zmniejsza wielkość inwestycji (np. 0.1 dla 10% zapasu).
    
    Returns:
    - dict: Kwota do zainwestowania, zapas kapitału i pozostały kapitał.
    """
    # Prawdopodobieństwo przegranej
    lose_probability = 1 - win_probability
    
    # Wzór Kelly'ego
    kelly_fraction = (reward_ratio * win_probability - lose_probability) / reward_ratio
    
    if kelly_fraction <= 0:
        return {"invest": 0, "reserve": initial_capital, "remaining": initial_capital}
    
    # Uwzględnienie marginesu bezpieczeństwa
    invest_fraction = kelly_fraction * (1 - safety_margin)
    invest_amount = initial_capital * invest_fraction
    reserve_capital = initial_capital - invest_amount
    
    return {
        "invest": invest_amount,
        "reserve": reserve_capital,
        "remaining": reserve_capital
    }


# Parametry
initial_capital = 41  # Kapitał początkowy w zł
win_probability = 0.5    # Prawdopodobieństwo wygranej (50%)
reward_ratio = 2         # Zysk w stosunku 2:1
safety_margin = 0.4      # Margines bezpieczeństwa 10%

# Obliczenia
result = kelly_criterion(initial_capital, win_probability, reward_ratio, safety_margin)

# Wynik
print("Ile zainwestować:", round(result["invest"], 2), "zł")
print("Zapas kapitału:", round(result["reserve"], 2), "zł")
print("Pozostały kapitał po inwestycji:", round(result["remaining"], 2), "zł")
