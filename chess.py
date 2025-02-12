import pandas as pd
# Expanding the dataset with more openings
expanded_data = {
    "ECO Code": [
        "C60", "C50", "D06", "B20", "E20", "B06", "C42", "C30", "C41", "D02",
        "B23", "C44", "C00", "C55", "D10", "B40", "E60", "D30", "A40", "C65"
    ],
    "Opening Name": [
        "Ruy López", "Italian Game", "Queen's Gambit", "Sicilian Defense", "Nimzo-Indian Defense", "Modern Defense",
        "Petrov's Defense", "King's Gambit", "Philidor Defense", "Colle System", "Sicilian Grand Prix Attack",
        "Scotch Game", "French Defense", "Two Knights Defense", "Slav Defense", "Sicilian Paulsen", "King's Indian Defense",
        "Tarrasch Defense", "Englund Gambit", "Berlin Defense"
    ],
    "First Moves": [
        "1.e4 e5 2.Nf3 Nc6 3.Bb5", "1.e4 e5 2.Nf3 Nc6 3.Bc4", "1.d4 d5 2.c4", "1.e4 c5",
        "1.d4 Nf6 2.c4 e6 3.Nc3 Bb4", "1.e4 g6", "1.e4 e5 2.Nf3 Nf6", "1.e4 e5 2.f4", "1.e4 e5 2.Nf3 d6",
        "1.d4 d5 2.Nf3 Nf6", "1.e4 c5 2.f4", "1.e4 e5 2.d4 exd4", "1.e4 e6", "1.e4 e5 2.Nf3 Nc6 3.Nc3",
        "1.d4 d5 2.c4 c6", "1.e4 c5 2.Nf3 e6", "1.d4 Nf6 2.c4 g6", "1.d4 d5 2.c4 e6 3.Nc3 c5", "1.d4 e5",
        "1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6"
    ],
    "Win Rate for White (%)": [
        54, 54, 58, 48.5, 48.5, 47.5, 52, 49, 51, 53, 50, 51, 47, 55, 56, 49, 48, 52, 45, 57
    ],
    "Win Rate for Black (%)": [
        46, 46, 42, 51.5, 51.5, 52.5, 48, 51, 49, 47, 50, 49, 53, 45, 44, 51, 52, 48, 55, 43
    ]
}

# Convert to DataFrame
expanded_df = pd.DataFrame(expanded_data)

# Save to CSV
file_path = "Data/chess_openings_large.csv"
expanded_df.to_csv(file_path, index=False)
file_path