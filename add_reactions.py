import sqlite3

def add_reaction(reaction, product, reaction_type):
    conn = sqlite3.connect('reactions.db')
    cursor = conn.cursor()

    cursor.execute("INSERT OR REPLACE INTO reactions (reaction, product, type) VALUES (?, ?, ?)",
                   (reaction, product, reaction_type))

    conn.commit()
    conn.close()

def main():
    # Example data
    reactions_data = [
        ("H2 + O2 -> H2O", "H2O", "Combustion"),
        ("Na + Cl -> NaCl", "NaCl", "Synthesis"),
        ("H2O -> H2 + O2", "H2 + O2", "Decomposition")
    ]

    for reaction, product, reaction_type in reactions_data:
        add_reaction(reaction, product, reaction_type)

    print("Reactions added to the database successfully.")

if __name__ == '__main__':
    main()
